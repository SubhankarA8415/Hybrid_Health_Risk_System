# ============================================
# 🧠 MODERN AI INTERPRETATION COMPONENT
# ============================================

import streamlit as st


# ============================================
# 🚀 RENDER INTERPRETATION
# ============================================

def render_interpretation(
    interpretation
):

    st.markdown("---")

    st.header(
        "🧠 AI Wellness Guidance"
    )

    st.caption("""
Personalized AI-generated wellness interpretation and preventive health insights.
""")


    # ========================================
    # 🌟 AI SUMMARY INTRO
    # ========================================

    st.markdown("""

<div class="glass-card">

<h3>
🤖 AI-Powered Personalized Wellness Insights
</h3>

<p style="
line-height: 1.8;
opacity: 0.92;
">

Your health and lifestyle profile has been analyzed using
our hybrid Machine Learning, Deep Learning,
and Conversational AI system to generate
personalized wellness observations,
risk-aware guidance,
and preventive health recommendations.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 📜 MAIN AI INTERPRETATION
    # ========================================

    st.markdown("""

<div class="glass-card">

<h3>
📋 Personalized AI Interpretation
</h3>

</div>

""", unsafe_allow_html=True)


    st.markdown(f"""

<div class="metric-card">

<div style="
line-height: 1.9;
font-size: 1rem;
opacity: 0.96;
">

{interpretation}

</div>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 🌿 WELLNESS PRINCIPLES
    # ========================================

    st.markdown("""

<div class="glass-card">

<h3>
🌿 Preventive Wellness Focus
</h3>

<p style="
line-height: 1.9;
opacity: 0.92;
">

Long-term wellness improvement is often driven by
small but consistent lifestyle enhancements involving:

</p>

<ul style="
line-height: 2;
">

<li>😴 Better sleep consistency</li>
<li>🏃 Increased physical activity</li>
<li>🥗 Balanced nutritional habits</li>
<li>🧠 Mental wellness management</li>
<li>💧 Hydration and recovery</li>
<li>🩺 Preventive healthcare awareness</li>

</ul>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # ⚠ IMPORTANT DISCLAIMER
    # ========================================

    st.warning("""
⚠ AI-generated wellness guidance is intended for educational and preventive wellness support purposes only.

This platform is NOT a certified medical diagnostic system and should not replace professional medical consultation, diagnosis, or treatment.
""")


    # ========================================
    # 💬 CONTINUE WITH AI
    # ========================================

    st.markdown("""

<div class="glass-card">

<h3>
💬 Continue Your Wellness Journey
</h3>

<p style="
line-height: 1.8;
opacity: 0.92;
">

You can continue interacting with the AI Health Assistant below for:

</p>

<ul style="
line-height: 2;
">

<li>🥗 Healthy meal recommendations</li>
<li>🏋 Beginner-friendly workout guidance</li>
<li>😴 Sleep improvement strategies</li>
<li>🧘 Stress and mental wellness support</li>
<li>❤️ Cardiovascular wellness tips</li>
<li>🌿 Sustainable healthy habit development</li>
<li>📚 Preventive healthcare education</li>

</ul>

</div>

""", unsafe_allow_html=True)