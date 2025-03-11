import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 

class FraudDashboard:
    """Handles fraud analytics dashboard visualization."""
    
    def __init__(self, df):
        self.df = df

    def display_dashboard(self):
        st.title("📊 Fraud Analytics Dashboard")

        st.subheader("📌 Transaction Data")
        st.write(self.df.head())

        # Fraud Count
        fraud_count = self.df['is_fraud'].sum()
        total_transactions = len(self.df)

        st.metric("🔍 Total Transactions", total_transactions)
        st.metric("⚠️ Fraud Cases Detected", fraud_count)

        # Fraud vs. Legitimate Transactions
        st.subheader("📈 Fraud vs. Legitimate Transactions")
        fig, ax = plt.subplots()
        ax.bar(["Legit", "Fraud"], self.df['is_fraud'].value_counts(), color=['green', 'red'])
        st.pyplot(fig)

# Example Usage:
df_features = pd.read_csv(r"D:\Videos\AItronix\Dataops_project\AI_AND_DATAOPS\df_features.csv")

dashboard = FraudDashboard(df_features)
dashboard.display_dashboard()
