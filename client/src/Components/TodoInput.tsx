import axios from 'axios';
import React, { useRef } from 'react'

function TodoInput() {

  const title = useRef() as React.MutableRefObject<HTMLInputElement>;
  const desc = useRef() as React.MutableRefObject<HTMLInputElement>;
  const clickHandle = async(e:any)=>{
    e.preventDefault()
    try {
      const {data} = await axios.post('/todos',{
        title:title.current.value,
        description:desc.current.value
      })
      console.log(data)
      window.location.reload()
    } catch (err) {
      
    }
  }
  return (
    <>

    <form >
      <input placeholder='title' ref={title} type="text" />
      <input placeholder='desc' ref={desc} type="text" />
      <button onClick={clickHandle} >Create</button>
    </form>
    </>
  )
}

export default TodoInput