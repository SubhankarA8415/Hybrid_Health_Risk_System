# ============================================
# 🧠 PREDICTION SERVICE
# ============================================

from project.api.dependencies import (

    predictor,

    interpreter
)

from project.api.services.wellness_service import (

    calculate_wellness_score
)

from project.database.crud import (

    get_user_by_email,

    save_health_report
)


# ============================================
# 🚀 RUN HEALTH PREDICTION
# ============================================

def run_health_prediction(
    user_input
):

    # ========================================
    # 📦 INPUT DATA
    # ========================================

    input_data = user_input.dict()


    # ========================================
    # 🚀 RUN PREDICTION PIPELINE
    # ========================================

    results = predictor.predict(
        input_data
    )


    # ========================================
    # 📊 FINAL PREDICTIONS
    # ========================================

    predictions = results.get(
        "final_results",
        {}
    )


    # ========================================
    # 🌿 WELLNESS SCORE
    # ========================================

    wellness_score = (
        calculate_wellness_score(
            user_input
        )
    )


    # ========================================
    # 🧠 AI INTERPRETATION
    # ========================================

    interpretation = interpreter.interpret(

        input_data,

        predictions
    )


    # ========================================
    # 💾 SAVE REPORT
    # ========================================

    if user_input.user_email:

        db_user = get_user_by_email(

            user_input.user_email
        )


        if db_user:

            try:

                save_health_report(

                    user_id=db_user.id,

                    input_data=input_data,

                    prediction_results=predictions,

                    interpretation=interpretation,

                    wellness_score=wellness_score
                )

                print(
                    "✅ REPORT SAVED"
                )

            except Exception as save_error:

                print(

                    "❌ REPORT SAVE FAILED:",

                    str(save_error)
                )


    # ========================================
    # 📦 FINAL OUTPUT
    # ========================================

    return {

        "predictions":
        predictions,

        "interpretation":
        interpretation,

        "wellness_score":
        wellness_score
    }