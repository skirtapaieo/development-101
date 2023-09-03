
// Uni-directional data flow

// Parent Component

/*
import React, { useState } from 'react';
import ChildComponent from './ChildComponent';

const ParentComponent = () => {
  const [count, setCount] = useState(0); // Declaring a state variable

  const handleIncrement = () => {
    setCount(count + 1); // Updating the 'count' state in the parent component
  };

  return (
    <div>
      <p>Count: {count}</p>
      <ChildComponent count={count} onIncrement={handleIncrement} /> // Passing the 'count' state and the 'handleIncrement' function as props to the child component
    </div>
  );
};

export default ParentComponent;


// Child Component
import React from 'react';

const ChildComponent = ({ count, onIncrement }) => { // Receiving the 'count' state and the 'handleIncrement' function as props from the parent component
    return (
        <div>
            <button onClick={onIncrement}>Increment</button> // Calling the 'handleIncrement' function when the button is clicked
        </div>
    );
};

export default ChildComponent;
*/