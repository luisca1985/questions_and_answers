import React, { useState, useEffect } from 'react';
import { Route, Routes, useParams } from 'react-router-dom';
import { Question as IQuestion } from '../Interfaces/Questions';
import { Answer as IAnswer } from '../Interfaces/Answers';
import moment from 'moment';
import QuestionsAnswersCreate from './QuestionsAnswersCreate';


const QuestionsAnswers: React.FC = () => {
  const questionId = useParams().id

  const questionUrlAPI = `/api/questions/${questionId}/`
  const [questionTitle, setQuestionTitle] = useState('');
  const [questionDetail, setQuestionDetail] = useState('');
  const [questionCreated, setQuestionCreated] = useState('');

  useEffect(() => {
    fetch(questionUrlAPI).then((response) => {
      if (response.status === 200) {
        return response.json()
      }
    }).then((data) => {
      setQuestionTitle(data.title);
      setQuestionDetail(data.detail);
      setQuestionCreated(moment(data.created).format('MMMM D, YYYY'));
    }
    )
  }, [])

  const answersUrlAPI = `/api/questions/${questionId}/answers/`
  const [answerList, setAnswers] = useState([]);
  useEffect(() => {
    fetch(answersUrlAPI).then(response => {
      if (response.status === 200) {
        return response.json()
      }
    }).then(data => setAnswers(data))
  }, [])

  return (
    <>
      <div className="row g-5">
        <div className="col-md-8">
          <h3 className="pb-4 mb-4 fst-italic border-bottom">

          </h3>
          <article className="blog-post">
            <h2 className="blog-post-title">{questionTitle}</h2>
            <p className="blog-post-meta">{questionCreated} by <a href="#">Mark</a></p>

            <p>{questionDetail}</p>
            <h2>Answers:</h2>
            {
              answerList.map((answer: IAnswer) =>
                <>
                  <hr />
                  <p className="blog-post-meta">{moment(answer.created).format('MMMM D, YYYY')} by <a href="#">Mark</a></p>
                  <p>{answer.detail}</p>
                </>
              )
            }
          </article>

        </div>
      </div>
      <Routes>
        <Route path='/' element={<QuestionsAnswersCreate />} />
      </Routes>
    </>
  );
};

export default QuestionsAnswers;