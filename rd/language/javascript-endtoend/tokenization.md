# Tokenization (lexical analysis)

Tokenization, also known as lexical analysis, is the first step in parsing and compiling JavaScript code (or any other languag
e, for that matter). In this step, the source code is read character by character, and those characters are grouped into tokens. Tokens are the language elements that are meaningful to the compiler, such as keywords, identifiers, operators, and literals.

### JavaScript Code Example

```javascript
var x = 10 + 20;
```

### Detailed Tokenization Steps

1. **Read Characters**: Start by reading the source code one character at a time.
2. **Identify Tokens**: As each character is read, it is grouped with adjacent characters to form tokens based on rules (i.e., the lexical grammar of JavaScript).

For our example, the tokens could be:

- `var` (keyword)
- ` ` (whitespace, usually ignored in further processing)
- `x` (identifier)
- ` ` (whitespace)
- `=` (operator)
- ` ` (whitespace)
- `10` (numeric literal)
- ` ` (whitespace)
- `+` (operator)
- ` ` (whitespace)
- `20` (numeric literal)
- `;` (punctuation)

### Example Token Types and Values

Here is how the tokens might be represented internally:

```plaintext
| Token Type      | Token Value |
|-----------------|-------------|
| Keyword         | var         |
| Identifier      | x           |
| Operator        | =           |
| NumericLiteral  | 10          |
| Operator        | +           |
| NumericLiteral  | 20          |
| Punctuation     | ;           |
```

### Code Example for Simple Tokenizer

A naive JavaScript tokenizer for this example could look like:

```javascript
function tokenize(code) {
  const tokens = [];
  let currentToken = "";

  for (let i = 0; i < code.length; i++) {
    const char = code[i];
    if ([" ", "=", "+", ";"].includes(char)) {
      if (currentToken) {
        tokens.push(currentToken);
      }
      if (char !== " ") {
        tokens.push(char);
      }
      currentToken = "";
    } else {
      currentToken += char;
    }
  }

  return tokens;
}

console.log(tokenize("var x = 10 + 20;")); // Output: ['var', 'x', '=', '10', '+', '20', ';']
```

Note: This is an overly simplified example. Real-world tokenizers need to handle a much wider variety of cases, including different kinds of literals, complex operators, comments, etc.
