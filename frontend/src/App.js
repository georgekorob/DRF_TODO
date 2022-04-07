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
import ProjectForm from "./components/ProjectForm";
import TodoForm from "./components/TodoForm";

// const DOMAIN = 'http://127.0.0.1:8000/'
// const DOMAIN = 'http://192.168.0.2:8000/'
const DOMAIN = 'http://k-bazz.duckdns.org:45088/'
const getUrl = (url) => `${DOMAIN}api/${url}`
const getQl = (query) => `${DOMAIN}graphql/?query=${query}`
const projects_ql = '{projects{id,name,link}}'
const users_ql = '{users{id,username,firstName,lastName,email}}'
const todos_ql = '{todos{id,text,createDate,updateDate,project{id},user{username}}}'
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
            'user': {
                'username': '',
                'is_auth': false,
            },
            'filterText': ''
        }
    }

    is_auth() {
        return this.state.user.is_auth;
    }

    get_user() {
        return this.state.user;
    }

    getHeaders() {
        const cookies = new Cookies()
        const access = cookies.get('access')
        let headers = {'Content-Type': 'application/json'}
        if (this.state.user.is_auth) {
            headers['Authorization'] = `Bearer ${access}`
        }
        return headers
    }

    load_data() {
        // console.log(this.state.token)
        const headers = this.getHeaders();
        axios.get(getQl(users_ql), {headers}).then(response => {
            this.setState({users: response.data.data.users})
        }).catch(error => {
            console.log(error)
            this.setState({users: []})
        });
        axios.get(getQl(projects_ql), {headers}).then(response => {
            this.setState({projects: response.data.data.projects})
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        });
        axios.get(getQl(todos_ql), {headers}).then(response => {
            response.data.data.todos.forEach((todo) => {
                todo.project = todo.project.id;
                todo.user = todo.user.username;
            })
            this.setState({todos: response.data.data.todos})
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        });
    }

    set_token(access, refresh, user) {
        const cookies = new Cookies()
        cookies.set('access', access)
        cookies.set('refresh', refresh)
        cookies.set('username', user.username)
        this.setState({user: user}, () => this.load_data())
    }

    logout() {
        const user = {'username': '', 'is_auth': false};
        this.set_token('', '', user)
    }

    get_token(username, password) {
        axios.post(getUrl('token/'), {
            username: username,
            password: password
        }).then(response => {
            const user = {'username': username, 'is_auth': true};
            this.set_token(response.data['access'], response.data['refresh'], user)
        }).catch(error => alert('Неверный логин или пароль'))
    }

    componentDidMount() {
        const cookies = new Cookies()
        const username = cookies.get('username')
        if ((username !== "") && (username != null)) {
            this.setState({user: {'username': username, 'is_auth': true}}, () => this.load_data())
        }
    }

    createProject(project) {
        const headers = this.getHeaders()
        axios.post(getUrl(`projects/`), project, {headers}).then(response => {
            axios.get(getQl(projects_ql), {headers}).then(response => {
                this.setState({projects: response.data.data.projects})
            }).catch(error => {
                console.log(error)
                this.setState({projects: []})
            });
            // const projects = [...this.state.projects, project]
            // this.setState({projects: projects})
        }).catch(error => {
            console.log(error)
        })
    }

    deleteProject(id) {
        const headers = this.getHeaders()
        axios.delete(getUrl(`projects/${id}`), {headers}).then(response => {
            const projects = this.state.projects.filter((project) => project.id !== id)
            this.setState({projects: projects})
        }).catch(error => {
            console.log(error)
            this.setState({projects: []})
        })
    }

    createTodo(todo) {
        const headers = this.getHeaders()
        axios.post(getUrl(`todos/`), todo, {headers}).then(response => {
            axios.get(getQl(todos_ql), {headers}).then(response => {
                response.data.data.todos.forEach((todo) => {
                    todo.project = todo.project.id;
                    todo.user = todo.user.username;
                })
                this.setState({todos: response.data.data.todos})
            }).catch(error => {
                console.log(error)
                this.setState({todos: []})
            });
        }).catch(error => {
            console.log(error)
        })
    }

    deleteTodo(id) {
        const headers = this.getHeaders()
        axios.delete(getUrl(`todos/${id}`), {headers}).then(response => {
            const todos = this.state.todos.filter((todo) => todo.id !== id)
            this.setState({todos: todos})
        }).catch(error => {
            console.log(error)
            this.setState({todos: []})
        })
    }

    filterProject(text) {
        this.setState({filterText: text})
    }

    render() {
        return (
            <div>
                <BrowserRouter>
                    <MenuList links={this.state.menulinks}
                              get_user={() => this.get_user()}
                              logout={() => this.logout()}
                              filterProject={(text) => this.filterProject(text)}/>
                    <Switch>
                        <Route exact path='/'>
                            <UserList users={this.state.users}/>
                        </Route>
                        <Route exact path='/projects'>
                            <ProjectList projects={this.state.projects.filter(project =>
                                project.name.includes(this.state.filterText))}
                                         get_user={() => this.get_user()}
                                         deleteProject={(id) => this.deleteProject(id)}/>
                        </Route>
                        <Route exact path='/projects/create' component={() =>
                            <ProjectForm users={this.state.users}
                                         createProject={(project) => this.createProject(project)}/>
                        }/>
                        <Route exact path='/todos'>
                            <TodoList todos={this.state.todos}
                                      get_user={() => this.get_user()}
                                      deleteTodo={(id) => this.deleteTodo(id)}/>
                        </Route>
                        <Route exact path='/todos/create' component={() =>
                            <TodoForm users={this.state.users}
                                      projects={this.state.projects}
                                      createTodo={(todo) => this.createTodo(todo)}/>
                        }/>
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
