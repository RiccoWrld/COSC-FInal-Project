import { Routes, Route, useNavigate } from 'react-router-dom';
import Login from './login.js'; // import your login component
import ShinyText from './ShinyText.js';
import './App.css';
import './ShinyText.css';

function Home() {
  const navigate = useNavigate();

  return (
    <div className="App">
      <ShinyText
        text={
          <>
            Welcome to Chat Server, <br />
            Where you can chat with your friends anytime, anywhere!
          </>
        }
        speed={3}
      />

      <button
        className="get-started-button"
        onClick={() => navigate('/login')}
      >
        <ShinyText text="Get Started" speed={3} fontSize="45px" />
      </button>

      <div className="footer">
        <ShinyText text="Chat Server" speed={3} fontSize="30px" />
        <ShinyText text="© 2025" speed={3} fontSize="30px" />
      </div>
    </div>
  );
}

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/login" element={<Login />} />
    </Routes>
  );
}

export default App;
