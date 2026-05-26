# ============================================
# 🧠 CONTROLLED LLM INTERPRETER
# ============================================

from project.llm.prompts import (
    MASTER_PROMPT
)

from project.llm.retriever import (
    KnowledgeRetriever
)

from project.llm.openrouter_client import (
    client
)


class HealthInterpreter:

    def __init__(self):

        self.retriever = (
            KnowledgeRetriever()
        )


    # ============================================
    # 🚀 GENERATE INTERPRETATION
    # ============================================

    def interpret(
        self,
        user_input,
        prediction_output
    ):

        # ========================================
        # 📚 KNOWLEDGE RETRIEVAL
        # ========================================

        knowledge = self.retriever.retrieve(
            user_input
        )

        knowledge_text = "\n".join(

            f"- {item}"

            for item in knowledge
        )


        # ========================================
        # 🧠 INTERPRETATION RULES
        # ========================================

        interpretation_rules = """

IMPORTANT INTERPRETATION RULES:

1. Probability Interpretation:
- Treat probabilities exactly as provided.
- If probability is shown as "<1%", interpret it as extremely low risk.
- Do NOT convert "<1%" into 1%, 10%, or 100%.
- Never misread decimal percentages.

2. Risk Language Calibration:
- Below 5% → describe as "very low risk"
- 5% to 15% → describe as "low risk"
- 15% to 40% → describe as "moderate risk"
- Above 40% → describe as "high risk"

3. Tone Control:
- Avoid alarming or dramatic language for low-risk users.
- Do not frame low probabilities as major concerns.
- For healthy profiles, focus on reassurance, prevention, and maintenance.
- Reserve stronger warning language only for moderate or high-risk predictions.

4. Medical Safety:
- Do not diagnose diseases.
- Clearly state that predictions are estimates, not medical conclusions.
- Encourage professional consultation only when appropriate.

5. Recommendation Priorities:
- Prioritize smoking cessation first if user smokes.
- Then address obesity/BMI.
- Then physical inactivity.
- Then sedentary behavior.
- Then diet quality.
- Then sleep/stress.

6. Formatting:
- Use clean sections.
- Keep recommendations practical and realistic.
- Avoid exaggerated claims.
"""


        # ========================================
        # 🧠 FINAL PROMPT
        # ========================================

        prompt = f"""

{MASTER_PROMPT}

------------------------------------------------

{interpretation_rules}

------------------------------------------------

USER INPUT:
{user_input}

------------------------------------------------

PREDICTION RESULTS:
{prediction_output}

------------------------------------------------

RELEVANT HEALTH KNOWLEDGE:
{knowledge_text}

------------------------------------------------

Generate the final response.

"""


        # ========================================
        # 🤖 OPENROUTER REQUEST
        # ========================================

        response = client.chat.completions.create(

            model="openai/gpt-oss-120b:free",

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        return response.choices[0].message.content