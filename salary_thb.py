import openpyxl
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

wb = openpyxl.Workbook()

# ── Exchange rates June 2026 (from ECB) ──────────────────────────────────────
AUD = 23.30   # 1 AUD = 23.30 THB
NZD = 19.18   # 1 NZD = 19.18 THB
EUR = 37.99   # 1 EUR = 37.99 THB
SGD = 25.43   # 1 SGD = 25.43 THB

def to_thb_month(annual_local, rate):
    return round((annual_local / 12) * rate)

def fmt(n):
    return f"{n:,.0f}"

# ── Styles ────────────────────────────────────────────────────────────────────
def hdr(ws, row, col, val, bg="1F4E79", size=11, span=1):
    c = ws.cell(row=row, column=col, value=val)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=size, name="Calibri")
    c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    thin = Side(style="thin", color="888888")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    if span > 1:
        ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+span-1)
    return c

def cell(ws, row, col, val, bg="FFFFFF", bold=False, color="222222",
         align="left", size=10, wrap=True):
    c = ws.cell(row=row, column=col, value=val)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(bold=bold, size=size, name="Calibri", color=color)
    c.alignment = Alignment(horizontal=align, vertical="center", wrap_text=wrap)
    thin = Side(style="thin", color="CCCCCC")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    return c

def money(ws, row, col, val, bg="FFFFFF", color="1A5276", bold=False):
    c = ws.cell(row=row, column=col, value=val)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(bold=bold, size=10, name="Calibri", color=color)
    c.alignment = Alignment(horizontal="right", vertical="center")
    thin = Side(style="thin", color="CCCCCC")
    c.border = Border(left=thin, right=thin, top=thin, bottom=thin)

def sec(ws, row, col, span, title, bg="1B4F72"):
    c = ws.cell(row=row, column=col, value=title)
    c.fill = PatternFill("solid", fgColor=bg)
    c.font = Font(color="FFFFFF", bold=True, size=13, name="Calibri")
    c.alignment = Alignment(horizontal="left", vertical="center", indent=1)
    ws.merge_cells(start_row=row, start_column=col, end_row=row, end_column=col+span-1)
    ws.row_dimensions[row].height = 30

# ═════════════════════════════════════════════════════════════════════════════
# SHEET 1 — ตารางงาน SAP ABAP (WHV + Graduate Program)
# ═════════════════════════════════════════════════════════════════════════════
ws1 = wb.active
ws1.title = "ตารางงาน SAP ABAP"
ws1.sheet_view.showGridLines = False

sec(ws1, 1, 1, 12,
    "  💼  ตำแหน่งงาน SAP ABAP ที่ทำได้ด้วย Work & Holiday / Graduate Program — แผนปีหน้า (2027)")

# Sub-header row 2: currency note
c = ws1.cell(row=2, column=1,
    value="  อัตราแลกเปลี่ยน ณ มิถุนายน 2569:  1 AUD = 23.30 ฿  |  1 NZD = 19.18 ฿  |  1 EUR = 37.99 ฿  |  1 SGD = 25.43 ฿")
c.fill = PatternFill("solid", fgColor="D6EAF8")
c.font = Font(bold=True, size=10, name="Calibri", color="1A5276")
c.alignment = Alignment(horizontal="left", vertical="center")
ws1.merge_cells(start_row=2, start_column=1, end_row=2, end_column=12)
ws1.row_dimensions[2].height = 22

headers = [
    "ประเทศ", "วีซ่า / เส้นทาง", "ตำแหน่ง", "ระดับ",
    "บริษัทตัวอย่าง",
    "เงินเดือน/ปี\n(สกุลท้องถิ่น)", "เงินเดือน/เดือน\n(สกุลท้องถิ่น)",
    "เงินเดือน/เดือน\n(บาท ฿)",
    "เงินเดือน/ปี\n(บาท ฿)",
    "ชั่วโมงทำงาน\n/สัปดาห์", "Contract\nType", "หมายเหตุ"
]
for i, h in enumerate(headers, 1):
    hdr(ws1, 3, i, h)

# ── DATA ─────────────────────────────────────────────────────────────────────
# (country, flag, visa_type, position, level, companies, ann_local, currency_sym, rate, hours, contract, note)
rows = [
    # ─ AUSTRALIA WHV ──────────────────────────────────────────────────────
    ("ออสเตรเลีย","🇦🇺","WHV Subclass 462\n(ไปได้เลย ไม่ต้องมี job offer)",
     "Graduate SAP Consultant","Graduate / Entry",
     "Accenture AU\nDeloitte AU\nKPMG AU\nCapgemini AU",
     70000,"AUD",AUD,38,"Permanent / 2yr Grad",
     "Big 4 / Consulting firms\nรับ recent grad ทำงานได้บน WHV\nปีแรกเน้น training + certification"),

    ("ออสเตรเลีย","🇦🇺","WHV Subclass 462",
     "Junior SAP ABAP Developer","Junior (0–2 ปี)",
     "SAP Australia\nInfosys AU\nTCS AU\nWipro AU",
     85000,"AUD",AUD,38,"Permanent / Contract",
     "บริษัท Indian IT มักรับ WHV\nทำงาน SAP project ให้ client ออสฯ\nVisa sponsor หลัง 6 เดือน"),

    ("ออสเตรเลีย","🇦🇺","WHV Subclass 462",
     "SAP ABAP Associate Developer","Junior (0–2 ปี)",
     "NTT Data AU\nDXC Technology\nHCL Technologies\nSoftware AG",
     90000,"AUD",AUD,38,"Contract 6–12 เดือน",
     "Contract บน WHV ได้\nทำงานหลาย client\nBuildup exp เร็ว"),

    ("ออสเตรเลีย","🇦🇺","WHV Subclass 462",
     "SAP ABAP Developer (S/4HANA)","Mid (2–4 ปี)",
     "EY AU\nPwC AU\nIBM AU\nSAP SE",
     113000,"AUD",AUD,38,"Permanent",
     "ต้องมีประสบการณ์ 2–3 ปีขึ้น\nWHV ทำได้แต่ต่อสัญญาต้อง\nขอ Subclass 482"),

    ("ออสเตรเลีย","🇦🇺","WHV Subclass 462",
     "SAP Contractor (ABAP)","All levels",
     "ผ่าน Recruiter:\nHays, Robert Half,\nMichael Page, Talent",
     0,"AUD",AUD,40,"Casual/Daily Rate",
     "Daily rate AUD 450–750/วัน\n≈ AUD 100k–165k/ปี\nWHV ทำ contract ได้\nไม่มี leave benefits"),

    # ─ NEW ZEALAND WHV ────────────────────────────────────────────────────
    ("นิวซีแลนด์","🇳🇿","WHV\n(Quota 100/ปี — สมัครเร็ว)",
     "SAP Consultant (Junior)","Graduate / Entry",
     "Deloitte NZ\nAccenture NZ\nASB Bank\nFonterra",
     75000,"NZD",NZD,37.5,"Permanent",
     "ตลาดเล็กกว่า AU แต่\nค่าครองชีพต่ำกว่า Auckland\nASB Bank รับ SAP ABAP โดยตรง"),

    ("นิวซีแลนด์","🇳🇿","WHV",
     "SAP ABAP Developer","Junior–Mid",
     "SAP NZ\nIBM NZ\nFonterra\nTelecom NZ",
     110000,"NZD",NZD,37.5,"Permanent / Contract",
     "Average NZD 144,657/ปี\nJob น้อยกว่า AU แต่\nแข่งขันน้อยกว่าด้วย"),

    # ─ GERMANY Skilled Worker ─────────────────────────────────────────────
    ("เยอรมนี","🇩🇪","Skilled Worker Visa\n(ต้องมี job offer ก่อน)",
     "SAP ABAP Developer (Junior)","Junior (0–2 ปี)",
     "SAP SE (Walldorf)\nAccenture DE\nCapgemini DE\nT-Systems",
     48000,"EUR",EUR,38,"Permanent",
     "ต้องยื่นสมัครจากไทยก่อน\nได้ offer → นายจ้าง sponsor visa\nค่าวีซ่า €100 เท่านั้น"),

    ("เยอรมนี","🇩🇪","Skilled Worker Visa",
     "SAP ABAP Consultant","Mid (2–4 ปี)",
     "Deloitte DE\nPwC DE\nIBM DE\nSAP SE",
     65000,"EUR",EUR,38,"Permanent",
     "มี relocation package บ่อย\nภาษาเยอรมันไม่จำเป็น\nสำหรับ SAP roles (ภาษาอังกฤษ OK)"),

    ("เยอรมนี","🇩🇪","Skilled Worker Visa",
     "SAP ABAP Senior Developer","Senior (4+ ปี)",
     "SAP SE\nSiemens\nBosch\nMercedes-Benz",
     85000,"EUR",EUR,38,"Permanent",
     "Germany: ขาด IT 109,000 ตน.\nต้องการ ABAP developer มาก\nมี benefits: 30 วันหยุด/ปี"),

    # ─ SINGAPORE EP ────────────────────────────────────────────────────────
    ("สิงคโปร์","🇸🇬","Employment Pass\n(ต้องมี job offer ก่อน\nเงินเดือน SGD 5,000+/เดือน)",
     "SAP ABAP Associate","Junior–Mid",
     "Accenture SG\nDeloitte SG\nInfosys SG\nTCS SG",
     72000,"SGD",SGD,44,"Permanent",
     "ต้องการเงินเดือน SGD 5,000+\nสำหรับ EP → คิดเป็น\nSGD 60,000+/ปี จึงผ่าน"),

    ("สิงคโปร์","🇸🇬","Employment Pass",
     "SAP ABAP Developer","Mid (2–4 ปี)",
     "SAP SE SG\nIBM SG\nDXC SG\nNCS (Singtel group)",
     96000,"SGD",SGD,44,"Permanent",
     "Average SGD 122,064/ปี\nSingapore เป็น APAC hub\nSAP ของหลายบริษัทใหญ่"),
]

row_colors = {
    "ออสเตรเลีย": ["E8F4FD","D6EEF8"],
    "นิวซีแลนด์":  ["E8F9F2","D5F5E3"],
    "เยอรมนี":     ["FFF9E8","FEF9E7"],
    "สิงคโปร์":    ["FDF2F8","F9EBF6"],
}
country_hdr_bg = {
    "ออสเตรเลีย": "1565C0",
    "นิวซีแลนด์":  "1E8449",
    "เยอรมนี":     "CA6F1E",
    "สิงคโปร์":    "7D3C98",
}

prev = None
r = 4
for idx, row_data in enumerate(rows):
    (country, flag, visa, pos, level, cos,
     ann_local, cur_sym, rate, hrs, ctype, note) = row_data

    # Country divider
    if country != prev:
        c = ws1.cell(row=r, column=1, value=f"  {flag}  {country}")
        c.fill = PatternFill("solid", fgColor=country_hdr_bg[country])
        c.font = Font(color="FFFFFF", bold=True, size=12, name="Calibri")
        c.alignment = Alignment(horizontal="left", vertical="center")
        ws1.merge_cells(start_row=r, start_column=1, end_row=r, end_column=12)
        ws1.row_dimensions[r].height = 28
        r += 1
        prev = country

    alt = idx % 2
    bg = row_colors[country][alt]

    # Special for contractor (daily rate)
    if ann_local == 0:
        ann_str = "AUD 450–750/วัน"
        mon_str = "~AUD 9,000–15,000"
        thb_mon = "~209,700–349,500 ฿"
        thb_ann = "~2,516,400–4,194,000 ฿"
    else:
        ann_str = f"{cur_sym} {fmt(ann_local)}"
        mon_local = ann_local / 12
        mon_str = f"{cur_sym} {fmt(mon_local)}"
        thb_mon_val = to_thb_month(ann_local, rate)
        thb_ann_val = thb_mon_val * 12
        thb_mon = f"{fmt(thb_mon_val)} ฿"
        thb_ann = f"{fmt(thb_ann_val)} ฿"

    cell(ws1, r, 1, f"{flag} {country}", bg=bg, bold=True)
    cell(ws1, r, 2, visa, bg=bg)
    cell(ws1, r, 3, pos, bg=bg, bold=True)
    cell(ws1, r, 4, level, bg=bg)
    cell(ws1, r, 5, cos, bg=bg)
    money(ws1, r, 6, ann_str, bg=bg, bold=True)
    money(ws1, r, 7, mon_str, bg=bg)
    # THB columns — highlight orange-ish
    c8 = ws1.cell(row=r, column=8, value=thb_mon)
    c8.fill = PatternFill("solid", fgColor="FEF9E7")
    c8.font = Font(bold=True, size=10, name="Calibri", color="784212")
    c8.alignment = Alignment(horizontal="right", vertical="center")
    thin = Side(style="thin", color="CCCCCC")
    c8.border = Border(left=thin, right=thin, top=thin, bottom=thin)

    c9 = ws1.cell(row=r, column=9, value=thb_ann)
    c9.fill = PatternFill("solid", fgColor="FDEBD0")
    c9.font = Font(bold=True, size=10, name="Calibri", color="6E2C00")
    c9.alignment = Alignment(horizontal="right", vertical="center")
    c9.border = Border(left=thin, right=thin, top=thin, bottom=thin)

    cell(ws1, r, 10, f"{hrs} ชม.", bg=bg, align="center")
    cell(ws1, r, 11, ctype, bg=bg)
    cell(ws1, r, 12, note, bg=bg)
    ws1.row_dimensions[r].height = 70
    r += 1

col_widths = [14, 22, 28, 16, 24, 18, 18, 20, 22, 12, 20, 36]
for i, w in enumerate(col_widths, 1):
    ws1.column_dimensions[get_column_letter(i)].width = w
ws1.row_dimensions[3].height = 38

# ═════════════════════════════════════════════════════════════════════════════
# SHEET 2 — เปรียบ ค่าตอบแทน สรุปรายเดือน (THB)
# ═════════════════════════════════════════════════════════════════════════════
ws2 = wb.create_sheet("สรุปค่าตอบแทน (THB)")
ws2.sheet_view.showGridLines = False

sec(ws2, 1, 1, 8, "  💰  สรุปเงินเดือน SAP ABAP ต่างประเทศ เทียบเป็นบาทไทย (มิ.ย. 2569)")

c = ws2.cell(row=2, column=1,
    value="  เทียบอัตราแลกเปลี่ยน: 1 AUD = 23.30 ฿  |  1 NZD = 19.18 ฿  |  1 EUR = 37.99 ฿  |  1 SGD = 25.43 ฿")
c.fill = PatternFill("solid", fgColor="D6EAF8")
c.font = Font(bold=True, size=10, name="Calibri", color="1A5276")
c.alignment = Alignment(horizontal="left", vertical="center")
ws2.merge_cells(start_row=2, start_column=1, end_row=2, end_column=8)
ws2.row_dimensions[2].height = 22

hdrs2 = ["ประเทศ / วีซ่า", "ตำแหน่ง", "ระดับ",
         "เงินเดือน/เดือน\n(สกุลท้องถิ่น)", "เงินเดือน/เดือน\n(บาท ฿)",
         "เงินเดือน/ปี\n(สกุลท้องถิ่น)", "เงินเดือน/ปี\n(บาท ฿)",
         "เปรียบกับ\nเงินเดือนไทย"]
for i, h in enumerate(hdrs2, 1):
    hdr(ws2, 3, i, h)

# Thai reference salary for ABAP
thai_ref = 45000  # THB/month for junior SAP ABAP in Thailand

summary_data = [
    ("🇦🇺 ออสเตรเลีย\nWHV (ไปได้เลย)", "Graduate SAP Consultant","Graduate",
     "AUD 5,833", to_thb_month(70000,AUD), "AUD 70,000", 70000*AUD),
    ("🇦🇺 ออสเตรเลีย\nWHV (ไปได้เลย)", "Junior ABAP Developer","Junior 0–2 ปี",
     "AUD 7,083", to_thb_month(85000,AUD), "AUD 85,000", 85000*AUD),
    ("🇦🇺 ออสเตรเลีย\nWHV (ไปได้เลย)", "ABAP Associate Developer","Junior 0–2 ปี",
     "AUD 7,500", to_thb_month(90000,AUD), "AUD 90,000", 90000*AUD),
    ("🇦🇺 ออสเตรเลีย\nWHV (ไปได้เลย)", "SAP Contractor (ABAP)","All levels",
     "AUD 9,000–15,000", None, "AUD 108k–180k", None),

    ("🇳🇿 นิวซีแลนด์\nWHV (Quota 100/ปี)", "SAP Consultant Junior","Graduate",
     "NZD 6,250", to_thb_month(75000,NZD), "NZD 75,000", 75000*NZD),
    ("🇳🇿 นิวซีแลนด์\nWHV (Quota 100/ปี)", "SAP ABAP Developer","Junior–Mid",
     "NZD 9,167", to_thb_month(110000,NZD), "NZD 110,000", 110000*NZD),

    ("🇩🇪 เยอรมนี\nSkilled Worker Visa", "SAP ABAP Developer Junior","Junior 0–2 ปี",
     "EUR 4,000", to_thb_month(48000,EUR), "EUR 48,000", 48000*EUR),
    ("🇩🇪 เยอรมนี\nSkilled Worker Visa", "SAP ABAP Consultant","Mid 2–4 ปี",
     "EUR 5,417", to_thb_month(65000,EUR), "EUR 65,000", 65000*EUR),

    ("🇸🇬 สิงคโปร์\nEmployment Pass", "SAP ABAP Associate","Junior–Mid",
     "SGD 6,000", to_thb_month(72000,SGD), "SGD 72,000", 72000*SGD),
    ("🇸🇬 สิงคโปร์\nEmployment Pass", "SAP ABAP Developer","Mid 2–4 ปี",
     "SGD 8,000", to_thb_month(96000,SGD), "SGD 96,000", 96000*SGD),

    ("🇹🇭 ไทย (อ้างอิง)", "Junior SAP ABAP Developer","Junior 0–2 ปี",
     "฿ 35,000–45,000", 40000, "฿ 420,000–540,000", 480000),
]

row_bg_map = {
    "🇦🇺": "E8F4FD",
    "🇳🇿": "E8F9F2",
    "🇩🇪": "FFF9E8",
    "🇸🇬": "FDF2F8",
    "🇹🇭": "FEF9E7",
}

for idx, rd in enumerate(summary_data):
    country_visa, pos, level, mon_local, mon_thb, ann_local, ann_thb = rd
    r = idx + 4
    flag = country_visa[:2]
    bg = row_bg_map.get(flag, "FFFFFF")

    if rd[0] == "🇹🇭 ไทย (อ้างอิง)":
        bg = "FFFDE7"

    cell(ws2, r, 1, country_visa, bg=bg, bold=True)
    cell(ws2, r, 2, pos, bg=bg, bold=True)
    cell(ws2, r, 3, level, bg=bg, align="center")
    money(ws2, r, 4, mon_local, bg=bg, bold=True)

    if mon_thb:
        c5 = ws2.cell(row=r, column=5, value=f"{fmt(mon_thb)} ฿")
        c5.fill = PatternFill("solid", fgColor="FEF9E7")
        c5.font = Font(bold=True, size=11, name="Calibri", color="784212")
        c5.alignment = Alignment(horizontal="right", vertical="center")
        thin = Side(style="thin", color="CCCCCC")
        c5.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    else:
        cell(ws2, r, 5, "~209,700–349,500 ฿", bg="FEF9E7", bold=True, color="784212", align="right")

    money(ws2, r, 6, ann_local, bg=bg)

    if ann_thb:
        c7 = ws2.cell(row=r, column=7, value=f"{fmt(ann_thb)} ฿")
        c7.fill = PatternFill("solid", fgColor="FDEBD0")
        c7.font = Font(bold=True, size=10, name="Calibri", color="6E2C00")
        c7.alignment = Alignment(horizontal="right", vertical="center")
        c7.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    else:
        cell(ws2, r, 7, "~2.5M–4.2M ฿/ปี", bg="FDEBD0", bold=True, color="6E2C00", align="right")

    # เปรียบกับไทย
    if mon_thb and rd[0] != "🇹🇭 ไทย (อ้างอิง)":
        multiplier = round(mon_thb / thai_ref, 1)
        compare_text = f"สูงกว่าไทย {multiplier}×\n(ไทย ≈ {fmt(thai_ref)} ฿/เดือน)"
        c8 = ws2.cell(row=r, column=8, value=compare_text)
        c8.fill = PatternFill("solid", fgColor="E8F8F5")
        c8.font = Font(bold=True, size=10, name="Calibri", color="1A5276")
        c8.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c8.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    elif rd[0] == "🇹🇭 ไทย (อ้างอิง)":
        c8 = ws2.cell(row=r, column=8, value="— ฐานเปรียบเทียบ —")
        c8.fill = PatternFill("solid", fgColor="FFFDE7")
        c8.font = Font(bold=True, size=10, name="Calibri", color="7D6608")
        c8.alignment = Alignment(horizontal="center", vertical="center")
        c8.border = Border(left=thin, right=thin, top=thin, bottom=thin)
    else:
        cell(ws2, r, 8, "ขึ้นกับ rate/วัน", bg="E8F8F5", align="center")

    ws2.row_dimensions[r].height = 42

ws2.column_dimensions["A"].width = 22
ws2.column_dimensions["B"].width = 28
ws2.column_dimensions["C"].width = 14
ws2.column_dimensions["D"].width = 20
ws2.column_dimensions["E"].width = 20
ws2.column_dimensions["F"].width = 20
ws2.column_dimensions["G"].width = 22
ws2.column_dimensions["H"].width = 22
ws2.row_dimensions[3].height = 38

# ═════════════════════════════════════════════════════════════════════════════
# SHEET 3 — ค่าครองชีพ + เงินเหลือ
# ═════════════════════════════════════════════════════════════════════════════
ws3 = wb.create_sheet("เงินเหลือหลังหักค่าครองชีพ")
ws3.sheet_view.showGridLines = False

sec(ws3, 1, 1, 7, "  🏠  เงินเดือน vs ค่าครองชีพ — เงินเหลือต่อเดือน (บาทไทย)")

c = ws3.cell(row=2, column=1,
    value="  ค่าครองชีพโดยประมาณสำหรับ 1 คน (ที่พัก + อาหาร + เดินทาง + ใช้จ่ายทั่วไป)")
c.fill = PatternFill("solid", fgColor="D6EAF8")
c.font = Font(bold=True, size=10, name="Calibri", color="1A5276")
c.alignment = Alignment(horizontal="left", vertical="center")
ws3.merge_cells(start_row=2, start_column=1, end_row=2, end_column=7)
ws3.row_dimensions[2].height = 22

hdrs3 = ["ประเทศ / เมือง","ตำแหน่ง","เงินเดือน/เดือน\n(บาท ฿)",
         "ค่าครองชีพ/เดือน\n(บาท ฿ โดยประมาณ)",
         "เงินเหลือ/เดือน\n(บาท ฿)","เงินเหลือ/ปี\n(บาท ฿)","หมายเหตุค่าครองชีพ"]
for i, h in enumerate(hdrs3, 1):
    hdr(ws3, 3, i, h)

# Living costs (THB/month)
living = {
    "Sydney":    {"rent":25000,"food":10000,"transport":4000,"misc":5000},  # AUD 1,800–2,200/mo
    "Melbourne": {"rent":22000,"food":9000, "transport":3500,"misc":4500},
    "Auckland":  {"rent":20000,"food":8500, "transport":3000,"misc":4000},
    "Berlin":    {"rent":30000,"food":11000,"transport":3500,"misc":5500},
    "Singapore": {"rent":35000,"food":9000, "transport":3000,"misc":5000},
    "Bangkok":   {"rent":8000, "food":5000, "transport":2000,"misc":3000},
}

def total_living(city):
    d = living[city]
    return d["rent"]+d["food"]+d["transport"]+d["misc"]

def living_note(city):
    d = living[city]
    return (f"ที่พัก: {fmt(d['rent'])} ฿\n"
            f"อาหาร: {fmt(d['food'])} ฿\n"
            f"เดินทาง: {fmt(d['transport'])} ฿\n"
            f"อื่นๆ: {fmt(d['misc'])} ฿")

col3_data = [
    ("🇦🇺 Sydney","Graduate SAP Consultant", to_thb_month(70000,AUD), "Sydney"),
    ("🇦🇺 Sydney","Junior ABAP Developer",   to_thb_month(85000,AUD), "Sydney"),
    ("🇦🇺 Melbourne","Junior ABAP Developer", to_thb_month(85000,AUD), "Melbourne"),
    ("🇦🇺 Melbourne","ABAP Associate",        to_thb_month(90000,AUD), "Melbourne"),
    ("🇳🇿 Auckland","SAP Consultant Junior",  to_thb_month(75000,NZD), "Auckland"),
    ("🇳🇿 Auckland","SAP ABAP Developer",     to_thb_month(110000,NZD),"Auckland"),
    ("🇩🇪 Berlin","SAP ABAP Junior",          to_thb_month(48000,EUR), "Berlin"),
    ("🇩🇪 Berlin","SAP ABAP Consultant",      to_thb_month(65000,EUR), "Berlin"),
    ("🇸🇬 Singapore","SAP ABAP Associate",    to_thb_month(72000,SGD), "Singapore"),
    ("🇸🇬 Singapore","SAP ABAP Developer",    to_thb_month(96000,SGD), "Singapore"),
    ("🇹🇭 Bangkok (อ้างอิง)","Junior ABAP TH", 40000,                 "Bangkok"),
]

row_bgs = {
    "🇦🇺": ["E8F4FD","D6EEF8"],
    "🇳🇿": ["E8F9F2","D5F5E3"],
    "🇩🇪": ["FFF9E8","FEF9E7"],
    "🇸🇬": ["FDF2F8","F9EBF6"],
    "🇹🇭": ["FFFDE7","FFFDE7"],
}
prev_flag = None
alt = 0
for idx, (city_label, pos, salary_thb, city_key) in enumerate(col3_data):
    r = idx + 4
    flag = city_label[:2]
    if flag != prev_flag:
        alt = 0
        prev_flag = flag
    bg = row_bgs[flag][alt % 2]
    alt += 1

    lc = total_living(city_key)
    remaining = salary_thb - lc
    annual_remaining = remaining * 12

    cell(ws3, r, 1, city_label, bg=bg, bold=True)
    cell(ws3, r, 2, pos, bg=bg)
    money(ws3, r, 3, f"{fmt(salary_thb)} ฿", bg=bg, bold=True)
    money(ws3, r, 4, f"{fmt(lc)} ฿", bg="FFE5E5")

    remain_bg = "E8F8F5" if remaining > 0 else "FFE5E5"
    remain_color = "1A5276" if remaining > 30000 else ("784212" if remaining > 0 else "CC0000")
    c5 = ws3.cell(row=r, column=5, value=f"{fmt(remaining)} ฿")
    c5.fill = PatternFill("solid", fgColor=remain_bg)
    c5.font = Font(bold=True, size=11, name="Calibri", color=remain_color)
    c5.alignment = Alignment(horizontal="right", vertical="center")
    thin = Side(style="thin", color="CCCCCC")
    c5.border = Border(left=thin, right=thin, top=thin, bottom=thin)

    c6 = ws3.cell(row=r, column=6, value=f"{fmt(annual_remaining)} ฿")
    c6.fill = PatternFill("solid", fgColor="FDEBD0" if remaining > 0 else "FFE5E5")
    c6.font = Font(bold=True, size=10, name="Calibri",
                   color="6E2C00" if remaining > 0 else "CC0000")
    c6.alignment = Alignment(horizontal="right", vertical="center")
    c6.border = Border(left=thin, right=thin, top=thin, bottom=thin)

    cell(ws3, r, 7, living_note(city_key), bg=bg, wrap=True)
    ws3.row_dimensions[r].height = 68

ws3.column_dimensions["A"].width = 22
ws3.column_dimensions["B"].width = 26
ws3.column_dimensions["C"].width = 20
ws3.column_dimensions["D"].width = 22
ws3.column_dimensions["E"].width = 22
ws3.column_dimensions["F"].width = 22
ws3.column_dimensions["G"].width = 28
ws3.row_dimensions[3].height = 38

# ═════════════════════════════════════════════════════════════════════════════
# SHEET 4 — Timeline สมัครงาน ปีหน้า
# ═════════════════════════════════════════════════════════════════════════════
ws4 = wb.create_sheet("Timeline ปีหน้า 2027")
ws4.sheet_view.showGridLines = False

sec(ws4, 1, 1, 4, "  📅  Timeline — แผนการเตรียมตัว & สมัครงาน SAP ABAP ปีหน้า (2027)")

hdr(ws4, 2, 1, "ช่วงเวลา")
hdr(ws4, 2, 2, "สิ่งที่ต้องทำ")
hdr(ws4, 2, 3, "เป้าหมาย")
hdr(ws4, 2, 4, "ค่าใช้จ่าย (บาท)")

timeline = [
    ("ก.ค.–ส.ค. 2569\n(ตอนนี้)",
     "• เรียน SAP ABAP บน SAP Learning Hub / Udemy\n• ฝึกบน SAP BTP free trial\n• ทำ ABAP project เล็กๆ ใส่ portfolio\n• เรียน IELTS / ติว",
     "มีพื้นฐาน ABAP\nและ portfolio 1–2 งาน",
     "SAP BTP trial: ฟรี\nUdemy ABAP: ~1,500 ฿\nIELTS ติว: ~5,000 ฿"),
    ("ก.ย.–ต.ค. 2569",
     "• สอบ IELTS ให้ได้ 4.5+ (WHV AU)\n• สอบ SAP Certified Associate – ABAP\n  (สอบ online ที่บ้านได้)",
     "ได้ IELTS 4.5+\nได้ SAP ABAP Certification",
     "IELTS: ~7,000 ฿\nSAP Cert: ~20,000 ฿"),
    ("พ.ย. 2569–ม.ค. 2570",
     "• สมัคร WHV Subclass 462\n  (เปิดรับปลายปี 2569 / ต้นปี 2570)\n• เตรียมเอกสาร: passport + ป.ตรี +\n  bank statement + travel plan\n• จองตั๋วเครื่องบินล่วงหน้า",
     "ได้วีซ่า WHV ออสเตรเลีย\nรออยู่ที่ไทย",
     "ค่าวีซ่า WHV: ~15,000 ฿\n(AUD 635)\nตั๋วเครื่องบิน: ~15,000–20,000 ฿"),
    ("ก.พ.–มี.ค. 2570",
     "• เดินทางไปออสเตรเลีย\n• เปิด Australian bank account\n• ลงทะเบียน Medicare / TFN\n• สมัครงาน SAP ABAP บน\n  SEEK / LinkedIn / Indeed AU\n• ติดต่อ SAP recruiters",
     "ลงทะเบียนในออสฯ\nเริ่มสัมภาษณ์งาน",
     "ค่าใช้จ่ายเดือนแรก AU:\n~50,000–70,000 ฿\n(ก่อนเริ่มทำงาน)"),
    ("เม.ย.–มิ.ย. 2570",
     "• เริ่มทำงาน SAP ABAP\n  ตำแหน่ง Junior / Graduate\n• เงินเดือน AUD 5,833–7,500/เดือน\n  = ~136,000–174,750 ฿/เดือน\n• ทำงานกับนายจ้างไม่เกิน 6 เดือน\n  (กฎ WHV) แล้ว negotiate ต่อ",
     "ได้งาน SAP ABAP\nใน Sydney หรือ Melbourne",
     "เริ่มรับเงินเดือน\n~136,000–175,000 ฿/เดือน"),
    ("ก.ค. 2570 เป็นต้นไป",
     "• ขอให้นายจ้าง sponsor\n  Subclass 482 (TSS Visa)\n• หรือสมัคร 2nd WHV\n  (ทำงาน farm 3 เดือน)\n• พัฒนา skills: ABAP OO,\n  SAP BTP, S/4HANA, Fiori",
     "อยู่ต่อได้ระยะยาว\nหรือได้ Subclass 482",
     "Subclass 482: ~AUD 310\n(~7,200 ฿)"),
]

tl_colors = ["E8F4FD","E8F9F2","FFF9E8","FDF2F8","E8F4FD","E8F9F2"]
for i, (period, tasks, goal, cost) in enumerate(timeline):
    r = i + 3
    bg = tl_colors[i % len(tl_colors)]
    cell(ws4, r, 1, period, bg=bg, bold=True, align="center")
    cell(ws4, r, 2, tasks, bg=bg, wrap=True)
    cell(ws4, r, 3, goal, bg=bg, bold=True, wrap=True)
    cell(ws4, r, 4, cost, bg=bg, wrap=True)
    ws4.row_dimensions[r].height = 85

ws4.column_dimensions["A"].width = 18
ws4.column_dimensions["B"].width = 54
ws4.column_dimensions["C"].width = 28
ws4.column_dimensions["D"].width = 24
ws4.row_dimensions[2].height = 35

out = "/home/user/fefa/SAP_ABAP_Jobs_Salary_THB_2027.xlsx"
wb.save(out)
print(f"Saved: {out}")
