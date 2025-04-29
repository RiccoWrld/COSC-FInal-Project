// src/App.js
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Login from './login'; // Create or import your login component
import Chat from './Chat'; // Create or import your chat component
import Signup from './signup'; // Create or import your signup component

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
      <Route path="/chat" element={<Chat />} /> {/* Add your chat component here */}
      
      <Route path="/signup" element={<Signup />} /> {/* Add your signup component here */}
     
      
    </Routes>
  );
}

export default App;
