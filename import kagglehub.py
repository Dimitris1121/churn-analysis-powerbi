import kagglehub
import pandas as pd
import os


# ── 1. Download dataset from Kaggle ──────────────────────────────────────────
path = kagglehub.dataset_download("blastchar/telco-customer-churn")

# List files in the downloaded directory to confirm contents
files = os.listdir(path)
print(files)


# ── 2. Load the CSV into a DataFrame ─────────────────────────────────────────
csv_path = os.path.join(path, "WA_Fn-UseC_-Telco-Customer-Churn.csv")

df = pd.read_csv(csv_path)

# Display settings: show all columns without truncation
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# ── 3. Drop irrelevant demographic columns ────────────────────────────────────
df = df.drop(columns=["gender", "SeniorCitizen", "Partner", "Dependents"])


# ── 4. Initial exploration ────────────────────────────────────────────────────
print(df.head())       # First 5 rows
print(df.info())       # Column types and null counts
print(df.describe())   # Summary statistics for numeric columns
print(df["Churn"].value_counts())  # Class distribution of target variable


# ── 5. Fix TotalCharges column ────────────────────────────────────────────────
# Convert to numeric (some entries are blank strings — coerce turns them to NaN)
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
# Fill NaN values with 0 (customers with 0 tenure had no charges yet)
df['TotalCharges'].fillna(0, inplace=True)


# ── 6. Export cleaned DataFrame to CSV ───────────────────────────────────────
df.to_csv(r"C:\Users\mypc\Desktop\telco_churn_cleaned.csv", index=False)
