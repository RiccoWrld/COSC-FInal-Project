import React, { useState } from 'react';
import './App.css';
import ShinyText from './ShinyText.js';
import './ShinyText.css';
import { useNavigate } from 'react-router-dom';

function Login() {
  const navigate = useNavigate();
  const [username, setUsername] = useState(''); // Track username

  const handleLogin = (e) => {
    e.preventDefault();
    if (username.trim() !== '') {
      navigate('/chat', { state: { username } }); // Pass username into Chat
    }
  };

  return (
    <div className="login-page">
      <ShinyText text="Chat Server" speed={3} />
      <div className="login-container">
        <h2>Login</h2>
        <form className="login-form" onSubmit={handleLogin}>
          <div className="form-group">
            <label htmlFor="username"></label>
            <input
              type="text"
              name="username"
              id="username"
              placeholder="Username"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label htmlFor="password"></label>
            <input
              type="password"
              name="password"
              id="password"
              placeholder="Password"
              required
            />
          </div>

          <div className="button-container">
            <button type="submit" className="login-button">Login</button>
            <button type="button" className="signUp" onClick={() => navigate('/signup')}>
              SignUp
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Login;
