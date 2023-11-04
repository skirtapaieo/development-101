// Create an object
const myObj = {
  name: "John",
};

// Object.prototype is the "grandparent" of all objects
console.log(Object.prototype); // Output: {...} (The base prototype object)

// __proto__ is a reference to myObj's parent prototype
console.log(myObj.__proto__); // Output: {...} (Same as Object.prototype for this example)

// Get the prototype using Object.getPrototypeOf()
console.log(Object.getPrototypeOf(myObj) === myObj.__proto__); // Output: true

// Create a new prototype object
const newProto = {
  sayHello: function () {
    console.log(`Hello, ${this.name}`);
  },
};

// Set the new prototype using Object.setPrototypeOf()
Object.setPrototypeOf(myObj, newProto);

// Now, myObj can use methods from newProto
myObj.sayHello(); // Output: "Hello, John"
