import React, {FC, InputHTMLAttributes} from 'react';

interface BriefInfoBlockProps extends InputHTMLAttributes<HTMLInputElement>{
    tag: string;
    title: string;
    date: string;
    detail: string;
}

const BriefInfoBlock:FC<BriefInfoBlockProps> = ({tag,title,date,detail}) => {
    return (
        <div className="row g-0 border rounded overflow-hidden flex-md-row mb-4 shadow-sm h-md-250 position-relative">
            <div className="col p-4 d-flex flex-column position-static">
                <strong className="d-inline-block mb-2 text-primary">{tag}</strong>
                <h3 className="mb-0">{title}</h3>
                <div className="mb-1 text-muted">{date}</div>
                <p className="card-text mb-auto">{ detail }</p>
                <a href="#" className="stretched-link">Know the answers...</a>
            </div>
        </div>
    );
};

export default BriefInfoBlock;