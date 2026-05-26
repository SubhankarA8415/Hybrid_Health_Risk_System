# ============================================
# 🧠 INPUT SCHEMA
# ============================================

INPUT_SCHEMA = {

    "age": {
        "type": int,
        "min": 18,
        "max": 100,
        "description": "Age in years"
    },

    "gender": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "Female",
            1: "Male"
        },
        "description": "Biological gender"
    },

    "bmi": {
        "type": float,
        "min": 10,
        "max": 60,
        "description": "Body Mass Index"
    },

    "general_health": {
        "type": int,
        "min": 1,
        "max": 5,
        "mapping": {
            1: "Excellent",
            2: "Very Good",
            3: "Good",
            4: "Fair",
            5: "Poor"
        },
        "description": "Self-rated health"
    },

    "mental_health_days": {
        "type": int,
        "min": 0,
        "max": 30,
        "description": "Poor mental health days"
    },

    "physical_health_days": {
        "type": int,
        "min": 0,
        "max": 30,
        "description": "Poor physical health days"
    },

    "activity_minutes": {
        "type": int,
        "min": 0,
        "max": 3000,
        "description": "Weekly activity minutes"
    },

    "sedentary": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Sedentary lifestyle"
    },

    "exercise_flag": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Meets exercise guideline"
    },

    "fruit_intake": {
        "type": int,
        "min": 0,
        "max": 3,
        "description": "Fruit intake quality"
    },

    "vegetable_intake": {
        "type": int,
        "min": 0,
        "max": 3,
        "description": "Vegetable intake quality"
    },

    "plant_food": {
        "type": int,
        "min": 0,
        "max": 10,
        "description": "Plant food score"
    },

    "smoking": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Smoking status"
    },

    "alcohol": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Alcohol consumption"
    },

    "sleep_hours": {
        "type": int,
        "min": 0,
        "max": 24,
        "description": "Average sleep hours"
    },

    "insurance": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Has health insurance"
    },

    "doctor_access": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Access to doctor"
    },

    "cost_issue": {
        "type": int,
        "choices": [0, 1],
        "mapping": {
            0: "No",
            1: "Yes"
        },
        "description": "Avoided healthcare due to cost"
    },

    "disability": {
        "type": int,
        "min": 0,
        "max": 5,
        "description": "Disability limitation score"
    }
}

# ============================================
# ✅ INPUT VALIDATION
# ============================================

def validate_input(user_input):

    """
    Validate user input against INPUT_SCHEMA
    """

    validated_data = {}

    # ============================================
    # 🔍 CHECK REQUIRED FIELDS
    # ============================================

    for field, rules in INPUT_SCHEMA.items():

        # Missing field
        if field not in user_input:

            raise ValueError(
                f"Missing required field: {field}"
            )

        value = user_input[field]

        # ============================================
        # 🔍 TYPE VALIDATION
        # ============================================

        expected_type = rules["type"]

        try:
            value = expected_type(value)

        except Exception:

            raise TypeError(
                f"Invalid type for '{field}'. "
                f"Expected {expected_type.__name__}"
            )

        # ============================================
        # 🔍 CHOICE VALIDATION
        # ============================================

        if "choices" in rules:

            if value not in rules["choices"]:

                raise ValueError(
                    f"Invalid value for '{field}'. "
                    f"Allowed: {rules['choices']}"
                )

        # ============================================
        # 🔍 RANGE VALIDATION
        # ============================================

        if "min" in rules:

            if value < rules["min"]:

                # Special adult-only rule
                if field == "age":

                    raise ValueError(
                        "System currently supports "
                        "adults only (18+ years)"
                    )

                raise ValueError(
                    f"'{field}' below minimum "
                    f"({rules['min']})"
                )

        if "max" in rules:

            if value > rules["max"]:

                raise ValueError(
                    f"'{field}' above maximum "
                    f"({rules['max']})"
                )
        
        # ============================================
        # ✅ STORE VALIDATED VALUE
        # ============================================

        validated_data[field] = value

    return validated_data

# ============================================
# 📦 IMPORTS
# ============================================

import random
import pandas as pd

# ============================================
# 🔄 INPUT → DATASET COLUMN MAPPING
# ============================================

COLUMN_MAPPING = {

    "gender": "sex",

    "general_health": "genhlth",

    "mental_health_days": "menthlth",

    "physical_health_days": "physhlth",

    "sleep_hours": "sleptim1",

    "smoking": "smoking_status",

    "alcohol": "drnkany5",

    "exercise_flag": "meets_guidelines",

    "activity_minutes": "total_activity_minutes",

    "plant_food": "total_plant_food",

    "disability": "disability_score",

    "insurance": "has_insurance",

    "doctor_access": "personal_doctor",

    "cost_issue": "cost_barrier"
}

# ============================================
# 🧠 FEATURE RECONSTRUCTION ENGINE
# ============================================

# ============================================
# 🔄 FEATURE RECONSTRUCTOR
# ============================================

class FeatureReconstructor:


    def __init__(self, dataset):

        self.dataset = dataset.copy()


    # ============================================
    # 🔄 APPLY USER INPUT
    # ============================================

    def apply_user_input(

        self,

        sample,

        user_input
    ):

        # ========================================
        # 🔄 DIRECT COLUMN MAPPING
        # ========================================

        for user_key, dataset_col in COLUMN_MAPPING.items():

            if dataset_col in sample.columns:

                sample[dataset_col] = user_input[
                    user_key
                ]


        # ========================================
        # 🔄 SPECIAL DIRECT FEATURES
        # ========================================

        if "bmi" in sample.columns:

            sample["bmi"] = user_input["bmi"]


        if "sedentary" in sample.columns:

            sample["sedentary"] = user_input[
                "sedentary"
            ]


        # ========================================
        # 🔄 ENGINEERED FEATURES
        # ========================================

        if "total_unhealthy_days" in sample.columns:

            sample["total_unhealthy_days"] = (

                user_input["mental_health_days"]

                +

                user_input["physical_health_days"]
            )


        return sample


    # ============================================
    # 🔍 FIND SIMILAR PROFILES
    # ============================================

    def find_similar_profiles(

        self,

        user_input
    ):

        df = self.dataset.copy()


        # ========================================
        # 🎯 AGE FILTER
        # ========================================

        if "X_age80" in df.columns:

            df = df[

                (df["X_age80"] >= user_input["age"] - 5)

                &

                (df["X_age80"] <= user_input["age"] + 5)
            ]


        # ========================================
        # 🎯 GENDER FILTER
        # ========================================

        if "sex" in df.columns:

            df = df[
                df["sex"] == user_input["gender"]
            ]


        # ========================================
        # 🎯 BMI FILTER
        # ========================================

        if "bmi" in df.columns:

            df = df[

                (df["bmi"] >= user_input["bmi"] - 2)

                &

                (df["bmi"] <= user_input["bmi"] + 2)
            ]


        # ========================================
        # 🚨 FALLBACK
        # ========================================

        if len(df) < 20:

            df = self.dataset.copy()


        # ========================================
        # 📊 SIMILARITY SCORE
        # ========================================

        df["similarity_score"] = 0.0


        # ========================================
        # 📊 AGE DISTANCE
        # ========================================

        if "X_age80" in df.columns:

            df["similarity_score"] += abs(

                df["X_age80"]

                -

                user_input["age"]
            )


        # ========================================
        # 📊 BMI DISTANCE
        # ========================================

        if "bmi" in df.columns:

            df["similarity_score"] += abs(

                df["bmi"]

                -

                user_input["bmi"]
            )


        # ========================================
        # 📊 SLEEP DISTANCE
        # ========================================

        if "sleptim1" in df.columns:

            df["similarity_score"] += abs(

                df["sleptim1"]

                -

                user_input["sleep_hours"]
            )


        # ========================================
        # 📊 GENERAL HEALTH DISTANCE
        # ========================================

        if "genhlth" in df.columns:

            df["similarity_score"] += abs(

                df["genhlth"]

                -

                user_input["general_health"]
            )


        # ========================================
        # 🚭 SMOKING PENALTY
        # ========================================

        if "smoking_status" in df.columns:

            df["similarity_score"] += (

                df["smoking_status"]

                !=

                user_input["smoking"]

            ).astype(int) * 10


        # ========================================
        # 🏃 ACTIVITY DISTANCE
        # ========================================

        if "total_activity_minutes" in df.columns:

            df["similarity_score"] += abs(

                df["total_activity_minutes"]

                -

                user_input["activity_minutes"]

            ) / 50


        # ========================================
        # 🔝 TOP MATCHES
        # ========================================

        df = df.sort_values(

            by="similarity_score"

        ).head(20)


        return df


    # ============================================
    # 🔄 FINAL RECONSTRUCTION
    # ============================================

    def reconstruct(

        self,

        user_input
    ):

        # ========================================
        # 🔍 SIMILAR USERS
        # ========================================

        similar_df = self.find_similar_profiles(
            user_input
        )


        # ========================================
        # 📊 AVERAGE NUMERIC FEATURES
        # ========================================

        # ========================================
        # 📊 NUMERIC FEATURES
        # ========================================

        numeric_cols = similar_df.select_dtypes(
            include=["number"]
        ).columns


        reconstructed = {}


        # ========================================
        # 📊 RECONSTRUCT FEATURES
        # ========================================

        for col in numeric_cols:

            unique_values = similar_df[col].nunique()


            # ====================================
            # 🔘 BINARY / CATEGORICAL
            # ====================================

            if unique_values <= 10:

                reconstructed[col] = (
                    similar_df[col]
                    .mode()
                    .iloc[0]
                )


            # ====================================
            # 📈 CONTINUOUS
            # ====================================

            else:

                reconstructed[col] = (
                    similar_df[col]
                    .mean()
                )


        # ========================================
        # 🔄 CONVERT TO DATAFRAME
        # ========================================

        reconstructed = pd.DataFrame(
            [reconstructed]
        )


        # ========================================
        # 🔄 APPLY TRUE USER INPUT
        # ========================================

        reconstructed = self.apply_user_input(

            reconstructed,

            user_input
        )


        # ========================================
        # 🧹 CLEANUP
        # ========================================

        reconstructed = reconstructed.drop(

            columns=["similarity_score"],

            errors="ignore"
        )


        return reconstructed.reset_index(
            drop=True
        )
    
    # ============================================
# 🧠 FEATURE PREPROCESSOR
# ============================================

class FeaturePreprocessor:

    def __init__(self, loader):

        self.loader = loader


    # ============================================
    # 🤖 PREPARE ML FEATURES
    # ============================================

    def prepare_ml_features(
        self,
        sample
    ):

        """
        Prepare ML model inputs
        """

        diabetes_input = sample[
            self.loader.diabetes_features
        ]

        heart_input = sample[
            self.loader.heart_features
        ]

        obesity_input = sample[
            self.loader.obesity_features
        ]

        return {
            "diabetes": diabetes_input,
            "heart_disease": heart_input,
            "obesity": obesity_input
        }


    # ============================================
    # 🤖 PREPARE DL FEATURES
    # ============================================

    def prepare_dl_features(
    self,
    sample
):

        """
        Prepare multi-input DL model features
        """

        # ============================================
        # 🚫 REMOVE TARGETS / META FEATURES
        # ============================================

        drop_cols = [

            "diabetes",
            "heart_disease",
            "obesity"
        ]

        existing_drop_cols = [

            col for col in drop_cols
            if col in sample.columns
        ]

        clean_sample = sample.drop(
            columns=existing_drop_cols
        )


        # ============================================
        # 🧠 SHARED INPUT
        # ============================================

        shared_input = clean_sample[
            self.loader.shared_features
        ]

        shared_scaled = (
            self.loader.shared_scaler.transform(
                shared_input
            )
        )


        # ============================================
        # ⚖️ OBESITY INPUT
        # ============================================

        obesity_input = clean_sample[
            self.loader.obesity_dl_features
        ]

        obesity_scaled = (
            self.loader.obesity_scaler.transform(
                obesity_input
            )
        )


        # ============================================
        # ✅ RETURN MULTI-INPUT FORMAT
        # ============================================

        return [
            shared_scaled,
            obesity_scaled
        ]