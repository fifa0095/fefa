import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

def hdr(ws, row, col, value, bg="1F4E79"):
    c = ws.cell(row=row, column=col, value=value)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=11, name="Calibri")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin = Side(style="thin", color="AAAAAA")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)

def lnk(ws, row, col, label, url, bg="FFFFFF"):
    c = ws.cell(row=row, column=col, value=label)
    c.hyperlink = url
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="0563C1", bold=True, size=10, name="Calibri", underline="single")
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=False)
    thin = Side(style="thin", color="DDDDDD")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)

def cell(ws, row, col, value, bg="FFFFFF", bold=False, color="000000", align="left"):
    c = ws.cell(row=row, column=col, value=value)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(bold=bold, size=10, name="Calibri", color=color)
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=True)
    thin = Side(style="thin", color="DDDDDD")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)

def sec(ws, row, col, span, title, bg="2E75B6"):
    c = ws.cell(row=row, column=col, value=title)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=13, name="Calibri")
    c.alignment = Alignment(horizontal="left", vertical="center")
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+span-1)

# ══════════════════════════════════════════════════════════════════════════════
# DATA: [country_label, flag, visa, sai, platform, link_label, url, note]
# ══════════════════════════════════════════════════════════════════════════════

jobs = [
    # ─── AUSTRALIA ────────────────────────────────────────────────────────────
    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462\n(ไปได้เลย ไม่ต้อง job offer)", "SAP ABAP",
     "SEEK", "🔍 SEEK – SAP ABAP Developer Jobs AU",
     "https://www.seek.com.au/sap-abap-developer-jobs",
     "Job board ใหญ่ที่สุดในออสเตรเลีย\nอัปเดตทุกวัน"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "SAP ABAP",
     "LinkedIn", "🔍 LinkedIn – SAP ABAP Jobs Australia",
     "https://au.linkedin.com/jobs/sap-abap-jobs",
     "109+ ตำแหน่ง กด Apply โดยตรง"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "SAP ABAP",
     "Indeed AU", "🔍 Indeed – SAP ABAP Developer AU",
     "https://au.indeed.com/q-sap-abap-developer-jobs.html",
     "50+ ตำแหน่ง มี Junior/Entry level"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "SAP ABAP",
     "Jora AU", "🔍 Jora – SAP ABAP Jobs Australia",
     "https://au.jora.com/Sap-Abap-jobs-in-Australia",
     "6,000+ listings รวม contractor"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "ServiceNow",
     "SEEK", "🔍 SEEK – ServiceNow Developer Jobs AU",
     "https://www.seek.com.au/servicenow-developer-jobs",
     "95+ ตำแหน่ง ทั้ง full-time & contract"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "ServiceNow",
     "LinkedIn", "🔍 LinkedIn – ServiceNow Jobs Australia",
     "https://au.linkedin.com/jobs/servicenow-developer-jobs",
     "กด Easy Apply ได้เลย"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "ServiceNow",
     "Indeed AU", "🔍 Indeed – ServiceNow Developer Sydney",
     "https://au.indeed.com/q-servicenow-developer-l-sydney-nsw-jobs.html",
     "filter Sydney NSW"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "ServiceNow",
     "Glassdoor AU", "🔍 Glassdoor – ServiceNow Dev Australia",
     "https://www.glassdoor.com.au/Job/servicenow-developer-Australia-SRCH_KO0,20_IL.21,30_IN16.htm",
     "70+ jobs พร้อมรีวิวบริษัท"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "ServiceNow",
     "EY Careers", "🏢 EY Australia – ServiceNow Graduate",
     "https://www.ey.com/en_au/careers/servicenow-student-opportunities",
     "Graduate program รับ recent grad\nบริษัท Big4 เงินเดือนดี"),

    ("ออสเตรเลีย", "🇦🇺", "WHV Subclass 462", "SAP ABAP\n+ ServiceNow",
     "SAP Careers", "🏢 SAP – Jobs in Australia",
     "https://jobs.sap.com/go/SAP-Jobs-in-Australia/",
     "ตำแหน่งจาก SAP โดยตรง\nVisa sponsor พร้อม"),

    # ─── NEW ZEALAND ──────────────────────────────────────────────────────────
    ("นิวซีแลนด์", "🇳🇿", "WHV\n(Quota 100/ปี — สมัครเร็ว!)", "SAP ABAP",
     "SEEK NZ", "🔍 SEEK NZ – SAP ABAP Developer",
     "https://nz.seek.com/sap-abap-developer-jobs",
     "126 jobs อัปเดตทุกวัน"),

    ("นิวซีแลนด์", "🇳🇿", "WHV", "SAP ABAP",
     "Jooble NZ", "🔍 Jooble NZ – SAP ABAP",
     "https://nz.jooble.org/jobs-sap-abap/New-Zealand",
     "198+ vacancies"),

    ("นิวซีแลนด์", "🇳🇿", "WHV", "SAP ABAP",
     "Glassdoor NZ", "🔍 Glassdoor NZ – SAP Jobs",
     "https://www.glassdoor.co.nz/Job/new-zealand-sap-jobs-SRCH_IL.0,11_IN186_KO12,15.htm",
     "213 SAP jobs ใน NZ"),

    ("นิวซีแลนด์", "🇳🇿", "WHV", "SAP ABAP",
     "SAP Careers", "🏢 SAP – Jobs in New Zealand",
     "https://jobs.sap.com/go/SAP-Jobs-in-New-Zealand/882701/",
     "ตำแหน่งจาก SAP โดยตรง"),

    ("นิวซีแลนด์", "🇳🇿", "WHV", "ServiceNow",
     "SEEK NZ", "🔍 SEEK NZ – ServiceNow Developer",
     "https://nz.seek.com/servicenow-developer-jobs",
     "Filter NZ ได้เลย"),

    ("นิวซีแลนด์", "🇳🇿", "WHV", "ServiceNow",
     "LinkedIn NZ", "🔍 LinkedIn – ServiceNow Jobs NZ",
     "https://nz.linkedin.com/jobs/servicenow-developer-jobs",
     "กด Easy Apply"),

    # ─── GERMANY ──────────────────────────────────────────────────────────────
    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa\n(ต้องมี job offer ก่อน\nนายจ้าง sponsor visa)", "SAP ABAP",
     "GermanTechJobs", "🔍 GermanTechJobs – SAP ABAP Germany",
     "https://germantechjobs.de/jobs/SAP-ABAP",
     "Job board เฉพาะ Tech เยอรมนี\nภาษาอังกฤษ OK ส่วนใหญ่"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "SAP ABAP",
     "Glassdoor DE", "🔍 Glassdoor – ABAP Developer Germany",
     "https://www.glassdoor.com/Job/germany-developer-english-abap-jobs-SRCH_IL.0,7_IN96_KO8,30.htm",
     "28+ jobs ภาษาอังกฤษ"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "SAP ABAP",
     "SAP Careers DE", "🏢 SAP – ABAP Jobs in Germany",
     "https://jobs.sap.com/go/ABAP-Jobs-in-Germany/889601/",
     "ABAP jobs จาก SAP HQ Walldorf\nโดยตรง"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "SAP ABAP",
     "Arbeitnow", "🔍 Arbeitnow – Visa Sponsored Jobs DE",
     "https://www.arbeitnow.com/visa-sponsorship-jobs",
     "filter SAP ABAP ได้\nระบุ visa sponsorship ชัดเจน"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "SAP ABAP",
     "Jora DE", "🔍 Jora – SAP ABAP Germany Visa",
     "https://nz.jora.com/Sap-Abap-Jobs-In-Germany-With-Visa-Sponsorship-jobs",
     "47 jobs Germany + visa sponsor"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "ServiceNow",
     "ServiceNow Careers", "🏢 ServiceNow – Germany Office",
     "https://careers.servicenow.com/locations/emea/germany/",
     "ตำแหน่งจาก ServiceNow DE\nโดยตรง"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "ServiceNow",
     "SNPro.jobs", "🔍 SNPro – ServiceNow Visa Sponsored",
     "https://snpro.jobs/visa-sponsored",
     "Job board เฉพาะ ServiceNow\nมี visa sponsored filter"),

    ("เยอรมนี", "🇩🇪", "Skilled Worker Visa", "ServiceNow",
     "DevJobs DE", "🔍 DevJobs – ServiceNow Germany",
     "https://en.devjobs.de/jobs/servicenow",
     "Tech jobs เยอรมนีทั้งหมด"),

    # ─── SINGAPORE ────────────────────────────────────────────────────────────
    ("สิงคโปร์", "🇸🇬", "Employment Pass\n(ต้องมี job offer ก่อน\nเงินเดือน SGD 5,000+/เดือน)", "SAP ABAP",
     "Indeed SG", "🔍 Indeed SG – ABAP Visa Sponsorship",
     "https://sg.indeed.com/q-visa-sponsorship-available,-abap-jobs.html",
     "300+ jobs พร้อม visa sponsor"),

    ("สิงคโปร์", "🇸🇬", "Employment Pass", "SAP ABAP",
     "JobStreet SG", "🔍 JobStreet – SAP Developer Singapore",
     "https://sg.jobstreet.com/sap-developer-jobs",
     "Job board หลักใน SG/SEA"),

    ("สิงคโปร์", "🇸🇬", "Employment Pass", "SAP ABAP",
     "SAP Careers SG", "🏢 SAP – Jobs in Singapore",
     "https://jobs.sap.com/go/SAP-Jobs-in-Singapore/944301/",
     "ตำแหน่งจาก SAP Singapore\nโดยตรง"),

    ("สิงคโปร์", "🇸🇬", "Employment Pass", "ServiceNow",
     "ServiceNow Careers", "🏢 ServiceNow – Singapore (APAC HQ)",
     "https://careers.servicenow.com/locations/apj/singapore/",
     "APAC Headquarters Singapore\nมี intern + full-time"),

    ("สิงคโปร์", "🇸🇬", "Employment Pass", "ServiceNow",
     "Glassdoor SG", "🔍 Glassdoor – ServiceNow Dev Singapore",
     "https://www.glassdoor.sg/Job/singapore-servicenow-developer-jobs-SRCH_IL.0,9_IC3235921_KO10,30.htm",
     "55 jobs + รีวิวบริษัท"),

    ("สิงคโปร์", "🇸🇬", "Employment Pass", "ServiceNow",
     "JobStreet SG", "🔍 JobStreet – ServiceNow Singapore",
     "https://sg.jobstreet.com/servicenow-jobs",
     "SAP + ServiceNow ใน SEA"),
]

# ══════════════════════════════════════════════════════════════════════════════
# BUILD SHEET
# ══════════════════════════════════════════════════════════════════════════════
ws = wb.active
ws.title = "ลิงก์สมัครงาน"
ws.sheet_view.showGridLines = False

sec(ws, 1, 1, 6, "  🔗  ลิงก์สมัครงานโดยตรง — SAP ABAP & ServiceNow (ประเทศที่คนไทยอายุ 24 จบแล้วไปได้)")

hdr(ws, 2, 1, "ประเทศ")
hdr(ws, 2, 2, "วีซ่า / เงื่อนไข")
hdr(ws, 2, 3, "สาย")
hdr(ws, 2, 4, "แพลตฟอร์ม")
hdr(ws, 2, 5, "ลิงก์ (กดได้เลย)")
hdr(ws, 2, 6, "หมายเหตุ")

country_bg = {
    "ออสเตรเลีย": "E8F4FD",
    "นิวซีแลนด์": "E8F9F2",
    "เยอรมนี":    "FFF9E8",
    "สิงคโปร์":   "FFF0F8",
}
country_hdr_bg = {
    "ออสเตรเลีย": "1565C0",
    "นิวซีแลนด์": "2E7D32",
    "เยอรมนี":    "E65100",
    "สิงคโปร์":   "880E4F",
}

prev_country = None
row = 3
for item in jobs:
    country, flag, visa, sai, platform, link_label, url, note = item
    bg = country_bg[country]

    # Country divider row
    if country != prev_country:
        c = ws.cell(row=row, column=1, value=f"  {flag}  {country}  —  {visa}")
        c.fill = PatternFill("solid", fgColor=country_hdr_bg[country])
        c.font = Font(color="FFFFFF", bold=True, size=12, name="Calibri")
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws.merge_cells(start_row=row, start_column=1, end_row=row, end_column=6)
        ws.row_dimensions[row].height = 36
        row += 1
        prev_country = country

    cell(ws, row, 1, f"{flag} {country}", bg=bg, bold=True)
    cell(ws, row, 2, visa, bg=bg)
    cell(ws, row, 3, sai, bg=bg, bold=True,
         color="1F4E79" if "SAP" in sai else ("BF5700" if "ServiceNow" in sai else "444444"))
    cell(ws, row, 4, platform, bg=bg)
    lnk(ws, row, 5, link_label, url, bg=bg)
    cell(ws, row, 6, note, bg=bg)
    ws.row_dimensions[row].height = 40
    row += 1

ws.column_dimensions["A"].width = 14
ws.column_dimensions["B"].width = 24
ws.column_dimensions["C"].width = 14
ws.column_dimensions["D"].width = 16
ws.column_dimensions["E"].width = 44
ws.column_dimensions["F"].width = 30
ws.row_dimensions[1].height = 30
ws.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — สมัคร WHV ออสเตรเลีย (ขั้นตอนเดียว)
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("สมัคร WHV ออสเตรเลีย")
ws2.sheet_view.showGridLines = False

sec(ws2, 1, 1, 3, "  🇦🇺  สมัคร Work & Holiday Visa (Subclass 462) — ลิงก์ทางการ")

hdr(ws2, 2, 1, "ขั้นตอน")
hdr(ws2, 2, 2, "ลิงก์ (กดได้เลย)")
hdr(ws2, 2, 3, "รายละเอียด")

whv_steps = [
    ("1️⃣ ดูรายละเอียด WHV\nSubclass 462 ทางการ",
     "🏛️ Home Affairs – WHV Subclass 462",
     "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/work-holiday-462",
     "เว็บทางการรัฐบาลออสเตรเลีย\nดูคุณสมบัติ + เอกสารที่ต้องใช้"),
    ("2️⃣ สมัครวีซ่า online\n(ImmiAccount)",
     "🏛️ ImmiAccount – สมัครวีซ่า online",
     "https://online.immi.gov.au/lusc/login",
     "สร้าง account + ยื่นใบสมัคร\nค่าวีซ่า AUD 635 (~15,000 บาท)"),
    ("3️⃣ เช็ค IELTS requirement\n+ สมัครสอบ",
     "📝 IDP – สมัครสอบ IELTS ไทย",
     "https://www.idp.com/thailand/ielts/register/",
     "ต้องได้ IELTS 4.5+\nสอบได้ทั่วประเทศไทย"),
    ("4️⃣ ข้อมูล WHV 2026\nสำหรับคนไทย",
     "📖 IDP – Work & Holiday 2026 Guide Thai",
     "https://ielts.idp.com/thailand/about/news-and-articles/article-work-and-holiday-visa",
     "กำหนดการเปิด-ปิดรับ\nปี 2026 สำหรับคนไทยโดยเฉพาะ"),
    ("5️⃣ Tourism Australia\n(ข้อมูล WHV official)",
     "🌏 Tourism Australia – WHV Guide",
     "https://www.australia.com/en/youth-travel/working-holiday-visa/how-to-apply-for-a-work-and-holiday-visa-462.html",
     "How to apply step-by-step\nภาษาอังกฤษ"),
]

for i, (step, label, url, note) in enumerate(whv_steps):
    r = i + 3
    bg = "F2FBF6" if i % 2 == 0 else "E8F9F2"
    cell(ws2, r, 1, step, bg=bg, bold=True)
    lnk(ws2, r, 2, label, url, bg=bg)
    cell(ws2, r, 3, note, bg=bg)
    ws2.row_dimensions[r].height = 50

ws2.column_dimensions["A"].width = 24
ws2.column_dimensions["B"].width = 44
ws2.column_dimensions["C"].width = 36
ws2.row_dimensions[1].height = 30
ws2.row_dimensions[2].height = 35

out = "/home/user/fefa/Job_Links_Direct.xlsx"
wb.save(out)
print(f"Saved: {out}")
