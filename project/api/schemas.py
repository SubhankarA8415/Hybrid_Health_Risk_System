# ============================================
# 📦 API SCHEMAS
# ============================================

from typing import List
from typing import Tuple
from typing import Optional

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr


# ============================================
# 📥 HEALTH INPUT SCHEMA
# ============================================

class HealthInputSchema(BaseModel):


    # ========================================
    # 👤 BASIC PROFILE
    # ========================================

    age: int = Field(
        ...,
        ge=18,
        le=100
    )

    gender: int = Field(
        ...,
        ge=0,
        le=1
    )

    bmi: float = Field(
        ...,
        ge=10.0,
        le=60.0
    )


    # ========================================
    # 🩺 GENERAL HEALTH
    # ========================================

    general_health: int = Field(
        ...,
        ge=1,
        le=5
    )

    sleep_hours: int = Field(
        ...,
        ge=0,
        le=24
    )

    mental_health_days: int = Field(
        ...,
        ge=0,
        le=30
    )

    physical_health_days: int = Field(
        ...,
        ge=0,
        le=30
    )


    # ========================================
    # 🏃 ACTIVITY & LIFESTYLE
    # ========================================

    activity_minutes: int = Field(
        ...,
        ge=0,
        le=3000
    )

    sedentary: int = Field(
        ...,
        ge=0,
        le=1
    )

    exercise_flag: int = Field(
        ...,
        ge=0,
        le=1
    )


    # ========================================
    # 🍎 NUTRITION
    # ========================================

    fruit_intake: int = Field(
        ...,
        ge=0,
        le=3
    )

    vegetable_intake: int = Field(
        ...,
        ge=0,
        le=3
    )

    plant_food: int = Field(
        ...,
        ge=0,
        le=10
    )


    # ========================================
    # 🚬 RISK FACTORS
    # ========================================

    smoking: int = Field(
        ...,
        ge=0,
        le=1
    )

    alcohol: int = Field(
        ...,
        ge=0,
        le=1
    )


    # ========================================
    # 🏥 HEALTHCARE ACCESS
    # ========================================

    insurance: int = Field(
        ...,
        ge=0,
        le=1
    )

    doctor_access: int = Field(
        ...,
        ge=0,
        le=1
    )

    cost_issue: int = Field(
        ...,
        ge=0,
        le=1
    )


    # ========================================
    # ♿ DISABILITY
    # ========================================

    disability: int = Field(
        ...,
        ge=0,
        le=5
    )


    # ========================================
    # 👤 OPTIONAL USER EMAIL
    # ========================================

    user_email: Optional[
        EmailStr
    ] = None


# ============================================
# 📊 DISEASE RESULT SCHEMA
# ============================================

class DiseasePredictionSchema(
    BaseModel
):

    probability: float

    risk_level: str

    confidence: str

    uncertainty_range: Tuple[
        float,
        float
    ]


# ============================================
# 📦 FINAL PREDICTION RESPONSE
# ============================================

class PredictionResponseSchema(
    BaseModel
):

    predictions: dict

    interpretation: str


# ============================================
# 📜 HISTORY ITEM
# ============================================

class HistoryItemSchema(
    BaseModel
):

    id: int

    prediction_results: str

    created_at: str


# ============================================
# 💬 CHAT ITEM
# ============================================

class ChatHistorySchema(
    BaseModel
):

    role: str

    message: str

    created_at: str


# ============================================
# 💬 CHAT REQUEST SCHEMA
# ============================================

class ChatRequestSchema(
    BaseModel
):

    message: str

    history: Optional[
        List[dict]
    ] = None

    user_email: Optional[
        EmailStr
    ] = None


# ============================================
# 💬 CHAT RESPONSE SCHEMA
# ============================================

class ChatResponseSchema(
    BaseModel
):

    response: str


# ============================================
# 🔐 REGISTER SCHEMA
# ============================================

class RegisterSchema(
    BaseModel
):

    name: str

    email: EmailStr

    password: str


# ============================================
# 🔑 LOGIN SCHEMA
# ============================================

class LoginSchema(
    BaseModel
):

    email: EmailStr

    password: str