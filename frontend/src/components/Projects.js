import React from 'react'
import {Link} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}`}>{project.name}</Link>
            </td>
            <td>{project.link}</td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Link</th>
                </tr>
            </thead>
            <tbody>
                {projects.map((project) => <ProjectItem key={project.id} project={project}/>)}
            </tbody>
        </table>
    )
}

export default ProjectList