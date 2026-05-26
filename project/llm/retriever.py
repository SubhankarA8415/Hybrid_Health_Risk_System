# ============================================
# 🧠 KNOWLEDGE RETRIEVER
# ============================================

from project.llm.knowledge_base import (
    get_knowledge_base
)


class KnowledgeRetriever:

    def __init__(self):

        self.kb = get_knowledge_base()


    # ============================================
    # 🚀 RETRIEVE RELEVANT KNOWLEDGE
    # ============================================

    def retrieve(
        self,
        user_input
    ):

        selected = []


        # ========================================
        # 🚬 SMOKING
        # ========================================

        if user_input.get("smoking") == 1:

            selected.extend(

                self.kb["smoking"]["yes"]
            )


        # ========================================
        # ⚖️ BMI
        # ========================================

        bmi = user_input.get("bmi", 0)

        if bmi >= 30:

            selected.extend(

                self.kb["weight"]["high"]
            )


        # ========================================
        # 🏃 ACTIVITY
        # ========================================

        if user_input.get(
            "activity_minutes",
            0
        ) < 150:

            selected.extend(

                self.kb["exercise"]["low"]
            )


        # ========================================
        # 😴 SLEEP
        # ========================================

        if user_input.get(
            "sleep_hours",
            0
        ) < 7:

            selected.extend(

                self.kb["sleep"]["low"]
            )


        # ========================================
        # 🥗 DIET
        # ========================================

        fruit = user_input.get(
            "fruit_intake",
            0
        )

        veg = user_input.get(
            "vegetable_intake",
            0
        )

        if fruit <= 1 or veg <= 1:

            selected.extend(

                self.kb["diet"]["low"]
            )


        return list(set(selected))