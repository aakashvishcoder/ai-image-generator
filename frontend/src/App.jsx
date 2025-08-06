import { useState } from "react";
import axios from "axios";

function App() {
  const [prompt, setPrompt] = useState('');
  const [image, setImage] = useState('');

  const generate = async () => {
    try {
      const res = await axios.post('http://localhost:8000/generate', { prompt });
      if(res.data.url) {
        setImage(res.data.url);
      } else {
        console.error("Error from backend:", res.data.error);
      }
    } catch (error) {
      console.error("Error generating image:", error);
    }
  };

  return (
    <div className="p-8 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">Stable Diffusion Image Generator</h1>
      <input 
        value={prompt} 
        onChange={e => setPrompt(e.target.value)} 
        className="border p-2 w-full" 
        placeholder="Enter prompt..." 
      />
      <button 
        onClick={generate} 
        className="bg-blue-500 text-white px-4 py-2 mt-2"
      >
        Generate
      </button>
      {image && <img src={image} alt="Generated" className="mt-4 rounded shadow" />}
    </div>
  );
}

export default App;
