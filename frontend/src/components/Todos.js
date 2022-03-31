import React from 'react'
import {Link} from "react-router-dom";

const TodoItem = ({todo, get_user, deleteTodo}) => {
    return (
        <tr>
            <td>{todo.text}</td>
            <td>{todo.createDate}</td>
            <td>{todo.updateDate}</td>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
            {get_user().is_auth && <td>
                <button onClick={() => deleteTodo(todo.id)} type="button">Delete</button>
            </td>}
        </tr>
    )
}

const TodoList = ({todos, get_user, deleteTodo}) => {
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Text</th>
                        <th>Create date</th>
                        <th>Update date</th>
                        <th>Project</th>
                        <th>User</th>
                        {get_user().is_auth && <th>Delete</th>}
                    </tr>
                </thead>
                <tbody>
                    {todos.map((todo) => <TodoItem key={todo.id} todo={todo} get_user={get_user}
                                                   deleteTodo={deleteTodo}/>)}
                </tbody>
            </table>
            {get_user().is_auth && <Link to='/todos/create'>Create</Link>}
        </div>
    )
}

export default TodoList