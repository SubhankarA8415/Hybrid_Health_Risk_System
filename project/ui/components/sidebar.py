# ============================================
# 🎛 FINAL PREMIUM SIDEBAR COMPONENT
# ============================================

import streamlit as st

from datetime import datetime


# ============================================
# 🌐 API CLIENT
# ============================================

from project.ui.services.api_client import (

    login_user,

    register_user,

    get_reports
)


# ============================================
# 🎨 WELLNESS STATUS
# ============================================

def get_wellness_indicator(
    score
):

    if score >= 80:

        return "🟢", "Excellent"

    elif score >= 60:

        return "🟡", "Good"

    elif score >= 40:

        return "🟠", "Moderate"

    return "🔴", "High Risk"


# ============================================
# 🚀 MAIN SIDEBAR
# ============================================

def render_sidebar(
    cookies
):

    with st.sidebar:

        # ====================================
        # 🩺 APP HERO
        # ====================================

        st.markdown("""

<div style="
text-align:center;
padding-top:0.4rem;
padding-bottom:1rem;
">

<div style="
font-size:3.7rem;
margin-bottom:-0.5rem;
">
🩺
</div>

<h1 style="
font-size:1.9rem;
font-weight:700;
margin-bottom:0.3rem;
">
AI Health Companion
</h1>

<p style="
opacity:0.84;
line-height:1.7;
font-size:0.93rem;
">

AI-powered preventive healthcare,
wellness intelligence,
and personalized risk analytics platform

</p>

</div>

""", unsafe_allow_html=True)


        st.markdown("---")


        # ====================================
        # 👤 AUTHENTICATED USER
        # ====================================

        if st.session_state.user:

            user = st.session_state.user


            # ================================
            # 👋 USER PROFILE
            # ================================

            st.markdown(f"""

<div class="glass-card">

<h3 style="
margin-bottom:0.4rem;
">
👋 Welcome Back
</h3>

<p style="
font-size:1.08rem;
font-weight:600;
margin-bottom:0.15rem;
">
{user['name']}
</p>

<p style="
opacity:0.72;
font-size:0.9rem;
margin-top:0;
">
📧 {user['email']}
</p>

</div>

""", unsafe_allow_html=True)


            # ================================
            # 🚀 CURRENT FEATURES
            # ================================

            with st.expander(
                "🚀 Current Platform Features",
                expanded=False
            ):

                st.markdown("""

### 🧠 Active AI Features

- 🤖 Hybrid ML + DL Predictions
- 🩸 Diabetes Risk Intelligence
- ❤️ Heart Disease Analysis
- ⚖️ Obesity Risk Assessment
- 🧠 AI Wellness Interpretation
- 💬 Conversational AI Assistant
- 📜 Persistent Health Reports
- 🌿 Wellness Score Engine
- 📊 Personalized Risk Analytics

""")


            # ================================
            # 📜 RECENT REPORTS
            # ================================

            st.markdown("""
### 📜 Recent Reports
""")


            try:

                response = get_reports(
                    user["email"]
                )


                if (

                    response

                    and response.status_code == 200
                ):

                    reports = response.json()


                    if len(reports) == 0:

                        st.info(
                            "No reports generated yet."
                        )

                    else:

                        for report in reports[:3]:

                            score = report.get(
                                "wellness_score",
                                0
                            )

                            emoji, label = (
                                get_wellness_indicator(
                                    score
                                )
                            )

                            formatted_time = report.get(
                                "created_at",
                                "Unknown"
                            )

                            try:

                                formatted_time = (
                                    datetime.fromisoformat(
                                        formatted_time
                                    ).strftime(
                                        "%d %b %Y • %I:%M %p"
                                    )
                                )

                            except Exception:

                                pass


                            st.markdown(f"""

<div class="glass-card">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
margin-bottom:0.5rem;
">

<b style="
font-size:1rem;
">
{emoji} {score}/100
</b>

<span style="
font-size:0.78rem;
opacity:0.72;
">
{label}
</span>

</div>

<div style="
font-size:0.82rem;
opacity:0.7;
line-height:1.5;
">
🕒 {formatted_time}
</div>

</div>

""", unsafe_allow_html=True)


                else:

                    st.warning(
                        "Unable to load reports."
                    )

            except Exception:

                st.warning(
                    "Backend unavailable."
                )


            # ================================
            # 🔮 FUTURE ROADMAP
            # ================================

            with st.expander(
                "🔮 Future Vision & Roadmap",
                expanded=False
            ):

                st.markdown("""

### 🚀 Planned Enhancements

- 📈 Longitudinal wellness tracking
- ⌚ Wearable & smartwatch integration
- 🧠 Medical image intelligence
- 🌿 Personalized AI health coaching
- 🩺 Expanded disease prediction ecosystem
- 📊 Real-time health analytics
- 🚑 Emergency healthcare assistance
- 🌐 Multilingual AI assistant
- 📱 Dedicated mobile application

---

### 💙 Long-Term Goal

Build an intelligent AI-assisted preventive
healthcare ecosystem capable of supporting
personalized wellness awareness,
risk monitoring,
and accessible healthcare intelligence.

""")


            # ================================
            # 🚪 LOGOUT
            # ================================

            st.markdown("<br>", unsafe_allow_html=True)

            if st.button(

                "🚪 Logout",

                use_container_width=True
            ):

                st.session_state.user = None

                st.session_state.chat_history = []

                st.session_state.last_predictions = None

                st.session_state.last_interpretation = None

                cookies["user_email"] = ""

                cookies["user_name"] = ""

                cookies.save()

                st.rerun()


        # ====================================
        # 👤 GUEST MODE
        # ====================================

        else:

            st.markdown("""

<div class="glass-card">

<h3 style="
margin-bottom:0.7rem;
">
🌿 Guest Mode
</h3>

<p style="
line-height:1.8;
opacity:0.9;
">

You are currently exploring the platform in guest mode.

Login or create an account to unlock:

• 📜 Persistent AI reports  
• 💬 Saved AI conversations  
• 🌿 Wellness history  
• 📊 Personalized analytics  
• 🧠 Continuous wellness insights  

</p>

</div>

""", unsafe_allow_html=True)


            # ================================
            # 🔑 LOGIN PANEL
            # ================================

            with st.expander(
                "🔑 Login",
                expanded=True
            ):

                login_email = st.text_input(

                    "Email Address",

                    key="login_email"
                )

                login_password = st.text_input(

                    "Password",

                    type="password",

                    key="login_password"
                )


                if st.button(

                    "🔓 Login",

                    use_container_width=True
                ):

                    try:

                        response = login_user({

                            "email":
                            login_email,

                            "password":
                            login_password
                        })


                        if (

                            response

                            and response.status_code == 200
                        ):

                            user_data = response.json()


                            st.session_state.user = {

                                "name":
                                user_data["name"],

                                "email":
                                user_data["email"]
                            }


                            cookies["user_email"] = (
                                user_data["email"]
                            )

                            cookies["user_name"] = (
                                user_data["name"]
                            )

                            cookies.save()

                            st.success(
                                "Login successful"
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Invalid credentials"
                            )

                    except Exception as e:

                        st.error(
                            f"Login Error: {str(e)}"
                        )


            # ================================
            # 📝 REGISTER PANEL
            # ================================

            with st.expander(
                "📝 Create Account",
                expanded=False
            ):

                register_name = st.text_input(

                    "Full Name",

                    key="register_name"
                )

                register_email = st.text_input(

                    "Email Address",

                    key="register_email"
                )

                register_password = st.text_input(

                    "Create Password",

                    type="password",

                    key="register_password"
                )


                if st.button(

                    "🚀 Create Account",

                    use_container_width=True
                ):

                    try:

                        response = register_user({

                            "name":
                            register_name,

                            "email":
                            register_email,

                            "password":
                            register_password
                        })


                        if (

                            response

                            and response.status_code == 200
                        ):

                            user_data = response.json()


                            st.session_state.user = {

                                "name":
                                user_data["name"],

                                "email":
                                user_data["email"]
                            }


                            cookies["user_email"] = (
                                user_data["email"]
                            )

                            cookies["user_name"] = (
                                user_data["name"]
                            )

                            cookies.save()

                            st.success(
                                "Account created successfully"
                            )

                            st.rerun()

                        else:

                            st.error(
                                "Registration failed"
                            )

                    except Exception as e:

                        st.error(
                            f"Registration Error: {str(e)}"
                        )


            # ================================
            # 🔮 FUTURE FEATURES
            # ================================

            with st.expander(
                "🔮 Future Vision",
                expanded=False
            ):

                st.markdown("""

### 🚀 Upcoming Enhancements

- 📈 Longitudinal wellness tracking
- 🌿 Personalized AI wellness coaching
- ⌚ Smart wearable integration
- 📱 Dedicated mobile application
- 🌐 Multilingual AI support
- 🧠 Advanced healthcare intelligence

""")


        # ====================================
        # 🌿 FOOTNOTE
        # ====================================

        st.markdown("<br>", unsafe_allow_html=True)

        st.caption("""
💙 Preventive Healthcare • AI Wellness Intelligence • Responsible AI Research Prototype
""")