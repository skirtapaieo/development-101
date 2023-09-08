# Rust and WebAssembly

## JavaScript - first class support for front-end development

first class support for front-end development it generally means that the language has libraries, frameworks, and tooling specifically designed to facilitate building front-end applications. This includes but is not limited to:

- Libraries for DOM manipulation
- UI frameworks
- Bundlers and package managers
- Debugging tools
- Tutorials and community support

JavaScript has first-class support for front-end development because it's designed to work natively in web browsers and has extensive libraries and frameworks like React, Angular, and Vue.js, among others.

## WebAssembly (Wasm)

WebAssembly is a binary instruction format that allows high-level languages like C, C++, and Rust to run in a web browser.

It serves as a compilation target for these languages, enabling them to run at near-native speed by taking advantage of common hardware capabilities.

### Principles

1. **Performance**: WebAssembly is designed to be fast to decode and execute.
2. **Safe Execution**: It runs inside a sandboxed execution environment to ensure safety.
3. **Open Standard**: WebAssembly is an open standard developed by a W3C Community Group.

##### Rust to WebAssembly

To compile Rust code to WebAssembly, you'll first need to install the Rust toolchain and `wasm-pack`. Then, you can create a new Rust project and build it as a WebAssembly package.

1. Install Rust and wasm-pack:

   ```bash
   curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
   cargo install wasm-pack
   ```

2. Create a new Rust library:

   ```bash
   cargo new --lib hello-wasm
   cd hello-wasm
   ```

3. Modify `src/lib.rs`:

   ```rust
   #[wasm_bindgen]
   extern "C" {
       pub fn alert(s: &str);
   }

   #[wasm_bindgen]
   pub fn greet(name: &str) {
       alert(&format!("Hello, {}!", name));
   }
   ```

4. Build the WebAssembly package:
   ```bash
   wasm-pack build
   ```

##### C/C++ to WebAssembly using Emscripten

1. Install Emscripten:

   ```bash
   git clone https://github.com/emscripten-core/emsdk.git
   cd emsdk
   ./emsdk install latest
   ./emsdk activate latest
   ```

2. Create a C file named `hello.c`:

   ```c
   #include <stdio.h>

   int main() {
       printf("Hello, WebAssembly!\n");
       return 0;
   }
   ```

3. Compile to WebAssembly:
   ```bash
   emcc hello.c -o hello.html
   ```

In both examples, you'll end up with a `.wasm` file that you can load into a web page to run the code.

These are just brief examples. Each language has its ecosystem and tooling for WebAssembly, and the workflow can differ. Rust, for example, has `wasm-bindgen` for interfacing with JavaScript, and Emscripten provides a full POSIX-like environment for C/C++ code.
