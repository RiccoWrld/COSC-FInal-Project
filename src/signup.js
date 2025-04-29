import React, { useState } from 'react';
import './App.css';
import './ShinyText.css';
import './signup.css';
import ShinyText from './ShinyText.js';
import { useNavigate } from 'react-router-dom';

function Signup() {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');

  const handleSignup = (e) => {
    e.preventDefault();
    if (username.trim() !== '') {
      navigate('/chat', { state: { username } }); // Pass username after signup
    }
  };

  return (
    <div className="signup-page">
      <ShinyText text="Chat Server" speed={3} />
      <div className="signup-container">
        <h2>Signup</h2>
        <form className="signup-form" onSubmit={handleSignup}>
          <div className="form-group">
            <label htmlFor="firstname"></label>
            <input type="text" name="firstname" id="firstname" placeholder="First Name" required />
            <label htmlFor="lastname"></label>
            <input type="text" name="lastname" id="lastname" placeholder="Last Name" required />
          </div>

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
            <input type="password" name="password" id="password" placeholder="Password" required />
          </div>

          <div className="button-container">
            <button type="submit" className="signUp">SignUp</button>
            <button type="button" className="login-button" onClick={() => navigate('/login')}>
              Login
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default Signup;
