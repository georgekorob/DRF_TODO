import React from "react";


class ProjectForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {name: '', link: '', users: []}
    }

    handleProjectChange(event) {
        if (!event.target.selectedOptions) {
            this.setState({users: []})
        } else {
            let users = []
            for (let i = 0; i < event.target.selectedOptions.length; i++) {
                users.push(event.target.selectedOptions.item(i).value)
            }
            this.setState({users: users})
        }
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value})
    }


    handleSubmit(event) {
        this.props.createProject(this.state)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="name">name</label>
                    <input type="text" className="form-control" name="name" value={this.state.name}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <div className="form-group">
                    <label htmlFor="link">link</label>
                    <input type="text" className="form-control" name="link" value={this.state.link}
                           onChange={(event) => this.handleChange(event)}/>
                </div>
                <select name="users" multiple onChange={(event) =>
                    this.handleProjectChange(event)}>
                    {this.props.users.map((item) =>
                        <option key={item.id} value={item.id}>{item.username}</option>)}
                </select>
                <input type="submit" className="btn btn-primary" value="Save"/>
            </form>
        );
    }
}

export default ProjectForm
