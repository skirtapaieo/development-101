# Webassembly and JavaScript

JavaScript and WebAssembly (Wasm) are both technologies that enable web development, but they serve different purposes and complement each other.

Here's how they're connected:

### Interoperability:

1. **Call JavaScript from WebAssembly**: WebAssembly modules can import JavaScript functions and call them as if they were native functions.
2. **Call WebAssembly from JavaScript**: You can instantiate WebAssembly modules in JavaScript and call their exported functions just like regular JavaScript functions.

### Execution Environment:

- Both JavaScript and WebAssembly run in the same web environment and share the same runtime capabilities. They can both access web APIs like the DOM, although WebAssembly needs to do this through JavaScript currently.

### Performance:

- WebAssembly is designed for speed and can execute at near-native speed by taking advantage of common hardware capabilities. This makes WebAssembly suitable for performance-critical tasks that JavaScript might struggle with.

### Use Cases:

- JavaScript is great for building dynamic, interactive websites and applications.
- WebAssembly can handle computationally intensive tasks, such as 3D graphics in games, real-time video encoding, and large-scale scientific computations.

### Code Example:

Here's a simple example where JavaScript interacts with a WebAssembly module. Assume you have a WebAssembly function `add` compiled from either C, C++, or Rust.

```javascript
// JavaScript code to fetch and instantiate a WebAssembly module
fetch("add.wasm")
  .then((response) => response.arrayBuffer())
  .then((bytes) =>
    WebAssembly.instantiate(bytes, {
      env: {
        // JavaScript functions can be imported into WebAssembly here
      },
    })
  )
  .then((results) => {
    // `add` is a WebAssembly function
    const add = results.instance.exports.add;

    // Call WebAssembly function from JavaScript
    console.log(add(2, 3)); // Output: 5
  });
```

In this example, the WebAssembly module for the `add` function is fetched and instantiated using JavaScript. Once that's done, you can call `add` just like any other JavaScript function.

So, the connection between JavaScript and WebAssembly is quite tight. They're designed to work together seamlessly, allowing developers to use each where it most makes sense and even mix them in a single project.
