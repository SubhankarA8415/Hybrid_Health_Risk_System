# ============================================
# 💬 CHAT ROUTES
# ============================================

from fastapi import APIRouter
from fastapi import HTTPException

from project.api.schemas import (

    ChatRequestSchema,

    ChatResponseSchema
)

from project.api.services.chat_service import (

    process_chat_message,

    fetch_chat_history
)

from project.database.connection import (
    SessionLocal
)

from project.database.models import (
    ChatHistory
)

from project.database.crud import (
    get_user_by_email
)


# ============================================
# 🚀 ROUTER
# ============================================

router = APIRouter()


# ============================================
# 💬 CHAT ENDPOINT
# ============================================

@router.post(

    "/chat",

    response_model=ChatResponseSchema
)

async def health_chat(

    payload: ChatRequestSchema
):

    try:

        result = process_chat_message(
            payload
        )

        return result


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=f"Chat Error: {str(e)}"
        )


# ============================================
# 📜 GET CHAT HISTORY
# ============================================

@router.get("/chat-history")

async def chat_history(

    email: str
):

    try:

        return fetch_chat_history(
            email
        )

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)
        )


# ============================================
# 🗑 CLEAR CHAT HISTORY
# ============================================

@router.delete("/clear-chat")

async def clear_chat_history(

    email: str
):

    db_user = get_user_by_email(
        email
    )


    if not db_user:

        raise HTTPException(

            status_code=404,

            detail="User not found"
        )


    db = SessionLocal()

    try:

        db.query(ChatHistory).filter(

            ChatHistory.user_id ==
            db_user.id

        ).delete()

        db.commit()


        return {

            "message":
            "Chat history cleared successfully"
        }


    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=str(e)
        )

    finally:

        db.close()