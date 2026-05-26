# ============================================
# 🌐 FASTAPI CLIENT
# ============================================

import requests


# ============================================
# 🔗 BACKEND URL
# ============================================

BASE_URL = "http://127.0.0.1:8000"


# ============================================
# 🚀 PREDICT API
# ============================================

def predict_health(data):

    url = f"{BASE_URL}/predict"


    response = requests.post(

        url,

        json=data
    )


    return response