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


  const [file, setFile] = useState()

  function handleFileChange(event) {
    console.log(event.target.files[0])
    setFile(event.target.files[0])
  }
  
  async function handleFileSubmit(event) {
    event.preventDefault()
    const url = 'http://localhost:8000/upload';
    const formData = new FormData();
    formData.append('file', file);
    const config = {
      headers: {
        'content-type': 'multipart/form-data',
      },
    };
    console.log(url, formData, config)
    try{
      const data = await axios.post(url, formData, config);
      
    }catch(err){
       
    }
   
    
    
  }

  return (
    <>

      <div className="heading">
        <h1>Semantic Search On Personalized Data</h1>
      </div>

      
      <div className="upload-top">
          <div className="upload-heading">
            Upload the pdf here
          </div>
          <div className='file-upload'>
            <input type="file" onChange={handleFileChange}/>
            <button onClick={handleFileSubmit}>Upload</button>
          </div>
      </div>

      <div className="search-box">
        <input type="text" placeholder="Enter the Query" onChange={handleChange} />
        <button onClick={getData}>Search</button>
      </div>

      <div className="content-box">
        {data.length != 0  ? (
          data.map((item, index) =>  (
            <div>
            <div className="file-name">
                {item.id} 
            </div>
            <div className="file-score">
              {item.score}
            </div>i

            </div>
          ))) : ( 
          <p>No data to display.</p>
        )}
      </div>
    </>
  );
}

export default App;
