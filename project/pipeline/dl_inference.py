# ============================================
# 🧠 DL INFERENCE ENGINE
# ============================================

import numpy as np


class DLInferenceEngine:

    def __init__(self, loader):

        self.loader = loader

        self.model = loader.dl_model


    # ============================================
    # 🚀 RUN DL PREDICTION
    # ============================================

    def predict(
        self,
        dl_inputs
    ):

        """
        Multi-input DL prediction
        """

        predictions = self.model.predict(
            dl_inputs,
            verbose=0
        )


        # ========================================
        # 🩺 EXTRACT OUTPUTS
        # ========================================

        diabetes_prob = float(
            predictions[0][0][0]
        )

        heart_prob = float(
            predictions[1][0][0]
        )

        obesity_prob = float(
            predictions[2][0][0]
        )


        # ========================================
        # 🚨 APPLY THRESHOLDS
        # ========================================

        diabetes_pred = int(

            diabetes_prob >=
            self.loader.model_thresholds[
                "diabetes"
            ]
        )

        heart_pred = int(

            heart_prob >=
            self.loader.model_thresholds[
                "heart_disease"
            ]
        )

        obesity_pred = int(

            obesity_prob >=
            self.loader.model_thresholds[
                "obesity"
            ]
        )


        # ========================================
        # 📊 RETURN RESULTS
        # ========================================

        return {

            "diabetes": {

                "probability": diabetes_prob,

                "prediction": diabetes_pred
            },

            "heart_disease": {

                "probability": heart_prob,

                "prediction": heart_pred
            },

            "obesity": {

                "probability": obesity_prob,

                "prediction": obesity_pred
            }
        }