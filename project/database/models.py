# ============================================
# 🧠 DATABASE MODELS
# ============================================

from datetime import datetime
from zoneinfo import ZoneInfo

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey

from sqlalchemy.orm import relationship

from project.database.connection import Base


# ============================================
# 👤 USERS TABLE
# ============================================

class User(Base):

    __tablename__ = "users"

    id = Column(

        Integer,

        primary_key=True,

        index=True
    )

    name = Column(

        String,

        nullable=False
    )

    email = Column(

        String,

        unique=True,

        index=True,

        nullable=False
    )

    password = Column(

        String,

        nullable=False
    )

    created_at = Column(

        DateTime,

        default=lambda: datetime.now(
        ZoneInfo("Asia/Kolkata")
)
    )


    # ========================================
    # 🔗 RELATIONSHIPS
    # ========================================

    reports = relationship(

        "HealthReport",

        back_populates="user",

        cascade="all, delete"
    )

    chats = relationship(

        "ChatHistory",

        back_populates="user",

        cascade="all, delete"
    )


# ============================================
# 📊 HEALTH REPORT TABLE
# ============================================

class HealthReport(Base):

    __tablename__ = "health_reports"

    id = Column(

        Integer,

        primary_key=True,

        index=True
    )


    # ========================================
    # 👤 USER RELATION
    # ========================================

    user_id = Column(

        Integer,

        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),

        nullable=False,

        index=True
    )


    # ========================================
    # 📥 INPUT DATA
    # ========================================

    input_data = Column(

        Text,

        nullable=False
    )


    # ========================================
    # 📊 PREDICTION RESULTS
    # ========================================

    prediction_results = Column(

        Text,

        nullable=False
    )


    # ========================================
    # 🧠 AI INTERPRETATION
    # ========================================

    interpretation = Column(

        Text,

        nullable=False
    )


    # ========================================
    # 🌿 WELLNESS SCORE
    # ========================================

    wellness_score = Column(

        Float,

        default=0
    )


    # ========================================
    # 🕒 TIMESTAMP
    # ========================================

    created_at = Column(

        DateTime,

        default=lambda: datetime.now(
        ZoneInfo("Asia/Kolkata")
        ),

        index=True
    )


    # ========================================
    # 🔗 RELATIONSHIP
    # ========================================

    user = relationship(

        "User",

        back_populates="reports"
    )


# ============================================
# 💬 CHAT HISTORY TABLE
# ============================================

class ChatHistory(Base):

    __tablename__ = "chat_history"

    id = Column(

        Integer,

        primary_key=True,

        index=True
    )


    # ========================================
    # 👤 USER RELATION
    # ========================================

    user_id = Column(

        Integer,

        ForeignKey(
            "users.id",
            ondelete="CASCADE"
        ),

        nullable=False,

        index=True
    )


    # ========================================
    # 💬 CHAT ROLE
    # ========================================

    role = Column(

        String,

        nullable=False
    )


    # ========================================
    # 📝 MESSAGE
    # ========================================

    message = Column(

        Text,

        nullable=False
    )


    # ========================================
    # 🕒 TIMESTAMP
    # ========================================

    created_at = Column(

        DateTime,

        default=lambda: datetime.now(
        ZoneInfo("Asia/Kolkata")
       ),

        index=True
    )


    # ========================================
    # 🔗 RELATIONSHIP
    # ========================================

    user = relationship(

        "User",

        back_populates="chats"
    )