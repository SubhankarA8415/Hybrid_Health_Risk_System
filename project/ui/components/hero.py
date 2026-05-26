# ============================================
# 🏥 MODERN HERO COMPONENT
# ============================================

import streamlit as st


# ============================================
# 🚀 HERO SECTION
# ============================================

def render_hero():

    # ========================================
    # 🏥 MAIN HERO
    # ========================================

    st.markdown("""

<div class="hero-card">

<h1>
🩺 AI Health Companion
</h1>

<p style="
font-size: 1.15rem;
margin-top: 1rem;
margin-bottom: 1.5rem;
max-width: 900px;
line-height: 1.8;
">

An intelligent hybrid AI-powered preventive healthcare platform
designed to analyze lifestyle patterns, estimate potential health risks,
and generate personalized wellness insights using advanced
Machine Learning, Deep Learning, and Conversational AI technologies.

</p>


<div style="
display: flex;
flex-wrap: wrap;
gap: 0.7rem;
margin-top: 1.5rem;
">

<span style="
background: rgba(255,255,255,0.12);
padding: 0.55rem 1rem;
border-radius: 999px;
font-size: 0.92rem;
">
🤖 Hybrid ML + DL Intelligence
</span>

<span style="
background: rgba(255,255,255,0.12);
padding: 0.55rem 1rem;
border-radius: 999px;
font-size: 0.92rem;
">
💬 Conversational AI Assistant
</span>

<span style="
background: rgba(255,255,255,0.12);
padding: 0.55rem 1rem;
border-radius: 999px;
font-size: 0.92rem;
">
📊 Personalized Risk Analytics
</span>

<span style="
background: rgba(255,255,255,0.12);
padding: 0.55rem 1rem;
border-radius: 999px;
font-size: 0.92rem;
">
🌿 Wellness Monitoring
</span>

<span style="
background: rgba(255,255,255,0.12);
padding: 0.55rem 1rem;
border-radius: 999px;
font-size: 0.92rem;
">
🧠 AI-generated Health Insights
</span>

</div>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 📊 QUICK PLATFORM STATS
    # ========================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🤖 AI Models",
            "Hybrid ML + DL"
        )

    with col2:

        st.metric(
            "📊 Analysis",
            "Multi-Disease"
        )

    with col3:

        st.metric(
            "💬 Assistant",
            "LLM Powered"
        )

    with col4:

        st.metric(
            "🌿 Focus",
            "Preventive Care"
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # ========================================
    # 🌿 PLATFORM OVERVIEW
    # ========================================

    st.markdown("""

<div class="glass-card">

<h3>
🌿 Intelligent Preventive Healthcare Ecosystem
</h3>

<p style="
font-size: 1rem;
line-height: 1.8;
opacity: 0.92;
">

This platform combines:
<b>Machine Learning</b>,
<b>Deep Learning</b>,
<b>Behavioral Analytics</b>,
and
<b>Large Language Models</b>

to assist users in understanding
potential lifestyle-related health risks and encourage
proactive wellness management through AI-generated insights,
risk estimation, and personalized health guidance.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # ⚠ IMPORTANT DISCLAIMER
    # ========================================

    st.warning("""
⚠ This platform is an AI-assisted wellness and preventive healthcare prototype and NOT a certified medical diagnostic system.

Predictions are probabilistic AI-generated estimates intended for educational and wellness support purposes only and should not replace professional medical consultation or clinical diagnosis.
""")


    # ========================================
    # 📘 HOW TO USE
    # ========================================

    with st.expander(
        "📘 How To Use The Platform"
    ):

        st.markdown("""

### 🚀 Quick Workflow

1. Enter your health and lifestyle information carefully.
2. Generate your AI-powered health assessment.
3. Review:
   - disease risk probabilities
   - wellness score
   - personalized AI-generated interpretation
4. Explore historical reports and AI wellness analytics.
5. Continue interacting with the AI Health Assistant for wellness guidance.

---

### 💡 Example Questions For The AI Assistant

- “How can I improve my sleep quality?”
- “Suggest a beginner home workout plan”
- “Tips for reducing stress naturally”
- “Healthy meal recommendations”
- “How to improve cardiovascular health?”
- “Daily wellness routine suggestions”

---

### 🧠 Core AI Capabilities

- Hybrid Machine Learning + Deep Learning pipeline
- Personalized health risk prediction
- Conversational AI wellness assistant
- Lifestyle-based preventive analytics
- Persistent AI-generated health reports
- Wellness scoring and monitoring

""")