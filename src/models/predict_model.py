import joblib
import pandas as pd

# Load model
model = joblib.load("../../models/healthcare_model.pkl")

# Prediction function
def predict(data):
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return predictions
