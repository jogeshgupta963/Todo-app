import { getSuggestedQuery } from '@testing-library/dom'
import axios from 'axios'
import Cookies from 'js-cookie'
import React, { useEffect, useState } from 'react'
import { Navigate } from 'react-router'
import { TodoInput, TodoList } from '../Components'

function Todo() {

    const [user,setUser] = useState()
  const getUser = async()=>{
    try {
        const {data} = await axios.get('/user')
        setUser(data)
    } catch (err) {
        
    }
  }  
  useEffect(() => {
    getUser()
  }, [])
  
  return (
    <>
    {
        !Cookies.get('JWT') &&
        <Navigate to='/login'/>
    }
    <div style={{textAlign:'center'}} >Todo App</div>
        <TodoInput/>
        <TodoList user={user} />
    </>
  )
}

export default Todo