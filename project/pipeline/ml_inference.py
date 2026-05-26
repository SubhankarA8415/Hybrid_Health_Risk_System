# ============================================
# 🤖 ML INFERENCE ENGINE
# ============================================

class MLInferenceEngine:

    def __init__(self, loader):

        self.loader = loader


    # ============================================
    # 🩺 DIABETES
    # ============================================

    def predict_diabetes(
        self,
        X
    ):

        model = self.loader.diabetes_model

        prob = model.predict_proba(X)[0][1]

        threshold = self.loader.model_thresholds[
            "diabetes"
        ]

        pred = int(prob >= threshold)

        return {
            "probability": float(prob),
            "prediction": pred
        }


    # ============================================
    # ❤️ HEART DISEASE
    # ============================================

    def predict_heart_disease(
        self,
        X
    ):

        model = self.loader.heart_model

        prob = model.predict_proba(X)[0][1]

        threshold = self.loader.model_thresholds[
            "heart_disease"
        ]

        pred = int(prob >= threshold)

        return {
            "probability": float(prob),
            "prediction": pred
        }


    # ============================================
    # ⚖️ OBESITY
    # ============================================

    def predict_obesity(
        self,
        X
    ):

        model = self.loader.obesity_model

        prob = model.predict_proba(X)[0][1]

        threshold = self.loader.model_thresholds[
            "obesity"
        ]

        pred = int(prob >= threshold)

        return {
            "probability": float(prob),
            "prediction": pred
        }


    # ============================================
    # 🚀 RUN ALL ML PREDICTIONS
    # ============================================

    def predict_all(
        self,
        ml_inputs
    ):

        diabetes_result = self.predict_diabetes(
            ml_inputs["diabetes"]
        )

        heart_result = self.predict_heart_disease(
            ml_inputs["heart_disease"]
        )

        obesity_result = self.predict_obesity(
            ml_inputs["obesity"]
        )

        return {

            "diabetes": diabetes_result,

            "heart_disease": heart_result,

            "obesity": obesity_result
        }