import logo from './logo.png'
import { NavLink } from 'react-router-dom'

const Navbar = () => {

    const onLogout = async () => {
        const response = await fetch("http://127.0.0.1:5000/logout", { method: "PATCH", headers: {"Content-Type": "application/json"} });
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            return
        }
    }

    return ( 
        <nav className="navbar">
            <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
            <img src={ logo } alt="logo" height="32" width="32" />
            <h1>Beetlejuice</h1>
            <div className="links">
                <NavLink activeStyle={{border: "2px solid #828196"}} exact to="/home">
                    Home
                </NavLink>
                <NavLink activeStyle={{border: "2px solid #828196"}} exact to="/portfolio">
                    My portfolio
                </NavLink>
                <NavLink exact to="/" className="logout">
                    <button onClick={onLogout} className='tbutton red' style={{padding: "8px", paddingLeft: "12px"}}>
                        Logout<span className="material-symbols-outlined">logout</span>
                    </button>
                </NavLink>
            </div>
        </nav>
    );
}
 
export default Navbar;