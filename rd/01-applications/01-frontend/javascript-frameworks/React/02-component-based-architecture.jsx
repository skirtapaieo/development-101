// React Component
import React, { useState } from 'react';

const Counter = () => {
  const [count, setCount] = useState(0); # declare a state variable

  const handleIncrement = () => {
    setCount(count + 1);
  };

  return (
    <div>
      <p>Count: {count}</p>
      <button onClick={handleIncrement}>Increment</button>
    </div>
  );
};

export default Counter;
