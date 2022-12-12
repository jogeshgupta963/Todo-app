import React, {  useRef } from 'react'
import { Link, Navigate } from 'react-router-dom'
import axios from 'axios'
import Cookies from 'js-cookie';

function Login() {

  const email = useRef() as React.MutableRefObject<HTMLInputElement>;
  const pass = useRef() as React.MutableRefObject<HTMLInputElement>;
  
  const submitHandle = async(e:any)=>{
      e.preventDefault()
      try {
        const {data} = await axios.post('/login',{
          email:email.current.value,
          password:pass.current.value
        })
        console.log(data)
      } catch (err) {
        
      }
  }
  
  return (

    <div>
      {
        Cookies.get('JWT') && <Navigate to='/' />
      }
      <form >
        <label htmlFor="">Email</label>
        <input ref={email} type="text" />
        <label htmlFor="">Password</label>
        <input ref={pass} type="password" />
        <button onClick={submitHandle}>Submit</button>

      </form>
      <br />
      <div>Dont have an account? <Link to='/signup'>Signup</Link></div>
    </div>
  )
}

export default Login