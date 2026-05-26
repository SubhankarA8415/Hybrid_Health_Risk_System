# ============================================
# 🔐 LOCAL AUTH UTILS
# ============================================

import hashlib


# ============================================
# 🔑 HASH PASSWORD
# ============================================

def hash_password(
    password: str
) -> str:

    return hashlib.sha256(

        password.encode(
            "utf-8"
        )

    ).hexdigest()


# ============================================
# ✅ VERIFY PASSWORD
# ============================================

def verify_password(

    plain_password: str,

    hashed_password: str
) -> bool:

    return (

        hash_password(
            plain_password
        )

        == hashed_password
    )