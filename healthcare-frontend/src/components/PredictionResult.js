import React from 'react';

const PredictionResult = ({ prediction }) => {
  if (!prediction) return null;

  return (
    <div>
      <h2>Prediction Result</h2>
      <p>{prediction}</p>
    </div>
  );
};

export default PredictionResult;
