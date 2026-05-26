# ============================================
# 🔥 HYBRID AGGREGATION ENGINE
# ============================================

import numpy as np


# ============================================
# 📊 PROBABILITY FORMATTER
# ============================================

def format_probability(probability):

    """
    Human-friendly probability formatting
    """

    if probability < 1:

        return "<1%"

    elif probability < 10:

        return f"{probability:.1f}%"

    else:

        return f"{probability:.0f}%"


# ============================================
# 🔥 HYBRID AGGREGATOR
# ============================================

class HybridAggregator:

    def __init__(self):

        pass


    # ============================================
    # 📊 CONFIDENCE CALCULATION
    # ============================================

    def calculate_confidence(
        self,
        ml_prob,
        dl_prob
    ):

        difference = abs(
            ml_prob - dl_prob
        )


        if difference < 0.10:

            return "High Confidence"

        elif difference < 0.20:

            return "Moderate Confidence"

        else:

            return "Low Confidence"


    # ============================================
    # 🚨 RISK LEVEL
    # ============================================

    # ============================================
    # 🚨 FINAL RISK LEVELS
    # ============================================

    def get_risk_level(
        self,
        probability
    ):

        percentage = probability * 100


        # ========================================
        # 🟢 LOW
        # ========================================

        if percentage < 15:

            return "Low"


        # ========================================
        # 🟡 MODERATE
        # ========================================

        elif percentage < 40:

            return "Moderate"


        # ========================================
        # 🟠 HIGH
        # ========================================

        elif percentage < 70:

            return "High"


        # ========================================
        # 🔴 VERY HIGH
        # ========================================

        else:

            return "Very High"


    # ============================================
    # 📈 UNCERTAINTY RANGE
    # ============================================

    def calculate_uncertainty_range(
        self,
        ml_prob,
        dl_prob
    ):

        low = min(
            ml_prob,
            dl_prob
        )

        high = max(
            ml_prob,
            dl_prob
        )

        return (

            round(low * 100, 2),

            round(high * 100, 2)
        )


    # ============================================
    # 🔥 AGGREGATE SINGLE DISEASE
    # ============================================

    def aggregate_disease(
        self,
        disease_name,
        ml_result,
        dl_result
    ):

        # ========================================
        # 📊 RAW PROBABILITIES
        # ========================================

        ml_prob = ml_result[
            "probability"
        ]

        dl_prob = dl_result[
            "probability"
        ]


        # ========================================
        # ⚖️ WEIGHTED FUSION
        # ========================================

        final_prob = (

            0.5 * ml_prob +

            0.5 * dl_prob
        )


        # ========================================
        # ⚖️ OBESITY CALIBRATION
        # ========================================

        if disease_name == "obesity":

            # soften aggressive obesity predictions
            # for moderate-risk users

            if final_prob > 0.70:

                final_prob *= 0.85


        # ========================================
        # 🚨 RISK LEVEL
        # ========================================

        risk_level = self.get_risk_level(
            final_prob
        )


        # ========================================
        # 🧠 CONFIDENCE
        # ========================================

        confidence = self.calculate_confidence(

            ml_prob,

            dl_prob
        )


        # ========================================
        # 📉 UNCERTAINTY
        # ========================================

        uncertainty = self.calculate_uncertainty_range(

            ml_prob,

            dl_prob
        )


        # ========================================
        # 📊 FINAL PERCENTAGE
        # ========================================

        final_percentage = round(
            final_prob * 100,
            2
        )


        # ========================================
        # 📦 FINAL OUTPUT
        # ========================================

        return {

            "probability": final_percentage,

            "display_probability": format_probability(
                final_percentage
            ),

            "risk_level": risk_level,

            "confidence": confidence,

            "uncertainty_range": uncertainty
        }


    # ============================================
    # 🚀 AGGREGATE ALL DISEASES
    # ============================================

    def aggregate_all(
        self,
        ml_results,
        dl_results
    ):

        # ========================================
        # 🩸 DIABETES
        # ========================================

        diabetes = self.aggregate_disease(

            "diabetes",

            ml_results["diabetes"],

            dl_results["diabetes"]
        )


        # ========================================
        # ❤️ HEART DISEASE
        # ========================================

        heart = self.aggregate_disease(

            "heart_disease",

            ml_results["heart_disease"],

            dl_results["heart_disease"]
        )


        # ========================================
        # ⚖️ OBESITY
        # ========================================

        obesity = self.aggregate_disease(

            "obesity",

            ml_results["obesity"],

            dl_results["obesity"]
        )


        # ========================================
        # 📦 FINAL RESULTS
        # ========================================

        return {

            "diabetes": diabetes,

            "heart_disease": heart,

            "obesity": obesity
        }