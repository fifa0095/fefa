import openpyxl
from openpyxl.styles import (
    PatternFill, Font, Alignment, Border, Side
)
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ─── Style helpers ────────────────────────────────────────────────────────────
def hdr(ws, row, col, value, bg="1F4E79", fg="FFFFFF", bold=True, size=11, wrap=False):
    c = ws.cell(row=row, column=col, value=value)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color=fg, bold=bold, size=size, name="Calibri")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=wrap)
    thin = Side(style="thin", color="AAAAAA")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    return c

def cell(ws, row, col, value, bg=None, bold=False, wrap=True, align="left", size=10):
    c = ws.cell(row=row, column=col, value=value)
    if bg:
        c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(bold=bold, size=size, name="Calibri")
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    thin = Side(style="thin", color="DDDDDD")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    return c

def section_title(ws, row, col, cols_span, title, bg="2E75B6"):
    c = ws.cell(row=row, column=col, value=title)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=12, name="Calibri")
    c.alignment = Alignment(horizontal="left", vertical="center")
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+cols_span-1)
    return c

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 1: Work & Holiday Visa
# ══════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "1_Work&Holiday Visa"
ws1.sheet_view.showGridLines = False
ws1.row_dimensions[1].height = 30

section_title(ws1, 1, 1, 9, "  🌏  Work & Holiday Visa สำหรับคนไทย — ตำแหน่ง SAP ABAP & ServiceNow")

headers_whv = [
    "ประเทศ", "วีซ่าประเภท", "อายุ", "Quota/ปี",
    "คุณสมบัติหลัก", "หา SAP ABAP ได้", "หา ServiceNow ได้",
    "เงินเดือนเฉลี่ย (SAP ABAP)", "หมายเหตุ"
]
for i, h in enumerate(headers_whv, 1):
    hdr(ws1, 2, i, h, bg="1F4E79", wrap=True)

whv_data = [
    ["🇦🇺 ออสเตรเลีย", "Work & Holiday\n(Subclass 462)", "18–30 ปี", "~500–1,000",
     "• ปริญญาตรีขึ้นไป\n• IELTS 4.5+\n• Bank statement\n• Travel plan",
     "✅ ใช่\n(SAP, Deloitte,\nAccenture, Infosys)",
     "✅ ใช่\n(EY, Accenture,\nInfosys, KPMG)",
     "AUD 85,000–200,000+/ปี\n(ServiceNow: AUD 114,000–285,000)",
     "ทำงานกับนายจ้างเดียวได้\nไม่เกิน 6 เดือน\nต่อยอดสู่ Subclass 482"],
    ["🇳🇿 นิวซีแลนด์", "Working Holiday\nVisa", "18–30 ปี", "⚠️ 100 คน/ปี\n(จำกัดมาก)",
     "• ปริญญาตรี 3 ปีขึ้นไป\n• มีเงินทุนพอ",
     "⚠️ หายาก\n(ตลาดเล็ก)",
     "⚠️ หายาก\n(ตลาดเล็ก)",
     "NZD 75,000–130,000/ปี",
     "Quota น้อยมาก\nแข่งขันสูง\nเหมาะเป็นทางเลือกสำรอง"],
    ["🇯🇵 ญี่ปุ่น", "Working Holiday\nVisa", "18–30 ปี", "N/A",
     "N/A",
     "❌ ไม่ได้\n(ไทยไม่มี bilateral\nagreement)",
     "❌ ไม่ได้",
     "—",
     "ไทยไม่อยู่ใน 32 ประเทศ\nที่ญี่ปุ่นรับ WHV"],
    ["🇸🇬 สิงคโปร์", "Work Holiday\nProgramme", "18–25 ปี", "N/A",
     "N/A",
     "❌ ไม่ได้\n(เฉพาะ AU/FR/DE/\nHK/JP/NZ/CH/UK/US)",
     "❌ ไม่ได้",
     "—",
     "ต้องใช้ Employment Pass\nแทน (ต้องมีประสบการณ์)"],
    ["🇩🇪 เยอรมนี", "ไม่มี WHV\n→ ใช้ Skilled\nWorker Visa", "ไม่จำกัด", "ไม่จำกัด",
     "• ประสบการณ์ SAP/ServiceNow\n• ปริญญาตรี IT\n• ภาษาอังกฤษ B2+\n• นายจ้างรับรอง",
     "✅ ใช่ (มาก)\n(SAP HQ อยู่ที่นี่\nขาด IT 109,000 ตน.)",
     "✅ ใช่\n(ขาดแคลนสูง)",
     "SAP ABAP: €42,000–95,000/ปี\nServiceNow: €46,000–63,000/ปี",
     "Germany Immigration Act 2025\nง่ายขึ้นมากสำหรับ\n non-EU IT specialist"],
]

row_colors = ["F2F7FF", "FFFFFF"]
for i, row_data in enumerate(whv_data):
    bg = row_colors[i % 2]
    for j, val in enumerate(row_data, 1):
        c = cell(ws1, i+3, j, val, bg=bg, wrap=True)
        if j == 1:
            c.font = Font(bold=True, size=10, name="Calibri")

col_widths_1 = [16, 16, 10, 14, 32, 22, 22, 32, 30]
for i, w in enumerate(col_widths_1, 1):
    ws1.column_dimensions[get_column_letter(i)].width = w

for r in range(3, 8):
    ws1.row_dimensions[r].height = 80

ws1.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 2: Internship Programs
# ══════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("2_Internship Programs")
ws2.sheet_view.showGridLines = False
ws2.row_dimensions[1].height = 30

section_title(ws2, 1, 1, 9, "  🎓  Internship Programs ต่างประเทศ — SAP ABAP & ServiceNow (คนไทย)")

headers_int = [
    "สาย", "บริษัท / โปรแกรม", "ประเทศ", "ตำแหน่ง",
    "ระยะเวลา", "คุณสมบัติหลัก", "Visa Support", "เงินเดือน/เดือน", "ลิงก์ / หมายเหตุ"
]
for i, h in enumerate(headers_int, 1):
    hdr(ws2, 2, i, h, bg="1F4E79", wrap=True)

intern_data = [
    # SAP ABAP
    ["SAP ABAP", "SAP iXp\n(Internship Experience\nProgram)", "🇩🇪 เยอรมนี\n(Walldorf / Berlin)",
     "iXp Intern –\nBTP ABAP AI Developer\n/ ABAP Developer",
     "10–12 สัปดาห์\n(summer) หรือ\n6 เดือน (working student)",
     "• Enrolled student\n• มี valid student visa\n• ส่ง CV + transcript\n+ cover letter\n• ABAP ไม่บังคับ (สอนให้)",
     "ต้องมี student visa\n(ต้องเรียนในเยอรมนีอยู่\nหรือผ่าน exchange)",
     "ไม่เปิดเผย\n(~€800–1,200/เดือน)",
     "jobs.sap.com/content/internships\n\n⭐ เหมาะนักศึกษา\nexchange ที่เยอรมนี"],
    ["SAP ABAP", "Accenture\nSAP ABAP Internship", "🇵🇱 โปแลนด์\n(Wrocław / Warsaw)",
     "SAP ABAP Internship\nProgram",
     "3–6 เดือน",
     "• กำลังเรียนปริญญาตรี/โท IT\n• ABAP ไม่บังคับ (สอนให้)\n• ภาษาอังกฤษ\n• ความสนใจ ERP",
     "ต้องมี EU work permit\nหรือ student visa โปแลนด์",
     "~PLN 3,500–5,000/เดือน\n(~€800–1,150)",
     "accenture.com/pl-en/careers\n\nID: R00292609\n\n⭐ ไม่ต้องมีประสบการณ์"],
    ["SAP ABAP", "SAP SE\n(Official Internship)", "🇺🇸 สหรัฐอเมริกา\n(Palo Alto / NYC)",
     "SAP ABAP / Software\nEngineer Intern",
     "12 สัปดาห์\n(June–August)",
     "• นักศึกษา CS/IT/SE\n• F-1 visa (CPT/OPT)\nหรือ visa sponsorship\n• GPA สูง",
     "F-1 CPT/OPT สำหรับ\nnon-US students\n(H-1B lottery สำหรับ\nfull-time)",
     "~$50–$70/ชั่วโมง\n(~$8,000–11,200/เดือน)",
     "jobs.sap.com\n\n⭐ เงินเดือนสูงสุด\nแต่แข่งขันสูงมาก"],
    ["SAP ABAP", "Deloitte / KPMG /\nCapgemini", "🇦🇺 ออสเตรเลีย\n🇸🇬 สิงคโปร์",
     "SAP Graduate /\nJunior Consultant",
     "Grad Program\n2–3 ปี",
     "• ปริญญาตรี IT/Business\n• SAP certificate\nเป็น advantage\n• Work rights ในประเทศ",
     "ออสเตรเลีย: WHV ใช้ได้\nสิงคโปร์: Employment Pass",
     "AU: AUD 65,000–85,000/ปี\nSG: SGD 48,000–70,000/ปี",
     "deloitte.com/careers\nkpmg.com/careers\n\n⭐ WHV ออสเตรเลีย\nสมัครได้โดยตรง"],
    # ServiceNow
    ["ServiceNow", "ServiceNow Official\nInternship Program", "🇸🇬 สิงคโปร์\n(APAC HQ)",
     "Intern – AI Foundry\nEngineer / Associate\nSolution Consultant",
     "12 สัปดาห์\n(แบบ rolling)",
     "• Enrolled student\nCS/IS/SE/AI/Data Science\n• ServiceNow fundamentals\n  (ผ่าน SNow university)\n• ภาษาอังกฤษ",
     "ต้องมี student visa\nหรือ work authorization\nสิงคโปร์\n(Thai ต้อง apply EP/DP)",
     "SGD 1,500–3,500/เดือน",
     "careers.servicenow.com\n\nID: 744000118558930\n(AI Foundry Singapore)\n\n⚠️ Acceptance rate <8%"],
    ["ServiceNow", "ServiceNow Official\nInternship Program", "🇺🇸 สหรัฐอเมริกา\n(Santa Clara / NYC)",
     "Software Engineer\nIntern / Platform\nDeveloper Intern",
     "12 สัปดาห์\n(June–August)",
     "• Enrolled student\nCS/SE/IS\n• ITSM/ITIL knowledge\n• ภาษาอังกฤษ\n• JavaScript / REST",
     "F-1 CPT/OPT\nH-1B lottery\n(full-time)",
     "~$53/ชั่วโมง\n(~$8,500/เดือน)",
     "careers.servicenow.com/\nearly-careers\n\n⭐ เงินดีมาก\nต้องมี US student status"],
    ["ServiceNow", "EY / Accenture /\nDeloitte Australia\n(ServiceNow Practice)", "🇦🇺 ออสเตรเลีย",
     "ServiceNow Graduate /\nJunior Developer",
     "Grad Program\n2–3 ปี",
     "• ปริญญาตรี IT/Business\n• ServiceNow CSA\n  certification เป็น plus\n• Work rights ในออสเตรเลีย",
     "✅ WHV (Subclass 462)\nใช้สมัครได้",
     "AUD 65,000–90,000/ปี\n(ServiceNow: AUD 114,000+\nเมื่อ senior)",
     "ey.com/en_au/careers/\nservicenow-student-opportunities\n\n⭐ WHV ออสเตรเลีย\nใช้สมัครได้โดยตรง"],
    ["ServiceNow", "Consulting Firms\n(Europe)", "🇩🇪 เยอรมนี\n🇳🇱 เนเธอร์แลนด์\n🇬🇧 สหราชอาณาจักร",
     "ServiceNow\nJunior Developer /\nFunctional Consultant",
     "Permanent / Contract",
     "• ประสบการณ์ ServiceNow\n• CSA / CIS certification\n• ภาษาอังกฤษ B2+\n• ไม่ต้องรู้ภาษาท้องถิ่น",
     "Skilled Worker Visa\nSponsorship พร้อม\n(55% demand surge)",
     "DE: €46,000–63,000/ปี\nNL/UK: £50,000–75,000/ปี",
     "remoterocketship.com/\ncountry/europe/jobs/\nservicenow-developer\n\ntotaljobs.com (Europe)"],
]

row_colors = ["F2F7FF", "FFFFFF"]
abap_color = "E8F4FD"
sn_color = "FFF3E0"

for i, row_data in enumerate(intern_data):
    r = i + 3
    bg = abap_color if row_data[0] == "SAP ABAP" else sn_color
    for j, val in enumerate(row_data, 1):
        c = cell(ws2, r, j, val, bg=bg, wrap=True)
        if j == 1:
            label_bg = "1F4E79" if row_data[0] == "SAP ABAP" else "BF5700"
            c.fill = PatternFill("solid", fgColor=label_bg)
            c.font = Font(color="FFFFFF", bold=True, size=9, name="Calibri")
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

col_widths_2 = [12, 22, 18, 22, 18, 32, 24, 22, 34]
for i, w in enumerate(col_widths_2, 1):
    ws2.column_dimensions[get_column_letter(i)].width = w

for r in range(3, 11):
    ws2.row_dimensions[r].height = 90

ws2.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 3: Salary Comparison
# ══════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("3_เงินเดือนเปรียบเทียบ")
ws3.sheet_view.showGridLines = False
ws3.row_dimensions[1].height = 30

section_title(ws3, 1, 1, 8, "  💰  เงินเดือนเปรียบเทียบ SAP ABAP vs ServiceNow ต่างประเทศ (2025–2026)")

headers_sal = [
    "ประเทศ", "สกุลเงิน",
    "SAP ABAP Entry-Level", "SAP ABAP Mid-Level", "SAP ABAP Senior",
    "ServiceNow Entry-Level", "ServiceNow Mid-Level", "ServiceNow Senior"
]
for i, h in enumerate(headers_sal, 1):
    hdr(ws3, 2, i, h, bg="1F4E79", wrap=True)

sal_data = [
    ["🇺🇸 สหรัฐอเมริกา", "USD/ปี", "$55,000–70,000", "$80,000–100,000", "$100,000–130,000+",
     "$70,000–85,000", "$95,000–120,000", "$130,000–160,000+"],
    ["🇦🇺 ออสเตรเลีย", "AUD/ปี", "85,000–100,000", "100,000–150,000", "150,000–200,000+",
     "114,000–140,000", "140,000–200,000", "200,000–285,000+"],
    ["🇩🇪 เยอรมนี", "EUR/ปี", "42,000–52,000", "55,000–72,000", "75,000–95,000+",
     "46,000–55,000", "55,000–68,000", "70,000–90,000+"],
    ["🇸🇬 สิงคโปร์", "SGD/ปี", "50,000–65,000", "70,000–90,000", "90,000–120,000+",
     "60,000–80,000", "80,000–100,000", "100,000–140,000+"],
    ["🇳🇿 นิวซีแลนด์", "NZD/ปี", "65,000–80,000", "80,000–110,000", "110,000–130,000+",
     "70,000–90,000", "90,000–115,000", "115,000–150,000+"],
    ["🇬🇧 สหราชอาณาจักร", "GBP/ปี", "35,000–45,000", "50,000–65,000", "65,000–90,000+",
     "40,000–55,000", "55,000–75,000", "75,000–100,000+"],
    ["🇹🇭 ไทย (อ้างอิง)", "THB/ปี", "300,000–500,000", "600,000–900,000", "900,000–1,500,000+",
     "350,000–550,000", "600,000–900,000", "900,000–1,500,000+"],
]

row_colors = ["F2F7FF", "FFFFFF"]
for i, row_data in enumerate(sal_data):
    bg = row_colors[i % 2]
    if row_data[0] == "🇹🇭 ไทย (อ้างอิง)":
        bg = "FFF9C4"
    for j, val in enumerate(row_data, 1):
        c = cell(ws3, i+3, j, val, bg=bg, wrap=True, align="center")
        if j == 1:
            c.font = Font(bold=True, size=10, name="Calibri")
            c.alignment = Alignment(horizontal="left", vertical="center")

col_widths_3 = [20, 12, 22, 22, 22, 22, 22, 22]
for i, w in enumerate(col_widths_3, 1):
    ws3.column_dimensions[get_column_letter(i)].width = w

for r in range(2, 11):
    ws3.row_dimensions[r].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 4: Skills & Job Market
# ══════════════════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet("4_Skills & Job Market")
ws4.sheet_view.showGridLines = False
ws4.row_dimensions[1].height = 30

section_title(ws4, 1, 1, 3, "  📊  SAP ABAP vs ServiceNow — ทักษะ & ตลาดงานต่างประเทศ")

hdr(ws4, 2, 1, "หัวข้อ", bg="1F4E79")
hdr(ws4, 2, 2, "SAP ABAP", bg="1F4E79")
hdr(ws4, 2, 3, "ServiceNow", bg="1F4E79")

compare_data = [
    ["ภาพรวมตลาด\n(2025–2026)", "• Global demand สูงมาก\n• SAP S/4HANA migration ยังต้องการ ABAP\n• ขาดแคลนผู้เชี่ยวชาญทั่วโลก\n• Germany: ขาด IT 109,000 ตำแหน่ง",
     "• 55% surge in demand YoY\n• Supply < Demand ทั่วโลก\n• AI + ITSM adoption พุ่ง\n• LinkedIn: 1,000+ jobs worldwide"],
    ["หางานต่างประเทศ\nง่ายแค่ไหน", "⭐⭐⭐⭐ ง่ายมาก\n• มี SAP offices 130+ ประเทศ\n• Consulting firms ทุกแห่งจ้าง\n• Visa sponsorship พร้อม (EU/AU)",
     "⭐⭐⭐⭐⭐ ง่ายกว่า!\n• Market ใหม่กว่า ขาดคนมาก\n• ไม่จำกัด industry\n• Remote-friendly มากกว่า"],
    ["ประเทศที่มีงานมาก\nสำหรับคนไทย", "1. ออสเตรเลีย (WHV ได้)\n2. เยอรมนี (Skilled Visa)\n3. สิงคโปร์ (Employment Pass)\n4. สหรัฐฯ (H-1B)\n5. สหราชอาณาจักร",
     "1. ออสเตรเลีย (WHV ได้) ⭐\n2. สิงคโปร์ (APAC HQ)\n3. สหรัฐฯ (HQ ที่ Santa Clara)\n4. เยอรมนี (55 jobs open)\n5. เนเธอร์แลนด์"],
    ["ทักษะที่ต้องมี\n(Entry Level)", "• ABAP programming พื้นฐาน\n• SAP architecture\n• BAPI/BADI/RFC\n• SAP Fiori/UI5 (plus)\n• BTP/RAP (plus++)\n• SQL / Database",
     "• JavaScript / Glide API\n• ITSM/ITIL knowledge\n• REST API / JSON\n• HTML/CSS พื้นฐาน\n• ServiceNow CSA cert\n• Integration Hub (plus)"],
    ["Certification\nที่แนะนำ", "• SAP Certified Associate –\n  ABAP with SAP NetWeaver\n• SAP S/4HANA Developer\n• SAP BTP Associate\n→ ค่าสอบ ~$550 USD",
     "• ServiceNow CSA\n  (Certified System Admin) ⭐\n• ServiceNow CIS\n  (Certified Implementation Spec)\n→ ค่าสอบ ~$250–350 USD\n→ ✅ ถูกกว่า + ได้งานเร็วกว่า"],
    ["ระยะเวลาเตรียมตัว\nถึงระดับ Internship", "6–12 เดือน\n(ต้องเรียน SAP system + ABAP)\nต้องมี SAP license (แพง)\nหรือใช้ SAP BTP free tier",
     "3–6 เดือน ⭐\n(ServiceNow Developer Portal\nฟรีทั้งหมด! PDI free)\nทำ portfolio บน personal instance\nได้ทันที"],
    ["ค่าใช้จ่ายในการเรียน", "• SAP ABAP training: $500–3,000\n• SAP certification: ~$550/ครั้ง\n• SAP license: แพงมาก\n  (ใช้ BTP trial แทน)",
     "• ServiceNow training: ฟรี!\n  (developer.servicenow.com)\n• CSA certification: ~$250\n• PDI (Personal Dev Instance):\n  ฟรีสมบูรณ์ ⭐⭐⭐"],
    ["Remote Work\nAvailability", "⭐⭐⭐ ทำได้\nแต่มักต้องอยู่ใกล้ client site\n(SAP implementation = onsite)\nRemote Europe jobs มีแต่น้อย",
     "⭐⭐⭐⭐⭐ Remote-friendly มาก\nงาน remote ServiceNow Europe\nมี 1,000+ ตำแหน่งใน LinkedIn\nบริษัทหลายแห่ง fully remote"],
    ["สรุปคำแนะนำ", "✅ เหมาะถ้า:\n• มีพื้นฐาน ERP/Business Process\n• ต้องการทำงานในบริษัทขนาดใหญ่\n• ชอบ Germany/Europe\n• เป้าหมาย: WHV ออสเตรเลีย\nแล้ว transition สู่ SAP consultant",
     "✅ เหมาะถ้า:\n• ต้องการเริ่มเร็ว (3–6 เดือน)\n• งบเตรียมตัวน้อย (ฟรี!)\n• ต้องการ remote work\n• ชอบ Singapore / Australia\n• เป้าหมาย: ServiceNow APAC\nหรือ Global remote role"],
]

abap_col = "E8F4FD"
sn_col = "FFF3E0"
topic_col = "EEF2F7"

for i, row_data in enumerate(compare_data):
    r = i + 3
    ws4.row_dimensions[r].height = 90
    cell(ws4, r, 1, row_data[0], bg=topic_col, bold=True, wrap=True, align="center")
    cell(ws4, r, 2, row_data[1], bg=abap_col, wrap=True)
    cell(ws4, r, 3, row_data[2], bg=sn_col, wrap=True)

ws4.column_dimensions["A"].width = 22
ws4.column_dimensions["B"].width = 48
ws4.column_dimensions["C"].width = 48
ws4.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 5: Action Plan
# ══════════════════════════════════════════════════════════════════════════════
ws5 = wb.create_sheet("5_Action Plan คนไทย")
ws5.sheet_view.showGridLines = False
ws5.row_dimensions[1].height = 30

section_title(ws5, 1, 1, 4, "  🗺️  Action Plan — เส้นทางสู่งาน SAP ABAP / ServiceNow ต่างประเทศ สำหรับคนไทย")

hdr(ws5, 2, 1, "เส้นทาง", bg="1F4E79")
hdr(ws5, 2, 2, "ขั้นตอน (Timeline)", bg="1F4E79")
hdr(ws5, 2, 3, "ประเทศเป้าหมาย", bg="1F4E79")
hdr(ws5, 2, 4, "งบประมาณ / หมายเหตุ", bg="1F4E79")

plan_data = [
    ["🅐 SAP ABAP\n→ ออสเตรเลีย\n(WHV Route)\n[แนะนำมากที่สุด\nสำหรับ SAP ABAP]",
     "เดือน 1–4: เรียน SAP ABAP บน BTP free / Udemy\nเดือน 5–6: สอบ SAP Certified Associate\nเดือน 7–8: สมัคร WHV Subclass 462\n         (IELTS 4.5 + ปริญญาตรี + bank)\nเดือน 9–12: เดินทาง หางาน SAP junior/intern\n            ใน Sydney/Melbourne\nปีที่ 2: ขอ Subclass 482 ผ่านนายจ้าง",
     "🇦🇺 ออสเตรเลีย\n(Sydney, Melbourne,\nBrisbane, Perth)",
     "ค่า IELTS: ~7,000 บาท\nค่าวีซ่า WHV: ~9,000 บาท\nSAP Cert: ~20,000 บาท\nตั๋วเครื่องบิน + ที่พักเริ่มต้น\n~80,000–120,000 บาท\n\n⚠️ WHV ปิดรับปี 2025 แล้ว\n→ เตรียมสมัครปี 2026"],
    ["🅑 ServiceNow\n→ ออสเตรเลีย\n(WHV Route)\n[เริ่มเร็วที่สุด\nค่าใช้จ่ายน้อย]",
     "เดือน 1–2: เรียนบน developer.servicenow.com (ฟรี)\n           สร้าง Personal Dev Instance (ฟรี)\nเดือน 3: สอบ ServiceNow CSA (~$250)\nเดือน 4–5: ทำ portfolio projects บน PDI\nเดือน 6: สมัคร WHV + IELTS\nเดือน 7–8: เดินทางออสเตรเลีย\nเดือน 9+: สมัคร ServiceNow junior\n           ที่ EY / Accenture / Deloitte AU",
     "🇦🇺 ออสเตรเลีย\n(เน้น Sydney)\n+ option\n🇸🇬 สิงคโปร์\n(ถ้าไม่ใช้ WHV)",
     "ServiceNow training: ฟรี! ⭐\nCSA cert: ~8,500 บาท\nค่าวีซ่า WHV: ~9,000 บาท\nIELTS: ~7,000 บาท\n\n✅ รวมถูกกว่าเส้นทาง A\nมาก (~40,000 บาทน้อยกว่า)"],
    ["🅒 SAP iXp Internship\n→ เยอรมนี\n(สำหรับ\nนักศึกษา\nที่ยังเรียนอยู่)",
     "ขณะเรียน ม.:\nเดือน 1–3: สมัคร exchange program\n           ไปมหาวิทยาลัยเยอรมัน\nเดือน 4–6: เรียนที่เยอรมนี ได้ student visa\nเดือน 7: สมัคร SAP iXp ABAP intern\n          ที่ jobs.sap.com (Walldorf)\nเดือน 8–13: ฝึกงานที่ SAP HQ\nหลังจบ: สมัคร Skilled Worker Visa",
     "🇩🇪 เยอรมนี\n(Walldorf, Berlin,\nMunich)",
     "ต้องมีสถานะ enrolled student\nค่าเรียน exchange: แล้วแต่มหา.\nSAP iXp: paid internship\n~€800–1,200/เดือน\n\n⭐ เหมาะนักศึกษา ปี 3–4\nหรือ Master's student"],
    ["🅓 ServiceNow\n→ สิงคโปร์\n(Internship Direct)\n[สำหรับนักศึกษา]",
     "เดือน 1–2: เรียน ServiceNow ฟรี + สร้าง portfolio\nเดือน 3: สอบ CSA\nเดือน 4: สมัคร ServiceNow internship SG\n          ที่ careers.servicenow.com\nเดือน 5: สัมภาษณ์ (multi-stage 3–6 สัปดาห์)\nเดือน 6–9: ฝึกงานที่สิงคโปร์\n           (AI Foundry / Solution Consultant)\nหลังฝึกงาน: convert เป็น full-time + EP",
     "🇸🇬 สิงคโปร์\n(ServiceNow APAC HQ)",
     "CSA cert: ~8,500 บาท\nตั๋ว BKK-SIN: ~5,000–8,000 บาท\nที่พักสิงคโปร์: แพงมาก\n~SGD 800–1,500/เดือน\n\n⚠️ แข่งขันสูงมาก\nAcceptance rate <8%\nต้องมี portfolio แน่นมาก"],
    ["🅔 Skilled Worker\nVisa → เยอรมนี\n(มีประสบการณ์\n1–3 ปีขึ้นไป)",
     "ขั้นตอน:\n1. มีประสบการณ์ SAP ABAP / ServiceNow 1–3 ปี\n2. มี certification ที่เกี่ยวข้อง\n3. หางานผ่าน LinkedIn / EURES / GermanTechJobs\n4. ได้ job offer → นายจ้าง sponsor Skilled Worker Visa\n5. ยื่น visa ที่สถานทูตเยอรมัน กรุงเทพฯ\n6. Processing ~4–12 สัปดาห์",
     "🇩🇪 เยอรมนี\n(ทุกเมืองหลัก)\n\n🇳🇱 เนเธอร์แลนด์\n🇬🇧 สหราชอาณาจักร",
     "ค่า visa: €100\nImmigration Act 2025:\nง่ายขึ้นมากสำหรับ non-EU IT\n\nSAP ABAP: €42k–95k/ปี\nServiceNow: €46k–90k/ปี\n\nทั้งสองสายได้งานง่ายมาก\nในยุโรปปี 2025–2026"],
]

plan_colors = ["E8F4FD", "FFF3E0", "E8F4FD", "FFF3E0", "E8F9F2"]
for i, row_data in enumerate(plan_data):
    r = i + 3
    ws5.row_dimensions[r].height = 120
    for j, val in enumerate(row_data, 1):
        c = cell(ws5, r, j, val, bg=plan_colors[i], wrap=True)
        if j == 1:
            c.font = Font(bold=True, size=10, name="Calibri")
            c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

ws5.column_dimensions["A"].width = 20
ws5.column_dimensions["B"].width = 52
ws5.column_dimensions["C"].width = 22
ws5.column_dimensions["D"].width = 34
ws5.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# SHEET 6: Quick Reference
# ══════════════════════════════════════════════════════════════════════════════
ws6 = wb.create_sheet("6_Quick Reference")
ws6.sheet_view.showGridLines = False

section_title(ws6, 1, 1, 3, "  🔗  Quick Reference — ลิงก์สมัครงานและทรัพยากรสำคัญ")

hdr(ws6, 2, 1, "หมวด", bg="1F4E79")
hdr(ws6, 2, 2, "แหล่งข้อมูล / ลิงก์", bg="1F4E79")
hdr(ws6, 2, 3, "หมายเหตุ", bg="1F4E79")

quick_data = [
    ["SAP ABAP\nInternship", "jobs.sap.com/content/internships\njobs.sap.com/go/Intern-Jobs-in-Germany/902401", "SAP iXp Program – Germany\nสมัครผ่าน SAP Careers"],
    ["SAP ABAP\nInternship", "accenture.com/pl-en/careers → R00292609", "Accenture SAP ABAP Intern – Poland\nไม่ต้องมีประสบการณ์ สอนให้"],
    ["ServiceNow\nInternship", "careers.servicenow.com/early-careers\ncareers.servicenow.com/locations/apj/singapore", "ServiceNow Official Program\nSingapore APAC HQ"],
    ["ServiceNow\nInternship", "ey.com/en_au/careers/servicenow-student-opportunities", "EY Australia – ServiceNow\nGraduate Program (WHV ใช้ได้)"],
    ["Work & Holiday\nออสเตรเลีย", "homeaffairs.gov.au → Subclass 462\nielts.idp.com/thailand (WHV guide)", "คนไทย อายุ 18–30\nIELTS 4.5 + ปริญญาตรี"],
    ["Work & Holiday\nนิวซีแลนด์", "immigration.govt.nz/visas/thailand-working-holiday-visa", "Quota 100/ปี เท่านั้น\nสมัครเร็ว ปิดเร็ว"],
    ["SAP ABAP\nเรียนฟรี", "learning.sap.com (SAP Learning Hub)\ndevelopers.sap.com (BTP free tier)", "บางคอร์สฟรี\nใช้ BTP free tier ได้"],
    ["ServiceNow\nเรียนฟรี ⭐", "developer.servicenow.com\nnowlearning.servicenow.com", "Personal Dev Instance ฟรี!\nคอร์สฟรีครบ ไม่ต้องจ่ายเลย"],
    ["หางาน SAP\nต่างประเทศ", "eursap.eu/jobs (Europe)\njooble.org → SAP abroad\nindeed.com → SAP ABAP visa sponsorship", "Jobs board เฉพาะ SAP\nยุโรปโดยเฉพาะ"],
    ["หางาน ServiceNow\nต่างประเทศ", "remoterocketship.com/country/europe/jobs/servicenow-developer\ntotaljobs.com → ServiceNow Europe\nLinkedIn → ServiceNow jobs worldwide", "1,000+ remote Europe jobs\nLinkedIn มีมากที่สุด"],
    ["Germany Tech Jobs", "germantechjobs.de\ndevjobs.de\narbeitsagentur.de (official German job agency)", "งาน SAP + ServiceNow เยอรมนี\nภาษาอังกฤษ OK"],
    ["Certification\nSAP", "training.sap.com → Associate ABAP exam\nC_TAW12_750 (ABAP with NetWeaver)", "~$550 USD/ครั้ง\nแนะนำสอบก่อนไปต่างประเทศ"],
    ["Certification\nServiceNow ⭐", "nowlearning.servicenow.com → CSA exam\nCertified System Administrator", "~$250 USD\nถูกกว่า SAP + ใช้ได้ทั่วโลก\nสอบ online ได้เลย"],
    ["Salary Research", "levels.fyi → SAP / ServiceNow\ngermantechjobs.de/en/salaries/ServiceNow\nglassdoor.com → SAP ABAP Germany", "เช็คเงินเดือนก่อนต่อรอง\nตามประเทศเป้าหมาย"],
]

row_colors = ["F2F7FF", "FFFFFF"]
section_colors = {
    "SAP ABAP\nInternship": "E8F4FD",
    "ServiceNow\nInternship": "FFF3E0",
    "Work & Holiday\nออสเตรเลีย": "E8F9F2",
    "Work & Holiday\nนิวซีแลนด์": "E8F9F2",
    "SAP ABAP\nเรียนฟรี": "E8F4FD",
    "ServiceNow\nเรียนฟรี ⭐": "FFF3E0",
    "หางาน SAP\nต่างประเทศ": "E8F4FD",
    "หางาน ServiceNow\nต่างประเทศ": "FFF3E0",
    "Germany Tech Jobs": "EEF2F7",
    "Certification\nSAP": "E8F4FD",
    "Certification\nServiceNow ⭐": "FFF3E0",
    "Salary Research": "EEF2F7",
}

for i, row_data in enumerate(quick_data):
    r = i + 3
    bg = section_colors.get(row_data[0], "FFFFFF")
    for j, val in enumerate(row_data, 1):
        c = cell(ws6, r, j, val, bg=bg, wrap=True)
        if j == 1:
            c.font = Font(bold=True, size=10, name="Calibri")
    ws6.row_dimensions[r].height = 45

ws6.column_dimensions["A"].width = 22
ws6.column_dimensions["B"].width = 55
ws6.column_dimensions["C"].width = 38
ws6.row_dimensions[2].height = 35

# ══════════════════════════════════════════════════════════════════════════════
# Save
# ══════════════════════════════════════════════════════════════════════════════
output = "/home/user/fefa/SAP_ABAP_vs_ServiceNow_Opportunities.xlsx"
wb.save(output)
print(f"Saved: {output}")
