import React, { useState } from 'react';

function Counter() {
  const [counter, setCounter] = useState(0);

  return (
    <div>
      <p>Counter: {counter}</p>
      <button onClick={() => setCounter(counter + 1)}>Increment</button>
    </div>
  );
}

export default Counter;