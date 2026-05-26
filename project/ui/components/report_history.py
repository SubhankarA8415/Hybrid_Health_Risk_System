# ============================================
# 📜 MODERN REPORT HISTORY COMPONENT
# ============================================

import json

from datetime import datetime

import streamlit as st


# ============================================
# 🌐 API CLIENT
# ============================================

from project.ui.services.api_client import (

    get_reports,

    delete_report,

    download_report_pdf
)


# ============================================
# 🎨 WELLNESS STATUS
# ============================================

def get_wellness_status(
    score
):

    if score >= 80:

        return "🟢 Excellent Wellness"

    elif score >= 60:

        return "🟡 Moderate Wellness"

    elif score >= 40:

        return "🟠 Elevated Risk"

    else:

        return "🔴 High Wellness Concern"


# ============================================
# 🚀 MAIN REPORT HISTORY
# ============================================

def render_report_history():

    # ========================================
    # 🚨 LOGIN CHECK
    # ========================================

    if not st.session_state.user:

        return


    user_email = (
        st.session_state.user["email"]
    )


    st.markdown("---")

    st.header(
        "📜 Saved AI Health Reports"
    )

    st.caption("""
Review your historical AI-generated wellness assessments,
risk analytics, and personalized health guidance.
""")


    # ========================================
    # 📥 FETCH REPORTS
    # ========================================

    try:

        response = get_reports(
            user_email
        )


        # ====================================
        # ❌ CONNECTION FAILURE
        # ====================================

        if response is None:

            st.error(
                "Unable to connect to the backend server."
            )

            return


        # ====================================
        # ❌ API FAILURE
        # ====================================

        if response.status_code != 200:

            st.error(
                "Unable to load saved reports."
            )

            return


        reports = response.json()


        # ====================================
        # 📭 EMPTY STATE
        # ====================================

        if len(reports) == 0:

            st.markdown("""

<div class="glass-card">

<h3>
📭 No Saved Reports Yet
</h3>

<p style="
line-height: 1.8;
opacity: 0.9;
">

Generate your first AI-powered health assessment
to begin building your personalized wellness history.

</p>

</div>

""", unsafe_allow_html=True)

            return


        # ====================================
        # 📊 REPORT ANALYTICS
        # ====================================

        avg_score = round(

            sum(
                r["wellness_score"]
                for r in reports
            ) / len(reports),

            1
        )


        highest_score = max(

            r["wellness_score"]
            for r in reports
        )


        # ====================================
        # 📊 DASHBOARD METRICS
        # ====================================

        metric_col1, metric_col2, metric_col3 = st.columns(3)

        with metric_col1:

            st.metric(

                "📄 Total Reports",

                len(reports)
            )

        with metric_col2:

            st.metric(

                "🌿 Avg Wellness",

                f"{avg_score}/100"
            )

        with metric_col3:

            st.metric(

                "🏆 Best Wellness",

                f"{highest_score}/100"
            )


        st.markdown("<br>", unsafe_allow_html=True)


        # ====================================
        # 📦 REPORT CARDS
        # ====================================

        for report in reports:

            # ================================
            # 🕒 FORMAT TIMESTAMP
            # ================================

            formatted_time = report.get(
                "created_at",
                "Unknown Time"
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


            # ================================
            # 🌿 WELLNESS SCORE
            # ================================

            wellness_score = report.get(

                "wellness_score",

                0
            )


            wellness_status = (
                get_wellness_status(
                    wellness_score
                )
            )


            # ================================
            # 📜 REPORT EXPANDER
            # ================================

            with st.expander(

                f"🕒 {formatted_time}"

            ):

                # ============================
                # 🌿 REPORT HEADER
                # ============================

                st.markdown(f"""

<div class="glass-card">

<h3>
🌿 Wellness Score: {wellness_score}/100
</h3>

<p style="
opacity: 0.92;
line-height: 1.7;
">

{wellness_status}

</p>

</div>

""", unsafe_allow_html=True)


                # ============================
                # 📊 PREDICTION RESULTS
                # ============================

                st.subheader(
                    "📊 AI Risk Predictions"
                )

                try:

                    predictions = report.get(
                        "prediction_results",
                        {}
                    )

                    if isinstance(
                        predictions,
                        str
                    ):

                        predictions = json.loads(
                            predictions
                        )

                    risk_col1, risk_col2, risk_col3 = st.columns(3)


                    with risk_col1:

                        diabetes = predictions.get(
                            "diabetes",
                            {}
                        )

                        st.metric(

                            "🩸 Diabetes",

                            diabetes.get(
                                "display_probability",
                                "N/A"
                            )
                        )


                    with risk_col2:

                        heart = predictions.get(
                            "heart_disease",
                            {}
                        )

                        st.metric(

                            "❤️ Heart Disease",

                            heart.get(
                                "display_probability",
                                "N/A"
                            )
                        )


                    with risk_col3:

                        obesity = predictions.get(
                            "obesity",
                            {}
                        )

                        st.metric(

                            "⚖️ Obesity",

                            obesity.get(
                                "display_probability",
                                "N/A"
                            )
                        )


                    st.markdown("<br>", unsafe_allow_html=True)

                    st.json(
                        predictions
                    )

                except Exception:

                    st.warning(
                        "Unable to parse prediction results."
                    )


                # ============================
                # 🧠 AI INTERPRETATION
                # ============================

                st.subheader(
                    "🧠 AI Wellness Guidance"
                )

                interpretation = report.get(
                    "interpretation",
                    ""
                )


                if interpretation:

                    st.markdown(f"""

<div class="glass-card">

<div style="
line-height: 1.9;
opacity: 0.96;
">

{interpretation}

</div>

</div>

""", unsafe_allow_html=True)

                else:

                    st.info(
                        "No AI interpretation available."
                    )


                # ============================
                # ⚙ REPORT ACTIONS
                # ============================

                st.markdown("---")

                action_col1, action_col2 = st.columns(2)

                # ============================
                # 📄 DOWNLOAD PDF
                # ============================

                with action_col1:

                    try:

                        pdf_response = (
                            download_report_pdf(

                                report["id"],

                                user_email
                            )
                        )


                        if (

                            pdf_response

                            and pdf_response.status_code == 200
                        ):

                            # ========================================
                            # 📄 PROFESSIONAL FILE NAME
                            # ========================================

                            safe_timestamp = (
                                formatted_time
                                .replace(" • ", "_")
                                .replace(":", "_")
                                .replace(" ", "_")
                            )

                            pdf_filename = (
                                f"AI_Wellness_Report_{safe_timestamp}.pdf"
                            )


                            # ========================================
                            # 📥 DOWNLOAD BUTTON
                            # ========================================

                            st.download_button(

                                label="📄 Download PDF",

                                data=pdf_response.content,

                                file_name=pdf_filename,

                                mime="application/pdf",

                                use_container_width=True,

                                key=f"pdf_{report['id']}"
                            )

                        else:

                            st.warning(
                                "PDF unavailable"
                            )

                    except Exception:

                        st.warning(
                            "PDF export unavailable"
                        )


                # ============================
                # 🗑 DELETE REPORT
                # ============================

                with action_col2:

                    if st.button(

                        "🗑 Delete Report",

                        key=f"delete_{report['id']}",

                        use_container_width=True
                    ):

                        try:

                            delete_response = delete_report(

                                report["id"],

                                user_email
                            )


                            if (

                                delete_response

                                and delete_response.status_code == 200
                            ):

                                st.success(
                                    "Report deleted successfully."
                                )

                                st.rerun()

                            else:

                                st.error(
                                    "Unable to delete report."
                                )

                        except Exception as e:

                            st.error(
                                f"Delete Error: {str(e)}"
                            )


    # ========================================
    # ❌ GLOBAL EXCEPTION
    # ========================================

    except Exception as e:

        st.error(
            f"History Error: {str(e)}"
        )