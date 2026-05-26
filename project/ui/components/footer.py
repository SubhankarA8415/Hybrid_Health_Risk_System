# ============================================
# 🚀 MODERN FOOTER & FUTURE ROADMAP
# ============================================

import streamlit as st


# ============================================
# 🚀 RENDER FOOTER
# ============================================

def render_footer():

    st.markdown("---")


    # ========================================
    # 🔮 FUTURE ROADMAP
    # ========================================

    with st.expander(
        "🔮 Future Vision & Platform Roadmap"
    ):

        st.markdown("""

<div class="glass-card">

<h2>
🌍 Long-Term Platform Vision
</h2>

<p style="
line-height: 1.9;
opacity: 0.92;
">

Our long-term vision is to gradually evolve this platform into a more advanced
AI-assisted preventive healthcare ecosystem capable of supporting
personalized wellness monitoring, intelligent health analytics,
and proactive lifestyle guidance through responsible AI technologies.

</p>

</div>

""", unsafe_allow_html=True)


        # ====================================
        # 🧠 CURRENT PLATFORM
        # ====================================

        st.markdown("""

<div class="glass-card">

<h3>
🧠 Current AI Healthcare Prototype
</h3>

<p style="
line-height: 1.9;
opacity: 0.92;
">

The current system supports AI-powered analysis of:

</p>

<ul style="
line-height: 2;
">

<li>🩸 Diabetes risk assessment</li>
<li>❤️ Heart disease risk assessment</li>
<li>⚖️ Obesity risk assessment</li>
<li>💬 Conversational wellness assistance</li>
<li>📊 AI-generated wellness analytics</li>

</ul>

<p style="
line-height: 1.9;
opacity: 0.92;
">

using a hybrid pipeline involving:

<b>Machine Learning</b>,
<b>Deep Learning</b>,
<b>Behavioral Analytics</b>,
and
<b>Large Language Models (LLMs)</b>.

</p>

</div>

""", unsafe_allow_html=True)


        # ====================================
        # 🚀 FUTURE FEATURES
        # ====================================

        st.markdown("""

<div class="glass-card">

<h3>
🚀 Planned Future Enhancements
</h3>

<ul style="
line-height: 2;
">

<li>📈 Longitudinal wellness and risk tracking</li>

<li>⌚ Smart wearable & IoT health integration</li>

<li>🧠 Medical image intelligence using deep learning</li>

<li>🌿 Personalized preventive health coaching</li>

<li>🩺 Expanded multi-disease prediction ecosystem</li>

<li>📊 Real-time health analytics & monitoring</li>

<li>🚑 Intelligent emergency health assistance support</li>

<li>🌐 Multilingual AI wellness assistance</li>

<li>📱 Dedicated mobile health companion application</li>

</ul>

</div>

""", unsafe_allow_html=True)


        # ====================================
        # 💙 MISSION
        # ====================================

        st.markdown("""

<div class="glass-card">

<h3>
💙 Responsible AI Wellness Mission
</h3>

<p style="
line-height: 1.9;
opacity: 0.92;
">

We believe responsible AI technologies can help improve
preventive wellness awareness, health education,
and accessibility when designed ethically and transparently.

This platform is intended as a supportive educational
wellness companion and research-oriented healthcare AI prototype —
not a replacement for professional healthcare services,
clinical diagnosis, or medical treatment.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 🌿 WELLNESS MESSAGE
    # ========================================

    st.success("""
🌱 Small healthy habits, preventive awareness, and consistent wellness improvements today can create a healthier tomorrow.
""")


    # ========================================
    # 🦶 FINAL FOOTER
    # ========================================

    st.markdown("""

<div class="footer">

<h2>
🩺 AI Health Companion
</h2>

<p style="
font-size: 1rem;
opacity: 0.88;
">

AI-powered preventive wellness and healthcare analytics platform prototype

</p>

<br>

<p style="
line-height: 2;
">

🤖 Hybrid Machine Learning & Deep Learning  
💬 Conversational AI Wellness Assistant  
📊 Personalized Risk Analytics  
⚡ FastAPI Backend Architecture  
🎨 Streamlit Intelligent Frontend  

</p>

<br>

<p style="
opacity: 0.75;
line-height: 1.8;
">

⚠ This platform is NOT a certified medical diagnostic system and should not replace professional healthcare consultation, diagnosis, or treatment.

</p>

<br>

<p style="
opacity: 0.6;
">

© 2026 AI Health Companion • Preventive Healthcare AI Research Prototype

</p>

</div>

""", unsafe_allow_html=True)