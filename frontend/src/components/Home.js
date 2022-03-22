import React from 'react'
import { Link } from 'react-router-dom'

const Home = () => {
    return (
        <div>
            <h1>Welcome to ValoStats!</h1>
            <Link to="/auth">Sign In</Link>
        </div>
    )
}

export default Home
