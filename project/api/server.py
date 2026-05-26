# ============================================
# 🚀 MAIN FASTAPI SERVER
# ============================================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from project.database.connection import (
    Base,
    engine
)


# ============================================
# 📦 ROUTES
# ============================================

from project.api.auth_routes import (
    router as auth_router
)

from project.api.prediction_routes import (
    router as prediction_router
)

from project.api.chat_routes import (
    router as chat_router
)

from project.api.report_routes import (
    router as report_router
)


# ============================================
# 🚀 CREATE DATABASE TABLES
# ============================================

Base.metadata.create_all(
    bind=engine
)

print("✅ DATABASE TABLES CREATED")


# ============================================
# 🚀 FASTAPI APP
# ============================================

app = FastAPI(

    title="Hybrid Health Risk System API"
)


# ============================================
# 🌐 CORS
# ============================================

app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]
)


# ============================================
# 📦 REGISTER ROUTES
# ============================================

app.include_router(
    auth_router
)

app.include_router(
    prediction_router
)

app.include_router(
    chat_router
)

app.include_router(
    report_router
)


# ============================================
# 🏠 ROOT ENDPOINT
# ============================================

@app.get("/")

async def root():

    return {

        "message":
        "Hybrid Health Risk System API Running"
    }


# ============================================
# ❤️ HEALTH CHECK
# ============================================

@app.get("/health")

async def health_check():

    return {

        "status":
        "healthy"
    }