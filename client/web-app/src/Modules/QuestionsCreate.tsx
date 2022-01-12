import React, { SyntheticEvent, useState } from 'react';
import { Navigate } from 'react-router-dom';

const QuestionsCreate = () => {
    const [title, setTitle] = useState('');
    const [detail, setDetail] = useState('');
    const asked_by = 1;
    const [redirect, setRedirect] = useState(false);

    // Provisional token
    const [token, setToken] = useState('')
    // Provisional token end
    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();
        await fetch('/api/questions/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Token ${token}`
            },
            body: JSON.stringify({
                title,
                detail,
                asked_by
            })
        })
        setRedirect(true)
    }

    if (redirect) {
        return <Navigate to={'/questions/'} />
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
            <hr />
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

export default QuestionsCreate;