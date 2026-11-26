# ตัวรับ Webhook e-GP (Supabase Edge Function)

ไฟล์:
- `migrations/20261126000000_egp_projects.sql` — สร้างตาราง `egp_projects`
- `functions/egp-webhook/index.ts` — ตัวรับ (ตรวจเวลา + ลายเซ็น HMAC แล้ว upsert)
- `../scripts/test-send.mjs` — สคริปต์ยิงข้อมูลทดสอบที่เซ็นแล้ว

## ขั้นตอน

1. ติดตั้ง Supabase CLI แล้ว login + ผูกโปรเจกต์ (project ref อยู่ใน Settings → General)
   ```bash
   npx supabase login
   npx supabase link --project-ref <project-ref>
   ```
2. สร้างตาราง (หรือก๊อป SQL ในไฟล์ migration ไปรันใน SQL Editor ก็ได้)
   ```bash
   npx supabase db push
   ```
3. ตั้ง secret ที่ได้จากเว็บผู้ส่ง (ห้าม commit ลงโค้ด)
   ```bash
   npx supabase secrets set EGP_WEBHOOK_SECRET=<secret>
   ```
4. Deploy (**ต้องมี `--no-verify-jwt`** ไม่งั้นได้ 401 ทุกครั้ง)
   ```bash
   npx supabase functions deploy egp-webhook --no-verify-jwt
   ```
   URL ที่ได้: `https://<project-ref>.supabase.co/functions/v1/egp-webhook`
5. ทดสอบเอง
   ```bash
   WEBHOOK_URL=https://<project-ref>.supabase.co/functions/v1/egp-webhook WEBHOOK_SECRET=<secret> node scripts/test-send.mjs ping
   ```
   ต้องได้ `200 {"ok":true,"received":0,...}`  
   (`real` = ส่งโครงการทดสอบ TEST-0001 ลงตาราง, `badsig` = ต้องได้ 401)
6. แจ้ง URL ให้ฝั่งผู้ส่ง แล้วให้เขากด "ทดสอบ" ในหน้า /webhooks/ ต้องขึ้น HTTP 200

ไม่ต้องตั้ง `SUPABASE_URL` / `SUPABASE_SERVICE_ROLE_KEY` เพราะ Edge Function มีให้อัตโนมัติ
ถ้าอยากเปลี่ยนชื่อผู้รับที่ตอบกลับ ตั้ง `EGP_RECEIVER_NAME` เพิ่มได้
