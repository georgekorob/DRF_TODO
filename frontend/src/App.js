import React from 'react';
import axios from 'axios';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js';
import MenuList from './components/Menu.js';
import Footer from './components/Footer.js';

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
        'name': 'Users',
        'url': 'http://127.0.0.1:3000/'
      },
      {
        'name': 'Главная',
        'url': '#'
      },
      {
        'name': 'Контакты',
        'url': '#'
      },
      {
        'name': 'О нас',
        'url': '#'
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
          <MenuList links={this.state.menulinks}/>
          <UserList users={this.state.users}/>
          <Footer/>
        </div>
    )
  }
}

export default App;
