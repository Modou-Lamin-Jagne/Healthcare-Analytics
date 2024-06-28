import React, { useState } from 'react';
import api from '../Services/api';

const PredictionForm = ({ setPrediction }) => {
  const [formData, setFormData] = useState({ age: '', bmi: '', blood_pressure: '' });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    api.getPrediction(formData).then(response => {
      setPrediction(response.data.prediction);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Age:
        <input type="number" name="age" value={formData.age} onChange={handleChange} />
      </label>
      <br />
      <label>
        BMI:
        <input type="number" name="bmi" value={formData.bmi} onChange={handleChange} />
      </label>
      <br />
      <label>
        Blood Pressure:
        <input type="number" name="blood_pressure" value={formData.blood_pressure} onChange={handleChange} />
      </label>
      <br />
      <button type="submit">Get Prediction</button>
    </form>
  );
};

export default PredictionForm;
