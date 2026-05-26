# ============================================
# 📦 AI ASSET DOWNLOADER
# ============================================

import os
import gdown


# ============================================
# 📁 CREATE REQUIRED DIRECTORIES
# ============================================

os.makedirs(
    "project/artifacts/dl_model",
    exist_ok=True
)

os.makedirs(
    "project/artifacts/ml_models",
    exist_ok=True
)

os.makedirs(
    "project/data",
    exist_ok=True
)


# ============================================
# 📦 ASSET CONFIGURATION
# ============================================

ASSETS = [

    # ========================================
    # 🧠 DEEP LEARNING MODEL FILES
    # ========================================

    {
        "name": "Best Thresholds",

        "file_id":
        "13ivtz-HK2gz8fWr9GtSsViTBju8KFT-a",

        "output":
        "project/artifacts/dl_model/best_thresholds.json"
    },

    {
        "name": "Feature Columns",

        "file_id":
        "17QSXTTgDWNXGgfLaof9m6X-hMU2w8ASo",

        "output":
        "project/artifacts/dl_model/feature_columns.json"
    },

    {
        "name": "Deep Learning Model",

        "file_id":
        "1Zkhd8rUJXrPcJ1XB41zCM7mc0dFuCJSz",

        "output":
        "project/artifacts/dl_model/model.keras"
    },

    {
        "name": "Obesity Scaler",

        "file_id":
        "134I5BPde80Vf3nhXIWIO_t6_sUy1eAIL",

        "output":
        "project/artifacts/dl_model/scaler_obesity.pkl"
    },

    {
        "name": "Shared Scaler",

        "file_id":
        "15IiYf47YF13ozY3h_CNGEyMlcwVokSIe",

        "output":
        "project/artifacts/dl_model/scaler_shared.pkl"
    },


    # ========================================
    # 🤖 MACHINE LEARNING MODEL FILES
    # ========================================

    {
        "name": "Diabetes Features",

        "file_id":
        "14okqedXHVoZHucv_AA7VMRa0bpr3Ced1",

        "output":
        "project/artifacts/ml_models/diabetes_features.pkl"
    },

    {
        "name": "Diabetes XGBoost Model",

        "file_id":
        "1cjphXuRj8RAtdAu5bTZCuyEaAvGYafd9",

        "output":
        "project/artifacts/ml_models/diabetes_xgb_model.pkl"
    },

    {
        "name": "Heart Disease Features",

        "file_id":
        "139DrK_IYMcGQwDZKYU_ldlj01tcV29lE",

        "output":
        "project/artifacts/ml_models/heart_disease_features.pkl"
    },

    {
        "name": "Heart Disease XGBoost Model",

        "file_id":
        "130zFTTjkmBMKlZ5nsH1qR5dnh-dnraFm",

        "output":
        "project/artifacts/ml_models/heart_xgb_model.pkl"
    },

    {
        "name": "ML Thresholds",

        "file_id":
        "1jwWHK5OsvNQ25sXvYN5kwvOtqD2L0bSg",

        "output":
        "project/artifacts/ml_models/model_thresholds.pkl"
    },

    {
        "name": "Obesity Features",

        "file_id":
        "1ZI9PZP8qo8aMxTc1jiqB91u9p4UAGwbh",

        "output":
        "project/artifacts/ml_models/obesity_features.pkl"
    },

    {
        "name": "Obesity LightGBM Model",

        "file_id":
        "1oUqv9HoFECMkHIsMDnRgfOh1ANqvDz0H",

        "output":
        "project/artifacts/ml_models/obesity_lgbm_model.pkl"
    },


    # ========================================
    # 📊 DATASET
    # ========================================

    {
        "name": "BRFSS Hybrid Dataset",

        "file_id":
        "19kR9vZSLQivFzHZwsC7QXbRLVOwXlp30",

        "output":
        "project/data/brfss_hybrid_dataset.csv"
    }
]


# ============================================
# 🚀 DOWNLOAD FUNCTION
# ============================================

def download_asset(

    file_id,

    output_path
):

    url = (
        f"https://drive.google.com/uc?id={file_id}"
    )

    gdown.download(

        url,

        output_path,

        quiet=False
    )


# ============================================
# 🚀 MAIN DOWNLOAD PIPELINE
# ============================================

print("\n============================================")
print("📦 AI ASSET DOWNLOADER INITIALIZED")
print("============================================\n")


for asset in ASSETS:

    output_path = asset["output"]


    # ========================================
    # ✅ FILE ALREADY EXISTS
    # ========================================

    if os.path.exists(output_path):

        print(

            f"✅ {asset['name']} already exists."
        )

        continue


    # ========================================
    # ⬇ START DOWNLOAD
    # ========================================

    print(

        f"\n⬇ Downloading {asset['name']}..."
    )

    print(

        f"📁 Saving to: {output_path}"
    )


    # ========================================
    # 🚀 DOWNLOAD EXECUTION
    # ========================================

    try:

        download_asset(

            asset["file_id"],

            output_path
        )


        print(

            f"✅ {asset['name']} downloaded successfully."
        )


    # ========================================
    # ❌ DOWNLOAD ERROR
    # ========================================

    except Exception as e:

        print(

            f"\n❌ Failed to download {asset['name']}"
        )

        print(

            f"📁 Output Path: {output_path}"
        )

        print(

            f"⚠ Error: {str(e)}\n"
        )


# ============================================
# 🎉 COMPLETION MESSAGE
# ============================================

print("\n============================================")
print("🎉 ALL AI ASSETS ARE READY")
print("============================================\n")

print(
    "You can now run the project normally.\n"
)