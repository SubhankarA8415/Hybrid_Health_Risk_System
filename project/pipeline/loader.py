# ============================================
# 📦 CENTRAL ARTIFACT LOADER
# ============================================

import json
import joblib
import pandas as pd
import tensorflow as tf

from pathlib import Path

# ============================================
# 📁 IMPORT CONFIG
# ============================================

from project.config.config import *


# ============================================
# 🧠 ARTIFACT LOADER CLASS
# ============================================

class ArtifactLoader:

    def __init__(self):

        print("🚀 Initializing Artifact Loader...")

        self.load_all_artifacts()

        print("✅ All artifacts loaded successfully")


    # ============================================
    # 📦 LOAD EVERYTHING
    # ============================================

    def load_all_artifacts(self):

        self.load_dl_artifacts()

        self.load_ml_artifacts()

        self.load_dataset()


    # ============================================
    # 🤖 LOAD DL ARTIFACTS
    # ============================================

    def load_dl_artifacts(self):

        print("\\n🔹 Loading DL artifacts...")

        # DL Model
        self.dl_model = tf.keras.models.load_model(
            DL_MODEL_FILE
        )

        # Scalers
        self.shared_scaler = joblib.load(
            SHARED_SCALER_FILE
        )

        self.obesity_scaler = joblib.load(
            OBESITY_SCALER_FILE
        )

        # Feature Columns
        with open(FEATURE_COLUMNS_FILE, "r") as f:

            feature_config = json.load(f)

            self.shared_features = (
                feature_config["shared_features"]
            )

            self.obesity_dl_features = (
                feature_config["obesity_features"]
            )

        # Thresholds
        with open(BEST_THRESHOLDS_FILE, "r") as f:

            self.best_thresholds = json.load(f)

        print("✅ DL artifacts loaded")


    # ============================================
    # 🤖 LOAD ML ARTIFACTS
    # ============================================

    def load_ml_artifacts(self):

        print("\\n🔹 Loading ML artifacts...")

        # Models
        self.diabetes_model = joblib.load(
            DIABETES_MODEL_FILE
        )

        self.heart_model = joblib.load(
            HEART_MODEL_FILE
        )

        self.obesity_model = joblib.load(
            OBESITY_MODEL_FILE
        )

        # Feature Columns
        self.diabetes_features = joblib.load(
            DIABETES_FEATURES_FILE
        )

        self.heart_features = joblib.load(
            HEART_FEATURES_FILE
        )

        self.obesity_features = joblib.load(
            OBESITY_FEATURES_FILE
        )

        # Thresholds
        self.model_thresholds = joblib.load(
            MODEL_THRESHOLDS_FILE
        )

        print("✅ ML artifacts loaded")


    # ============================================
    # 📊 LOAD DATASET
    # ============================================

    def load_dataset(self):

        print("\\n🔹 Loading dataset...")

        self.dataset = pd.read_csv(
            DATASET_PATH
        )

        print(
            f"✅ Dataset loaded: {self.dataset.shape}"
        )


    # ============================================
    # 📋 SUMMARY
    # ============================================

    def summary(self):

        print("\\n" + "=" * 50)

        print("📦 ARTIFACT SUMMARY")

        print("=" * 50)

        print(f"DL Model Loaded: {self.dl_model is not None}")

        print(
            f"Dataset Shape: {self.dataset.shape}"
        )

        print(
            f"Diabetes Features: {len(self.diabetes_features)}"
        )

        print(
            f"Heart Features: {len(self.heart_features)}"
        )

        print(
            f"Obesity Features: {len(self.obesity_features)}"
        )

        print("=" * 50)