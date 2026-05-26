# ============================================
# 📊 PREMIUM HEALTH ASSESSMENT FORM
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
        max(value, min_value),
        max_value
    )


# ============================================
# 📏 MODEL LIMITS
# ============================================

LIMITS = {

    "age": (18, 100),
    "gender": (0, 1),
    "bmi": (10.0, 60.0),

    "general_health": (1, 5),
    "sleep_hours": (0, 24),
    "mental_health_days": (0, 30),
    "physical_health_days": (0, 30),

    "activity_minutes": (0, 3000),
    "sedentary": (0, 1),
    "exercise_flag": (0, 1),

    "fruit_intake": (0, 3),
    "vegetable_intake": (0, 3),
    "plant_food": (0, 10),

    "smoking": (0, 1),
    "alcohol": (0, 1),

    "insurance": (0, 1),
    "doctor_access": (0, 1),
    "cost_issue": (0, 1),

    "disability": (0, 5)
}


# ============================================
# 🧠 DEFAULT VALUES
# ============================================

DEFAULT_VALUES = {

    "age": 28,
    "gender": 1,
    "bmi": 23.5,

    "general_health": 2,
    "sleep_hours": 7,
    "mental_health_days": 2,
    "physical_health_days": 2,

    "activity_minutes": 180,
    "sedentary": 0,
    "exercise_flag": 1,

    "fruit_intake": 2,
    "vegetable_intake": 2,
    "plant_food": 6,

    "smoking": 0,
    "alcohol": 0,

    "insurance": 1,
    "doctor_access": 1,
    "cost_issue": 0,

    "disability": 0
}


# ============================================
# 💾 INITIALIZE SESSION STATE
# ============================================

def initialize_session_state():

    for key, value in DEFAULT_VALUES.items():

        if key not in st.session_state:

            st.session_state[key] = value


# ============================================
# 🛡 CALIBRATION
# ============================================

def calibrate_session_state():

    for key, limits in LIMITS.items():

        if key in st.session_state:

            min_v, max_v = limits

            st.session_state[key] = clamp(

                st.session_state[key],

                min_v,

                max_v
            )


# ============================================
# 🎨 PREMIUM SECTION HEADER
# ============================================

def section_header(
    emoji,
    title,
    description
):

    st.markdown(f"""

<div class="glass-card">

<h2 style="
margin-bottom:0.5rem;
">
{emoji} {title}
</h2>

<p style="
opacity:0.88;
line-height:1.8;
margin-bottom:0;
">

{description}

</p>

</div>

""", unsafe_allow_html=True)


# ============================================
# 🚀 BOOLEAN SELECTBOX
# ============================================

def boolean_selectbox(
    label,
    session_key,
    help_text=""
):

    selected = st.selectbox(

        label,

        options=[
            "No",
            "Yes"
        ],

        index=int(
            st.session_state[
                session_key
            ]
        ),

        help=help_text
    )

    return (
        1 if selected == "Yes"
        else 0
    )


# ============================================
# 🚀 MAIN FORM
# ============================================

def render_assessment_form():

    initialize_session_state()

    calibrate_session_state()

    st.markdown("---")


    # ========================================
    # 🌿 HERO SECTION
    # ========================================

    st.markdown("""

<div class="glass-card">

<h1>
🩺 AI Health Assessment
</h1>

<p style="
line-height:1.9;
opacity:0.92;
font-size:1rem;
">

Complete the wellness assessment below to generate your personalized AI-powered preventive healthcare analysis using hybrid Machine Learning, Deep Learning, behavioral analytics, and AI-generated interpretation systems.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 📝 FORM START
    # ========================================

    with st.form("premium_health_form"):


        # ====================================
        # 👤 BASIC PROFILE
        # ====================================

        section_header(

            "👤",

            "Basic Profile",

            "Core demographic and body composition information used for foundational wellness analysis."
        )


        col1, col2, col3 = st.columns(3)

        with col1:

            age = st.slider(

                "Age",

                18,
                100,

                int(st.session_state.age)
            )


        with col2:

            gender_text = st.selectbox(

                "Gender",

                [
                    "Female",
                    "Male"
                ],

                index=int(
                    st.session_state.gender
                )
            )

            gender = (
                1 if gender_text == "Male"
                else 0
            )


        with col3:

            bmi = st.slider(

                "Body Mass Index (BMI)",

                10.0,
                60.0,

                float(st.session_state.bmi),

                step=0.1
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🩺 GENERAL WELLNESS
        # ====================================

        section_header(

            "🩺",

            "General Wellness",

            "Overall wellness perception, recovery quality, and daily health patterns."
        )


        col1, col2 = st.columns(2)

        with col1:

            general_health = st.slider(

                "General Health Rating",

                1,
                5,

                int(
                    st.session_state.general_health
                )
            )


        with col2:

            sleep_hours = st.slider(

                "Average Sleep Hours",

                0,
                24,

                int(
                    st.session_state.sleep_hours
                )
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🧠 MENTAL WELLNESS
        # ====================================

        section_header(

            "🧠",

            "Mental & Physical Wellness",

            "Stress recovery, emotional wellness, fatigue, and physical discomfort indicators."
        )


        col1, col2 = st.columns(2)

        with col1:

            mental_health_days = st.slider(

                "Poor Mental Health Days",

                0,
                30,

                int(
                    st.session_state.mental_health_days
                )
            )


        with col2:

            physical_health_days = st.slider(

                "Poor Physical Health Days",

                0,
                30,

                int(
                    st.session_state.physical_health_days
                )
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🏃 ACTIVITY
        # ====================================

        section_header(

            "🏃",

            "Lifestyle & Physical Activity",

            "Movement habits, activity consistency, exercise behavior, and sedentary lifestyle analysis."
        )


        col1, col2, col3 = st.columns(3)

        with col1:

            activity_minutes = st.slider(

                "Weekly Physical Activity",

                0,
                3000,

                int(
                    st.session_state.activity_minutes
                )
            )


        with col2:

            sedentary = boolean_selectbox(

                "Sedentary Lifestyle",

                "sedentary"
            )


        with col3:

            exercise_flag = boolean_selectbox(

                "Regular Exercise Habit",

                "exercise_flag"
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🍎 NUTRITION
        # ====================================

        section_header(

            "🍎",

            "Nutrition & Dietary Habits",

            "Daily nutrition quality, plant-based diversity, and healthy eating patterns."
        )


        col1, col2, col3 = st.columns(3)

        with col1:

            fruit_intake = st.slider(

                "Fruit Intake Score",

                0,
                3,

                int(
                    st.session_state.fruit_intake
                )
            )


        with col2:

            vegetable_intake = st.slider(

                "Vegetable Intake Score",

                0,
                3,

                int(
                    st.session_state.vegetable_intake
                )
            )


        with col3:

            plant_food = st.slider(

                "Plant Food Diversity",

                0,
                10,

                int(
                    st.session_state.plant_food
                )
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🚬 RISK FACTORS
        # ====================================

        section_header(

            "🚬",

            "Lifestyle Risk Factors",

            "Behavioral patterns associated with long-term wellness decline and chronic health risk."
        )


        col1, col2 = st.columns(2)

        with col1:

            smoking = boolean_selectbox(

                "Smoking Habit",

                "smoking"
            )


        with col2:

            alcohol = boolean_selectbox(

                "Alcohol Consumption",

                "alcohol"
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🏥 HEALTHCARE ACCESS
        # ====================================

        section_header(

            "🏥",

            "Healthcare Accessibility",

            "Availability of healthcare support, affordability, and medical accessibility."
        )


        col1, col2, col3 = st.columns(3)

        with col1:

            insurance = boolean_selectbox(

                "Health Insurance",

                "insurance"
            )


        with col2:

            doctor_access = boolean_selectbox(

                "Personal Doctor Access",

                "doctor_access"
            )


        with col3:

            cost_issue = boolean_selectbox(

                "Medical Cost Barrier",

                "cost_issue"
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # ♿ DISABILITY
        # ====================================

        section_header(

            "♿",

            "Mobility & Disability",

            "Functional limitations and mobility-related wellness indicators."
        )


        disability = st.slider(

            "Disability Limitation Score",

            0,
            5,

            int(
                st.session_state.disability
            )
        )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 🚀 SUBMIT HERO
        # ====================================

        st.markdown("""

<div class="glass-card">

<h2>
🚀 Generate AI Wellness Assessment
</h2>

<p style="
line-height:1.9;
opacity:0.9;
">

The AI system will now analyze your wellness profile using hybrid predictive intelligence models and generate personalized healthcare analytics, wellness insights, and preventive recommendations.

</p>

</div>

""", unsafe_allow_html=True)


        submitted = st.form_submit_button(

            "🧠 Generate Personalized AI Assessment",

            use_container_width=True
        )


    # ========================================
    # 💾 UPDATE SESSION
    # ========================================

    updated_values = {

        "age": age,
        "gender": gender,
        "bmi": bmi,

        "general_health": general_health,
        "sleep_hours": sleep_hours,
        "mental_health_days": mental_health_days,
        "physical_health_days": physical_health_days,

        "activity_minutes": activity_minutes,
        "sedentary": sedentary,
        "exercise_flag": exercise_flag,

        "fruit_intake": fruit_intake,
        "vegetable_intake": vegetable_intake,
        "plant_food": plant_food,

        "smoking": smoking,
        "alcohol": alcohol,

        "insurance": insurance,
        "doctor_access": doctor_access,
        "cost_issue": cost_issue,

        "disability": disability
    }


    # ========================================
    # 🛡 CALIBRATION
    # ========================================

    for key, value in updated_values.items():

        min_v, max_v = LIMITS[key]

        st.session_state[key] = clamp(

            value,

            min_v,

            max_v
        )


    # ========================================
    # 📦 PAYLOAD
    # ========================================

    payload = {

        "age": int(st.session_state.age),
        "gender": int(st.session_state.gender),
        "bmi": float(st.session_state.bmi),

        "general_health": int(st.session_state.general_health),
        "sleep_hours": int(st.session_state.sleep_hours),
        "mental_health_days": int(st.session_state.mental_health_days),
        "physical_health_days": int(st.session_state.physical_health_days),

        "activity_minutes": int(st.session_state.activity_minutes),
        "sedentary": int(st.session_state.sedentary),
        "exercise_flag": int(st.session_state.exercise_flag),

        "fruit_intake": int(st.session_state.fruit_intake),
        "vegetable_intake": int(st.session_state.vegetable_intake),
        "plant_food": int(st.session_state.plant_food),

        "smoking": int(st.session_state.smoking),
        "alcohol": int(st.session_state.alcohol),

        "insurance": int(st.session_state.insurance),
        "doctor_access": int(st.session_state.doctor_access),
        "cost_issue": int(st.session_state.cost_issue),

        "disability": int(st.session_state.disability)
    }


    # ========================================
    # ✅ RETURN
    # ========================================

    return submitted, payload