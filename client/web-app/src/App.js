import './App.css';
import {useState, useEffect} from 'react';
import { Question } from './Components/Question';

function App() {

  const [initialState, setState] = useState([])

  const url = '/api/questions/1'

  useEffect(()=>{
    fetch(url).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
  })

  return (
    <div className="App">
      <Question data={initialState}/>
    </div>
  );
}

export default App;
