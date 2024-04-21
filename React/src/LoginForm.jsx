import { useState, useEffect } from 'react'
import { Redirect } from 'react-router-dom'

const LoginForm = () => {

    const [users, setUsers] = useState([])
    const [username, setUsername] = useState("")
    const [password, setPassword] = useState("")
    const [createUsername, setCreateUsername] = useState("")
    const [createPassword, setCreatePassword] = useState("")
    const [goToApp, setGoToApp] = useState(false)

    useEffect(() => {
        fetchUsers()
    }, [])

    const fetchUsers = async () => {
        const response = await fetch("http://127.0.0.1:5000/users");
        const fetchData = await response.json();
        setUsers(fetchData.users);
    };    

    const onSubmit = async (e) => {
        e.preventDefault()
        
        const data = {
            username,
            password            
        }

        let found_id = 0;

        for(let i = 0; i < users.length; i++) {
            if ( (users[i].username == username) && (users[i].password == password) ) {
                found_id = users[i].id
            }
        }

        const url = `http://127.0.0.1:5000/set-active-user${found_id}`
        const options = {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }

        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            setGoToApp(true)
        }
    }

    const onSubmitCreate = async (e) => {
        e.preventDefault()

        const data = {
            createUsername,
            createPassword
        }
        
        const url = `http://127.0.0.1:5000/create_user`
        const options = {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        }

        const response = await fetch(url, options)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            setGoToApp(true)
        }
    }

    if (goToApp) {
        console.log("navigating")
        return (
            <div>
                <Redirect to = "/home" />
            </div>
        )
    }

    return (
        <div className="content">
            <div className='row'>
                <div className='column'>
                    <div className='block'>
                    <h3>Returning User</h3>
                        <form onSubmit={onSubmit}>
                            <div>
                                <label htmlFor="username">Username:</label>
                                <input
                                    type="text"
                                    id="username"
                                    value={username}
                                    onChange={(e) => setUsername(e.target.value)}
                                />
                            </div>
                            <div>
                                <label htmlFor="password">Password:</label>
                                <input
                                    type="text"
                                    id="password"
                                    value={password}
                                    onChange={(e) => setPassword(e.target.value)}
                                />
                            </div>
                            <button type="submit" className='button'>
                                Login
                            </button>
                        </form>
                    </div>
                </div>
                <div className='column'>
                    <div className='block'>
                    <h3>New User</h3>
                        <form onSubmit={onSubmitCreate}>
                            <div>
                                <label htmlFor="createUsername">Username:</label>
                                <input
                                    type="text"
                                    id="createUsername"
                                    value={createUsername}
                                    onChange={(e) => setCreateUsername(e.target.value)}
                                />
                            </div>
                            <div>
                                <label htmlFor="createPassword">Password:</label>
                                <input
                                    type="text"
                                    id="createPassword"
                                    value={createPassword}
                                    onChange={(e) => setCreatePassword(e.target.value)}
                                />
                            </div>
                            <button type="submit" className='button'>
                                Create Account
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>
    );
}
 
export default LoginForm;