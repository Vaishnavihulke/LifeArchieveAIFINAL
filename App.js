import React, { useState } from "react";
import "./App.css";

function App() {
  const [news, setNews] = useState("");
  const [result, setResult] = useState("");

  const checkNews = async () => {
    const response = await fetch("http://127.0.0.1:5000/check", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: news }),
    });

    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div className="container">
      <h1>🧠 TruthLens AI</h1>
      <p>Detect Fake News Instantly</p>

      <textarea
        placeholder="Paste news here..."
        value={news}
        onChange={(e) => setNews(e.target.value)}
      />

      <button onClick={checkNews}>Check News</button>

      {result && <h2>Result: {result}</h2>}
    </div>
  );
}

export default App;
