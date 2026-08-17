import React, { useState } from "react";

function App() {
  const [temperature, setTemperature] = useState("");
  const [vibration, setVibration] = useState("");
  const [prediction, setPrediction] = useState("");
  const [loading, setLoading] = useState(false);

  const handlePredict = async () => {
    if (temperature === "" || vibration === "") {
      alert("Please enter temperature and vibration");
      return;
    }

    setLoading(true);
    setPrediction("");

    try {
      const response = await fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          temperature: Number(temperature),
          vibration: Number(vibration),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.error || "Prediction failed");
      }

      setPrediction(data.prediction);
    } catch (error) {
      console.error(error);
      setPrediction("Error: Could not get prediction");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Predictive Maintenance</h1>

      <label>Temperature:</label>
      <input
        type="number"
        value={temperature}
        onChange={(e) => setTemperature(e.target.value)}
        placeholder="Enter temperature"
      />

      <br />
      <br />

      <label>Vibration:</label>
      <input
        type="number"
        value={vibration}
        onChange={(e) => setVibration(e.target.value)}
        placeholder="Enter vibration"
      />

      <br />
      <br />

      <button onClick={handlePredict} disabled={loading}>
        {loading ? "Predicting..." : "Predict"}
      </button>

      {prediction && (
        <h2>
          Prediction: {prediction}
        </h2>
      )}
    </div>
  );
}

export default App;