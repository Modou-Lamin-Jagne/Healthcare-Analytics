import pandas as pd

# Load data
data = pd.read_csv("../../data/raw/healthcare_data.csv")

# Data cleaning
data.dropna(inplace=True)
data['age'] = data['age'].astype(int)
data['bmi'] = data['bmi'].astype(float)

# Save cleaned data
data.to_csv("../../data/cleaned/cleaned_healthcare_data.csv", index=False)
