# ============================================
# 📄 PREMIUM PDF REPORT GENERATION SERVICE
# ============================================

import io
import json
import re

from reportlab.platypus import (

    SimpleDocTemplate,

    Paragraph,

    Spacer,

    Table,

    TableStyle
)

from reportlab.lib import colors

from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.platypus.flowables import (
    HRFlowable
)

from reportlab.lib.enums import (
    TA_CENTER,
    TA_LEFT
)

from reportlab.lib.styles import (
    ParagraphStyle
)


# ============================================
# 🎨 GLOBAL STYLES
# ============================================

styles = getSampleStyleSheet()


# ============================================
# 🎨 CUSTOM STYLES
# ============================================

TITLE_STYLE = ParagraphStyle(

    "TitleStyle",

    parent=styles["Heading1"],

    fontName="Helvetica-Bold",

    fontSize=24,

    leading=30,

    textColor=colors.HexColor("#1B4332"),

    alignment=TA_CENTER,

    spaceAfter=20
)


SUBTITLE_STYLE = ParagraphStyle(

    "SubtitleStyle",

    parent=styles["BodyText"],

    fontName="Helvetica",

    fontSize=12,

    leading=18,

    textColor=colors.HexColor("#555555"),

    alignment=TA_CENTER,

    spaceAfter=18
)


SECTION_STYLE = ParagraphStyle(

    "SectionStyle",

    parent=styles["Heading2"],

    fontName="Helvetica-Bold",

    fontSize=17,

    leading=22,

    textColor=colors.HexColor("#1D3557"),

    spaceAfter=12
)


BODY_STYLE = ParagraphStyle(

    "BodyStyle",

    parent=styles["BodyText"],

    fontName="Helvetica",

    fontSize=11,

    leading=20,

    textColor=colors.HexColor("#333333"),

    alignment=TA_LEFT
)


HIGHLIGHT_STYLE = ParagraphStyle(

    "HighlightStyle",

    parent=styles["BodyText"],

    fontName="Helvetica-Bold",

    fontSize=11,

    leading=18,

    textColor=colors.HexColor("#1B4332")
)


# ============================================
# 🌿 WELLNESS LABEL
# ============================================

def get_wellness_label(
    score
):

    if score >= 80:

        return "Excellent Wellness"

    elif score >= 60:

        return "Good Wellness"

    elif score >= 40:

        return "Moderate Wellness"

    return "High Health Concern"


# ============================================
# 🎨 RISK COLOR
# ============================================

def get_risk_color(
    risk_level
):

    risk_level = risk_level.lower()


    if "very high" in risk_level:

        return colors.HexColor("#8B0000")

    elif "high" in risk_level:

        return colors.HexColor("#D62828")

    elif "moderate" in risk_level:

        return colors.HexColor("#F77F00")

    elif "mixed" in risk_level:

        return colors.HexColor("#6A4C93")

    return colors.HexColor("#2A9D8F")


# ============================================
# 🧹 CLEAN AI TEXT
# ============================================

def clean_ai_text(
    text
):

    if not text:

        return ""


    # ========================================
    # REMOVE MARKDOWN HEADERS
    # ========================================

    text = re.sub(
        r"#+",
        "",
        text
    )


    # ========================================
    # REMOVE TABLE LINES
    # ========================================

    text = re.sub(
        r"\|.*?\|",
        "",
        text
    )

    text = re.sub(
        r"-{3,}",
        "",
        text
    )


    # ========================================
    # REMOVE SPECIAL SYMBOLS
    # ========================================

    replacements = {

        "■": "",

        "•": "-",

        "❤": "Heart",

        "❤️": "Heart",

        "🧠": "AI",

        "⚠": "Warning",

        "🚨": "Alert",

        "✅": "Success",

        "📊": "Analytics",

        "📄": "Report",

        "🌿": "Wellness",

        "💬": "AI"
    }


    for old, new in replacements.items():

        text = text.replace(
            old,
            new
        )


    # ========================================
    # REMOVE NON-ASCII CHARACTERS
    # ========================================

    text = re.sub(

        r"[^\x00-\x7F]+",

        " ",

        text
    )


    # ========================================
    # CLEAN ASTERISKS
    # ========================================

    text = text.replace(
        "**",
        ""
    )


    # ========================================
    # CLEAN EXCESS SPACING
    # ========================================

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text
    )

    text = re.sub(
        r" {2,}",
        " ",
        text
    )


    return text.strip()


# ============================================
# 📄 GENERATE PDF REPORT
# ============================================

def generate_health_report_pdf(
    report
):

    # ========================================
    # 📦 MEMORY BUFFER
    # ========================================

    buffer = io.BytesIO()


    # ========================================
    # 📄 DOCUMENT SETUP
    # ========================================

    doc = SimpleDocTemplate(

        buffer,

        pagesize=letter,

        rightMargin=45,

        leftMargin=45,

        topMargin=40,

        bottomMargin=35
    )


    elements = []


    # ========================================
    # 📊 PARSE PREDICTIONS
    # ========================================

    try:

        predictions = json.loads(
            report.prediction_results
        )

    except Exception:

        predictions = {}


    # ========================================
    # 🌿 WELLNESS SCORE
    # ========================================

    wellness_score = report.wellness_score

    wellness_label = (
        get_wellness_label(
            wellness_score
        )
    )


    # ========================================
    # 🧹 CLEAN INTERPRETATION
    # ========================================

    interpretation_text = clean_ai_text(
        report.interpretation
    )


    # ========================================
    # 🩺 HEADER
    # ========================================

    elements.append(

        Paragraph(

            "AI Health Companion",

            TITLE_STYLE
        )
    )


    elements.append(

        Paragraph(

            "AI-Assisted Preventive Wellness & Health Risk Report",

            SUBTITLE_STYLE
        )
    )


    elements.append(

        HRFlowable(

            width="100%",

            thickness=1.2,

            color=colors.HexColor("#CCCCCC")
        )
    )

    elements.append(
        Spacer(1, 18)
    )


    # ========================================
    # 🕒 REPORT DATE
    # ========================================

    formatted_date = (
        report.created_at.strftime(
            "%d %B %Y • %I:%M %p"
        )
    )


    elements.append(

        Paragraph(

            f"<b>Generated On:</b> {formatted_date}",

            BODY_STYLE
        )
    )

    elements.append(
        Spacer(1, 20)
    )


    # ========================================
    # 🌿 WELLNESS OVERVIEW
    # ========================================

    elements.append(

        Paragraph(

            "Wellness Overview",

            SECTION_STYLE
        )
    )


    wellness_table = Table(

        [

            [
                "Wellness Score",
                f"{wellness_score}/100"
            ],

            [
                "Overall Status",
                wellness_label
            ]
        ],

        colWidths=[160, 160]
    )


    wellness_table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#D8F3DC")),

        ("BACKGROUND", (0, 1), (-1, 1), colors.HexColor("#F8F9FA")),

        ("TEXTCOLOR", (0, 0), (-1, -1), colors.black),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("FONTSIZE", (0, 0), (-1, -1), 11),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 12),

        ("TOPPADDING", (0, 0), (-1, -1), 12),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#DDDDDD"))
    ]))

    elements.append(
        wellness_table
    )

    elements.append(
        Spacer(1, 22)
    )


    # ========================================
    # 📊 RISK ANALYTICS
    # ========================================

    elements.append(

        Paragraph(

            "AI Risk Analytics",

            SECTION_STYLE
        )
    )


    prediction_rows = [[

        "Condition",

        "Probability",

        "Risk Level"
    ]]


    for disease, data in predictions.items():

        if not isinstance(
            data,
            dict
        ):

            continue


        probability = data.get(
            "probability",
            0
        )

        risk_level = data.get(
            "risk_level",
            "Unknown"
        )


        prediction_rows.append([

            disease.replace(
                "_",
                " "
            ).title(),

            f"{probability:.2f}%",

            risk_level
        ])


    prediction_table = Table(

        prediction_rows,

        colWidths=[180, 120, 120]
    )


    table_style = [

        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1D3557")),

        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),

        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),

        ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#F8F9FA")),

        ("GRID", (0, 0), (-1, -1), 1, colors.HexColor("#DDDDDD")),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

        ("TOPPADDING", (0, 0), (-1, -1), 10),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("FONTSIZE", (0, 0), (-1, -1), 10)
    ]


    # ========================================
    # 🎨 COLOR RISK LEVELS
    # ========================================

    for idx, row in enumerate(prediction_rows[1:], start=1):

        risk_level = row[2]

        risk_color = get_risk_color(
            risk_level
        )

        table_style.append(

            (
                "TEXTCOLOR",

                (2, idx),

                (2, idx),

                risk_color
            )
        )

        table_style.append(

            (
                "FONTNAME",

                (2, idx),

                (2, idx),

                "Helvetica-Bold"
            )
        )


    prediction_table.setStyle(
        TableStyle(table_style)
    )

    elements.append(
        prediction_table
    )

    elements.append(
        Spacer(1, 25)
    )


    # ========================================
    # 🧠 AI INTERPRETATION
    # ========================================

    elements.append(

        Paragraph(

            "AI Wellness Interpretation",

            SECTION_STYLE
        )
    )


    interpretation_paragraphs = (

        interpretation_text.split("\n\n")
    )


    for paragraph in interpretation_paragraphs:

        cleaned_paragraph = (
            paragraph.strip()
        )

        if not cleaned_paragraph:

            continue


        elements.append(

            Paragraph(

                cleaned_paragraph,

                BODY_STYLE
            )
        )

        elements.append(
            Spacer(1, 12)
        )


    # ========================================
    # ⚠ DISCLAIMER
    # ========================================

    elements.append(
        Spacer(1, 12)
    )

    elements.append(

        HRFlowable(

            width="100%",

            thickness=1,

            color=colors.HexColor("#CCCCCC")
        )
    )

    elements.append(
        Spacer(1, 18)
    )


    elements.append(

        Paragraph(

            "Medical Disclaimer",

            SECTION_STYLE
        )
    )


    disclaimer_text = """

This report is an AI-generated preventive wellness assessment
created for educational, research, and wellness-awareness purposes only.

It is NOT a medical diagnosis and should not replace
professional clinical evaluation, diagnosis,
or treatment from licensed healthcare providers.

Always consult qualified healthcare professionals
for medical decisions and treatment guidance.

"""


    elements.append(

        Paragraph(

            disclaimer_text,

            BODY_STYLE
        )
    )

    elements.append(
        Spacer(1, 28)
    )


    # ========================================
    # 💙 FOOTER
    # ========================================

    footer = Paragraph(

        """
        <font size=9 color='#666666'>

        AI Health Companion • Preventive Wellness Intelligence Platform • 2026

        </font>
        """,

        styles["BodyText"]
    )

    elements.append(
        footer
    )


    # ========================================
    # 🚀 BUILD PDF
    # ========================================

    doc.build(elements)


    # ========================================
    # 📦 RETURN BUFFER
    # ========================================

    buffer.seek(0)

    return buffer