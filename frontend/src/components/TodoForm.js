import React from "react";


class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {project: 1, text: '', user: 1}
    }

    handleTodoChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({[event.target.name]: 1})
        } else {
            this.setState({[event.target.name]: +event.target.selectedOptions.item(0).value})
        }
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }

    handleSubmit(event) {
        this.props.createTodo(this.state)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="text">text</label>
                    <input type="text" className="form-control" name="text" value={this.state.text}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <select name="project" onChange={(event) =>
                    this.handleTodoChange(event)}>
                    {this.props.projects.map((item) =>
                        <option key={item.id} value={item.id}>{item.name}</option>)}
                </select>
                <select name="user" onChange={(event) =>
                    this.handleTodoChange(event)}>
                    {this.props.users.map((item) =>
                        <option key={item.id} value={item.id}>{item.username}</option>)}
                </select>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default TodoForm
