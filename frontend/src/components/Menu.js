import React from 'react'
import {Link} from "react-router-dom";

const MenuItem = ({link}) => {
    return (
        <li>
            <Link className="nav-link" to={link.url}>{link.name}</Link>
        </li>
    )
}

const MenuList = ({links}) => {
    return (
        <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
            <a className="navbar-brand" href="/">GeekBrains</a>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
                    aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <div className="collapse navbar-collapse" id="navbarCollapse">
                <ul className="navbar-nav mr-auto col-9">
                    {links.map((link) => <MenuItem key={link.id} link={link}/>)}
                </ul>
                <form className="navbar-nav justify-content-end col-3">
                    <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search" />
                    <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Поиск</button>
                </form>
            </div>
        </nav>
    )
}

export default MenuList