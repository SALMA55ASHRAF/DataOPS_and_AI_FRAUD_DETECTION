import pandas as pd
import numpy as np

# Generate fake transaction data
np.random.seed(42)
data = pd.DataFrame({
    'transaction_id': np.arange(1, 1001),
    'user_id': np.random.randint(1000, 2000, 1000),
    'transaction_amount': np.random.uniform(10, 5000, 1000),
    'transaction_time': pd.date_range(start='2025-01-01', periods=1000, freq='H'),
    'is_fraud': np.random.choice([0, 1], size=1000, p=[0.95, 0.05])
})

# Save to CSV and Excel
data.to_csv(r"D:\Videos\AItronix\Dataops_project\AI_AND_DATAOPS\synthetic_transactions.csv", index=False)
data.to_excel(r"D:\Videos\AItronix\Dataops_project\AI_AND_DATAOPS\synthetic_transactions.xlsx", index=False)

print("Synthetic Data Generated")
