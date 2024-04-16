import logo from './logo.png'
import { Link } from 'react-router-dom'

const Navbar = () => {
    return ( 
        <nav className="navbar">
            <img src={ logo } alt="logo" height="32" width="32" />
            <h1>Beetlejuice</h1>
            <div className="links">
                <Link to="/">Home</Link>
                <Link to="/portfolio">My portfolio</Link>
            </div>
        </nav>
    );
}
 
export default Navbar;