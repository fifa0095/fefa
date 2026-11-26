-- ตารางเก็บโครงการยาที่ได้รับจากเว็บผู้ส่ง (e-GP)
create table if not exists public.egp_projects (
  project_no    text primary key,          -- upsert: ส่งซ้ำไม่เกิดแถวซ้ำ
  type          text not null,             -- tor / invitation / selection
  project_name  text,
  agency        text,
  province      text,
  announced_by  text,
  announce_date date,
  status        text,
  drugs         text[],
  egp_url       text,
  delivery_id   bigint,
  received_at   timestamptz default now()
);

-- เปิด RLS โดยไม่สร้าง policy: คนนอกอ่าน/เขียนผ่าน API สาธารณะไม่ได้
-- ตัวรับเขียนด้วย service_role key ฝั่งเซิร์ฟเวอร์เท่านั้น
alter table public.egp_projects enable row level security;
