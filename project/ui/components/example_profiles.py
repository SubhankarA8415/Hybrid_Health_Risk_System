# ============================================
# 📘 EXAMPLE PROFILES COMPONENT
# ============================================

import streamlit as st


# ============================================
# 🛡 SAFE VALUE CALIBRATION
# ============================================

def clamp(

    value,

    min_value,

    max_value
):

    return min(

        max(
            value,
            min_value
        ),

        max_value
    )


# ============================================
# 📏 MODEL-ALIGNED LIMITS
# ============================================

LIMITS = {

    # 👤 BASIC
    "age": (18, 100),
    "gender": (0, 1),
    "bmi": (10.0, 60.0),

    # 🩺 WELLNESS
    "general_health": (1, 5),
    "sleep_hours": (0, 24),
    "mental_health_days": (0, 30),
    "physical_health_days": (0, 30),

    # 🏃 LIFESTYLE
    "activity_minutes": (0, 3000),
    "sedentary": (0, 1),
    "exercise_flag": (0, 1),

    # 🍎 NUTRITION
    "fruit_intake": (0, 3),
    "vegetable_intake": (0, 3),
    "plant_food": (0, 10),

    # 🚬 RISKS
    "smoking": (0, 1),
    "alcohol": (0, 1),

    # 🏥 HEALTHCARE
    "insurance": (0, 1),
    "doctor_access": (0, 1),
    "cost_issue": (0, 1),

    # ♿ DISABILITY
    "disability": (0, 5)
}


# ============================================
# 📦 PROFILE DEFINITIONS
# ============================================

EXAMPLE_PROFILES = {


    # ========================================
    # 🟢 HEALTHY PROFILE
    # ========================================

    "healthy": {

        "age": 28,
        "gender": 1,
        "bmi": 22.5,

        "general_health": 1,
        "sleep_hours": 8,
        "mental_health_days": 2,
        "physical_health_days": 1,

        "activity_minutes": 350,
        "sedentary": 0,
        "exercise_flag": 1,

        "fruit_intake": 3,
        "vegetable_intake": 3,
        "plant_food": 8,

        "smoking": 0,
        "alcohol": 0,

        "insurance": 1,
        "doctor_access": 1,
        "cost_issue": 0,

        "disability": 0
    },


    # ========================================
    # 🟡 MODERATE PROFILE
    # ========================================

    "moderate": {

        "age": 44,
        "gender": 1,
        "bmi": 27.5,

        "general_health": 3,
        "sleep_hours": 6,
        "mental_health_days": 6,
        "physical_health_days": 5,

        "activity_minutes": 100,
        "sedentary": 1,
        "exercise_flag": 0,

        "fruit_intake": 1,
        "vegetable_intake": 1,
        "plant_food": 4,

        "smoking": 0,
        "alcohol": 1,

        "insurance": 1,
        "doctor_access": 1,
        "cost_issue": 0,

        "disability": 1
    },


    # ========================================
    # 🔴 HIGH RISK PROFILE
    # ========================================

    "high_risk": {

        "age": 60,
        "gender": 1,
        "bmi": 33.0,

        "general_health": 5,
        "sleep_hours": 4,
        "mental_health_days": 18,
        "physical_health_days": 16,

        "activity_minutes": 20,
        "sedentary": 1,
        "exercise_flag": 0,

        "fruit_intake": 0,
        "vegetable_intake": 0,
        "plant_food": 1,

        "smoking": 1,
        "alcohol": 1,

        "insurance": 0,
        "doctor_access": 0,
        "cost_issue": 1,

        "disability": 3
    },


    # ========================================
    # 🚨 VERY HIGH RISK PROFILE
    # ========================================

    "very_high_risk": {

        "age": 68,
        "gender": 1,
        "bmi": 41.0,

        "general_health": 5,
        "sleep_hours": 3,
        "mental_health_days": 25,
        "physical_health_days": 24,

        "activity_minutes": 5,
        "sedentary": 1,
        "exercise_flag": 0,

        "fruit_intake": 0,
        "vegetable_intake": 0,
        "plant_food": 0,

        "smoking": 1,
        "alcohol": 1,

        "insurance": 0,
        "doctor_access": 0,
        "cost_issue": 1,

        "disability": 5
    },


    # ========================================
    # 🧠 BURNOUT & STRESS PROFILE
    # ========================================

    "burnout_stress": {

        "age": 34,
        "gender": 1,
        "bmi": 24.5,

        "general_health": 3,
        "sleep_hours": 4,
        "mental_health_days": 22,
        "physical_health_days": 8,

        "activity_minutes": 40,
        "sedentary": 1,
        "exercise_flag": 0,

        "fruit_intake": 1,
        "vegetable_intake": 1,
        "plant_food": 3,

        "smoking": 0,
        "alcohol": 1,

        "insurance": 1,
        "doctor_access": 1,
        "cost_issue": 0,

        "disability": 0
    },


    # ========================================
    # ⚠️ MIXED RISK PROFILE
    # ========================================

    "mixed_risk": {

        "age": 39,
        "gender": 0,
        "bmi": 26.0,

        "general_health": 3,
        "sleep_hours": 5,
        "mental_health_days": 14,
        "physical_health_days": 7,

        "activity_minutes": 180,
        "sedentary": 0,
        "exercise_flag": 1,

        "fruit_intake": 2,
        "vegetable_intake": 1,
        "plant_food": 5,

        "smoking": 0,
        "alcohol": 1,

        "insurance": 1,
        "doctor_access": 1,
        "cost_issue": 0,

        "disability": 1
    }
}


# ============================================
# 🚀 APPLY PROFILE
# ============================================

def apply_profile(
    profile_name
):

    profile = EXAMPLE_PROFILES[
        profile_name
    ]

    for key, value in profile.items():

        if key in LIMITS:

            min_v, max_v = LIMITS[key]

            value = clamp(

                value,

                min_v,

                max_v
            )

        st.session_state[key] = value


# ============================================
# 🎨 PROFILE CARD
# ============================================

def profile_card(

    emoji,

    title,

    bullets,

    expected,

    button_text,

    profile_key
):

    bullet_html = "".join(

        [
            f"<li>{bullet}</li>"
            for bullet in bullets
        ]
    )

    st.markdown(

        f"""

<div class="example-card">

<h3>{emoji} {title}</h3>

<ul>
{bullet_html}
</ul>

<p>
<b>Expected Result:</b><br>
{expected}
</p>

</div>

""",

        unsafe_allow_html=True
    )

    if st.button(

        button_text,

        key=profile_key,

        use_container_width=True
    ):

        apply_profile(
            profile_key
        )

        st.rerun()


# ============================================
# 🚀 RENDER EXAMPLE PROFILES
# ============================================

def render_example_profiles():

    st.subheader(
        "📘 Example Health Profiles"
    )

    st.caption("""
Quickly test different realistic AI-generated health scenarios.
""")


    # ========================================
    # 🟢 FIRST ROW
    # ========================================

    col1, col2, col3 = st.columns(3)

    with col1:

        profile_card(

            "🟢",

            "Healthy Active Adult",

            [
                "Regular exercise",
                "Balanced nutrition",
                "Healthy BMI",
                "Good sleep quality"
            ],

            "Low wellness risk",

            "Load Healthy",

            "healthy"
        )

    with col2:

        profile_card(

            "🟡",

            "Moderate Lifestyle Risk",

            [
                "Average sleep quality",
                "Moderate BMI",
                "Low physical activity",
                "Occasional unhealthy habits"
            ],

            "Moderate wellness risk",

            "Load Moderate",

            "moderate"
        )

    with col3:

        profile_card(

            "🔴",

            "High Risk Lifestyle",

            [
                "Smoking habit",
                "Poor diet quality",
                "Very low activity",
                "Poor sleep cycle"
            ],

            "High overall risk",

            "Load High Risk",

            "high_risk"
        )


    # ========================================
    # 🚨 SECOND ROW
    # ========================================

    col4, col5, col6 = st.columns(3)

    with col4:

        profile_card(

            "🚨",

            "Very High Risk",

            [
                "Extreme obesity",
                "Very poor sleep",
                "Smoking & inactivity",
                "Multiple severe risk indicators"
            ],

            "Very high wellness risk",

            "Load Very High Risk",

            "very_high_risk"
        )

    with col5:

        profile_card(

            "🧠",

            "Burnout & Stress",

            [
                "Poor sleep routine",
                "High mental stress",
                "Sedentary work lifestyle",
                "Low recovery & activity"
            ],

            "Elevated wellness decline risk",

            "Load Burnout Profile",

            "burnout_stress"
        )

    with col6:

        profile_card(

            "⚠️",

            "Mixed Risk Profile",

            [
                "Mixed lifestyle indicators",
                "Moderate BMI",
                "Mental wellness concerns",
                "Partially healthy habits"
            ],

            "Mixed moderate-to-high risk",

            "Load Mixed Risk",

            "mixed_risk"
        )