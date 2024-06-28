from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load('../../models/healthcare_model.pkl')

@app.route('/data', methods=['GET'])
def get_data():
    data = pd.read_csv("../../data/cleaned/cleaned_healthcare_data.csv")
    data_dict = data.to_dict(orient='records')
    return jsonify(data_dict)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)
    predictions = model.predict(df)
    return jsonify(predictions.tolist())

if __name__ == '__main__':
    app.run(debug=True)
