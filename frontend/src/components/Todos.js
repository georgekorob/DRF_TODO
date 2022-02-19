import React from 'react'

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

const TodoList = ({todos}) => {
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
                {todos.map((todo) => <TodoItem key={todo.id} todo={todo}/>)}
            </tbody>
        </table>
    )
}

export default TodoList