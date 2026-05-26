# ============================================
# 🌐 FRONTEND API CLIENT
# ============================================

import requests


# ============================================
# 🌐 API CONFIG
# ============================================

API_BASE = "http://127.0.0.1:8000"

REQUEST_TIMEOUT = 120


# ============================================
# 🚀 GENERIC REQUEST HANDLER
# ============================================

def safe_request(

    method,

    endpoint,

    **kwargs
):

    try:

        response = requests.request(

            method,

            f"{API_BASE}{endpoint}",

            timeout=REQUEST_TIMEOUT,

            **kwargs
        )

        return response

    except Exception as e:

        print(
            "❌ API CLIENT ERROR:",
            str(e)
        )

        return None


# ============================================
# 🧠 HEALTH PREDICTION
# ============================================

def predict_health(
    payload
):

    return safe_request(

        "POST",

        "/predict",

        json=payload
    )


# ============================================
# 🔐 LOGIN
# ============================================

def login_user(
    payload
):

    return safe_request(

        "POST",

        "/login",

        json=payload
    )


# ============================================
# 📝 REGISTER
# ============================================

def register_user(
    payload
):

    return safe_request(

        "POST",

        "/register",

        json=payload
    )


# ============================================
# 💬 CHAT
# ============================================

def send_chat_message(
    payload
):

    return safe_request(

        "POST",

        "/chat",

        json=payload
    )


# ============================================
# 📜 REPORT HISTORY
# ============================================

def get_reports(
    email
):

    return safe_request(

        "GET",

        "/reports",

        params={
            "email": email
        }
    )


# ============================================
# 📄 DOWNLOAD PDF REPORT
# ============================================

def download_report_pdf(

    report_id,

    email
):

    return safe_request(

        "GET",

        f"/download-report/{report_id}",

        params={
            "email": email
        }
    )


# ============================================
# 🗑 DELETE REPORT
# ============================================

def delete_report(

    report_id,

    email
):

    return safe_request(

        "DELETE",

        f"/reports/{report_id}",

        params={
            "email": email
        }
    )


# ============================================
# 💬 GET CHAT HISTORY
# ============================================

def get_chat_history(
    email
):

    return safe_request(

        "GET",

        "/chat-history",

        params={
            "email": email
        }
    )


# ============================================
# 🗑 CLEAR CHAT
# ============================================

def clear_chat_history(
    email
):

    return safe_request(

        "DELETE",

        "/clear-chat",

        params={
            "email": email
        }
    )