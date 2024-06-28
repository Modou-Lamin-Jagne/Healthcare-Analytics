import React, { useState, useEffect } from 'react';
import api from '../Services/api';

const DataFetcher = () => {
  const [data, setData] = useState(null);

  useEffect(() => {
    api.getData().then(response => {
      setData(response.data);
    });
  }, []);

  if (!data) return <div>Loading...</div>;

  return (
    <div>
      <h2>Data</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default DataFetcher;
