import React from 'react'


const MenuItem = ({link}) => {
    return (
        <a type={'button'} href={link.url}>{link.name}</a>
    )
}


const MenuList = ({links}) => {
    return (
        <header>
            {links.map((link) => <MenuItem link={link}/>)}
        </header>
    )
}


export default MenuList