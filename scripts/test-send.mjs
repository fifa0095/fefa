// ยิงข้อมูลที่เซ็นแล้วเข้าตัวรับ เพื่อทดสอบก่อนต่อกับเว็บผู้ส่งจริง
// ใช้: WEBHOOK_URL=<url> WEBHOOK_SECRET=<secret> node scripts/test-send.mjs [ping|real|badsig]
import { createHmac } from "node:crypto";

const url = process.env.WEBHOOK_URL ?? "http://localhost:54321/functions/v1/egp-webhook";
const secret = process.env.WEBHOOK_SECRET ?? "test-secret";
const mode = process.argv[2] ?? "real";

const body = JSON.stringify(mode === "ping"
  ? { delivery_id: 0, test: true, tor: [], invitation: [], selection: [] }
  : {
      delivery_id: 0, sent_at: new Date().toISOString(), batch: "test.csv",
      tor: [], invitation: [],
      selection: [{
        project_no: "TEST-0001", project_name: "ทดสอบ", agency: "ทดสอบ",
        province: "ขอนแก่น", announced_by: "", announce_date: "2026-11-19",
        status: "จัดทำ TOR", drugs: ["test"], egp_url: "https://example.com",
      }],
    });
const ts = Math.floor(Date.now() / 1000).toString();
const key = mode === "badsig" ? "wrong-secret" : secret;
const sig = "sha256=" + createHmac("sha256", key).update(`${ts}.${body}`).digest("hex");

const r = await fetch(url, {
  method: "POST", body,
  headers: { "Content-Type": "application/json; charset=utf-8",
             "X-EGP-Timestamp": ts, "X-EGP-Signature": sig, "X-EGP-Delivery-Id": "0" },
});
console.log(r.status, await r.text());
