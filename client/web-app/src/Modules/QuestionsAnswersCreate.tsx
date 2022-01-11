import React, { SyntheticEvent, useState } from 'react';
import {useParams} from 'react-router-dom';

const QuestionsAnswersCreate: React.FC = () => {
    const questionId = useParams().id
    const question_to_answer = questionId
    const [detail, setDetail] = useState('');
    const answered_by = 1;

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        await fetch(`/api/answers/`,{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                detail,
                question_to_answer,
                answered_by
            })
        })
    }

    return (
        <div>
            <h2>Create new answer</h2>
            <form onSubmit={submit}>
                <div className="mb-3">
                    <textarea className="form-control" id="detail" name="detail"
                        onChange={e => setDetail(e.target.value)}
                    ></textarea>
                </div>
                <button className="btn btn-outline-secondary">Create new answer</button>
            </form>
        </div>
    );
};

export default QuestionsAnswersCreate;