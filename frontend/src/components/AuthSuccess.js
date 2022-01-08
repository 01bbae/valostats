import React, { useState, useEffect } from 'react'
import Stats from './Stats'

const AuthSuccess = () => {
    const [data, setData] =useState([{}])

    useEffect(() => {
        fetch("/authsuccess").then(
            response => response.json()
        ).then(
            data => {
                setData(data)
                console.log(data)
            }
        )
    }, [])
    return (
        <div>
           <h1>Auth Successful</h1>
           <h1>Hello {data.gameName} !</h1>
           <h2>Here are your stats for this season:</h2>
           <Stats />
        </div>
    )
}

export default AuthSuccess
