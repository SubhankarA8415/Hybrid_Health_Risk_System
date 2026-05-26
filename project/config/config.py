# ============================================
# 🧠 CENTRAL CONFIGURATION FILE
# ============================================

from pathlib import Path


# ============================================
# 📁 PROJECT ROOT
# ============================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent


# ============================================
# 📁 ARTIFACT DIRECTORIES
# ============================================

ARTIFACTS_DIR = PROJECT_ROOT / "artifacts"

DL_ARTIFACTS_DIR = ARTIFACTS_DIR / "dl_model"

ML_ARTIFACTS_DIR = ARTIFACTS_DIR / "ml_models"


# # ============================================
# # 📁 GOOGLE DRIVE SOURCE PATHS
# # ============================================

# DRIVE_BASE_PATH = Path(
#     "/content/drive/MyDrive/Colab Notebooks/BRFSS_MODELS"
# )

# DL_DRIVE_PATH = DRIVE_BASE_PATH / "DL_Models" / "Final_DL_Model"

# ML_DRIVE_PATH = DRIVE_BASE_PATH / "ML_Final_Models_Features"

# DATASET_PATH = (
#     DRIVE_BASE_PATH
#     / "BRFSS_DATA"
#     / "brfss_hybrid_dataset.csv"
# )


# # ============================================
# # 🤖 DL MODEL FILES
# # ============================================

# DL_MODEL_FILE = DL_DRIVE_PATH / "model.keras"

# SHARED_SCALER_FILE = DL_DRIVE_PATH / "scaler_shared.pkl"

# OBESITY_SCALER_FILE = DL_DRIVE_PATH / "scaler_obesity.pkl"

# FEATURE_COLUMNS_FILE = DL_DRIVE_PATH / "feature_columns.json"

# BEST_THRESHOLDS_FILE = DL_DRIVE_PATH / "best_thresholds.json"


# # ============================================
# # 🤖 ML MODEL FILES
# # ============================================

# DIABETES_MODEL_FILE = (
#     ML_DRIVE_PATH / "diabetes_xgb_model.pkl"
# )

# HEART_MODEL_FILE = (
#     ML_DRIVE_PATH / "heart_xgb_model.pkl"
# )

# OBESITY_MODEL_FILE = (
#     ML_DRIVE_PATH / "obesity_lgbm_model.pkl"
# )


# # ============================================
# # 📊 FEATURE FILES
# # ============================================

# DIABETES_FEATURES_FILE = (
#     ML_DRIVE_PATH / "diabetes_features.pkl"
# )

# HEART_FEATURES_FILE = (
#     ML_DRIVE_PATH / "heart_disease_features.pkl"
# )

# OBESITY_FEATURES_FILE = (
#     ML_DRIVE_PATH / "obesity_features.pkl"
# )

# ============================================
# 📁 LOCAL DATA PATHS
# ============================================

DATA_DIR = PROJECT_ROOT / "data"

DATASET_PATH = DATA_DIR / "brfss_hybrid_dataset.csv"


# ============================================
# 🤖 DL MODEL FILES
# ============================================

DL_MODEL_FILE = (
    DL_ARTIFACTS_DIR / "model.keras"
)

SHARED_SCALER_FILE = (
    DL_ARTIFACTS_DIR / "scaler_shared.pkl"
)

OBESITY_SCALER_FILE = (
    DL_ARTIFACTS_DIR / "scaler_obesity.pkl"
)

FEATURE_COLUMNS_FILE = (
    DL_ARTIFACTS_DIR / "feature_columns.json"
)

BEST_THRESHOLDS_FILE = (
    DL_ARTIFACTS_DIR / "best_thresholds.json"
)


# ============================================
# 🤖 ML MODEL FILES
# ============================================

DIABETES_MODEL_FILE = (
    ML_ARTIFACTS_DIR / "diabetes_xgb_model.pkl"
)

HEART_MODEL_FILE = (
    ML_ARTIFACTS_DIR / "heart_xgb_model.pkl"
)

OBESITY_MODEL_FILE = (
    ML_ARTIFACTS_DIR / "obesity_lgbm_model.pkl"
)

MODEL_THRESHOLDS_FILE = (
    ML_ARTIFACTS_DIR / "model_thresholds.pkl"
)


# ============================================
# 📊 FEATURE FILES
# ============================================

DIABETES_FEATURES_FILE = (
    ML_ARTIFACTS_DIR / "diabetes_features.pkl"
)

HEART_FEATURES_FILE = (
    ML_ARTIFACTS_DIR / "heart_disease_features.pkl"
)

OBESITY_FEATURES_FILE = (
    ML_ARTIFACTS_DIR / "obesity_features.pkl"
)


# ============================================
# ⚙️ SYSTEM SETTINGS
# ============================================

N_MONTE_CARLO_SAMPLES = 20

RANDOM_STATE = 42


# ============================================
# 📈 RISK CALIBRATION
# ============================================

LOW_RISK_THRESHOLD = 0.10

MODERATE_RISK_THRESHOLD = 0.30


# ============================================
# 🧠 CONFIDENCE SETTINGS
# ============================================

HIGH_CONFIDENCE_THRESHOLD = 0.10

MODERATE_CONFIDENCE_THRESHOLD = 0.30

LOW_CONFIDENCE_THRESHOLD = 0.60


# ============================================
# 🌐 OPENROUTER SETTINGS
# ============================================

OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"

DEFAULT_LLM_MODEL = "openai/gpt-oss-120b:free"


# ============================================
# 🧾 APP SETTINGS
# ============================================

APP_NAME = "Hybrid Health Risk Prediction System"

APP_VERSION = "1.0.0"