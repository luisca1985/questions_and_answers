import './App.css';
import {useState, useEffect} from 'react';
import { Question } from './Components/Question';

function App() {

  const [initialState, setState] = useState([])

  const url = '/api/questions'

  useEffect(()=>{
    fetch(url).then(response => {
      if(response.status === 200){
        return response.json()
      }
    }).then(data => setState(data))
  })

  const questionList = initialState
  const questions = questionList.map((question) =>
    <Question data={question}/>
  );

  return (
    <div>
      {questions}
    </div>
  );
}

export default App;
