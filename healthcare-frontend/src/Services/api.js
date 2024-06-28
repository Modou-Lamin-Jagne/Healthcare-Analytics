import axios from 'axios';

const api = axios.create({
  baseURL: process.env.REACT_APP_API_URL || 'http://127.0.0.1:5000',
});

const getData = () => api.get('/data');
const getPrediction = (data) => api.post('/predict', data);

const apiService = {
  getData,
  getPrediction,
};

export default apiService;
