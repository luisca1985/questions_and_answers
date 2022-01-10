import React, { PropsWithRef } from 'react';
import {useParams} from 'react-router-dom';

const QuestionsAnswers: React.FC = () => {
    const questionId = useParams().id
    const url = `/api/questions/${ questionId }/answers`
    return (
        <div>
            Pregunta: { questionId}
        </div>
    );
};

export default QuestionsAnswers;