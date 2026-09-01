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

**AI Health Companion** is a **Hybrid AI-Powered Preventive Healthcare & Wellness Intelligence System** that combines **Machine Learning**, **Deep Learning**, **Large Language Models (LLMs)**, and **Full-Stack Web Development** to deliver intelligent disease risk prediction, personalized wellness analytics, AI-assisted health interpretation, and preventive healthcare recommendations.

Designed with a modular full-stack architecture, the platform transforms lifestyle and behavioral health indicators into meaningful health insights through an end-to-end hybrid AI pipeline. It integrates predictive analytics, interactive visualizations, conversational AI, and automated reporting into a unified healthcare intelligence platform.

---

# 🎬 Project Videos

This repository includes two complementary project walkthroughs designed for different audiences.

## 🌐 Public Project Showcase

The public showcase presents a concise overview of the complete project, covering:

- Problem Statement
- Solution Overview
- System Architecture
- Hybrid AI Pipeline
- Technology Stack
- Core Features
- Results & Performance
- Future Scope

### ▶ Watch the Project Showcase

**YouTube:**  
https://youtu.be/k3Olp_ZIYmk?si=32OMqzRVaXd_MMmP

---

## 🔒 Complete Project Demonstration

A comprehensive implementation walkthrough is also available for professional evaluation purposes.

The demonstration includes:

- Complete Working Prototype
- Source Code Walkthrough
- Project Architecture
- Backend & Frontend Workflow
- AI Pipeline Implementation
- Model Integration
- Database Design
- Feature Demonstration
- Technical Design Decisions
- End-to-End Project Execution

To protect the project's implementation while supporting genuine technical evaluations, this demonstration is kept **unlisted**.

It can be shared upon request for:

- Recruiters
- Hiring Managers
- Technical Interviewers
- Internship & Placement Evaluations
- Academic Reviews
- Research Discussions
- Project Collaborations
- Professional Technical Assessments

---

# 📂 Project Resources

| Resource | Description |
|----------|-------------|
| 🎥 Public Project Showcase | Presentation-based overview of the complete project |
| 📄 Project Presentation | Complete project presentation (available in the `docs` directory) |
| 🏗️ Architecture Documentation | Detailed explanation of the complete system architecture (available in the `docs` directory)|
| 📚 Technical Documentation | Additional implementation and development documentation (available in the `docs` directory)|

---

# 🚀 Key Features

## 🧠 Hybrid AI Prediction Engine

- Hybrid Machine Learning and Deep Learning inference
- Multi-disease risk prediction
- Intelligent risk aggregation
- Confidence-based probability calibration
- Personalized health risk assessment

---

## 📊 Interactive Healthcare Dashboard

- Modern healthcare analytics dashboard
- Interactive Plotly visualizations
- Disease probability charts
- Wellness score analytics
- Personalized health insights
- Responsive user interface

---

## 🌿 Wellness Intelligence

- Lifestyle assessment
- Behavioral health analysis
- Wellness score generation
- Preventive healthcare recommendations
- Personalized wellness insights

---

## 🤖 AI Healthcare Assistant

- LLM-powered conversational assistant
- AI-generated health interpretation
- Personalized healthcare guidance
- Natural language interaction
- Intelligent report explanation

---

## 📄 Smart PDF Reporting

- AI-generated healthcare reports
- Downloadable PDF reports
- Disease risk summaries
- Wellness analytics
- Preventive healthcare recommendations
- Professional report formatting

---

## 🔐 Authentication & User Management

- Secure user authentication
- Password hashing
- Session management
- User profile management
- Protected healthcare records

---

## 📜 Report & Chat History

- Persistent report history
- Download previous reports
- Delete saved reports
- Chat history management
- User-specific healthcare analytics

---

# 🏗️ High-level System Architecture

AI Health Companion follows a modular, scalable, and production-oriented full-stack architecture. Each layer is designed to operate independently while contributing to a unified healthcare intelligence platform.

The system consists of the following major components:

| Layer | Description |
|--------|-------------|
| 🎨 Frontend | Interactive Streamlit-based user interface for assessments, dashboards, reports, and AI chat. |
| ⚙️ Backend | FastAPI-powered REST API responsible for authentication, prediction, report generation, and business logic. |
| 🧠 AI Engine | Hybrid Machine Learning + Deep Learning inference pipeline for disease risk prediction and wellness analytics. |
| 🤖 LLM Layer | OpenRouter-powered Large Language Model for conversational assistance and AI-generated health interpretation. |
| 🗄️ Database | SQLite database used for user accounts, report history, authentication, and chat persistence. |

For detailed architecture diagrams and technical explanations, refer to:

📄 **`docs/Architecture.md`**

---

# 🧠 Hybrid AI Pipeline

The core intelligence of AI Health Companion is built upon a **Hybrid AI Pipeline** that combines classical Machine Learning models with Deep Learning to generate more reliable healthcare predictions.

```text
                 User Health Assessment
                          │
                          ▼
                Data Preprocessing
                          │
                          ▼
                Feature Engineering
                          │
          ┌───────────────┴───────────────┐
          ▼                               ▼
Machine Learning Models         Deep Learning Model
(XGBoost & LightGBM)            (TensorFlow / Keras)
          │                               │
          └───────────────┬───────────────┘
                          ▼
               Hybrid Risk Aggregation
                          │
                          ▼
              Wellness Intelligence Engine
                          │
                          ▼
            LLM Health Interpretation Layer
                          │
                          ▼
          Interactive Dashboard & PDF Report
```

The hybrid approach combines the interpretability of traditional Machine Learning with the feature learning capability of Deep Learning, producing more robust and personalized healthcare insights.

---

# 📊 Prediction Categories

The platform currently predicts and analyzes the following healthcare indicators:

- 🩸 Diabetes Risk
- ❤️ Heart Disease Risk
- ⚖️ Obesity Risk
- 🌿 Lifestyle Wellness Score
- 📈 Behavioral Health Indicators

Each prediction includes probability estimation, confidence calibration, AI interpretation, and preventive healthcare recommendations.

---

# 💻 Technology Stack

## 🎨 Frontend

- Streamlit
- Plotly
- HTML5
- CSS3
- Custom UI Components

---

## ⚙️ Backend

- FastAPI
- Uvicorn
- Pydantic
- Requests

---

## 🧠 Artificial Intelligence & Machine Learning

- TensorFlow / Keras
- Scikit-learn
- XGBoost
- LightGBM
- NumPy
- Pandas

---

## 🤖 Large Language Model

- OpenRouter API
- AI-powered Health Interpretation
- Conversational Healthcare Assistant

---

## 🗄️ Database

- SQLite
- SQLAlchemy ORM

---

# 📂 Project Structure

```text
Hybrid-Health-Risk-System/
│
├── project/
│   │
│   ├── api/
│   │   ├── services/
│   │   ├── auth_routes.py
│   │   ├── chat_routes.py
│   │   ├── prediction_routes.py
│   │   ├── report_routes.py
│   │   ├── schemas.py
│   │   └── server.py
│   │
│   │
│   ├── config/
│   │   └── config.py
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
├── docs/
│   ├── AI-Health-Companion-1.0-Presentation.pdf
│   ├── Architecture.md
│
├── download_assets.py
├── init_db.py
├── requirements.txt
└── README.md
```

# 📚 Documentation

Additional documentation is available in the `docs/` directory.

- 📄 Project Presentation
- 🏗️ System Architecture
- 📚 Technical Documentation
- 🚀 Deployment Guide *(Planned)*

---

# 📈 Future Scope

Potential future enhancements include:

- JWT-based Authentication
- PostgreSQL Database Migration
- Docker Containerization
- Cloud Deployment
- CI/CD Pipeline Integration
- Wearable Device Integration
- Voice-based AI Health Assistant
- Multi-step Health Assessment Wizard
- Real-time Health Monitoring
- Mobile Application Support

---

# ⚠️ Disclaimer

AI Health Companion is developed for **educational**, **research**, and **preventive healthcare awareness** purposes.

The predictions and recommendations generated by this platform are intended to assist users in understanding potential health risks and wellness indicators. They should **not** be considered a substitute for professional medical advice, diagnosis, or treatment.

Always consult qualified healthcare professionals before making medical decisions.

---

# 👨‍💻 Developers & Contributors

## **Subhankar Pandit**

**Computer Science Engineer | Full Stack Developer | AI & Machine Learning Enthusiast**

Passionate about building scalable full-stack applications, intelligent AI systems, and real-world software solutions that combine modern engineering practices with practical problem-solving.

### Contributions

- Full-stack application architecture and development
- Backend API development and integration
- Hybrid AI prediction pipeline
- Machine Learning and Deep Learning model integration
- LLM integration and healthcare interpretation
- Authentication, report management, and database implementation
- Interactive dashboard and frontend development
- End-to-end system integration

### 🔗 Connect With Subhankar

- 🌐 **Portfolio:** https://portfolio-subhankar-pandits-projects.vercel.app/
- 💼 **LinkedIn:** https://linkedin.com/in/subhankar-pandit-080449255
- 💻 **GitHub:** https://github.com/SubhankarA8415
- 🎥 **YouTube:** https://youtube.com/@subhankardevlab
- 📧 **Email:** subhankar.pandit2002@gmail.com

---

## **Siba Prasad Mishra**

**Data Science | Machine Learning | AI Systems**

Passionate about Data Science, ML & AI systems, and real-world software solutions that combine modern engineering practices with practical problem-solving.

### Contributions

- Data analytics and exploratory analysis
- Dataset preparation and preprocessing
- Machine Learning baseline modelling
- Model evaluation and comparative analysis
- Supporting data-driven insights for the prediction pipeline

### 🔗 Connect With Siba

- 💼 **LinkedIn:** https://www.linkedin.com/in/siba-mishra-078b6020a/
- 💻 **GitHub:** https://github.com/SibaMishra200
- 📧 **Email:** sibamishra200@gmail.com

---

# 🤝 Contributing

Contributions, suggestions, feature requests, and feedback are always welcome.

If you'd like to improve this project, feel free to fork the repository, open an issue, or submit a pull request.

---

# ⭐ Support

If you found this project helpful or interesting, consider giving it a **⭐ Star** on GitHub.

Your support helps increase the visibility of the project and motivates the development of future open-source AI and Full Stack projects.

---

<p align="center">

### 🚀 Building Intelligent Software for Real-World Impact

**Designed & Developed by Subhankar Pandit and Siba Prasad Mishra**

</p>
