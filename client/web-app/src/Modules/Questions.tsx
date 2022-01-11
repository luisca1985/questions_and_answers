import React from 'react';
import BriefInfoBlock from '../Components/BriefInfoBlock';
import {useState, useEffect} from 'react';
import { Question as IQuestion } from '../Interfaces/Questions';

const Questions = () => {
    const [questionList, setQuestions] = useState([])
    const url = '/api/questions'
    
    useEffect(()=>{
      fetch(url).then(response => {
        if(response.status === 200){
          return response.json()
        }
      }).then(data => setQuestions(data))
    })

    return (
      <>
        <div className="row">
          {
            questionList.map((question:IQuestion) =>
              <div className="col-md-6">
                <BriefInfoBlock  
                  key={question.id} 
                  tag="" 
                  title={question.title} 
                  date='Nov 12'
                  detail={ question.detail }
                  url={ `/questions/${ question.id }/answers` }/>
              </div>
            )
          }
        </div>
      </>
    );
};

export default Questions;