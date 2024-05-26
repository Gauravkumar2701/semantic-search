import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import axios from "axios";

function App() {
  const [data, setData] = useState([]);
  const [inputValue, setInputValue] = useState("");

  async function getData() {
    const data = await axios.get(`http://localhost:8000/search?q=${inputValue}`);
    console.log("dfsdf");
    console.log(data.data);
    setData(data.data);
  }

  const handleChange = (event) => {
    setInputValue(event.target.value);
    console.log(event.target.value);
  };

  return (
    <>
      <div className="heading">
        <h1>Semantic Search On Personalized Data</h1>
      </div>

      <div className="search-box">
        <input type="text" placeholder="Enter the Query" onChange={handleChange} />
        <button onClick={getData}>Search</button>
      </div>

      <div className="answer-list">
        {data ? (
          data.map((item, index) => <div key={index}>{item.id}</div>)
        ) : (
          <p>No data to display.</p>
        )}
      </div>
    </>
  );
}

export default App;
