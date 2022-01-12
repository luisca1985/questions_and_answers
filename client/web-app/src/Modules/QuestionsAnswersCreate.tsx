import React, { SyntheticEvent, useState } from 'react';
import { Navigate, useParams } from 'react-router-dom';

const QuestionsAnswersCreate: React.FC = () => {
    const questionId = useParams().id
    const question_to_answer = questionId
    const [detail, setDetail] = useState('');
    const answered_by = 1;
    const [redirect, setRedirect] = useState(false);

    // Provisional token
    const [token, setToken] = useState('')
    // Provisional token end

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        await fetch(`/api/answers/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify({
                detail,
                question_to_answer,
                answered_by
            })
        }).then(response => {
            if (response.status===201){
                console.log(response.status);
                setRedirect(true);
            }
        })
    }

    // useEffect(() => {
    //     effect
    //     return () => {
    //         <Navigate to={`/questions/${ questionId }/answers/`} />
    //     }
    // }, [input])
    
    if (redirect) {
        return <Navigate to={`/questions/${ questionId }/answers/`} />
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
            {/* Provisional token */}
            <div className="input-group mb-3">
                <div className="input-group-prepend">
                    <span className="input-group-text" id="basic-addon3">Authorization Token</span>
                </div>
                <input type="text" className="form-control" id="basic-url"
                    aria-describedby="basic-addon3" onChange={e => setToken(e.target.value)} />
            </div>
            {/* Provisional token end */}
        </div>
    );
};

export default QuestionsAnswersCreate;