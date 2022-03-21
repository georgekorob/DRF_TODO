import React from 'react'
import {useParams} from "react-router-dom";

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.text}</td>
            <td>{todo.createDate}</td>
            <td>{todo.updateDate}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
        </tr>
    )
}

const ProjectTodoList = ({todos}) => {
    let {id} = useParams();
    let filteresTodos = todos.filter(todo => todo.project === id);
    return (
        <table>
            <thead>
                <tr>
                    <th>Text</th>
                    <th>Create date</th>
                    <th>Update date</th>
                    <th>Project</th>
                    <th>User</th>
                </tr>
            </thead>
            <tbody>
                {filteresTodos.map((todo) => <TodoItem key={todo.id} todo={todo}/>)}
            </tbody>
        </table>
    )
}

export default ProjectTodoList