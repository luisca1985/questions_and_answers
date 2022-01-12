import React from 'react';
import BriefInfoBlock from '../Components/BriefInfoBlock';
import { useState, useEffect } from 'react';
import { Question as IQuestion } from '../Interfaces/Questions';

const Questions = () => {
  const [questionList, setQuestions] = useState([])
  const [search, setSearch] = useState('')

  useEffect(() => {
    getQuestions()
  }, [search])

  const getQuestions = async () => {
    const url = `/api/questions/?search=${search}`
    fetch(url).then(response => {
      if (response.status === 200) {
        return response.json()
      }
    }).then(data => setQuestions(data))

  }

  return (
    <>
      <div className="input-group rounded col-md-6">
        <input type="search" className="form-control rounded" placeholder="Search" aria-label="Search"
          aria-describedby="search-addon" onChange={e => setSearch(e.target.value)} />
        <span className="input-group-text border-0" id="search-addon">
          <a className="link-secondary" href="#" aria-label="Search">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" 
            fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" 
            stroke-width="2" className="mx-3" role="img" viewBox="0 0 24 24"><title>Search</title>
            <circle cx="10.5" cy="10.5" r="7.5" /><path d="M21 21l-5.2-5.2" /></svg>
          </a>
        </span>
      </div>
      <hr></hr>

      <div className="row">
        {
          questionList.map((question: IQuestion) =>
            <div className="col-md-6">
              <BriefInfoBlock
                key={question.id}
                tag=""
                title={question.title}
                date='Nov 12'
                detail={question.detail}
                url={`/questions/${question.id}/answers`} />
            </div>
          )
        }
      </div>
    </>
  );
};

export default Questions;