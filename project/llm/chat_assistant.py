# ============================================
# 💬 AI HEALTH CHAT ASSISTANT
# ============================================

from project.llm.prompts import (
    CHAT_PROMPT
)

from project.llm.openrouter_client import (
    client
)


# ============================================
# 💬 CHAT ASSISTANT ENGINE
# ============================================

class HealthChatAssistant:


    # ========================================
    # 🚀 INIT
    # ========================================

    def __init__(self):

        pass


    # ========================================
    # 💬 GENERATE CHAT RESPONSE
    # ========================================

    def chat(

        self,

        user_message,

        conversation_history=None
    ):

        try:

            # ====================================
            # 📜 DEFAULT HISTORY
            # ====================================

            if conversation_history is None:

                conversation_history = []


            # ====================================
            # 🧠 SYSTEM MESSAGE
            # ====================================

            messages = [

                {
                    "role": "system",

                    "content": CHAT_PROMPT
                }
            ]


            # ====================================
            # 💬 PREVIOUS CHAT HISTORY
            # ====================================

            for item in conversation_history:

                try:

                    # ============================
                    # SUPPORT BOTH:
                    # content / message
                    # ============================

                    content = item.get(

                        "content",

                        item.get(
                            "message",
                            ""
                        )
                    )


                    role = item.get(
                        "role",
                        "user"
                    )


                    if content:

                        messages.append({

                            "role":
                            role,

                            "content":
                            content
                        })

                except Exception:

                    continue


            # ====================================
            # 👤 CURRENT USER MESSAGE
            # ====================================

            messages.append({

                "role": "user",

                "content": user_message
            })


            # ====================================
            # 🤖 OPENROUTER REQUEST
            # ====================================

            response = client.chat.completions.create(

                model="openai/gpt-oss-120b:free",

                messages=messages,

                temperature=0.7,

                max_tokens=800
            )


            # ====================================
            # 🚨 EMPTY RESPONSE SAFETY
            # ====================================

            if (

                not response

                or not hasattr(
                    response,
                    "choices"
                )

                or len(response.choices) == 0
            ):

                return (
                    "I'm unable to generate "
                    "a response right now."
                )


            # ====================================
            # 📦 EXTRACT RESPONSE
            # ====================================

            choice = response.choices[0]


            if (

                not hasattr(
                    choice,
                    "message"
                )

                or not choice.message
            ):

                return (
                    "I couldn't process "
                    "that request properly."
                )


            content = getattr(

                choice.message,

                "content",

                None
            )


            # ====================================
            # 🚨 EMPTY CONTENT SAFETY
            # ====================================

            if not content:

                return (
                    "I don't have a proper "
                    "response for that yet."
                )


            # ====================================
            # ✅ FINAL RESPONSE
            # ====================================

            return content.strip()


        # ========================================
        # 🚨 GLOBAL ERROR HANDLER
        # ========================================

        except Exception as e:

            print(
                "❌ CHAT ASSISTANT ERROR:",
                str(e)
            )

            return (
                "Sorry, I encountered an "
                "issue while processing "
                "your message."
            )