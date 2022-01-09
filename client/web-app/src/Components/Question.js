import React from 'react';

export const Question = ({data}) => {
    return (
        <div>
            <h2>{ data.title }</h2>
            <p> <b>Question:</b> { data.detail }</p>
        </div>
    );
};