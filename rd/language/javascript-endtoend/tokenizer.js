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
