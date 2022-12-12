import React from 'react';
import './App.css';
import {Routes,Route} from 'react-router-dom'
import {Login, Signup, Todo} from './Pages/';
function App() {
  return (
    <>
      <Routes>
           <Route  path='/' element={<Todo/>}/>
           <Route path='/login' element={<Login/>}/>
           <Route path='/signup' element={<Signup/>}/>
      </Routes>
    </> 
  );
}

export default App;
