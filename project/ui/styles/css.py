# ============================================
# 🎨 MODERN PREMIUM UI THEME
# ============================================

CUSTOM_CSS = """

<style>


/* =========================================
🌌 GLOBAL APP
========================================= */

html,
body,
[class*="css"]  {

    font-family:
        "Inter",
        "Segoe UI",
        sans-serif;
}


.stApp {

    background:
        radial-gradient(
            circle at top left,
            rgba(67, 97, 238, 0.12),
            transparent 25%
        ),

        radial-gradient(
            circle at bottom right,
            rgba(45, 106, 79, 0.15),
            transparent 25%
        ),

        linear-gradient(
            135deg,
            #0B1220,
            #111827,
            #0F172A
        );

    color: #F8FAFC;
}


/* =========================================
📦 MAIN CONTAINER
========================================= */

.block-container {

    padding-top: 2rem;

    padding-bottom: 2rem;

    max-width: 1400px;
}


/* =========================================
🎛 SIDEBAR
========================================= */

[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            rgba(15, 23, 42, 0.98),
            rgba(17, 24, 39, 0.98)
        );

    border-right:
        1px solid rgba(255,255,255,0.06);
}


/* =========================================
✨ GLASS CARD
========================================= */

.glass-card {

    background:
        rgba(255, 255, 255, 0.05);

    backdrop-filter:
        blur(12px);

    -webkit-backdrop-filter:
        blur(12px);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 1.2rem;

    margin-bottom: 1rem;

    box-shadow:
        0 8px 32px rgba(0,0,0,0.25);
}


/* =========================================
🩺 HERO SECTION
========================================= */

.hero-card {

    background:

        linear-gradient(
            135deg,
            rgba(29, 78, 216, 0.92),
            rgba(67, 56, 202, 0.88),
            rgba(13, 148, 136, 0.85)
        );

    border-radius: 28px;

    padding: 2.8rem;

    color: white;

    margin-bottom: 2rem;

    box-shadow:
        0 10px 40px rgba(37, 99, 235, 0.35);

    border:
        1px solid rgba(255,255,255,0.08);
}


.hero-card h1 {

    font-size: 3rem;

    font-weight: 800;

    margin-bottom: 0.5rem;
}


.hero-card p {

    font-size: 1.05rem;

    opacity: 0.92;

    line-height: 1.7;
}


/* =========================================
📊 METRIC CARDS
========================================= */

.metric-card {

    background:
        rgba(255,255,255,0.05);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 20px;

    padding: 1.2rem;

    margin-bottom: 1rem;

    box-shadow:
        0 8px 20px rgba(0,0,0,0.22);

    transition:
        all 0.25s ease;
}


.metric-card:hover {

    transform:
        translateY(-3px);

    border:
        1px solid rgba(99,102,241,0.4);
}


/* =========================================
🌿 WELLNESS SCORE
========================================= */

.wellness-score {

    background:

        linear-gradient(
            135deg,
            rgba(76, 29, 149, 0.95),
            rgba(79, 70, 229, 0.92),
            rgba(59, 130, 246, 0.88)
        );

    border-radius: 24px;

    padding: 2rem;

    color: white;

    text-align: center;

    margin-bottom: 2rem;

    box-shadow:
        0 12px 35px rgba(79,70,229,0.35);
}


/* =========================================
📘 EXAMPLE PROFILE CARD
========================================= */

.example-card {

    background:
        rgba(255,255,255,0.045);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 1.3rem;

    min-height: 320px;

    margin-bottom: 1rem;

    backdrop-filter:
        blur(10px);

    transition:
        all 0.25s ease;

    box-shadow:
        0 6px 20px rgba(0,0,0,0.22);
}


.example-card:hover {

    transform:
        translateY(-4px);

    border:
        1px solid rgba(99,102,241,0.4);
}


.example-card h3 {

    margin-bottom: 1rem;

    font-size: 1.2rem;
}


.example-card ul {

    padding-left: 1.2rem;

    line-height: 1.8;
}


.example-card p {

    margin-top: 1rem;

    opacity: 0.9;
}


/* =========================================
📥 INPUTS
========================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {

    background:
        rgba(255,255,255,0.05) !important;

    color: white !important;

    border-radius: 14px !important;

    border:
        1px solid rgba(255,255,255,0.08) !important;

    padding: 0.7rem !important;
}


/* =========================================
🎚 SLIDERS
========================================= */

.stSlider {

    padding-top: 0.5rem;
}


/* =========================================
🔘 BUTTONS
========================================= */

.stButton button {

    width: 100%;

    border-radius: 14px;

    border: none;

    padding: 0.75rem 1rem;

    font-weight: 600;

    font-size: 0.95rem;

    background:
        linear-gradient(
            135deg,
            #4F46E5,
            #2563EB
        );

    color: white;

    transition:
        all 0.25s ease;

    box-shadow:
        0 6px 18px rgba(79,70,229,0.28);
}


.stButton button:hover {

    transform:
        translateY(-2px);

    box-shadow:
        0 10px 24px rgba(79,70,229,0.38);
}


/* =========================================
📜 EXPANDERS
========================================= */

.streamlit-expanderHeader {

    background:
        rgba(255,255,255,0.04);

    border-radius: 14px;

    border:
        1px solid rgba(255,255,255,0.08);
}


details {

    background:
        rgba(255,255,255,0.03);

    border-radius: 16px;

    padding: 0.4rem;
}


/* =========================================
💬 CHAT SECTION
========================================= */

.chat-section {

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 1.4rem;

    backdrop-filter:
        blur(10px);
}


/* =========================================
📊 JSON DISPLAY
========================================= */

.stJson {

    border-radius: 16px;

    overflow: hidden;
}


/* =========================================
📈 METRICS
========================================= */

[data-testid="metric-container"] {

    background:
        rgba(255,255,255,0.045);

    border:
        1px solid rgba(255,255,255,0.08);

    padding: 1rem;

    border-radius: 20px;

    box-shadow:
        0 4px 18px rgba(0,0,0,0.18);
}


/* =========================================
🦶 FOOTER
========================================= */

.footer {

    text-align: center;

    color: rgba(255,255,255,0.65);

    padding-top: 3rem;

    padding-bottom: 1rem;

    font-size: 0.92rem;
}


/* =========================================
📱 RESPONSIVE
========================================= */

@media (max-width: 768px) {

    .hero-card {

        padding: 2rem;
    }

    .hero-card h1 {

        font-size: 2rem;
    }

    .example-card {

        min-height: auto;
    }
}

/* =========================================
💬 PREMIUM CHAT BUBBLES
========================================= */

[data-testid="stChatMessage"] {

    background:
        rgba(255,255,255,0.04);

    border:
        1px solid rgba(255,255,255,0.08);

    border-radius: 22px;

    padding: 1rem 1.2rem;

    margin-bottom: 1rem;

    backdrop-filter:
        blur(10px);

    box-shadow:
        0 6px 20px rgba(0,0,0,0.18);

    transition:
        all 0.25s ease;
}


[data-testid="stChatMessage"]:hover {

    transform:
        translateY(-2px);

    border:
        1px solid rgba(99,102,241,0.35);
}


/* =========================================
🤖 ASSISTANT CHAT
========================================= */

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) {

    background:
        linear-gradient(
            135deg,
            rgba(79,70,229,0.14),
            rgba(37,99,235,0.10)
        );

    border:
        1px solid rgba(99,102,241,0.22);
}


/* =========================================
👤 USER CHAT
========================================= */

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {

    background:
        linear-gradient(
            135deg,
            rgba(16,185,129,0.10),
            rgba(6,182,212,0.08)
        );

    border:
        1px solid rgba(16,185,129,0.18);
}


/* =========================================
💬 CHAT INPUT
========================================= */

[data-testid="stChatInput"] {

    background:
        rgba(255,255,255,0.04);

    border-radius: 20px;

    border:
        1px solid rgba(255,255,255,0.08);

    padding: 0.5rem;

    box-shadow:
        0 4px 16px rgba(0,0,0,0.18);
}


/* =========================================
✨ CHAT INPUT FIELD
========================================= */

[data-testid="stChatInput"] textarea {

    color: white !important;

    background:
        transparent !important;
}


/* =========================================
🧠 CHAT SECTION CONTAINER
========================================= */

.chat-wrapper {

    background:
        rgba(255,255,255,0.03);

    border:
        1px solid rgba(255,255,255,0.06);

    border-radius: 28px;

    padding: 1.5rem;

    backdrop-filter:
        blur(10px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.2);
}


/* =========================================
🌿 SUGGESTION PILLS
========================================= */

.suggestion-pill {

    display: inline-block;

    padding: 0.55rem 1rem;

    margin: 0.35rem;

    border-radius: 999px;

    background:
        rgba(99,102,241,0.14);

    border:
        1px solid rgba(99,102,241,0.25);

    color: white;

    font-size: 0.9rem;

    transition:
        all 0.25s ease;
}


.suggestion-pill:hover {

    background:
        rgba(99,102,241,0.24);

    transform:
        translateY(-2px);
}


/* =========================================
🤖 AI THINKING
========================================= */

.ai-thinking {

    display: flex;

    align-items: center;

    gap: 0.6rem;

    padding: 1rem;

    border-radius: 18px;

    background:
        rgba(99,102,241,0.08);

    border:
        1px solid rgba(99,102,241,0.16);

    margin-top: 0.5rem;

    margin-bottom: 1rem;
}

/* =========================================
✨ GLOBAL SMOOTHNESS
========================================= */

* {

    transition:
        background 0.25s ease,
        border 0.25s ease,
        transform 0.25s ease,
        box-shadow 0.25s ease,
        opacity 0.25s ease;
}


/* =========================================
🌌 FLOATING GLASS EFFECT
========================================= */

.glass-card {

    position: relative;

    overflow: hidden;
}


.glass-card::before {

    content: "";

    position: absolute;

    inset: 0;

    background:
        linear-gradient(
            120deg,
            rgba(255,255,255,0.04),
            transparent 40%
        );

    opacity: 0;

    transition:
        opacity 0.4s ease;
}


.glass-card:hover::before {

    opacity: 1;
}


.glass-card:hover {

    transform:
        translateY(-4px);

    border:
        1px solid rgba(99,102,241,0.25);

    box-shadow:
        0 14px 40px rgba(0,0,0,0.32),
        0 0 22px rgba(99,102,241,0.12);
}


/* =========================================
🚀 HERO FLOAT EFFECT
========================================= */

.hero-card {

    position: relative;

    overflow: hidden;
}


.hero-card::after {

    content: "";

    position: absolute;

    width: 220px;
    height: 220px;

    background:
        radial-gradient(
            rgba(255,255,255,0.18),
            transparent 70%
        );

    top: -80px;
    right: -80px;

    opacity: 0.4;
}


/* =========================================
📊 METRIC HOVER GLOW
========================================= */

[data-testid="metric-container"]:hover {

    transform:
        translateY(-3px);

    border:
        1px solid rgba(99,102,241,0.28);

    box-shadow:
        0 12px 30px rgba(0,0,0,0.28),
        0 0 18px rgba(99,102,241,0.10);
}


/* =========================================
📘 EXAMPLE PROFILE GLOW
========================================= */

.example-card:hover {

    transform:
        translateY(-5px)
        scale(1.01);

    box-shadow:
        0 14px 35px rgba(0,0,0,0.3),
        0 0 18px rgba(99,102,241,0.12);
}


/* =========================================
🔘 BUTTON PREMIUM EFFECT
========================================= */

.stButton button {

    position: relative;

    overflow: hidden;
}


.stButton button::before {

    content: "";

    position: absolute;

    top: 0;
    left: -120%;

    width: 120%;
    height: 100%;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(255,255,255,0.22),
            transparent
        );

    transition:
        all 0.6s ease;
}


.stButton button:hover::before {

    left: 120%;
}


.stButton button:hover {

    transform:
        translateY(-3px)
        scale(1.01);

    box-shadow:
        0 14px 30px rgba(79,70,229,0.4);
}


/* =========================================
💬 CHAT PREMIUM DEPTH
========================================= */

[data-testid="stChatMessage"]:hover {

    transform:
        translateY(-3px)
        scale(1.005);

    box-shadow:
        0 10px 28px rgba(0,0,0,0.25),
        0 0 18px rgba(99,102,241,0.08);
}


/* =========================================
🌿 WELLNESS GLOW
========================================= */

.wellness-score:hover {

    transform:
        translateY(-4px);

    box-shadow:
        0 18px 42px rgba(79,70,229,0.42),
        0 0 25px rgba(59,130,246,0.16);
}


/* =========================================
📈 PLOTLY CHART CONTAINERS
========================================= */

.js-plotly-plot {

    border-radius: 22px;

    overflow: hidden;

    backdrop-filter:
        blur(8px);
}


/* =========================================
🎛 SIDEBAR HOVER ITEMS
========================================= */

[data-testid="stSidebar"] .stButton button:hover {

    box-shadow:
        0 10px 22px rgba(79,70,229,0.32);
}


/* =========================================
📥 INPUT GLOW
========================================= */

.stTextInput input:focus,
.stTextArea textarea:focus {

    border:
        1px solid rgba(99,102,241,0.4) !important;

    box-shadow:
        0 0 0 3px rgba(99,102,241,0.12) !important;
}


/* =========================================
🎚 SLIDER GLOW
========================================= */

.stSlider:hover {

    filter:
        drop-shadow(
            0 0 10px rgba(99,102,241,0.18)
        );
}


/* =========================================
📱 RESPONSIVE ENHANCEMENTS
========================================= */

@media (max-width: 768px) {

    .glass-card,
    .example-card,
    .wellness-score {

        padding: 1rem;
    }

    .hero-card {

        padding: 1.6rem;
    }

    .hero-card h1 {

        font-size: 1.8rem;
    }
}


/* =========================================
✨ SOFT PAGE ENTRY
========================================= */

.block-container {

    animation:
        fadeIn 0.6s ease;
}


@keyframes fadeIn {

    from {

        opacity: 0;

        transform:
            translateY(10px);
    }

    to {

        opacity: 1;

        transform:
            translateY(0);
    }
}

</style>

"""

