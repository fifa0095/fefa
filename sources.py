import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

thin = Side(style="thin", color="CCCCCC")
bd = Border(left=thin, right=thin, top=thin, bottom=thin)

def hdr(ws, row, col, val, bg="1F4E79", span=1):
    c = ws.cell(row=row, column=col, value=val)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=11, name="Calibri")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    c.border = bd
    if span > 1:
        ws.merge_cells(start_row=row, start_column=col,
                       end_row=row, end_column=col+span-1)

def lnk(ws, row, col, label, url, bg="FFFFFF", bold=False):
    c = ws.cell(row=row, column=col, value=label)
    c.hyperlink = url
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="0563C1", bold=bold, size=10, name="Calibri", underline="single")
    c.alignment = Alignment(horizontal="left", vertical="center", wrap_text=False)
    c.border = bd

def cell(ws, row, col, val, bg="FFFFFF", bold=False,
         color="222222", align="left", wrap=True, size=10):
    c = ws.cell(row=row, column=col, value=val)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(bold=bold, size=size, name="Calibri", color=color)
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    c.border = bd

def flag_hdr(ws, row, col, span, title, bg):
    c = ws.cell(row=row, column=col, value=title)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=12, name="Calibri")
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    c.border = bd
    ws.merge_cells(start_row=row, start_column=col,
                   end_row=row, end_column=col+span-1)
    ws.row_dimensions[row].height = 26

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1 — ลิงก์สมัครงาน SAP ABAP (แยกตามประเทศ)
# ══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "สมัครงาน SAP ABAP"
ws1.sheet_view.showGridLines = False

# Title
t = ws1.cell(row=1, column=1,
    value="  🔗  แหล่งสมัครงาน SAP ABAP — คลิกกดสมัครได้เลย (อัปเดต มิ.ย. 2569)")
t.fill = PatternFill("solid", fgColor="1B4F72")
t.font = Font(color="FFFFFF", bold=True, size=13, name="Calibri")
t.alignment = Alignment(horizontal="left", vertical="center", indent=1)
ws1.merge_cells("A1:E1")
ws1.row_dimensions[1].height = 30

hdr(ws1, 2, 1, "ประเทศ / วีซ่า")
hdr(ws1, 2, 2, "ประเภท")
hdr(ws1, 2, 3, "บริษัท / แพลตฟอร์ม")
hdr(ws1, 2, 4, "คลิกสมัคร / ดูงาน")
hdr(ws1, 2, 5, "หมายเหตุ")
ws1.row_dimensions[2].height = 35

data = [
    # ─ Australia WHV ──────────────────────────────────────────────
    ("AU_FLAG",),
    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462\n✅ ไปได้เลย",
     "🏢 Graduate Program", "Accenture AU 2027",
     "Accenture – Consulting Analyst 2027",
     "https://au.gradconnection.com/employers/accenture/jobs/accenture-consulting-analystgraduate-program-2027-australia-and-new-zealand/",
     "⚠️ ต้องการ PR/Citizen บางตำแหน่ง\nเช็คแต่ละ job posting ก่อนสมัคร\nProgram เริ่ม 2027"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🏢 Graduate Program", "Deloitte AU 2027",
     "Deloitte – Students & Graduates",
     "https://www.deloitte.com/au/en/careers/students.html",
     "✅ มีหน้า International Students\nProgram เริ่ม มี.ค. 2027\nรับผู้จบการศึกษาภายใน 2 ปี"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🏢 Graduate Program", "Deloitte – International Students",
     "Deloitte – International Students Page",
     "https://www.deloitte.com/au/en/careers/students/international-students.html",
     "✅ หน้าสำหรับ international\nstudent/grad โดยเฉพาะ\nเช็คสิทธิ์ก่อนสมัคร"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🏢 Graduate Program", "KPMG AU 2027",
     "KPMG – Technology & Digital Graduate (Feb 2027)",
     "https://au.prosple.com/graduate-employers/kpmg-australia/jobs-internships/technology-digital-graduate-program",
     "✅ รับผู้จบการศึกษา\nภายใน 2 ปีล่าสุด\nสมัครผ่าน Prosple"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🏢 Graduate Program", "KPMG AU Careers",
     "KPMG – Graduate & Student Opportunities",
     "https://kpmg.com/au/en/home/careers/graduates.html",
     "หน้า official KPMG AU\nสมัคร graduate ทุกสาย"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🏢 Graduate Program", "Capgemini AU",
     "Capgemini – Students & Graduates Program",
     "https://www.capgemini.com/careers/career-paths/students-and-graduates/",
     "Graduate program SAP focus\nทั้ง AU & Global"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🔍 Job Board", "SEEK Australia",
     "SEEK – SAP ABAP Developer Jobs AU",
     "https://www.seek.com.au/sap-abap-developer-jobs",
     "Job board ใหญ่ที่สุดใน AU\nอัปเดตทุกวัน 18+ jobs"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🔍 Job Board", "SEEK – Melbourne",
     "SEEK – SAP ABAP Jobs Melbourne VIC",
     "https://www.seek.com.au/sap-abap-developer-jobs/in-All-Melbourne-VIC",
     "กรอง Melbourne เท่านั้น"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🔍 Job Board", "Indeed Australia",
     "Indeed AU – SAP ABAP Jobs",
     "https://au.indeed.com/q-sap-abap-jobs.html",
     "25+ ตำแหน่ง\nกด Apply โดยตรงได้"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🔍 Job Board", "Glassdoor Australia",
     "Glassdoor AU – SAP ABAP Jobs",
     "https://www.glassdoor.com.au/Job/australia-sap-abap-jobs-SRCH_IL.0,9_IN16_KO10,18.htm",
     "26 jobs มิ.ย. 2026\nมีรีวิวบริษัท + เงินเดือน"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🔍 Job Board", "Jora Australia",
     "Jora AU – SAP ABAP Jobs Australia",
     "https://au.jora.com/Sap-Abap-jobs-in-Australia",
     "5,000+ listings รวม contract\nค้นหาง่าย"),

    ("🇦🇺 ออสเตรเลีย\nWHV Subclass 462",
     "🔍 Job Board", "Adzuna Australia",
     "Adzuna AU – SAP ABAP Jobs",
     "https://www.adzuna.com.au/sap-abap",
     "18 jobs มิ.ย. 2026\nแสดงเงินเดือนชัดเจน"),

    # ─ New Zealand WHV ────────────────────────────────────────────
    ("NZ_FLAG",),
    ("🇳🇿 นิวซีแลนด์\nWHV (Quota 100/ปี)\n⚠️ สมัครเร็ว!",
     "🔍 Job Board", "SEEK NZ",
     "SEEK NZ – SAP ABAP Developer Jobs",
     "https://nz.seek.com/sap-abap-developer-jobs",
     "Job board หลัก NZ\nอัปเดตทุกวัน"),

    ("🇳🇿 นิวซีแลนด์\nWHV",
     "🔍 Job Board", "Jooble NZ",
     "Jooble NZ – SAP ABAP Jobs NZ",
     "https://nz.jooble.org/jobs-sap-abap/New-Zealand",
     "198 vacancies\nรวม Junior ด้วย"),

    ("🇳🇿 นิวซีแลนด์\nWHV",
     "🔍 Job Board", "Glassdoor NZ",
     "Glassdoor NZ – SAP Jobs New Zealand",
     "https://www.glassdoor.co.nz/Job/new-zealand-sap-jobs-SRCH_IL.0,11_IN186_KO12,15.htm",
     "213 SAP jobs ทั่ว NZ"),

    ("🇳🇿 นิวซีแลนด์\nWHV",
     "🏢 Direct", "SAP NZ Careers",
     "SAP – Jobs in New Zealand",
     "https://jobs.sap.com/go/SAP-Jobs-in-New-Zealand/882701/",
     "ตำแหน่งจาก SAP โดยตรง"),

    # ─ Germany Skilled Worker ──────────────────────────────────────
    ("DE_FLAG",),
    ("🇩🇪 เยอรมนี\nSkilled Worker Visa\n⚠️ ต้องมี job offer ก่อน",
     "🔍 Job Board", "GermanTechJobs",
     "GermanTechJobs – ABAP Developer Germany",
     "https://germantechjobs.de/en/jobs/ABAP/all",
     "21 jobs ภาษาอังกฤษ OK\nเฉพาะ Tech Germany"),

    ("🇩🇪 เยอรมนี",
     "🔍 Job Board", "WeAreDevelopers – Berlin",
     "WeAreDevelopers – ABAP Jobs Berlin",
     "https://www.wearedevelopers.com/en/jobs/ls/germany/berlin/abap",
     "48+ jobs Berlin\nVisa sponsor ระบุชัด"),

    ("🇩🇪 เยอรมนี",
     "🔍 Job Board", "WeAreDevelopers – ทั่วเยอรมนี",
     "WeAreDevelopers – ABAP Developer Germany",
     "https://www.wearedevelopers.com/en/jobs/s/abap",
     "2,880+ jobs ทั่วโลก\nกรอง Germany ได้"),

    ("🇩🇪 เยอรมนี",
     "🔍 Job Board", "Glassdoor Germany",
     "Glassdoor – ABAP Developer Jobs Germany",
     "https://www.glassdoor.com/Job/germany-abap-developer-jobs-SRCH_IL.0,7_IN96_KO8,22.htm",
     "301 jobs เม.ย. 2026\nกรอง English-speaking"),

    ("🇩🇪 เยอรมนี",
     "🔍 Job Board", "Glassdoor – English only",
     "Glassdoor – ABAP Jobs Germany (English)",
     "https://www.glassdoor.com/Job/germany-developer-english-abap-jobs-SRCH_IL.0,7_IN96_KO8,30.htm",
     "51 jobs ที่ใช้ภาษาอังกฤษ\nไม่ต้องรู้เยอรมัน"),

    ("🇩🇪 เยอรมนี",
     "🔍 Job Board", "Eursap – SAP Recruitment",
     "Eursap – SAP Jobs Germany",
     "https://eursap.eu/sap-recruitment/germany",
     "Recruiter เฉพาะ SAP\nช่วยหางานและ sponsor visa"),

    ("🇩🇪 เยอรมนี",
     "🔍 Job Board", "Arbeitnow (Visa Sponsored)",
     "Arbeitnow – Visa Sponsored Jobs Germany",
     "https://www.arbeitnow.com/visa-sponsorship-jobs",
     "filter 'SAP ABAP'\nระบุ visa sponsorship ชัดเจน"),

    ("🇩🇪 เยอรมนี",
     "🏢 Direct", "SAP Careers – Walldorf",
     "SAP – ABAP Jobs in Germany (Official)",
     "https://jobs.sap.com/go/ABAP-Jobs-in-Germany/889601/",
     "ตำแหน่ง ABAP จาก SAP HQ\nWalldorf โดยตรง"),

    # ─ Singapore EP ────────────────────────────────────────────────
    ("SG_FLAG",),
    ("🇸🇬 สิงคโปร์\nEmployment Pass\n⚠️ ต้องมี job offer ก่อน",
     "🔍 Job Board", "Indeed Singapore",
     "Indeed SG – SAP ABAP Jobs Singapore",
     "https://sg.indeed.com/q-sap-abap-jobs.html",
     "75+ ตำแหน่ง พ.ค. 2026\nApply โดยตรงได้"),

    ("🇸🇬 สิงคโปร์\nEmployment Pass",
     "🔍 Job Board", "JobStreet Singapore",
     "JobStreet SG – SAP ABAP Developer",
     "https://sg.jobstreet.com/sap-abap-developer-jobs",
     "Job board หลัก SEA\nมีทั้ง Junior & Senior"),

    ("🇸🇬 สิงคโปร์\nEmployment Pass",
     "🔍 Job Board", "Glassdoor Singapore",
     "Glassdoor SG – SAP ABAP Jobs",
     "https://www.glassdoor.sg/Job/singapore-sap-abap-jobs-SRCH_IL.0,9_IN217_KO10,18.htm",
     "57 jobs พ.ค. 2026\nดูเงินเดือน + รีวิว"),

    ("🇸🇬 สิงคโปร์\nEmployment Pass",
     "🏢 Direct", "SAP Careers Singapore",
     "SAP – Jobs in Singapore",
     "https://jobs.sap.com/go/SAP-Jobs-in-Singapore/944301/",
     "ตำแหน่งจาก SAP SG โดยตรง"),
]

flag_labels = {
    "AU_FLAG": ("  🇦🇺  ออสเตรเลีย — Work & Holiday Visa Subclass 462 (ไปได้เลย ไม่ต้องมี job offer)", "1565C0"),
    "NZ_FLAG": ("  🇳🇿  นิวซีแลนด์ — Working Holiday Visa (Quota 100/ปี — สมัครเร็ว!)", "1E8449"),
    "DE_FLAG": ("  🇩🇪  เยอรมนี — Skilled Worker Visa (ต้องได้ job offer ก่อน → นายจ้าง sponsor)", "CA6F1E"),
    "SG_FLAG": ("  🇸🇬  สิงคโปร์ — Employment Pass (ต้องได้ job offer ก่อน + SGD 5,000+/เดือน)", "7D3C98"),
}
row_bg = {
    "🇦🇺": ["E8F4FD", "D6EEF8"],
    "🇳🇿": ["E8F9F2", "D5F5E3"],
    "🇩🇪": ["FFF9E8", "FEF9E7"],
    "🇸🇬": ["FDF2F8", "F9EBF6"],
}
counters = {}

r = 3
for item in data:
    if len(item) == 1:
        key = item[0]
        label, bg_col = flag_labels[key]
        flag_hdr(ws1, r, 1, 5, label, bg_col)
        r += 1
        counters = {}
        continue

    country_raw, typ, company, link_label, url, note = item
    flag = country_raw[:2]
    idx = counters.get(flag, 0)
    counters[flag] = idx + 1
    bg = row_bg[flag][idx % 2]

    cell(ws1, r, 1, country_raw, bg=bg, bold=True, wrap=True)
    cell(ws1, r, 2, typ, bg=bg, align="center", wrap=True)
    cell(ws1, r, 3, company, bg=bg, bold=True)
    lnk(ws1, r, 4, f"🔗 {link_label}", url, bg=bg)
    cell(ws1, r, 5, note, bg=bg, wrap=True)
    ws1.row_dimensions[r].height = 38
    r += 1

ws1.column_dimensions["A"].width = 20
ws1.column_dimensions["B"].width = 16
ws1.column_dimensions["C"].width = 22
ws1.column_dimensions["D"].width = 50
ws1.column_dimensions["E"].width = 34
ws1.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2 — แหล่งข้อมูลเงินเดือน (ที่มา)
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("แหล่งข้อมูลเงินเดือน")
ws2.sheet_view.showGridLines = False

t2 = ws2.cell(row=1, column=1,
    value="  📊  แหล่งที่มาข้อมูลเงินเดือน SAP ABAP — ตรวจสอบได้โดยตรง")
t2.fill = PatternFill("solid", fgColor="1B4F72")
t2.font = Font(color="FFFFFF", bold=True, size=13, name="Calibri")
t2.alignment = Alignment(horizontal="left", vertical="center", indent=1)
ws2.merge_cells("A1:D1")
ws2.row_dimensions[1].height = 30

hdr(ws2, 2, 1, "ประเทศ")
hdr(ws2, 2, 2, "แหล่งข้อมูล")
hdr(ws2, 2, 3, "คลิกดูได้เลย")
hdr(ws2, 2, 4, "ตัวเลขที่ได้ (2026)")
ws2.row_dimensions[2].height = 35

salary_sources = [
    ("🇦🇺 ออสเตรเลีย","SalaryExpert (ERI)",
     "SAP ABAP Developer Salary Australia",
     "https://www.salaryexpert.com/salary/job/sap-abap-developer/australia",
     "Avg AUD 196,178/ปี\nEntry AUD 113,132/ปี"),
    ("🇦🇺 ออสเตรเลีย","Indeed AU",
     "SAP ABAP Developer Salary – Indeed AU",
     "https://au.indeed.com/career/sap-abap-developer/salaries",
     "ข้อมูลจาก job postings จริง\nreal-time"),
    ("🇦🇺 ออสเตรเลีย","Glassdoor AU",
     "SAP ABAP Developer Salary – Glassdoor",
     "https://www.glassdoor.com.au/Salaries/sap-abap-developer-salary-SRCH_KO0,18.htm",
     "AUD 108k–196k/ปี\nมีรีวิวจากพนักงาน"),
    ("🇦🇺 ออสเตรเลีย","PayScale AU",
     "SAP ABAP Salary Australia – PayScale",
     "https://www.payscale.com/research/AU/Skill=SAP_ABAP/Salary",
     "แยกตาม experience level\nชัดเจน"),
    ("🇳🇿 นิวซีแลนด์","SalaryExpert (ERI)",
     "SAP ABAP Developer Salary New Zealand",
     "https://www.salaryexpert.com/salary/job/sap-abap-developer/new-zealand",
     "Avg NZD 144,657/ปี\nAuckland NZD 149,348/ปี"),
    ("🇳🇿 นิวซีแลนด์","PayScale NZ",
     "SAP ABAP Salary New Zealand – PayScale",
     "https://www.payscale.com/research/NZ/Skill=SAP_ABAP/Salary",
     "แยกตาม experience\nReal survey data"),
    ("🇩🇪 เยอรมนี","GermanTechJobs Salary",
     "ServiceNow/SAP Developer Salary Germany",
     "https://germantechjobs.de/en/salaries/SAP-ABAP",
     "€42k–95k/ปี\nแยก Junior/Mid/Senior"),
    ("🇩🇪 เยอรมนี","Glassdoor Germany",
     "SAP ABAP Salary Germany – Glassdoor",
     "https://www.glassdoor.com/Salaries/germany-sap-abap-developer-salary-SRCH_IL.0,7_IN96_KO8,27.htm",
     "€50k–85k/ปี avg"),
    ("🇸🇬 สิงคโปร์","SalaryExpert Singapore",
     "SAP ABAP Developer Salary Singapore",
     "https://www.salaryexpert.com/salary/job/sap-abap-developer/singapore",
     "Avg SGD 122,064/ปี\n(~SGD 10,172/เดือน)"),
    ("🇸🇬 สิงคโปร์","Indeed Singapore",
     "SAP ABAP Developer Salary – Indeed SG",
     "https://sg.indeed.com/career/sap-abap-developer/salaries",
     "SGD 6,119/เดือน avg\nfrom real job postings"),
    ("🇸🇬 สิงคโปร์","Glassdoor Singapore",
     "SAP ABAP Salary Singapore – Glassdoor",
     "https://www.glassdoor.sg/Job/singapore-sap-abap-jobs-SRCH_IL.0,9_IN217_KO10,18.htm",
     "57 jobs + salary info"),
    ("💱 อัตราแลกเปลี่ยน","ECB (European Central Bank)",
     "ECB FX Reference Rates June 2026",
     "https://www.ecb.europa.eu/stats/shared/pdf/eurofxref.pdf",
     "1 AUD=23.30฿, 1 NZD=19.18฿\n1 EUR=37.99฿, 1 SGD=25.43฿"),
    ("💱 อัตราแลกเปลี่ยน","OANDA Currency Converter",
     "OANDA – Live Exchange Rates",
     "https://www.oanda.com/currency-converter/en/",
     "เช็คอัตราล่าสุด real-time"),
]

sal_bgs = {
    "🇦🇺": ["E8F4FD","D6EEF8"],
    "🇳🇿": ["E8F9F2","D5F5E3"],
    "🇩🇪": ["FFF9E8","FEF9E7"],
    "🇸🇬": ["FDF2F8","F9EBF6"],
    "💱": ["F4F6F7","EAECEE"],
}
sal_counters = {}

for idx, (country, src, link_label, url, note) in enumerate(salary_sources):
    r2 = idx + 3
    flag = country[:2]
    c2 = sal_counters.get(flag, 0)
    sal_counters[flag] = c2 + 1
    bg = sal_bgs.get(flag, ["FFFFFF","F0F0F0"])[c2 % 2]

    cell(ws2, r2, 1, country, bg=bg, bold=True)
    cell(ws2, r2, 2, src, bg=bg, bold=True)
    lnk(ws2, r2, 3, f"🔗 {link_label}", url, bg=bg)
    cell(ws2, r2, 4, note, bg=bg, wrap=True)
    ws2.row_dimensions[r2].height = 40

ws2.column_dimensions["A"].width = 18
ws2.column_dimensions["B"].width = 24
ws2.column_dimensions["C"].width = 46
ws2.column_dimensions["D"].width = 30

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3 — สมัคร WHV + วีซ่า
# ══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("สมัคร WHV & วีซ่า")
ws3.sheet_view.showGridLines = False

t3 = ws3.cell(row=1, column=1,
    value="  🛂  ลิงก์สมัครวีซ่าทางการ — Work & Holiday + Skilled Worker")
t3.fill = PatternFill("solid", fgColor="1B4F72")
t3.font = Font(color="FFFFFF", bold=True, size=13, name="Calibri")
t3.alignment = Alignment(horizontal="left", vertical="center", indent=1)
ws3.merge_cells("A1:D1")
ws3.row_dimensions[1].height = 30

hdr(ws3, 2, 1, "ประเทศ / ขั้นตอน")
hdr(ws3, 2, 2, "ลิงก์ทางการ")
hdr(ws3, 2, 3, "รายละเอียด")
hdr(ws3, 2, 4, "ค่าธรรมเนียม")
ws3.row_dimensions[2].height = 35

visa_links = [
    ("AU_VF",),
    ("🇦🇺 WHV Subclass 462\nขั้นที่ 1: ดูคุณสมบัติ",
     "Home Affairs – WHV 462 (Official)",
     "https://immi.homeaffairs.gov.au/visas/getting-a-visa/visa-listing/work-holiday-462",
     "เว็บทางการ รัฐบาลออสเตรเลีย\nดูเงื่อนไขทั้งหมด",
     "ดูก่อน ฟรี"),
    ("🇦🇺 WHV Subclass 462\nขั้นที่ 2: สมัครวีซ่า online",
     "ImmiAccount – Apply Online",
     "https://online.immi.gov.au/lusc/login",
     "สร้าง account + ยื่นใบสมัคร\nแนบเอกสารทั้งหมด",
     "AUD 635\n(~14,800 บาท)"),
    ("🇦🇺 WHV Subclass 462\nขั้นที่ 3: คู่มือ WHV คนไทย",
     "IDP – Work & Holiday 2026 Guide Thai",
     "https://ielts.idp.com/thailand/about/news-and-articles/article-work-and-holiday-visa",
     "ข้อมูลสำหรับคนไทยโดยเฉพาะ\nรวมกำหนดการเปิดรับ",
     "ดูฟรี"),
    ("🇦🇺 WHV Subclass 462\nขั้นที่ 4: สมัคร IELTS",
     "IDP Thailand – Register IELTS",
     "https://www.idp.com/thailand/ielts/register/",
     "สอบ IELTS ต้องได้ 4.5+\nสมัครสอบทั่วไทย",
     "~7,000 บาท"),
    ("NZ_VF",),
    ("🇳🇿 WHV นิวซีแลนด์\nข้อมูลสำหรับคนไทย",
     "Immigration NZ – Thailand WHV",
     "https://www.immigration.govt.nz/visas/thailand-working-holiday-visa/",
     "หน้าวีซ่า NZ สำหรับไทยโดยตรง\nQuota 100 คน/ปีเท่านั้น",
     "NZD 165\n(~3,165 บาท)"),
    ("DE_VF",),
    ("🇩🇪 Skilled Worker Visa\nขั้นที่ 1: หางานก่อน",
     "Arbeitnow – Visa Sponsored Jobs",
     "https://www.arbeitnow.com/visa-sponsorship-jobs",
     "หางาน + ให้นายจ้าง\nsponsor visa ให้",
     "ฟรี (นายจ้างช่วย)"),
    ("🇩🇪 Skilled Worker Visa\nขั้นที่ 2: ข้อมูลวีซ่า",
     "Make it in Germany – IT Worker",
     "https://www.make-it-in-germany.com/en/visa-residence/types/skilled-workers-employment",
     "คู่มือ Skilled Worker Visa\nจากรัฐบาลเยอรมัน (ภาษาอังกฤษ)",
     "€100\n(~3,800 บาท)"),
    ("🇩🇪 Skilled Worker Visa\nขั้นที่ 3: ยื่นวีซ่าที่ไทย",
     "สถานทูตเยอรมัน กรุงเทพฯ",
     "https://bangkok.diplo.de/th-en/services/visa",
     "ยื่นวีซ่าที่สถานทูตเยอรมัน\nวิทยุ กรุงเทพฯ",
     "€100\n(นัดหมายล่วงหน้า)"),
    ("SG_VF",),
    ("🇸🇬 Employment Pass\nข้อมูลทางการ",
     "MOM Singapore – Employment Pass",
     "https://www.mom.gov.sg/passes-and-permits/employment-pass",
     "ข้อมูล EP ทางการ\nต้องได้ SGD 5,000+/เดือน",
     "SGD 105\n(~2,670 บาท)\n(นายจ้างยื่นให้)"),
]

vf_bgs = {
    "🇦🇺": ["E8F4FD","D6EEF8"],
    "🇳🇿": ["E8F9F2","D5F5E3"],
    "🇩🇪": ["FFF9E8","FEF9E7"],
    "🇸🇬": ["FDF2F8","F9EBF6"],
}
vf_flags = {
    "AU_VF": ("  🇦🇺  ออสเตรเลีย — Work & Holiday Visa (Subclass 462)", "1565C0"),
    "NZ_VF": ("  🇳🇿  นิวซีแลนด์ — Working Holiday Visa", "1E8449"),
    "DE_VF": ("  🇩🇪  เยอรมนี — Skilled Worker Visa", "CA6F1E"),
    "SG_VF": ("  🇸🇬  สิงคโปร์ — Employment Pass (EP)", "7D3C98"),
}
vf_counters = {}
r3 = 3
for item in visa_links:
    if len(item) == 1:
        label, bg_col = vf_flags[item[0]]
        flag_hdr(ws3, r3, 1, 4, label, bg_col)
        r3 += 1
        vf_counters = {}
        continue
    country_label, src, url, note, fee = item
    flag = country_label[:2]
    c3 = vf_counters.get(flag, 0)
    vf_counters[flag] = c3 + 1
    bg = vf_bgs.get(flag, ["FFFFFF"])[c3 % 2]
    cell(ws3, r3, 1, country_label, bg=bg, bold=True, wrap=True)
    lnk(ws3, r3, 2, f"🔗 {src}", url, bg=bg, bold=True)
    cell(ws3, r3, 3, note, bg=bg, wrap=True)
    cell(ws3, r3, 4, fee, bg=bg, align="center", bold=True,
         color="1A5276", wrap=True)
    ws3.row_dimensions[r3].height = 48
    r3 += 1

ws3.column_dimensions["A"].width = 24
ws3.column_dimensions["B"].width = 44
ws3.column_dimensions["C"].width = 32
ws3.column_dimensions["D"].width = 16

out = "/home/user/fefa/Sources_Apply_Links.xlsx"
wb.save(out)
print(f"Saved: {out}")
