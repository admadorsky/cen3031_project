import logo from './logo.png'
import { NavLink } from 'react-router-dom'


const Navbar = () => {
    return ( 
        <nav className="navbar">
            <img src={ logo } alt="logo" height="32" width="32" />
            <h1>Beetlejuice</h1>
            <div className="links">
                <NavLink activeStyle={{border: "2px solid #828196"}} exact to="/">
                    Home
                </NavLink>
                <NavLink activeStyle={{border: "2px solid #828196"}} exact to="/portfolio">
                    My portfolio
                </NavLink>
            </div>
        </nav>
    );
}
 
export default Navbar;