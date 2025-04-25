import React from 'react';
import './App.css'; // Make sure it's imported

function Login() {
  return (
    <div className="login-container">
      <h1>Login</h1>
      <form action="/login" method="POST">
        <label htmlFor="username">Username</label>
        <input type="text" name="username" id="username" required />
        <br />
        <label htmlFor="password">Password</label>
        <input type="password" name="password" id="password" required />
      </form>
    </div>
  );
}

export default Login;
