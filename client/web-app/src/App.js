import './App.css';
import {useState, useEffect} from 'react';
import { Channel } from './Components/Channel';

function App() {

  const [initialState, setState] = useState([])

  // const url = '/api/answers/1'
  const url = '/api'

  useEffect(()=>{
    fetch(url).then(response => {
      if(response.status === 200){
        console.log(response)
        return response.json()
      }
    }).then(data => setState(data))
  })

  return (
    <div className="App">
      <Channel data={initialState}/>
    </div>
  );
}

export default App;
