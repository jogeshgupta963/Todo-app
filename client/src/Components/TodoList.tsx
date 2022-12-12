import axios from 'axios'
import React, { useEffect, useState } from 'react'

function TodoList({user}:any) {

    const [todos,setTodos] = useState<any[]>([])

    const getAllTodos= async()=>{
        const {data} = await axios.get('/todos')
        setTodos(data)
    }
    
    console.log(todos)
    useEffect(() => {
        getAllTodos()
    }, [])
        
    return (
        <div>
            {
                todos.length>0 && todos.map(todo=>{
                    return (<>
                    <div key={todo._id} style={{border:"2px solid black"}} >
                        <h3>Title: <span>{todo.title}</span> </h3>
                        <h3>Description: <span>{todo.description}</span> </h3>
                    </div>
                    </>)
                })
            }
        </div>
  )
}

export default TodoList