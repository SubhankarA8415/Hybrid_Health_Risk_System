# ============================================
# 🧠 GLOBAL AI DEPENDENCIES
# ============================================

from project.pipeline.loader import (
    ArtifactLoader
)

from project.pipeline.predictor import (
    HealthPredictor
)

from project.llm.interpreter import (
    HealthInterpreter
)

from project.llm.chat_assistant import (
    HealthChatAssistant
)


# ============================================
# 🚀 LOAD ARTIFACTS
# ============================================

loader = ArtifactLoader()


# ============================================
# 🧠 PREDICTOR
# ============================================

predictor = HealthPredictor(
    loader
)


# ============================================
# 🧠 HEALTH INTERPRETER
# ============================================

interpreter = HealthInterpreter()


# ============================================
# 💬 CHAT ASSISTANT
# ============================================

chat_assistant = (
    HealthChatAssistant()
)