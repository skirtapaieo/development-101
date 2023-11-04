The terms "Isomorphic JavaScript" and "Universal JavaScript" are often used interchangeably in the context of web development, but they have nuanced differences:

# Isomorphic JavaScript

- **Primary Focus**: The main focus is on sharing code between the server and the client.
- **Historical Context**: This term was popularized first and has been more traditionally used to describe JavaScript that can execute both on the client and server.
- **Terminology**: The term "Isomorphic" is derived from mathematics, implying that the same code runs in multiple environments in the same "shape" or form.

# Universal JavaScript

- **Primary Focus**: While it also pertains to running code on both the client and the server, Universal JavaScript places a stronger emphasis on the application's functionality and user experience across multiple platforms (browser, server, native mobile apps, etc.).
- **Modern Usage**: This term is newer and has become more popular with the advent of frameworks and libraries that aim to provide a seamless user experience across different platforms and devices.
- **Terminology**: The term "Universal" is used to imply a broader scope, suggesting that the code isn't just limited to client and server but could potentially run anywhere JavaScript is supported.

| Property         | Isomorphic JavaScript | Universal JavaScript |
| ---------------- | --------------------- | -------------------- |
| Focus            | Code Sharing          | Functionality & UX   |
| Historical Usage | Earlier               | More recent          |
| Scope            | Client & Server       | Multi-platform       |

Both approaches aim to provide advantages like SEO benefits, quicker page loads, and easier maintainability by using the same codebase to run on both the client and the server. The choice of term often depends on the developer's focus or the specific technologies being used.

# Code examples

For the purpose of illustration, let's consider a very basic example using React for both Isomorphic and Universal JavaScript.

In the Universal example, the `fetchData` function is designed to be "universal" - it can run on the server during server-side rendering and also on the client for dynamic updates.

### Isomorphic JavaScript Example

Here, the focus is primarily on sharing code between the client and the server. We'll use Node.js and Express for the server and React for the UI.

**server.js**

```javascript
const express = require("express");
const React = require("react");
const ReactDOMServer = require("react-dom/server");

const App = require("./App");

const app = express();

app.get("/", (req, res) => {
  const appString = ReactDOMServer.renderToString(React.createElement(App));
  res.send(`<html><body><div id="root">${appString}</div></body></html>`);
});

app.listen(3000);
```

**App.js**

```javascript
const React = require("react");

function App() {
  return <h1>Hello, world!</h1>;
}

if (typeof window !== "undefined") {
  const ReactDOM = require("react-dom");
  ReactDOM.hydrate(React.createElement(App), document.getElementById("root"));
}

module.exports = App;
```

### Universal JavaScript Example

In Universal JavaScript, we would extend this example to include functionality that is applicable both on the server and the client, maybe even other platforms.

Let's add a function to fetch some data. This function can be used both on the server to pre-fetch data and on the client for subsequent updates.

**fetchData.js**

```javascript
async function fetchData() {
  // Simulate an API call
  return new Promise((resolve) => {
    setTimeout(() => resolve("Hello from API"), 1000);
  });
}
```

**server.js**

```javascript
// ... previous code
const fetchData = require("./fetchData");

app.get("/", async (req, res) => {
  const data = await fetchData();
  const appString = ReactDOMServer.renderToString(
    React.createElement(App, { data })
  );
  res.send(`<html><body><div id="root">${appString}</div></body></html>`);
});
// ... previous code
```

**App.js**

```javascript
const React = require("react");
const fetchData = require("./fetchData");

function App(props) {
  const [data, setData] = React.useState(props.data || "Fetching...");

  React.useEffect(() => {
    if (!props.data) {
      fetchData().then(setData);
    }
  }, []);

  return <h1>{data}</h1>;
}
// ... previous code for hydrate
```
