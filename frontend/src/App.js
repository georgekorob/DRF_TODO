import React from 'react';
import axios from 'axios';
// import logo from './logo.svg';
import './App.css';
import UserList from './components/Users.js';
import MenuList from './components/Menu.js';
import Footer from './components/Footer.js';
import {BrowserRouter, Redirect, Route, Switch} from "react-router-dom";
import ProjectList from "./components/Projects";
import TodoList from "./components/Todos";
import LoginForm from "./components/Auth";
import NotFound404 from "./components/NotFound404";
import ProjectTodoList from "./components/ProjectTodos";
import Cookies from "universal-cookie";

const DOMAIN = 'http://127.0.0.1:8000/api/'
const get_url = (url) => `${DOMAIN}${url}`
const menulist = [
    {'id': 1, 'name': 'Users', 'url': '/'},
    {'id': 2, 'name': 'Projects', 'url': '/projects'},
    {'id': 3, 'name': 'Todos', 'url': '/todos'},
    {'id': 4, 'name': 'Главная', 'url': '/'},
    {'id': 5, 'name': 'Контакты', 'url': '/'},
    {'id': 6, 'name': 'О нас', 'url': '/'}
]

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            'users': [],
            'menulinks': menulist,
            'projects': [],
            'todos': [],
            'token': '',
            'username': '',
        }
    }

    is_auth() {
        return !!this.state.token;
    }

    logout() {
        this.set_token('', '');
        this.setState({'username': ''})
    }

    load_data() {
        // console.log(this.state.token)
        let headers = {'Content-Type': 'application/json'}
        if (this.is_auth()) {
            headers['Authorization'] = `Token ${this.state.token}`
        }
        axios.get(get_url('users/'), {headers}).then(response => {
            this.setState({
                'users': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'users': []})
        });
        axios.get(get_url('projects/'), {headers}).then(response => {
            this.setState({
                'projects': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'projects': []})
        });
        axios.get(get_url('todos/'), {headers}).then(response => {
            this.setState({
                'todos': response.data
            })
        }).catch(error => {
            console.log(error)
            this.setState({'todos': []})
        });
    }

    set_token(token, username) {
        const cookies = new Cookies()
        cookies.set('token', token)
        cookies.set('username', username)
        this.setState({'token': token, 'username': username}, () => this.load_data())
    }

    get_token(username, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {
            username: username,
            password: password
        }).then(response => {
            this.set_token(response.data['token'], username)
        }).catch(error => alert('Неверный логин или пароль'))
    }

    get_token_from_cookies() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        const username = cookies.get('username')
        this.setState({'token': token, 'username': username}, () => this.load_data())
    }

    componentDidMount() {
        this.get_token_from_cookies()
    }

    get_username() {
        return this.state.username;
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <MenuList links={this.state.menulinks}
                              is_auth={() => this.is_auth()}
                              logout={() => this.logout()}
                              username={() => this.get_username()}/>
                    <Switch>
                        <Route exact path='/'>
                            <UserList users={this.state.users}/>
                        </Route>
                        <Route exact path='/projects'>
                            <ProjectList projects={this.state.projects}/>
                        </Route>
                        <Route exact path='/todos'>
                            <TodoList todos={this.state.todos}/>
                        </Route>
                        <Route path='/project/:id'>
                            <ProjectTodoList todos={this.state.todos}/>
                        </Route>
                        <Route exact path='/login'>
                            <LoginForm get_token={(username, password) => this.get_token(username, password)}/>
                        </Route>
                        <Redirect from='/users' to='/'/>
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>
                <Footer/>
            </div>
        )
    }
}

export default App;
