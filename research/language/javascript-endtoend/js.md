# JavaScript

<br>

# The process

| Step # | Process               | Description                                         |
| ------ | --------------------- | --------------------------------------------------- |
| 1      | Fetching              | HTML, CSS, and JS files are downloaded              |
| 2      | Parsing & Compilation | JS code is parsed and compiled to bytecode          |
| 3      | JIT Compilation       | Bytecode is converted to native machine code        |
| 4      | Execution Context     | Global and function contexts manage variable scopes |
| 5      | DOM/CSSOM Interaction | JS interacts with DOM and CSSOM                     |
| 6      | Event Loop            | Handles asynchronous operations                     |
| 7      | Physical Execution    | Native machine code is executed by the CPU          |

<br>

## Step 1: HTML/CSS/JS Fetching

1. When you navigate to a web page (www.site.com), the browser fetches the HTML, CSS, and JavaScript files from the server.

<br>

2. The server listens to requests.

```Javascript
// Fetch the HTML page
fetch('http://www.site.se')
  .then(response => response.text())
  .then(html => {
    // Process HTML
    processHTML(html);
  });

```

<br>

3. Server Returns HTML.

```HTML
<!DOCTYPE html>
<html>
<head>
  <title>Sample Page</title>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<body>
  <h1>Hello, World!</h1>
  <script src="main.js"></script>
</body>
</html>
```

<br>

4. The client browser parses the HTML, and finds the script and stylesheets tags, and then starts loading.

```Javascript
function processHTML(htmlText) {
  // Convert the HTML text into a DOM object
  const parser = new DOMParser();
  const doc = parser.parseFromString(htmlText, 'text/html');

  // Find the script and link (CSS) tags
  const scriptTags = doc.querySelectorAll('script[src]');
  const linkTags = doc.querySelectorAll('link[rel="stylesheet"]');

  // Start loading the JS and CSS
  loadResources(scriptTags, linkTags);
}
```

<br>

5. JS and CSS are fetched

```Javascript
function loadResources(scriptTags, linkTags) {
  // Load each JS file
  scriptTags.forEach(tag => {
    const src = tag.getAttribute('src');
    fetch(src).then(response => response.text()).then(eval);
  });

  // Load each CSS file
  linkTags.forEach(tag => {
    const href = tag.getAttribute('href');
    fetch(href).then(response => response.text()).then(css => {
      const style = document.createElement('style');
      style.innerHTML = css;
      document.head.appendChild(style);
    });
  });
}
```

<br>

6. HTML and CSS rendering starts creating the Document Object Model (DOM) and the CSS Object Model (CSSOM).

- HTML is a **tree structure**, each node in the tree represents a part of the page. The object can be an element node, text node or other (lika attribute nodes).

- DOM nodes contains references to parent, first child, last child, previous sibling, next sibling, essentially forming a **doubly linked** list for traversing in both directions

- For quick lookup elements may be store in hash tables (or dictionaries).

- CSS Ojbect Model (CSSOM) is similar to DOM but each node represents a CSS rule (or declaration block). The roots is generally a stylesheet and it can have multiple rule nodes as children.

- Arrays/lists. Within each rules the individual CSS declarations (like font-size) may be stored in an array or list structure.

- For quick lookup hashtables/dictionaries might be used.

<br>

## Step 2: Parsing and Compilation

1. JavaScript code is parsed by the JavaScript engine in the browser - tokenization/lexical analysis scans the source code and converts it to meaningful chunks, tokens.
2. Parsing converts the source code into an Abstract Syntax Tree (AST).
3. The AST is then converted into bytecode, which is a lower-level representation of your source code but not quite machine code.

## Step 3: Just-In-Time Compilation (JIT)

1. Modern JavaScript engines use Just-In-Time (JIT) compilation to convert bytecode into native machine code for execution.
2. Not all code is JIT-compiled; some might just be interpreted, depending on how frequently it is used.

## Step 4: Execution Context and Stack

1. Execution starts in a global context.
2. Functions, when invoked, get their execution contexts.
3. These contexts are pushed onto the call stack and popped off when execution is complete.

## Step 5: Interaction with DOM/CSSOM

1. JavaScript can interact with the DOM and CSSOM to manipulate the web page.
2. Any changes to the DOM might trigger reflows or repaints in the browser rendering engine.

## Step 6: Event Loop

1. JavaScript is single-threaded, but asynchronous operations like API calls, timers, etc., are handled by the browser's event loop.
2. When asynchronous operations complete, their callbacks are pushed onto the message queue.
3. The event loop checks the message queue and pushes any completed callbacks onto the call stack for execution.

## Step 7: Physical Execution

1. The native machine code is finally executed by the computer's CPU.
2. The browser’s rendering engine updates the webpage if there are changes to the DOM or CSSOM.
