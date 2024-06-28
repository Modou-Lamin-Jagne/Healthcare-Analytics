import React, { useState } from 'react';
import DataFetcher from './components/DataFetcher';
import PredictionForm from './components/PredictionForm';
import PredictionResult from './components/PredictionResult';
import './App.css';

const App = () => {
  const [prediction, setPrediction] = useState(null);

  return (
    <div className="App">
      <h1>Healthcare Analytics System</h1>
      <DataFetcher />
      <PredictionForm setPrediction={setPrediction} />
      <PredictionResult prediction={prediction} />
    </div>
  );
};

export default App;
