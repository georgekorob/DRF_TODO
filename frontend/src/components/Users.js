import React from 'react'


const UserItem = ({useritem}) => {
    return (
        <tr>
            <td>
                {useritem.username}
            </td>
            <td>
                {useritem.first_name}
            </td>
            <td>
                {useritem.last_name}
            </td>
            <td>
                {useritem.email}
            </td>
        </tr>
    )
}


const UserList = ({users}) => {
    return (
        <table>
            <th>
                Login
            </th>
            <th>
                First name
            </th>
            <th>
                Last Name
            </th>
            <th>
                Email
            </th>
            {users.map((useritem) => <UserItem useritem={useritem}/>)}
        </table>
    )
}


export default UserList