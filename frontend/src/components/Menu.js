import React from 'react'
import {Link} from "react-router-dom";

const MenuItem = ({link}) => {
    return (
        <li>
            <Link className="nav-link" to={link.url}>{link.name}</Link>
        </li>
    )
}

class MenuList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {text: ''}
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }

    handleSubmit(event) {
        this.props.filterProject(this.state.text)
        event.preventDefault()
    }

    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-dark bg-dark">
                <a className="navbar-brand" href="/">GeekBrains</a>
                <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse"
                        aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarCollapse">
                    <ul className="navbar-nav mr-auto col-9">
                        {this.props.links.map((link) => <MenuItem key={link.id} link={link}/>)}
                        <li>
                            {this.props.get_user().is_auth ? <Link className="nav-link" to='/'
                                                                   onClick={() => this.props.logout()}>Выйти</Link> :
                                <Link className="nav-link" to='/login'>Войти</Link>}
                        </li>
                        {this.props.get_user().is_auth ? <li><h5 className="text-white m-2">
                            {this.props.get_user().username}</h5></li> : <i/>}
                    </ul>
                    <form className="navbar-nav justify-content-end col-3"
                          onSubmit={(event) => this.handleSubmit(event)}>
                        <input className="form-control mr-sm-2" type="text" placeholder="Search" aria-label="Search"
                               name="text" onChange={(event) => this.handleChange(event)}/>
                        <button className="btn btn-outline-success my-2 my-sm-0" type="submit">Поиск</button>
                    </form>
                </div>
            </nav>
        )
    }
}

export default MenuList