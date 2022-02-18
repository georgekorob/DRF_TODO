import React from 'react';
import axios from 'axios';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js';
import MenuList from './components/Menu.js';
import Footer from './components/Footer.js';
import {BrowserRouter, Route} from "react-router-dom";

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`

class App extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      'users': [],
      'menulinks': [],
    }
  }

  componentDidMount() {
    const menulist = [
      {
        'id': 1,
        'name': 'Users',
        'url': '/'
      },
      {
        'id': 2,
        'name': 'Projects',
        'url': '/'
      },
      {
        'id': 3,
        'name': 'Todos',
        'url': '/'
      },
      {
        'id': 4,
        'name': 'Главная',
        'url': '/'
      },
      {
        'id': 5,
        'name': 'Контакты',
        'url': '/'
      },
      {
        'id': 6,
        'name': 'О нас',
        'url': '/'
      }
    ]

    axios.get(get_url('users/')).then(response => {
      this.setState({
        'users': response.data,
        'menulinks': menulist
      })
    }).catch(error => console.log(error))
  }

  render () {
    return (
        <div>
          <BrowserRouter>
            <MenuList links={this.state.menulinks}/>
            <Route exact path='/'>
              <UserList users={this.state.users}/>
            </Route>
          </BrowserRouter>
          <Footer/>
        </div>
    )
  }
}

export default App;
