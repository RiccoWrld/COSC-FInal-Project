import React, { useState, useEffect, useRef } from 'react';
import './App.css';
import './ShinyText.css';
import ShinyText from './ShinyText';
import { useNavigate } from 'react-router-dom'; // (fix spelling!)
import { useLocation } from 'react-router-dom'; // (fix spelling!)

function Chat() {
  const [messages, setMessages] = useState([]);
  const [text, setText] = useState('');
  const ws = useRef(null);
  const bottomRef = useRef(null);
  const navigate = useNavigate();
  const location = useLocation();
  const { username } = location.state || {};

  // Redirect if no username
  useEffect(() => {
    if (!username) {
      navigate('/login');
    }
  }, [username, navigate]);

  // Scroll to bottom when messages change
  useEffect(() => {
    if (bottomRef.current) {
      bottomRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  // Connect to WebSocket server
  useEffect(() => {
    ws.current = new WebSocket('ws://localhost:6789');

    ws.current.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, message]);
    };

    return () => {
      ws.current.close();
    };
  }, []);

  const sendMessage = (e) => {
    e.preventDefault();
    if (text.trim() !== '') {
      const messageObj = { sender: username, text }; // <-- use username here!
      ws.current.send(JSON.stringify(messageObj));
      setText('');
    }
  };

  return (
    <div className="chat-page">
      <ShinyText
        text={
          <>
            Welcome to the Chat Room <br />
          </>
        }
        speed={3}
        fontSize="50px"
      />

      <div className="chat-container">
        <div className="message-list">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`chat-bubble ${msg.sender === username ? 'user' : 'bot'}`}
              style={{ alignSelf: msg.sender === username ? 'flex-end' : 'flex-start' }}
            >
              <strong>{msg.sender}: </strong> {msg.text}
            </div>
          ))}
        </div>
        <div ref={bottomRef}></div>

        <form className="message-form" onSubmit={sendMessage}>
          <input
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Type a message..."
          />
          <button type="submit">Send</button>
        </form>
      </div>

      <div className="sidenav-container">
        <div className="sidenav">
          <h2>Chat Rooms</h2>
          <ul>
            <li>Room 1</li>
            <li>Room 2</li>
            <li>Room 3</li>
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Chat;
