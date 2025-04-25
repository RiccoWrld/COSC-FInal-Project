// src/App.js
import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './Home';
import Login from './login'; // Create or import your login component

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  );
}

export default App;
