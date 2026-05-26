# 🩺 AI Health Companion  
### Hybrid AI-Powered Preventive Healthcare & Wellness Intelligence System

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-FF6F00?style=for-the-badge&logo=tensorflow)
![XGBoost](https://img.shields.io/badge/XGBoost-MLModel-EC6B23?style=for-the-badge)
![LightGBM](https://img.shields.io/badge/LightGBM-MLModel-7CB342?style=for-the-badge)

</p>

---

# 📌 Overview

AI Health Companion is a hybrid AI-powered preventive healthcare and wellness intelligence platform designed to analyze lifestyle, behavioral, and wellness indicators to generate:

- Disease risk predictions
- Wellness analytics
- AI-generated health interpretation
- Preventive healthcare insights
- Interactive dashboards
- Downloadable PDF reports
- AI healthcare assistant support

The system combines:

- Machine Learning
- Deep Learning
- Wellness Analytics
- LLM-based Interpretation
- Full Stack Web Development

into a complete healthcare analytics platform.

---

# 🚀 Key Features

## 🧠 Hybrid AI Prediction System

- Hybrid Machine Learning + Deep Learning inference
- Multi-model health risk prediction
- Intelligent risk aggregation
- Dynamic risk calibration system

---

## 📊 Interactive Health Analytics Dashboard

- Premium healthcare dashboard UI
- Interactive Plotly analytics
- Risk probability visualization
- Wellness score analytics
- Dynamic healthcare insights

---

## 🌿 Wellness Intelligence System

- AI-generated wellness scoring
- Lifestyle analytics
- Behavioral health analysis
- Preventive wellness recommendations

---

## 💬 AI Healthcare Assistant

- AI-powered wellness chatbot
- Healthcare-related conversational support
- Personalized interpretation assistance
- LLM-based interaction system

---

## 📄 Smart PDF Report Generation

- Professionally formatted PDF reports
- AI-generated wellness interpretation
- Risk analytics tables
- Preventive healthcare summaries
- Downloadable assessment reports

---

## 🔐 Authentication System

- Secure user registration & login
- Password hashing with Argon2
- Session management
- Persistent report history

---

## 📜 Report History Management

- View previous reports
- Download PDF reports
- Delete saved reports
- Persistent user-specific analytics history

---

# 🏗️ System Architecture

The project follows a modular full-stack architecture divided into:

## 🎨 Frontend

Built using:
- Streamlit
- Plotly
- Custom HTML/CSS

Responsibilities:
- User interaction
- Assessment forms
- Dashboard rendering
- Visualization
- Chat interface
- Report management

---

## ⚙️ Backend

Built using:
- FastAPI
- Uvicorn
- Pydantic

Responsibilities:
- API routing
- Authentication
- Prediction handling
- Report management
- AI integration
- Database communication

---

## 🧬 AI Pipeline

Built using:
- TensorFlow / Keras
- XGBoost
- LightGBM
- Scikit-learn

Responsibilities:
- ML inference
- DL inference
- Hybrid aggregation
- Risk analytics
- Wellness scoring

---

## 🗄️ Database

Built using:
- SQLite
- SQLAlchemy

Stores:
- User accounts
- Report history
- Chat history
- Authentication data

---

# 📂 Project Structure

```bash
HYBRID-HEALTH-RISK-SYSTEM/
│
├── project/
│
│   ├── api/
│   │   ├── services/
│   │   ├── auth_routes.py
│   │   ├── chat_routes.py
│   │   ├── prediction_routes.py
│   │   ├── report_routes.py
│   │   ├── schemas.py
│   │   └── server.py
│   │
│   ├── artifacts/
│   │   ├── dl_model/
│   │   └── ml_models/
│   │
│   ├── config/
│   │   └── config.py
│   │
│   ├── data/
│   │   └── brfss_hybrid_dataset.csv
│   │
│   ├── database/
│   │   ├── connection.py
│   │   ├── crud.py
│   │   └── models.py
│   │
│   ├── llm/
│   │   ├── chat_assistant.py
│   │   ├── interpreter.py
│   │   ├── prompts.py
│   │   ├── retriever.py
│   │   └── openrouter_client.py
│   │
│   ├── pipeline/
│   │   ├── predictor.py
│   │   ├── aggregator.py
│   │   ├── dl_inference.py
│   │   ├── ml_inference.py
│   │   └── preprocess.py
│   │
│   └── ui/
│       ├── components/
│       ├── services/
│       ├── styles/
│       ├── utils/
│       └── app.py
│
├── download_assets.py
├── requirements.txt
├── init_db.py
├── .env
└── health_system.db
```

---

# 🧬 AI Models Used

| Model Type | Purpose |
|---|---|
| XGBoost | Disease Risk Prediction |
| LightGBM | Obesity Risk Prediction |
| Deep Learning Model | Hybrid Multi-risk Inference |
| Wellness Engine | Wellness Score Calculation |
| LLM Integration | AI Interpretation & Chat |

---

# 📊 Prediction Categories

The system analyzes:

- Diabetes Risk
- Heart Disease Risk
- Obesity Risk
- Lifestyle Wellness Risk
- Behavioral Health Indicators

---

# 🎨 Frontend Highlights

- Modern glassmorphism UI
- Premium healthcare dashboard
- Interactive analytics visualization
- AI processing animations
- Responsive layouts
- Dynamic Plotly charts
- Wellness gauge analytics

---

# 🔧 Tech Stack

## 🎨 Frontend

- Streamlit
- Plotly
- HTML/CSS
- Custom CSS Styling

---

## ⚙️ Backend

- FastAPI
- Uvicorn
- Pydantic
- Requests

---

## 🧬 AI & ML

- TensorFlow / Keras
- Scikit-learn
- XGBoost
- LightGBM
- NumPy
- Pandas

---

## 🗄️ Database

- SQLite
- SQLAlchemy

---

## 🤖 AI Integration

- OpenRouter API
- LLM-based interpretation system

---

# ⚙️ Environment Variables

Create a `.env` file inside the root directory and add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
SECRET_KEY=your_secret_key
```

---

# 📦 Downloading AI Assets

The trained AI models and dataset are not included in the GitHub repository due to file size limitations.

Before running the project, execute:

```bash
python download_assets.py
```

This script will automatically:

- Download Deep Learning models
- Download Machine Learning models
- Download preprocessing files
- Download dataset files
- Create required folders automatically

After downloading completes, the project can be run normally.

---

# ▶️ Running the Project

## 1️⃣ Clone Repository

```bash
git clone <your-repository-url>
cd HYBRID-HEALTH-RISK-SYSTEM
```

---

## 2️⃣ Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file and add:

```env
OPENROUTER_API_KEY=your_openrouter_api_key
SECRET_KEY=your_secret_key
```

---

## 5️⃣ Download AI Assets

```bash
python download_assets.py
```

---

## 6️⃣ Initialize Database

```bash
python init_db.py
```

---

## 7️⃣ Start Backend Server

```bash
uvicorn project.api.server:app --reload
```

Backend runs at:

```bash
http://127.0.0.1:8000
```

---

## 8️⃣ Start Frontend

Open another terminal and run:

```bash
streamlit run project/ui/app.py
```

Frontend runs at:

```bash
http://localhost:8501
```

---

# 📄 PDF Reporting

The system automatically generates:

- AI wellness reports
- Risk analytics reports
- Preventive healthcare summaries
- Downloadable PDF reports

---

# 🔐 Authentication Flow

- User Registration
- Secure Login
- Session Persistence
- Report Ownership Management
- Chat History Persistence

---

# 📈 Future Scope

Potential future improvements:

- JWT Authentication
- PostgreSQL Migration
- Cloud Deployment
- Wearable Device Integration
- Voice-based AI Assistant
- Multi-step Health Assessment Wizard
- Real-time Health Monitoring

---

# ⚠️ Disclaimer

This platform is developed for:

- Educational purposes
- AI research
- Preventive wellness awareness

It is NOT intended to replace professional medical diagnosis, treatment, or healthcare consultation.

Always consult qualified healthcare professionals for medical decisions.

---

# 👨‍💻 Author

## Subhankar Pandit

Final Year B.Tech Computer Science Student  
ITER, SOA University

- GitHub: github.com/SubhankarA8415
- LinkedIn: linkedin.com/in/subhankar-pandit-080449255

---

# ⭐ If You Like This Project

Consider giving the repository a ⭐ on GitHub.