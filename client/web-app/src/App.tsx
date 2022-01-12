import React from 'react';
import './App.css';
import Nav from './Components/Nav';
import Header from './Components/Header';
import Display from './Components/Display';
import Questions from './Modules/Questions';
import {BrowserRouter, Routes, Route, Outlet} from "react-router-dom"
import QuestionsCreate from './Modules/QuestionsCreate';
import QuestionsAnswers from './Modules/QuestionsAnswers';
import QuestionsAnswersCreate from './Modules/QuestionsAnswersCreate';
import Home from './Modules/Home';

function App() {
  return (
    <div className="App">
      {/* view-source:https://getbootstrap.com/docs/5.1/examples/blog/ */}
      <BrowserRouter>
      <div className="container">
        <Header title="Questions and Answers"/>
        <Nav/>
      </div>
      <main className="container">
        {/* <Display/> */}
          <Routes>
            <Route path='/' element={ <Home /> }/>
            <Route path='/questions' element= { <Questions />} />
            <Route path='/questions/create' element= { <QuestionsCreate />} />
            <Route path='/questions/:id/answers' element= { <QuestionsAnswers />} />
          </Routes>
      </main>
    
    </BrowserRouter>
    </div>
  );
}

export default App;
