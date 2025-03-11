# Fraud Detection System 🚀

## **Project Overview**
This project is an **AI-powered Fraud Detection System** that integrates **DataOps principles** with **Machine Learning** to detect fraudulent transactions. The system collects data from multiple sources (CSV, Excel, SQL Server), processes it, trains an AI model, and provides insights via a **Streamlit dashboard**.

---

## **🔹 Key Features**
- **Data Ingestion** from CSV, Excel, and SQL Server.
- **Data Cleaning & Transformation** using Pandas and PySpark.
- **Fraud Detection Model** trained using XGBoost.
- **API for Predictions** built with FastAPI.
- **Real-Time Fraud Dashboard** using Streamlit.
- **Logging & Error Handling** following SOLID principles.

---

## **📂 Project Structure**
```
📁 AI_AND_DATAOPS/
│── 📂 data/                 # Raw and processed data
│── 📂 models/               # Trained ML models
│── 📂 scripts/              # Data processing scripts
│── fraud_detection.py       # AI model training script
│── fraud_dashboard.py       # Streamlit dashboard
│── api.py                   # FastAPI implementation
│── requirements.txt         # Python dependencies
│── README.md                # Project documentation
```

---

## **🔧 Installation & Setup**
1️⃣ **Clone the Repository:**
```bash
git clone https://github.com/SALMA55ASHRAF/DataOPS_and_AI_FRAUD_DETECTION.git
cd DataOPS_and_AI_FRAUD_DETECTION
```

2️⃣ **Install Dependencies:**
```bash
pip install -r requirements.txt
```

3️⃣ **Run the API Server:**
```bash
uvicorn api:app --reload
```

4️⃣ **Launch the Dashboard:**
```bash
streamlit run fraud_dashboard.py
```

---

## **📊 Streamlit Dashboard**
The dashboard visualizes:
- Fraudulent vs. Non-Fraudulent Transactions
- Transaction Amount Trends
- AI Model Predictions

**To access it, open:**  
🔗 `http://localhost:8501`

---

## **🚀 Next Steps**
- 🔹 Integrate **Grafana for real-time fraud alerts**.
- 🔹 Optimize model with **Deep Learning**.
- 🔹 Implement CI/CD using **GitHub Actions**.

---

🎯 **Contributors:** [Your Name]  
📌 **GitHub Repo:** [GitHub Link](https://github.com/SALMA55ASHRAF/DataOPS_and_AI_FRAUD_DETECTION)

🚀 **Happy Coding!** 🎯

