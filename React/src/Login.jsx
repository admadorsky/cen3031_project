import React, { useState, useEffect } from "react"
import LoginForm from "./LoginForm"

const Login = () => {

    const [users, setUsers] = useState([])

useEffect(() => {
    fetchUsers()
}, [])

const fetchUsers = async () => {
    const response = await fetch("http://127.0.0.1:5000/users");
    const fetchData = await response.json();
    setUsers(fetchData.users);
  };

console.log(users)

    return (
        <div className="login">
            <div className="login-content">
                <LoginForm />
            </div>
        </div>
    );
}
 
export default Login;