import React from 'react';
import './ShinyText.css';

const ShinyText = ({ text, disabled = false, speed = 5, fontSize = '100px', className = '' }) => {
  const animationDuration = `${speed}s`;

  return (
    <div
      className={`shiny-text ${disabled ? 'disabled' : ''} ${className}`}
      style={{ animationDuration, fontSize }}
    >
      {text}
    </div>
  );
};

export default ShinyText;
