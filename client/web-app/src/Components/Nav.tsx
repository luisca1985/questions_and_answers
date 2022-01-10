import React from 'react';
import { Link } from 'react-router-dom';



const Nav = () => {
    const options = [{value:"Home", url:"/"},{value:"Show questions", url:"/questions"},{value:"Create question", url:"/questions/create"}]
    return (
        <div className="nav-scroller py-1 mb-2">
            <nav className="nav d-flex justify-content-between">
                {
                options.map((option, index)=>
                    <Link key={index} to={option.url} className="p-2 link-secondary">{option.value}</Link>
                )
                }
            </nav>
        </div>
    );
};

export default Nav;