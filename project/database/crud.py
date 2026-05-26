# ============================================
# 🗄 DATABASE CRUD OPERATIONS
# ============================================

import json

from project.database.connection import (
    SessionLocal
)

from project.database.models import (

    User,

    HealthReport,

    ChatHistory
)


# ============================================
# 👤 GET USER BY EMAIL
# ============================================

def get_user_by_email(
    email
):

    db = SessionLocal()

    try:

        user = db.query(
            User
        ).filter(

            User.email == email

        ).first()

        return user

    finally:

        db.close()


# ============================================
# 📊 SAVE HEALTH REPORT
# ============================================

def save_health_report(

    user_id,

    input_data,

    prediction_results,

    interpretation,

    wellness_score
):

    db = SessionLocal()

    try:

        report = HealthReport(

            user_id=user_id,

            input_data=json.dumps(
                input_data
            ),

            prediction_results=json.dumps(
                prediction_results
            ),

            interpretation=interpretation,

            wellness_score=wellness_score
        )

        db.add(report)

        db.commit()

        db.refresh(report)

        return report


    except Exception as e:

        db.rollback()

        print(
            "❌ REPORT SAVE FAILED:",
            str(e)
        )

        raise e


    finally:

        db.close()


# ============================================
# 📜 GET USER REPORTS
# ============================================

def get_user_reports(
    user_id
):

    db = SessionLocal()

    try:

        reports = db.query(
            HealthReport
        ).filter(

            HealthReport.user_id == user_id

        ).order_by(

            HealthReport.created_at.desc()

        ).all()

        return reports


    finally:

        db.close()


# ============================================
# 💬 SAVE CHAT MESSAGE
# ============================================

def save_chat_message(

    user_id,

    role,

    message
):

    db = SessionLocal()

    try:

        chat = ChatHistory(

            user_id=user_id,

            role=role,

            message=message
        )

        db.add(chat)

        db.commit()

        db.refresh(chat)

        return chat


    except Exception as e:

        db.rollback()

        print(
            "❌ CHAT SAVE FAILED:",
            str(e)
        )

        raise e


    finally:

        db.close()


# ============================================
# 💬 GET CHAT HISTORY
# ============================================

def get_chat_history(
    user_id
):

    db = SessionLocal()

    try:

        chats = db.query(
            ChatHistory
        ).filter(

            ChatHistory.user_id == user_id

        ).order_by(

            ChatHistory.created_at.asc()

        ).all()

        return chats


    finally:

        db.close()