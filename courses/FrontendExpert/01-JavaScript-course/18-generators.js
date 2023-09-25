function* getNumbers(count) {
  for (let i = 0; i < count; i++) {
    yield Math.random();
  }
}

const generator = getNumbers(3);

for (value of generator) {
  generator.return(value);
}

console.log(generator.next());
