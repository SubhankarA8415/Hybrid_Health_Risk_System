# ============================================
# 📜 REPORT ROUTES
# ============================================

import json

from fastapi import APIRouter
from fastapi import HTTPException

from fastapi.responses import (
    StreamingResponse
)

from project.database.crud import (
    get_user_by_email,
    get_user_reports
)

from project.database.connection import (
    SessionLocal
)

from project.database.models import (
    HealthReport
)

from project.api.services.pdf_service import (
    generate_health_report_pdf
)


# ============================================
# 🚀 ROUTER
# ============================================

router = APIRouter()


# ============================================
# 📜 GET USER REPORTS
# ============================================

@router.get("/reports")

async def get_reports(
    email: str
):

    db_user = get_user_by_email(
        email
    )

    if not db_user:

        raise HTTPException(

            status_code=404,

            detail="User not found"
        )


    reports = get_user_reports(
        db_user.id
    )


    response = []


    for report in reports:

        try:

            predictions = json.loads(
                report.prediction_results
            )

        except Exception:

            predictions = {}


        response.append({

            "id":
            report.id,

            "created_at":
            str(report.created_at),

            "prediction_results":
            predictions,

            "interpretation":
            report.interpretation,

            "wellness_score":
            report.wellness_score
        })


    return response


# ============================================
# 📄 DOWNLOAD PDF REPORT
# ============================================

@router.get(
    "/download-report/{report_id}"
)

async def download_report(

    report_id: int,

    email: str
):

    db_user = get_user_by_email(
        email
    )

    if not db_user:

        raise HTTPException(

            status_code=404,

            detail="User not found"
        )


    db = SessionLocal()

    try:

        # ====================================
        # 📜 FIND REPORT
        # ====================================

        report = db.query(
            HealthReport
        ).filter(

            HealthReport.id == report_id,

            HealthReport.user_id == db_user.id

        ).first()


        if not report:

            raise HTTPException(

                status_code=404,

                detail="Report not found"
            )


        # ====================================
        # 📄 GENERATE PDF
        # ====================================

        pdf_buffer = (
            generate_health_report_pdf(
                report
            )
        )


        # ====================================
        # 🕒 FORMAT TIMESTAMP
        # ====================================

        formatted_timestamp = (
            report.created_at.strftime(
                "%d_%b_%Y_%I_%M_%p"
            )
        )


        # ====================================
        # 📄 PROFESSIONAL FILE NAME
        # ====================================

        filename = (
            f"AI_Wellness_Report_{formatted_timestamp}.pdf"
        )


        # ====================================
        # 📦 RETURN PDF RESPONSE
        # ====================================

        return StreamingResponse(

            pdf_buffer,

            media_type="application/pdf",

            headers={

                "Content-Disposition":

                f"attachment; filename={filename}"
            }
        )


    except HTTPException:

        raise


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=f"PDF Generation Error: {str(e)}"
        )


    finally:

        db.close()


# ============================================
# 🗑 DELETE REPORT
# ============================================

@router.delete("/reports/{report_id}")

async def delete_report(

    report_id: int,

    email: str
):

    db_user = get_user_by_email(
        email
    )

    if not db_user:

        raise HTTPException(

            status_code=404,

            detail="User not found"
        )


    db = SessionLocal()

    try:

        report = db.query(
            HealthReport
        ).filter(

            HealthReport.id == report_id,

            HealthReport.user_id == db_user.id

        ).first()


        if not report:

            raise HTTPException(

                status_code=404,

                detail="Report not found"
            )


        db.delete(report)

        db.commit()


        return {

            "message":
            "Report deleted successfully"
        }


    except HTTPException:

        raise


    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=str(e)
        )


    finally:

        db.close()