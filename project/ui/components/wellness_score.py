# ============================================
# 🌿 PREMIUM WELLNESS SCORE COMPONENT
# ============================================

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px


# ============================================
# 🚀 CALCULATE WELLNESS SCORE
# ============================================

def calculate_wellness_score(
    payload
):

    score = 100

    breakdown = []


    # ========================================
    # 🚬 SMOKING
    # ========================================

    if payload["smoking"] == 1:

        score -= 20

        breakdown.append(
            ("🚬 Smoking", -20)
        )

    else:

        breakdown.append(
            ("🌿 Non-Smoker", +5)
        )


    # ========================================
    # 🍺 ALCOHOL
    # ========================================

    if payload["alcohol"] == 1:

        score -= 8

        breakdown.append(
            ("🍺 Alcohol Use", -8)
        )

    else:

        breakdown.append(
            ("💧 No Alcohol", +3)
        )


    # ========================================
    # ⚖ BMI
    # ========================================

    bmi = payload["bmi"]

    if bmi >= 35:

        score -= 25

        breakdown.append(
            ("⚖ Severe Obesity", -25)
        )

    elif bmi >= 30:

        score -= 18

        breakdown.append(
            ("⚖ Obesity", -18)
        )

    elif bmi >= 25:

        score -= 10

        breakdown.append(
            ("⚖ Overweight", -10)
        )

    elif bmi >= 18.5:

        breakdown.append(
            ("✅ Healthy BMI", +8)
        )


    # ========================================
    # 😴 SLEEP
    # ========================================

    sleep = payload["sleep_hours"]

    if sleep < 5:

        score -= 15

        breakdown.append(
            ("😴 Poor Sleep", -15)
        )

    elif sleep < 7:

        score -= 7

        breakdown.append(
            ("😴 Insufficient Sleep", -7)
        )

    elif 7 <= sleep <= 9:

        breakdown.append(
            ("🌙 Healthy Sleep", +5)
        )


    # ========================================
    # 🏃 ACTIVITY
    # ========================================

    activity = payload[
        "activity_minutes"
    ]

    if activity < 30:

        score -= 20

        breakdown.append(
            ("🏃 Very Low Activity", -20)
        )

    elif activity < 150:

        score -= 8

        breakdown.append(
            ("🏃 Low Activity", -8)
        )

    else:

        breakdown.append(
            ("💪 Active Lifestyle", +10)
        )


    # ========================================
    # 🍎 NUTRITION
    # ========================================

    fruits = payload[
        "fruit_intake"
    ]

    vegetables = payload[
        "vegetable_intake"
    ]


    if fruits < 2:

        score -= 5

        breakdown.append(
            ("🍎 Low Fruit Intake", -5)
        )

    else:

        breakdown.append(
            ("🍎 Good Fruit Intake", +3)
        )


    if vegetables < 2:

        score -= 5

        breakdown.append(
            ("🥦 Low Vegetable Intake", -5)
        )

    else:

        breakdown.append(
            ("🥦 Good Vegetable Intake", +3)
        )


    # ========================================
    # 🧠 MENTAL HEALTH
    # ========================================

    mental = payload[
        "mental_health_days"
    ]

    if mental > 20:

        score -= 15

        breakdown.append(
            ("🧠 High Mental Stress", -15)
        )

    elif mental > 10:

        score -= 8

        breakdown.append(
            ("🧠 Moderate Mental Stress", -8)
        )


    # ========================================
    # 🩺 PHYSICAL HEALTH
    # ========================================

    physical = payload[
        "physical_health_days"
    ]

    if physical > 20:

        score -= 15

        breakdown.append(
            ("🩺 Frequent Physical Discomfort", -15)
        )

    elif physical > 10:

        score -= 8

        breakdown.append(
            ("🩺 Moderate Physical Discomfort", -8)
        )


    score = max(
        min(score, 100),
        0
    )

    breakdown = sorted(
        breakdown,
        key=lambda x: x[1]
    )

    return score, breakdown


# ============================================
# 🎨 WELLNESS LABEL
# ============================================

def get_wellness_label(score):

    if score >= 85:

        return (
            "🌟",
            "Excellent Wellness"
        )

    elif score >= 70:

        return (
            "🟢",
            "Good Wellness"
        )

    elif score >= 50:

        return (
            "🟡",
            "Moderate Wellness"
        )

    elif score >= 30:

        return (
            "🟠",
            "Needs Improvement"
        )

    else:

        return (
            "🔴",
            "High Health Concern"
        )


# ============================================
# 📊 GAUGE CHART
# ============================================

def render_wellness_gauge(score):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=score,

        number={
            "suffix": "/100"
        },

        title={
            "text": "Wellness Score"
        },

        gauge={

            "axis": {
                "range": [0, 100]
            },

            "bar": {
                "color": "#6366F1"
            },

            "steps": [

                {
                    "range": [0, 30],
                    "color": "#991B1B"
                },

                {
                    "range": [30, 50],
                    "color": "#F59E0B"
                },

                {
                    "range": [50, 70],
                    "color": "#FBBF24"
                },

                {
                    "range": [70, 85],
                    "color": "#10B981"
                },

                {
                    "range": [85, 100],
                    "color": "#059669"
                }
            ]
        }
    ))


    fig.update_layout(

        height=340,

        paper_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white"
        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================
# 📈 WELLNESS BREAKDOWN CHART
# ============================================

def render_breakdown_chart(breakdown):

    df = pd.DataFrame({

        "Factor": [
            x[0] for x in breakdown
        ],

        "Impact": [
            x[1] for x in breakdown
        ]
    })


    fig = px.bar(

        df,

        x="Impact",

        y="Factor",

        orientation="h",

        text="Impact",

        color="Impact",

        color_continuous_scale=[
            "#EF4444",
            "#F59E0B",
            "#10B981"
        ]
    )


    fig.update_traces(

        textposition="outside",

        marker_line_width=0
    )


    fig.update_layout(

        height=550,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white"
        ),

        margin=dict(
            l=20,
            r=20,
            t=20,
            b=20
        ),

        coloraxis_showscale=False,

        xaxis=dict(

            showgrid=True,

            gridcolor="rgba(255,255,255,0.08)"
        ),

        yaxis=dict(
            showgrid=False
        )
    )


    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================
# 🚀 MAIN COMPONENT
# ============================================

def render_wellness_score(
    payload
):

    score, breakdown = (
        calculate_wellness_score(
            payload
        )
    )


    emoji, label = (
        get_wellness_label(
            score
        )
    )


    # ========================================
    # 🌿 HERO SECTION
    # ========================================

    st.markdown(f"""

<div class="wellness-score">

<h1>
{emoji} Wellness Intelligence Score
</h1>

<h3 style="
margin-top:0.5rem;
opacity:0.92;
">
{label}
</h3>

<p style="
line-height:1.9;
margin-top:1rem;
opacity:0.9;
">

Your AI wellness score summarizes how your current lifestyle habits, activity levels, nutrition patterns, sleep quality, and wellness indicators may influence long-term preventive health outcomes.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 📊 ANALYTICS SECTION
    # ========================================

    analytics_col1, analytics_col2 = st.columns([1, 1.3])


    with analytics_col1:

        render_wellness_gauge(
            score
        )

    with analytics_col2:

        st.markdown("""

<div class="glass-card">

<h3>
🧠 Wellness Summary
</h3>

<p style="
line-height:1.9;
opacity:0.9;
">

The AI wellness engine evaluated multiple behavioral and lifestyle indicators to estimate your overall preventive wellness profile.

Higher scores generally indicate stronger wellness habits and healthier long-term lifestyle patterns.

</p>

</div>

""", unsafe_allow_html=True)


        positive_factors = [

            x for x in breakdown
            if x[1] > 0
        ]

        negative_factors = [

            x for x in breakdown
            if x[1] < 0
        ]


        strongest_positive = (

            max(
                positive_factors,
                key=lambda x: x[1]
            )[0]

            if positive_factors
            else "None"
        )


        strongest_negative = (

            min(
                negative_factors,
                key=lambda x: x[1]
            )[0]

            if negative_factors
            else "None"
        )


        metric_col1, metric_col2 = st.columns(2)

        with metric_col1:

            st.metric(
                "✅ Strongest Positive",
                strongest_positive
            )

        with metric_col2:

            st.metric(
                "⚠ Main Concern",
                strongest_negative
            )


    # ========================================
    # 📈 BREAKDOWN ANALYTICS
    # ========================================

    st.markdown("---")

    st.subheader(
        "📈 Wellness Impact Analytics"
    )

    st.caption("""
AI-evaluated contribution of lifestyle and wellness factors.
""")


    render_breakdown_chart(
        breakdown
    )


    # ========================================
    # 🧠 AI WELLNESS INSIGHT
    # ========================================

    st.markdown("---")


    if score >= 80:

        insight = """
Your wellness indicators currently reflect relatively healthy lifestyle patterns. Maintaining consistency in exercise, nutrition, sleep, and preventive wellness habits can further support long-term health stability.
"""

    elif score >= 60:

        insight = """
Your wellness profile appears moderately stable, though several lifestyle areas may still benefit from gradual improvement. Improving activity consistency, nutrition quality, stress management, and recovery habits may help optimize long-term wellness.
"""

    else:

        insight = """
Several wellness indicators currently suggest elevated lifestyle-related health concerns. Improved nutrition, increased physical activity, better sleep consistency, stress reduction, and preventive healthcare attention are strongly recommended.
"""


    st.markdown(f"""

<div class="glass-card">

<h2>
🧠 AI Wellness Insight
</h2>

<p style="
line-height:1.9;
opacity:0.92;
">

{insight}

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # ⚠ DISCLAIMER
    # ========================================

    st.info("""
💡 Wellness scores are AI-generated educational wellness estimates based on lifestyle patterns and should not be interpreted as medical diagnoses or clinical evaluations.
""")