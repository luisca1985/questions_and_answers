import React, { SyntheticEvent, useState } from 'react';
import { Navigate } from 'react-router-dom';

const QuestionsCreate = () => {
    const [title, setTitle] = useState('');
    const [detail, setDetail] = useState('');
    const asked_by = 1;
    const [redirect,setRedirect] = useState(false);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        await fetch('/api/questions',{
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                detail,
                asked_by
            })
        })
        setRedirect(true)
    }

    if(redirect){
        return <Navigate to={'/questions'}/>
    }

    return (
        <div>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label htmlFor="title" className="form-label">Title</label>
                    <input type="text" className="form-control" id="title" name="title"
                        onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="mb-3">
                    <label htmlFor="detail" className="form-label">Detail</label>
                    <textarea className="form-control" id="detail" name="detail"
                        onChange={e => setDetail(e.target.value)}
                    ></textarea>
                </div>
                <button className="btn btn-outline-secondary">Save</button>
            </form>
        </div>
    );
};

export default QuestionsCreate;