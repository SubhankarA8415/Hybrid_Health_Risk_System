# ============================================
# 📊 PREMIUM AI RISK DASHBOARD
# ============================================

import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# ============================================
# 🎨 RISK BADGE
# ============================================

def risk_badge(risk_level):

    risk_level = risk_level.lower()

    if "low" in risk_level:

        return "🟢 LOW RISK"

    elif "moderate" in risk_level:

        return "🟡 MODERATE RISK"

    elif "high" in risk_level:

        return "🔴 HIGH RISK"

    elif "very high" in risk_level:

        return "🚨 VERY HIGH RISK"

    return f"⚠ {risk_level.upper()}"


# ============================================
# 🎨 RISK COLOR
# ============================================

def get_risk_color(probability):

    if probability < 20:
        return "#10B981"

    elif probability < 50:
        return "#F59E0B"

    elif probability < 75:
        return "#EF4444"

    return "#DC2626"


# ============================================
# 📊 MODERN RISK CARD
# ============================================

def render_risk_card(

    emoji,
    title,
    data
):

    probability = data["probability"]

    color = get_risk_color(
        probability
    )


    st.markdown(f"""

<div class="glass-card">

<h3 style="
margin-bottom:0.4rem;
">
{emoji} {title}
</h3>

<p style="
opacity:0.75;
margin-top:0;
margin-bottom:1rem;
">
AI-powered probabilistic analysis
</p>

<h1 style="
font-size:2.5rem;
margin-bottom:0.5rem;
color:{color};
">
{data["display_probability"]}
</h1>

<p style="
font-weight:600;
font-size:1rem;
">
{risk_badge(data["risk_level"])}
</p>

<hr style="
border:0.5px solid rgba(255,255,255,0.08);
margin-top:1rem;
margin-bottom:1rem;
">

<p style="
line-height:1.8;
opacity:0.88;
">

<b>Confidence:</b>
{data["confidence"]}

<br>

<b>Uncertainty:</b>
{data["uncertainty_range"]}

</p>

</div>

""", unsafe_allow_html=True)


# ============================================
# 📈 MODERN BAR CHART
# ============================================

def render_risk_chart(chart_df):

    fig = px.bar(

        chart_df,

        x="Risk Probability",

        y="Condition",

        orientation="h",

        text="Risk Probability",

        color="Risk Probability",

        color_continuous_scale=[
            "#10B981",
            "#F59E0B",
            "#EF4444"
        ]
    )


    fig.update_traces(

        texttemplate='%{text:.1f}%',

        textposition='outside',

        marker_line_width=0
    )


    fig.update_layout(

        height=420,

        paper_bgcolor="rgba(0,0,0,0)",

        plot_bgcolor="rgba(0,0,0,0)",

        font=dict(
            color="white",
            size=14
        ),

        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        ),

        xaxis=dict(

            title="Risk Probability (%)",

            showgrid=True,

            gridcolor="rgba(255,255,255,0.08)",

            zeroline=False
        ),

        yaxis=dict(

            title="",

            showgrid=False
        ),

        coloraxis_showscale=False
    )


    st.plotly_chart(

        fig,

        use_container_width=True
    )


# ============================================
# 🌿 GAUGE CHART
# ============================================

def render_gauge_chart(avg_risk):

    fig = go.Figure(go.Indicator(

        mode="gauge+number",

        value=avg_risk,

        title={

            "text":
            "Overall Health Risk"
        },

        number={

            "suffix":
            "%"
        },

        gauge={

            "axis": {

                "range":
                [0, 100]
            },

            "bar": {

                "color":
                "#6366F1"
            },

            "steps": [

                {

                    "range":
                    [0, 25],

                    "color":
                    "#10B981"
                },

                {

                    "range":
                    [25, 50],

                    "color":
                    "#F59E0B"
                },

                {

                    "range":
                    [50, 75],

                    "color":
                    "#EF4444"
                },

                {

                    "range":
                    [75, 100],

                    "color":
                    "#991B1B"
                }
            ]
        }
    ))


    fig.update_layout(

        height=320,

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
# 🚀 MAIN DASHBOARD
# ============================================

def render_risk_dashboard(
    predictions
):

    st.markdown("---")

    st.header(
        "📊 AI Risk Assessment Dashboard"
    )

    st.caption("""
Advanced AI-powered healthcare analytics generated using hybrid Machine Learning and Deep Learning models.
""")


    # ========================================
    # 📦 EXTRACT DATA
    # ========================================

    diabetes = predictions["diabetes"]

    heart = predictions["heart_disease"]

    obesity = predictions["obesity"]


    risks = {

        "Diabetes":
        diabetes["probability"],

        "Heart Disease":
        heart["probability"],

        "Obesity":
        obesity["probability"]
    }


    top_risk = max(
        risks,
        key=risks.get
    )

    lowest_risk = min(
        risks,
        key=risks.get
    )

    avg_risk = round(

        sum(
            risks.values()
        ) / len(risks),

        1
    )


    # ========================================
    # 🧠 AI SUMMARY
    # ========================================

    st.markdown("""

<div class="glass-card">

<h2>
🧠 AI Health Intelligence Summary
</h2>

<p style="
line-height:1.9;
opacity:0.9;
font-size:1rem;
">

Your health profile has been analyzed using a hybrid AI system combining Machine Learning, Deep Learning, and wellness analytics to estimate possible lifestyle-related health risks and patterns.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 📊 METRICS
    # ========================================

    metric_col1, metric_col2, metric_col3 = st.columns(3)

    with metric_col1:

        st.metric(
            "🚨 Highest Risk",
            top_risk
        )

    with metric_col2:

        st.metric(
            "🌿 Average Risk",
            f"{avg_risk}%"
        )

    with metric_col3:

        st.metric(
            "🛡 Lowest Risk",
            lowest_risk
        )


    st.markdown("<br>", unsafe_allow_html=True)


    # ========================================
    # 📊 RISK CARDS
    # ========================================

    col1, col2, col3 = st.columns(3)

    with col1:

        render_risk_card(
            "🩸",
            "Diabetes",
            diabetes
        )

    with col2:

        render_risk_card(
            "❤️",
            "Heart Disease",
            heart
        )

    with col3:

        render_risk_card(
            "⚖️",
            "Obesity",
            obesity
        )


    # ========================================
    # 📈 ANALYTICS SECTION
    # ========================================

    st.markdown("---")

    st.subheader(
        "📈 Risk Analytics Visualization"
    )


    analytics_col1, analytics_col2 = st.columns([1.2, 1])


    chart_df = pd.DataFrame({

        "Condition": [

            "Diabetes",

            "Heart Disease",

            "Obesity"
        ],

        "Risk Probability": [

            diabetes["probability"],

            heart["probability"],

            obesity["probability"]
        ]
    })


    with analytics_col1:

        render_risk_chart(
            chart_df
        )

    with analytics_col2:

        render_gauge_chart(
            avg_risk
        )


    # ========================================
    # 🧠 AI INSIGHTS
    # ========================================

    st.markdown("---")

    st.subheader(
        "🧠 AI Risk Insights"
    )


    insight_col1, insight_col2 = st.columns(2)


    with insight_col1:

        st.markdown(f"""

<div class="glass-card">

<h3>
🚨 Highest Predicted Risk
</h3>

<h2 style="
color:#EF4444;
">
{top_risk}
</h2>

<p style="
line-height:1.8;
opacity:0.88;
">

This condition currently demonstrates the strongest predicted probability based on the provided health and lifestyle indicators.

</p>

</div>

""", unsafe_allow_html=True)


    with insight_col2:

        st.markdown(f"""

<div class="glass-card">

<h3>
🛡 Lowest Predicted Risk
</h3>

<h2 style="
color:#10B981;
">
{lowest_risk}
</h2>

<p style="
line-height:1.8;
opacity:0.88;
">

This area currently appears comparatively stable based on the analyzed wellness profile and behavioral indicators.

</p>

</div>

""", unsafe_allow_html=True)


    # ========================================
    # 🌿 WELLNESS RECOMMENDATION
    # ========================================

    st.markdown("---")


    if avg_risk < 20:

        recommendation = """

✅ Your current wellness profile appears relatively stable.

Continue maintaining:
- balanced nutrition
- regular activity
- healthy sleep
- preventive wellness habits
"""

    elif avg_risk < 50:

        recommendation = """

⚠ Moderate health risks detected.

Recommended improvements:
- consistent exercise
- stress management
- nutritional improvements
- sleep optimization
"""

    else:

        recommendation = """

🚨 Elevated health risk patterns detected.

Strongly recommended:
- lifestyle intervention
- medical consultation
- improved diet
- regular health monitoring
"""


    st.markdown(f"""

<div class="glass-card">

<h2>
🌿 Personalized Wellness Recommendation
</h2>

<p style="
line-height:1.9;
white-space:pre-line;
opacity:0.92;
">

{recommendation}

</p>

</div>

""", unsafe_allow_html=True)