import React, { useState, useEffect } from "react";
import Stats from "./Stats";
import ReactLoading from 'react-loading';

const Auth = () => {
  const [data, setData] = useState([{}]);
  const [loading, setLoading] = useState(false);
  const [auth, setAuth] = useState(false);

  async function fetchdata(path){
    const res = await fetch(path)
    if (res.ok){
      return res
    }
    return Promise.reject(new Error('Response Error Code '+res.status));
  }
  useEffect(() => {
    setLoading(true);
    fetch("/auth")
      .then((response) => {
        if (response.ok) {
            return response.json();
        }
        return Promise.reject(new Error('Response Error Code '+response.status))
      })
      .then((data) => {
        setData(data);
        setLoading(false);
        setAuth(true); //placeholder
        // fetch().then((res)=>{
        //   if (res.ok){
        //     return res.json()
        //   }
        // })
        console.log(data);
      })
      .catch((err) => {
        console.log(err);
        setLoading(false);
        setAuth(false);
      });
  }, []);

    if(loading){
      return(
        <div className="Loading">
          <ReactLoading type="spin" color="black" />
        </div>
      )
    }else if(!loading && auth){
      return(
        <div className="StatsScreen">
          <h1>Hello {data.gameName} !</h1>
          <h2>Here are your stats for this season:</h2>
          <Stats data={data} />
        </div>
      )
    }else if(!loading && !auth){
      return(
        <div>
          <h1>Cant Authenticate</h1>
        </div>
      )
    }
};

export default Auth;
