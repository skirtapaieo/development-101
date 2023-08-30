import React, { useEffect } from 'react';

const HelloWorld = () => {
  useEffect(() => {
    fetch('http://localhost:3000')
      .then((response) => response.text())
      .then((data) => {
        console.log('Received data:\n' + data); // "Hello, World!"
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }, []);

  return null; // or your component JSX here
};

export default HelloWorld;
