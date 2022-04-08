import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project, get_user, deleteProject}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}`}>{project.name}</Link>
            </td>
            <td>{project.link}</td>
            {get_user().is_auth && <td>
                <button onClick={() => deleteProject(project.id)} type="button">Delete</button>
            </td>}
        </tr>
    )
}

const ProjectList = ({projects, get_user, deleteProject}) => {
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Link</th>
                        {get_user().is_auth && <th>Delete</th>}
                    </tr>
                </thead>
                <tbody>
                    {projects.map((project) => <ProjectItem
                        key={project.id}
                        project={project}
                        get_user={get_user}
                        deleteProject={deleteProject}
                    />)}
                </tbody>
            </table>
            {get_user().is_auth && <Link to='/projects/create'>Create</Link>}
        </div>
    )
}

export default ProjectList