// Making a GET request using XMLHttpRequest

// Create a new XMLHttpRequest object (xhr)
const xhr = new XMLHttpRequest();

// Open the request
xhr.open("GET", "https://api.example.com/data", true);

// Send the request
xhr.onreadystatechange = function () {
  // Process the response from the server, readyState 4 means the request is done, status 200 means "OK"
  if (xhr.readyState === 4 && xhr.status === 200)
    console.log(JSON.parse(xhr.responseText));
};
xhr.send();

// Making a GET request using fetch

// Fetch returns a promise
fetch("https://api.example.com/data")
  // Process the response from the server, response.json() returns a promise
  .then((response) => response.json())
  // Process the data in the response, data is the result of response.json()
  .then((data) => console.log(data))
  // Handle errors
  .catch((error) => console.error("There was an error!", error));
