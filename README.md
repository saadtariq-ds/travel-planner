# ✈️ AI Travel Planner

AI Travel Planner is a **Generative AI–powered travel planning application** that helps users generate personalized travel itineraries based on preferences such as destination, duration, budget, and interests.

The application leverages **Groq LLM** with **LangChain** for intelligent planning, a **Streamlit frontend** for user interaction, and is deployed as a **containerized, Kubernetes-based system** on a GCP VM. It also integrates a complete **ELK (Elasticsearch, Logstash, Kibana) stack** for centralized logging and monitoring.

---

## 🚀 Features

- 🧠 AI-powered travel itinerary generation using Groq LLM
- 🔗 Prompt orchestration with LangChain
- 🎨 Interactive Streamlit-based frontend
- 🐳 Dockerized application
- ☸️ Kubernetes deployment using Minikube
- ☁️ Hosted on Google Cloud VM
- 📜 Centralized logging with Filebeat + Logstash
- 🔍 Searchable logs in Elasticsearch
- 📊 Visual dashboards with Kibana

---

## 🧱 High-Level Architecture

1. User enters travel preferences in Streamlit UI  
2. Streamlit sends request to backend logic  
3. LangChain structures prompts and calls Groq LLM  
4. LLM generates a customized travel plan  
5. App runs inside Docker containers on Minikube (Kubernetes)  
6. Application and Kubernetes logs are collected by Filebeat  
7. Logstash processes and enriches logs  
8. Logs are stored in Elasticsearch  
9. Kibana visualizes logs and system insights  

---

## 🛠️ Tech Stack

| Category | Tools |
|--------|------|
| LLM | Groq |
| GenAI Framework | LangChain |
| Frontend | Streamlit |
| Containerization | Docker |
| Orchestration | Kubernetes (Minikube) |
| CLI | kubectl |
| Cloud | GCP VM |
| Logging | Filebeat |
| Log Processing | Logstash |
| Log Storage | Elasticsearch |
| Visualization | Kibana |

---

# ⚙️ Setup & Run Locally
## 1️⃣ Clone
```bash
git clone https://github.com/saadtariq-ds/travel-planner.git
cd travel-planner
```

## 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

## 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
pip install -e .
```

## 4️⃣ Run streamlit app
```bash
streamlit run app.py
```