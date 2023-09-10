// React Component
import React from 'react'; # import React library

const NamesList = ({ names }) => { # declare a function component
  return (
    <ul>
      {names.map((name, index) => ( # use map() to iterate over the names array
        <li key={index}>{name}</li>
      ))}
    </ul>
  );
};

export default NamesList;
