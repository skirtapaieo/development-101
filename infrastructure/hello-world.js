// Import the express module
const express = require('express');

// Create a new express application
const app = express();

// Define the port to listen on. Use the PORT environment variable if it's set.
const port = process.env.PORT || 3000;

// Handle GET requests to the root path
app.get('/', (req, res) => {
    res.send('Hello World');
});

// Start listening for requests
app.listen(port, () => {
    console.log(`Hello World service listening at http://localhost:${port}`);
});
