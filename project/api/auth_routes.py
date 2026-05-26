# ============================================
# 🔐 AUTH ROUTES
# ============================================

from fastapi import APIRouter
from fastapi import HTTPException

from sqlalchemy.exc import IntegrityError

from project.api.schemas import (

    RegisterSchema,

    LoginSchema
)

from project.api.local_auth import (

    hash_password,

    verify_password
)

from project.database.connection import (
    SessionLocal
)

from project.database.models import (
    User
)


# ============================================
# 🚀 ROUTER
# ============================================

router = APIRouter()


# ============================================
# 📝 REGISTER
# ============================================

@router.post("/register")

async def register(

    payload: RegisterSchema
):

    db = SessionLocal()

    try:

        # ====================================
        # ✨ CLEAN INPUT
        # ====================================

        email = payload.email.strip().lower()

        name = payload.name.strip()


        # ====================================
        # 🚨 EXISTING USER CHECK
        # ====================================

        existing_user = db.query(
            User
        ).filter(

            User.email == email

        ).first()


        if existing_user:

            raise HTTPException(

                status_code=400,

                detail="Email already registered"
            )


        # ====================================
        # 🔐 HASH PASSWORD
        # ====================================

        hashed_password = hash_password(
            payload.password
        )


        # ====================================
        # 👤 CREATE USER
        # ====================================

        new_user = User(

            name=name,

            email=email,

            password=hashed_password
        )


        # ====================================
        # 💾 SAVE USER
        # ====================================

        db.add(new_user)

        db.commit()

        db.refresh(new_user)


        # ====================================
        # ✅ SUCCESS RESPONSE
        # ====================================

        return {

            "name":
            new_user.name,

            "email":
            new_user.email
        }


    # ========================================
    # 🚨 HANDLE HTTP EXCEPTIONS
    # ========================================

    except HTTPException:

        raise


    # ========================================
    # 🚨 DATABASE DUPLICATE ERROR
    # ========================================

    except IntegrityError:

        db.rollback()

        raise HTTPException(

            status_code=400,

            detail="Email already exists"
        )


    # ========================================
    # 🚨 GENERIC ERROR
    # ========================================

    except Exception as e:

        db.rollback()

        raise HTTPException(

            status_code=500,

            detail=f"Registration Error: {str(e)}"
        )


    finally:

        db.close()


# ============================================
# 🔑 LOGIN
# ============================================

@router.post("/login")

async def login(

    payload: LoginSchema
):

    db = SessionLocal()

    try:

        # ====================================
        # ✨ CLEAN INPUT
        # ====================================

        email = payload.email.strip().lower()


        # ====================================
        # 👤 FIND USER
        # ====================================

        user = db.query(
            User
        ).filter(

            User.email == email

        ).first()


        if not user:

            raise HTTPException(

                status_code=401,

                detail="Invalid credentials"
            )


        # ====================================
        # 🔐 VERIFY PASSWORD
        # ====================================

        valid_password = verify_password(

            payload.password,

            user.password
        )


        if not valid_password:

            raise HTTPException(

                status_code=401,

                detail="Invalid credentials"
            )


        # ====================================
        # ✅ SUCCESS RESPONSE
        # ====================================

        return {

            "name":
            user.name,

            "email":
            user.email
        }


    # ========================================
    # 🚨 HANDLE HTTP EXCEPTIONS
    # ========================================

    except HTTPException:

        raise


    # ========================================
    # 🚨 GENERIC ERROR
    # ========================================

    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=f"Login Error: {str(e)}"
        )


    finally:

        db.close()