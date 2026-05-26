# ============================================
# 🧠 HEALTH PREDICTION ROUTES
# ============================================

from fastapi import APIRouter
from fastapi import HTTPException

from project.api.schemas import (

    HealthInputSchema,

    PredictionResponseSchema
)

from project.api.services.prediction_service import (
    run_health_prediction
)


# ============================================
# 🚀 ROUTER
# ============================================

router = APIRouter()


# ============================================
# 🔥 HEALTH PREDICTION API
# ============================================

@router.post(

    "/predict",

    response_model=PredictionResponseSchema
)

async def predict_health(

    user_input: HealthInputSchema
):

    try:

        result = run_health_prediction(
            user_input
        )

        return {

            "predictions":
            result["predictions"],

            "interpretation":
            result["interpretation"]
        }


    except Exception as e:

        print(
            "❌ PREDICTION ERROR:",
            str(e)
        )

        raise HTTPException(

            status_code=500,

            detail=f"Prediction Error: {str(e)}"
        )