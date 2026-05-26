# ============================================
# 🩺 AI HEALTH COMPANION
# ============================================

import sys
import time

from pathlib import Path


# ============================================
# 📁 ROOT PATH
# ============================================

ROOT_DIR = Path(__file__).resolve().parents[2]

if str(ROOT_DIR) not in sys.path:

    sys.path.append(str(ROOT_DIR))


# ============================================
# 📦 IMPORTS
# ============================================

import streamlit as st

from streamlit_cookies_manager import (
    EncryptedCookieManager
)


# ============================================
# 🎨 GLOBAL STYLES
# ============================================

from project.ui.styles.css import (
    CUSTOM_CSS
)


# ============================================
# 🌐 API CLIENT
# ============================================

from project.ui.services.api_client import (
    predict_health
)


# ============================================
# 🧩 COMPONENTS
# ============================================

from project.ui.components.sidebar import (
    render_sidebar
)

from project.ui.components.hero import (
    render_hero
)

from project.ui.components.example_profiles import (
    render_example_profiles
)

from project.ui.components.assessment_form import (
    render_assessment_form
)

from project.ui.components.wellness_score import (
    render_wellness_score
)

from project.ui.components.risk_dashboard import (
    render_risk_dashboard
)

from project.ui.components.interpretation import (
    render_interpretation
)

from project.ui.components.chat import (
    render_chat
)

from project.ui.components.report_history import (
    render_report_history
)

from project.ui.components.footer import (
    render_footer
)


# ============================================
# 🚀 PAGE CONFIG
# ============================================

st.set_page_config(

    page_title="AI Health Companion",

    page_icon="🩺",

    layout="wide",

    initial_sidebar_state="expanded"
)


# ============================================
# 🍪 COOKIE MANAGER
# ============================================

cookies = EncryptedCookieManager(

    prefix="health_app_",

    password="super_secret_password"
)

if not cookies.ready():

    st.stop()


# ============================================
# 🎨 APPLY GLOBAL CSS
# ============================================

st.markdown(

    CUSTOM_CSS,

    unsafe_allow_html=True
)


# ============================================
# 👤 USER SESSION
# ============================================

if "user" not in st.session_state:

    saved_email = cookies.get(
        "user_email"
    )

    saved_name = cookies.get(
        "user_name"
    )

    if saved_email and saved_name:

        st.session_state.user = {

            "name": saved_name,

            "email": saved_email
        }

    else:

        st.session_state.user = None


# ============================================
# 💬 CHAT HISTORY
# ============================================

if "chat_history" not in st.session_state:

    st.session_state.chat_history = []


# ============================================
# 📊 LAST RESULTS
# ============================================

if "last_predictions" not in st.session_state:

    st.session_state.last_predictions = None


if "last_interpretation" not in st.session_state:

    st.session_state.last_interpretation = None


# ============================================
# 🎛 SIDEBAR
# ============================================

render_sidebar(
    cookies
)


# ============================================
# 🏥 HERO SECTION
# ============================================

render_hero()


# ============================================
# 📘 EXAMPLE PROFILES
# ============================================

render_example_profiles()


# ============================================
# 📊 HEALTH ASSESSMENT FORM
# ============================================

submitted, payload = (
    render_assessment_form()
)


# ============================================
# 🚀 AI PREDICTION PIPELINE
# ============================================

if submitted:

    try:

        # ====================================
        # 🧠 PREMIUM AI LOADING EXPERIENCE
        # ====================================

        progress_container = st.container()

        with progress_container:

            st.markdown("""

<div class="glass-card">

<h2>
🧠 AI Health Intelligence Pipeline
</h2>

<p style="
opacity:0.9;
line-height:1.8;
">

The hybrid AI system is currently analyzing your wellness profile using Machine Learning, Deep Learning, behavioral analytics, and AI interpretation models.

</p>

</div>

""", unsafe_allow_html=True)


            progress_bar = st.progress(0)

            status_text = st.empty()


            loading_steps = [

                (
                    "🧠 Initializing Hybrid AI Pipeline...",
                    12
                ),

                (
                    "📊 Running Wellness Analytics...",
                    28
                ),

                (
                    "🤖 Evaluating Machine Learning Models...",
                    48
                ),

                (
                    "🧬 Running Deep Learning Inference...",
                    68
                ),

                (
                    "💬 Generating AI Wellness Interpretation...",
                    84
                ),

                (
                    "📄 Preparing Healthcare Analytics Report...",
                    96
                ),

                (
                    "✅ Finalizing Assessment Results...",
                    100
                )
            ]


            for step_text, progress_value in loading_steps:

                status_text.markdown(f"""

<div class="glass-card">

<h4>
{step_text}
</h4>

</div>

""", unsafe_allow_html=True)

                progress_bar.progress(
                    progress_value
                )

                time.sleep(0.55)


        # ====================================
        # 👤 ATTACH USER EMAIL
        # ====================================

        if st.session_state.user:

            payload["user_email"] = (

                st.session_state.user["email"]
            )


        # ====================================
        # 🌐 API REQUEST
        # ====================================

        response = predict_health(
            payload
        )


        progress_container.empty()


        # ========================================
        # ❌ API FAILURE
        # ========================================

        if response is None:

            st.error(
                "Unable to connect to backend API."
            )

            st.stop()


        # ========================================
        # ✅ SUCCESS
        # ========================================

        if response.status_code == 200:

            data = response.json()


            predictions = data.get(
                "predictions",
                {}
            )

            interpretation = data.get(
                "interpretation",
                ""
            )


            # ====================================
            # 💾 STORE SESSION RESULTS
            # ====================================

            st.session_state.last_predictions = (
                predictions
            )

            st.session_state.last_interpretation = (
                interpretation
            )


            # ====================================
            # 🎉 SUCCESS MESSAGE
            # ====================================

            st.success(
                "✅ AI Health Assessment Generated Successfully"
            )


            # ====================================
            # 🌿 WELLNESS SCORE
            # ====================================

            render_wellness_score(
                payload
            )


            # ====================================
            # 📊 RISK DASHBOARD
            # ====================================

            render_risk_dashboard(
                predictions
            )


            # ====================================
            # 🧠 AI INTERPRETATION
            # ====================================

            render_interpretation(
                interpretation
            )


        # ========================================
        # ❌ API ERROR
        # ========================================

        else:

            try:

                error_detail = response.json()

            except Exception:

                error_detail = response.text


            st.error(
                f"API Error: {error_detail}"
            )


    # ============================================
    # ❌ GLOBAL EXCEPTION
    # ============================================

    except Exception as e:

        st.error(
            f"Unexpected Error: {str(e)}"
        )


# ============================================
# 💬 AI HEALTH CHAT
# ============================================

render_chat()


# ============================================
# 📜 REPORT HISTORY
# ============================================

if st.session_state.user:

    render_report_history()


# ============================================
# 🚀 FOOTER
# ============================================

render_footer()