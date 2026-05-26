# ============================================
# 🌐 OPENROUTER CLIENT
# ============================================

import os

from dotenv import load_dotenv

from openai import OpenAI


# ============================================
# 🚀 LOAD ENV
# ============================================

load_dotenv()


# ============================================
# 🔑 API KEY
# ============================================

OPENROUTER_API_KEY = os.getenv(
    "OPENROUTER_API_KEY"
)


# ============================================
# 🤖 CLIENT
# ============================================

client = OpenAI(

    api_key=OPENROUTER_API_KEY,

    base_url="https://openrouter.ai/api/v1"
)