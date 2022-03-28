import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}`}>{project.name}</Link>
            </td>
            <td>{project.link}</td>
            <td>
                <button onClick={() => deleteProject(project.id)} type="button">Delete</button>
            </td>
        </tr>
    )
}

const ProjectList = ({projects, deleteProject}) => {
    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Link</th>
                        <th>Delete</th>
                    </tr>
                </thead>
                <tbody>
                    {projects.map((project) => <ProjectItem
                        key={project.id}
                        project={project}
                        deleteProject={deleteProject}
                    />)}
                </tbody>
            </table>
            <Link to='/projects/create'>Create</Link>
        </div>
    )
}

export default ProjectList