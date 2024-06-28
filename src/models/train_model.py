import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Load data
data = pd.read_csv("../../data/cleaned/cleaned_healthcare_data.csv")

# Feature engineering
X = data[['age', 'bmi', 'blood_pressure']]
y = data['disease']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "../../models/healthcare_model.pkl")
