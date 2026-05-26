# ============================================
# 🌿 WELLNESS SCORING SERVICE
# ============================================


# ============================================
# 🌿 CALCULATE WELLNESS SCORE
# ============================================

def calculate_wellness_score(
    user_input
):

    score = 100


    # ========================================
    # 🚬 SMOKING
    # ========================================

    if user_input.smoking == 1:

        score -= 20


    # ========================================
    # ⚖ BMI
    # ========================================

    if user_input.bmi >= 30:

        score -= 20

    elif user_input.bmi >= 25:

        score -= 10


    # ========================================
    # 🏃 ACTIVITY
    # ========================================

    if user_input.activity_minutes < 30:

        score -= 15

    elif user_input.activity_minutes < 150:

        score -= 7


    # ========================================
    # 😴 SLEEP
    # ========================================

    if user_input.sleep_hours < 5:

        score -= 15

    elif user_input.sleep_hours < 7:

        score -= 7


    # ========================================
    # 🍎 FRUIT INTAKE
    # ========================================

    if user_input.fruit_intake < 2:

        score -= 5


    # ========================================
    # 🥦 VEGETABLE INTAKE
    # ========================================

    if user_input.vegetable_intake < 2:

        score -= 5


    # ========================================
    # 🍺 ALCOHOL
    # ========================================

    if user_input.alcohol == 1:

        score -= 5


    # ========================================
    # 🧠 MENTAL HEALTH
    # ========================================

    if user_input.mental_health_days > 15:

        score -= 10

    elif user_input.mental_health_days > 7:

        score -= 5


    # ========================================
    # 💪 PHYSICAL HEALTH
    # ========================================

    if user_input.physical_health_days > 15:

        score -= 10

    elif user_input.physical_health_days > 7:

        score -= 5


    # ========================================
    # 🌿 FINAL LIMITS
    # ========================================

    score = max(
        min(score, 100),
        0
    )

    return round(score, 2)