# ============================================
# 💬 CHAT SERVICE
# ============================================

from project.api.dependencies import (
    chat_assistant
)

from project.database.crud import (

    get_user_by_email,

    get_chat_history,

    save_chat_message
)


# ============================================
# 💬 PROCESS CHAT MESSAGE
# ============================================

def process_chat_message(
    payload
):

    # ========================================
    # 💬 GENERATE RESPONSE
    # ========================================

    response = chat_assistant.chat(

        user_message=payload.message,

        conversation_history=(
            payload.history or []
        )
    )


    # ========================================
    # 💾 SAVE CHAT
    # ========================================

    if payload.user_email:

        db_user = get_user_by_email(

            payload.user_email
        )


        if db_user:

            try:

                # ============================
                # 👤 USER MESSAGE
                # ============================

                save_chat_message(

                    user_id=db_user.id,

                    role="user",

                    message=payload.message
                )


                # ============================
                # 🤖 ASSISTANT RESPONSE
                # ============================

                save_chat_message(

                    user_id=db_user.id,

                    role="assistant",

                    message=response
                )

                print(
                    "✅ CHAT SAVED"
                )

            except Exception as save_error:

                print(

                    "❌ CHAT SAVE FAILED:",

                    str(save_error)
                )


    # ========================================
    # 📦 FINAL OUTPUT
    # ========================================

    return {

        "response":
        response
    }


# ============================================
# 📜 FETCH CHAT HISTORY
# ============================================

def fetch_chat_history(
    email
):

    db_user = get_user_by_email(
        email
    )


    if not db_user:

        return []


    chats = get_chat_history(
        db_user.id
    )


    response = []


    for chat in chats:

        response.append({

            "role":
            chat.role,

            "message":
            chat.message,

            "created_at":
            str(chat.created_at)
        })


    return response