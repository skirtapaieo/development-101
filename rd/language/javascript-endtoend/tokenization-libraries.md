# Tokenization libraries

## Esprima

Esprima is a high-performance, standard-compliant ECMAScript parsing library. It generates an Abstract Syntax Tree (AST) from JavaScript code, but it also provides tokenization.

GitHub: [Esprima GitHub Repository](https://github.com/jquery/esprima)

**Example of using Esprima for tokenization:**

```javascript
const esprima = require("esprima");
const tokens = esprima.tokenize("var x = 42");
console.log(tokens);
```

## Acorn

Acorn is a small, fast, JavaScript-based JavaScript parser, which also supports tokenization.

GitHub: [Acorn GitHub Repository](https://github.com/acornjs/acorn)

**Example of using Acorn for tokenization:**

```javascript
const acorn = require("acorn");
const tokens = [];
acorn.tokenizer("var x = 42").tokenize((token) => tokens.push(token));
console.log(tokens);
```

## Babel Parser

Babel Parser is part of the Babel toolchain, and it's used to parse ECMAScript proposals that are not yet part of the language standard. It also supports tokenization.

GitHub: [Babel GitHub Repository](https://github.com/babel/babel)

**Example of using Babel Parser for tokenization:**

```javascript
const parser = require("@babel/parser");
const tokens = parser.tokenize("var x = 42");
console.log(tokens);
```
