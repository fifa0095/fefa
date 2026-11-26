// ตัวรับ webhook จากระบบติดตามประกาศยา e-GP
// deploy: supabase functions deploy egp-webhook --no-verify-jwt
import { createClient } from "npm:@supabase/supabase-js@2";

const SECRET = Deno.env.get("EGP_WEBHOOK_SECRET") ?? "";
const RECEIVER = Deno.env.get("EGP_RECEIVER_NAME") ?? "supabase-edge";
const TYPES = ["tor", "invitation", "selection"] as const;
const enc = new TextEncoder();

const supabase = createClient(
  Deno.env.get("SUPABASE_URL")!,
  Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!,
);

async function hmacHex(data: Uint8Array): Promise<string> {
  const key = await crypto.subtle.importKey(
    "raw", enc.encode(SECRET), { name: "HMAC", hash: "SHA-256" }, false, ["sign"],
  );
  const sig = new Uint8Array(await crypto.subtle.sign("HMAC", key, data));
  return [...sig].map((b) => b.toString(16).padStart(2, "0")).join("");
}

function safeEqual(a: string, b: string): boolean {
  if (a.length !== b.length) return false;
  let r = 0;
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i);
  return r === 0;
}

const reply = (status: number, body: Record<string, unknown>) =>
  Response.json(body, { status });

Deno.serve(async (req) => {
  if (req.method !== "POST") return reply(405, { ok: false, error: "method not allowed" });
  if (!SECRET) return reply(500, { ok: false, error: "EGP_WEBHOOK_SECRET not set" });

  // 1) body ดิบ (ลายเซ็นคำนวณจาก byte ดิบ ห้ามแปลง JSON ก่อน)
  const raw = new Uint8Array(await req.arrayBuffer());
  const ts = req.headers.get("x-egp-timestamp") ?? "";
  const sig = (req.headers.get("x-egp-signature") ?? "").replace(/^sha256=/, "");

  // 2) เวลาห่างจากปัจจุบันไม่เกิน 5 นาที
  if (!/^\d+$/.test(ts) || Math.abs(Date.now() / 1000 - Number(ts)) > 300) {
    return reply(401, { ok: false, error: "timestamp" });
  }

  // 3) ลายเซ็น HMAC-SHA256(secret, timestamp + "." + body)
  const signed = new Uint8Array(enc.encode(ts + ".").length + raw.length);
  signed.set(enc.encode(ts + "."), 0);
  signed.set(raw, enc.encode(ts + ".").length);
  if (!safeEqual(sig, await hmacHex(signed))) {
    return reply(401, { ok: false, error: "bad signature" });
  }

  let data: Record<string, unknown>;
  try {
    data = JSON.parse(new TextDecoder().decode(raw));
  } catch {
    return reply(400, { ok: false, error: "invalid json" });
  }
  if (data.test) return reply(200, { ok: true, received: 0, receiver: RECEIVER });

  // 4) upsert ด้วย project_no (รวมแถวที่ project_no ซ้ำในชุดเดียวกันก่อน
  //    ไม่งั้น Postgres จะ error "cannot affect row a second time")
  const now = new Date().toISOString();
  const byNo = new Map<string, Record<string, unknown>>();
  for (const type of TYPES) {
    const list = Array.isArray(data[type]) ? data[type] as Record<string, unknown>[] : [];
    for (const p of list) {
      if (!p?.project_no) continue;
      byNo.set(String(p.project_no), {
        project_no: String(p.project_no), type,
        project_name: p.project_name ?? null, agency: p.agency ?? null,
        province: p.province ?? null, announced_by: p.announced_by ?? null,
        announce_date: p.announce_date || null, status: p.status ?? null,
        drugs: Array.isArray(p.drugs) ? p.drugs : [], egp_url: p.egp_url ?? null,
        delivery_id: data.delivery_id ?? null, received_at: now,
      });
    }
  }
  const rows = [...byNo.values()];
  if (rows.length) {
    const { error } = await supabase.from("egp_projects").upsert(rows, { onConflict: "project_no" });
    if (error) {
      console.error("upsert failed:", error.message);
      return reply(500, { ok: false, error: error.message });
    }
  }

  // 5) ตอบกลับ
  return reply(200, { ok: true, received: rows.length, receiver: RECEIVER });
});
