# ============================================
# 🚀 MASTER PREDICTOR ORCHESTRATOR
# ============================================

from project.pipeline.preprocess import (
    validate_input,
    FeatureReconstructor,
    FeaturePreprocessor
)

from project.pipeline.ml_inference import (
    MLInferenceEngine
)

from project.pipeline.dl_inference import (
    DLInferenceEngine
)

from project.pipeline.aggregator import (
    HybridAggregator
)


class HealthPredictor:

    def __init__(
        self,
        loader
    ):

        self.loader = loader


        # ========================================
        # 🧠 PIPELINE COMPONENTS
        # ========================================

        self.reconstructor = (
            FeatureReconstructor(
                loader.dataset
            )
        )

        self.preprocessor = (
            FeaturePreprocessor(
                loader
            )
        )

        self.ml_engine = (
            MLInferenceEngine(
                loader
            )
        )

        self.dl_engine = (
            DLInferenceEngine(
                loader
            )
        )

        self.aggregator = (
            HybridAggregator()
        )


    # ============================================
    # 🚀 FULL PIPELINE
    # ============================================

    def predict(
        self,
        user_input
    ):

        # ========================================
        # ✅ VALIDATION
        # ========================================

        validated = validate_input(
            user_input
        )


        # ========================================
        # 🔄 RECONSTRUCTION
        # ========================================

        reconstructed = (
            self.reconstructor.reconstruct(
                validated
            )
        )


        # ========================================
        # 🤖 ML FEATURES
        # ========================================

        ml_inputs = (
            self.preprocessor.prepare_ml_features(
                reconstructed
            )
        )


        # ========================================
        # 🧠 DL FEATURES
        # ========================================

        dl_inputs = (
            self.preprocessor.prepare_dl_features(
                reconstructed
            )
        )


        # ========================================
        # 🤖 ML PREDICTIONS
        # ========================================

        ml_results = (
            self.ml_engine.predict_all(
                ml_inputs
            )
        )


        # ========================================
        # 🧠 DL PREDICTIONS
        # ========================================

        dl_results = (
            self.dl_engine.predict(
                dl_inputs
            )
        )


        # ========================================
        # 🔥 HYBRID AGGREGATION
        # ========================================

        final_results = (
            self.aggregator.aggregate_all(

                ml_results,

                dl_results
            )
        )

        # ============================================
        # 🧪 DEBUG OUTPUTS
        # ============================================

        print("\n==============================")
        print("🧪 RAW MODEL OUTPUTS")
        print("==============================")

        print("\n📊 ML OUTPUTS")
        print(ml_results)

        print("\n🧠 DL OUTPUTS")
        print(dl_results)

        print("\n🔥 FINAL OUTPUTS")
        print(final_results)

        print("==============================\n")

        # ========================================
        # 📦 RETURN EVERYTHING
        # ========================================

        return {

            "validated_input": validated,

            "ml_results": ml_results,

            "dl_results": dl_results,

            "final_results": final_results
        }