# General questions

- [General questions](#general-questions)
  - [Type of variables in JavaScript?](#type-of-variables-in-javascript)
  - [Difference between const, let, var](#difference-between-const-let-var)
    - [Brief Description and Examples](#brief-description-and-examples)
      - [`var`](#var)
      - [`let`](#let)
      - [`const`](#const)
  - [What is hoisting and why does it exist?](#what-is-hoisting-and-why-does-it-exist)
    - [What is Hoisting?](#what-is-hoisting)
    - [Why Does Hoisting Exist?](#why-does-hoisting-exist)
    - [Practical Implications](#practical-implications)
    - [Hoisting with `let` and `const`](#hoisting-with-let-and-const)
  - [What is Object.prototype and proto (and example with getPrototypeOf and setPrototypeOf)](#what-is-objectprototype-and-proto-and-example-with-getprototypeof-and-setprototypeof)
    - [Example](#example)
    - [Summary](#summary)
  - [What is the difference between a normal function and an arrow function?](#what-is-the-difference-between-a-normal-function-and-an-arrow-function)
- [What is a promise?](#what-is-a-promise)

  - [Key Points](#key-points)
  - [Code Examples](#code-examples)
    - [Creating a Promise](#creating-a-promise)
    - [Using `.then()` and `.catch()`](#using-then-and-catch)
    - [Using `Promise.all()`](#using-promiseall)
    - [Async/Await Syntax](#asyncawait-syntax)
    - [What did promises "replace"?](#what-did-promises-replace)
  - [How do we use promises outside of asynch and await?](#how-do-we-use-promises-outside-of-asynch-and-await)
    - [Key Points](#key-points-1)
    - [Code Example](#code-example)

- [What does immutable/mutable mean? What about in React?](#what-does-immutablemutable-mean-what-about-in-react)
- [What is closure? Give examples.](#what-is-closure-give-examples)
- [Why are block-scoped (rather than function-scope) variables not available after we have exited a function?](#why-are-block-scoped-rather-than-function-scope-variables-not-available-after-we-have-exited-a-function)
- [Tell me everything about front-end caching (and caching in general)](#tell-me-everything-about-front-end-caching-and-caching-in-general)
- [What is the difference between local and session storage?](#what-is-the-difference-between-local-and-session-storage)
- [How to use Redis?](#how-to-use-redis)
- [What are cookies and what do we use them for?](#what-are-cookies-and-what-do-we-use-them-for)
- [What is HTTP and REST?](#what-is-http-and-rest)
- [Which HTTP verbs are there and when are they used?](#which-http-verbs-are-there-and-when-are-they-used)
- [Explain the lifecycles of a react component? (mounted, rerendered and unmounted)](#explain-the-lifecycles-of-a-react-component-mounted-rerendered-and-unmounted)
- [Tell me everything about useEffect?](#tell-me-everything-about-useeffect)
- [How do class components differ from functional components (not syntactically, in relation to state management)](#how-do-class-components-differ-from-functional-components-not-syntactically-in-relation-to-state-management)
- [MOBX - how do we make react components observable? What are computed values? what are the things to look out for using MOBX and how do we improve its performance?](#mobx-how-do-we-make-react-components-observable-what-are-computed-values-what-are-the-things-to-look-out-for-using-mobx-and-how-do-we-improve-its-performance)

## Type of variables in JavaScript?

In JavaScript, variables can be of various types.

Below is a table that outlines the different types:

Mnemonic: NUBBSON to remember that they are eight and give hints on which :-)

| Type      | Description                                                          | Example                   |
| --------- | -------------------------------------------------------------------- | ------------------------- |
| Number    | Represents both integer and floating-point numbers.                  | `42`, `3.14`              |
| String    | Represents a sequence of characters.                                 | `"Hello"`, `'world'`      |
| Boolean   | Represents either `true` or `false`.                                 | `true`, `false`           |
| Undefined | A variable that has been declared but has not been assigned a value. | `let x;`                  |
| Null      | Represents a "nothing" or "empty" value.                             | `null`                    |
| Object    | Can store a collection of data and more complex entities.            | `{name: "John", age: 30}` |
| Symbol    | Represents a unique value that's not equal to any other value.       | `Symbol('description')`   |
| BigInt    | Can represent integers in arbitrary precision.                       | `9007199254740991n`       |

JavaScript is a dynamically-typed language, meaning variables do not need to be declared as a specific type. However, the language introduced "TypeScript," a statically-typed superset of JavaScript, to allow for type checking and other features.

```javascript
let a = 42; // Number
let b = "Hello World"; // String
let c = true; // Boolean
let d; // Undefined
let e = null; // Null
let f = { name: "Alice" }; // Object
let g = Symbol("sym"); // Symbol
let h = 123n; // BigInt
```

## Difference between const, let, var

Use let when you plan to reassign new values to a variable and const when you don't. Don't use var, it has hoisting quirks.

In JavaScript, `const`, `let`, and `var` are known as variable declaration keywords. They are used to declare variables in different scopes and with different behaviors. Here's a table to summarize their differences:

| Keyword | Scope          | Hoisting             | Re-assignable | Re-declarable |
| ------- | -------------- | -------------------- | ------------- | ------------- |
| `var`   | Function-scope | Yes                  | Yes           | Yes           |
| `let`   | Block-scope    | Yes, not initialized | Yes           | No            |
| `const` | Block-scope    | Yes, not initialized | No            | No            |

### Brief Description and Examples:

#### `var`:

- **Scope**: Function-scope
- **Hoisting**: Yes, but initialized as `undefined`
- **Re-assignable**: Yes
- **Re-declarable**: Yes

```js
function exampleVar() {
  console.log(a); // undefined
  var a = 10;
  console.log(a); // 10
}
```

#### `let`:

- **Scope**: Block-scope
- **Hoisting**: No
- **Re-assignable**: Yes
- **Re-declarable**: No

```js
{
  // console.log(b); // ReferenceError
  let b = 20;
  console.log(b); // 20
}
```

#### `const`:

- **Scope**: Block-scope
- **Hoisting**: No
- **Re-assignable**: No
- **Re-declarable**: No

```js
{
  // console.log(c); // ReferenceError
  const c = 30;
  console.log(c); // 30
  // c = 40; // TypeError
}
```

## What is hoisting and why does it exist?

### What is Hoisting?

Hoisting is a behavior in JavaScript where variable and function declarations are moved, or "hoisted," to the top of their containing scope during compilation. However, only the declarations are hoisted, not the initializations. This means that variables declared with `var` are initialized with `undefined`, and function declarations are fully hoisted, making them accessible even before the code that defines them is executed.

### Example of Hoisting with `var`

```js
console.log(a); // Output: undefined
var a = 5;
console.log(a); // Output: 5
```

In this example, the `var a` declaration is hoisted to the top of the code, but not its initialization (`= 5`).

### Example of Hoisting with Function Declarations

```js
console.log(foo()); // Output: "Hello"
function foo() {
  return "Hello";
}
```

Here, the entire function `foo` is hoisted, so it can be called before the function definition in the code.

### Why Does Hoisting Exist?

Hoisting exists mainly due to the way JavaScript is interpreted by the engine. The JavaScript engine scans through the code and compiles it before running it. During this compilation phase, it identifies variable and function declarations and hoists them to maintain scopes.

### Practical Implications

1. **Variable Initialization**: When using `var`, it's easy to run into issues where you think a variable has been initialized, but it's actually `undefined`.
2. **Function Ordering**: You can call functions before they appear in your code if they are function declarations. However, function expressions are not hoisted.

### Hoisting with `let` and `const`

Variables declared with `let` and `const` are not initialized and accessing them before their declaration in the code will result in a `ReferenceError`.

```js
console.log(b); // ReferenceError: Cannot access 'b' before initialization
let b = 10;
```

Understanding hoisting helps to prevent bugs and understand the code's behavior, especially when working with `var` or functions. It's generally advisable to declare and initialize variables and functions at the top of their scope to make the code more readable and predictable.

<br>

## What is Object.prototype and proto (and example with getPrototypeOf and setPrototypeOf)

The `Object.prototype` is essentially the "grandparent" of all objects in JavaScript. It serves as a common repository of properties and methods that all objects inherit by default. The `__proto__` property is a reference to the object's parent prototype. In contrast, `Object.prototype` is the object from which other objects inherit properties and methods.

`Object.getPrototypeOf()` and `Object.setPrototypeOf()` are methods for directly getting and setting an object's prototype.

### Example:

Here's a simple example to demonstrate `Object.prototype`, `__proto__`, `Object.getPrototypeOf()`, and `Object.setPrototypeOf()`.

```javascript
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
```

### Summary

| Term                      | Description                                | Example                                  |
| ------------------------- | ------------------------------------------ | ---------------------------------------- |
| `Object.prototype`        | The base prototype for all objects.        | `Object.prototype`                       |
| `__proto__`               | Reference to an object's parent prototype. | `myObj.__proto__`                        |
| `Object.getPrototypeOf()` | Gets an object's parent prototype.         | `Object.getPrototypeOf(myObj)`           |
| `Object.setPrototypeOf()` | Sets an object's parent prototype.         | `Object.setPrototypeOf(myObj, newProto)` |

Note that manipulating an object's prototype with `Object.setPrototypeOf()` can lead to performance issues and is generally not recommended for performance-critical code.

<br>

## What is the difference between a normal function and an arrow function?

Mnemonic: NAIGANAMF
Now an intelligent genious acts naturally, acquires methods fast

JavaScript have several type of functions.

Each type serves specific purposes and has its own use-cases. Learning when and how to use each type will improve your JavaScript skills.

| Function Type       | Description                                                                                             |
| ------------------- | ------------------------------------------------------------------------------------------------------- |
| Generator Functions | Functions that return an iterator. Use `function*` syntax and `yield`.                                  |
| Async Functions     | Functions that return a Promise. Use `async` and `await` for asynchronous operations.                   |
| IIFE                | Immediately Invoked Function Expressions run as soon as they are defined.                               |
| Callback Functions  | Functions passed as arguments to other functions.                                                       |
| Anonymous Functions | Functions without a name, usually used as a one-time operation.                                         |
| Named Functions     | Functions with a name, useful for recursion and debugging.                                              |
| Method              | Functions defined inside objects or classes.                                                            |
| Pure Functions      | Functions where the output value is determined only by its input, without side effects.                 |
| Higher-Order        | Functions that take other functions as parameters or return a function.                                 |
| First-Class         | Functions that can be assigned to a variable, passed as an argument, or returned from another function. |

### Key points

- Normal Function: Versatile and can be used in most scenarios. Useful when dynamic this binding is needed.
- Arrow Function: Great for short callbacks or anonymous functions. Lexical binding of this.
- IIFE: Used mainly for data privacy and creating a new variable environment.
- Generator Function: Special function that can pause its execution and is generally used for implementing custom iterators.
- Async Function: Designed to work with Promises and make asynchronous code look like synchronous code.
- Named Function: Use when the function is recursive or when it improves code readability and debuggability.
- Anonymous Function: Use for quick, disposable functionality.
- Method: Special functions that are part of objects/classes.
- Function Expression: When you need to pass a function as an argument to another function, function expressions are very useful.

<br>

## What is a promise?

Promises are powerful and form the backbone of modern asynchronous JavaScript code. They make it easier to write clean, maintainable, and robust code.

In JavaScript, a Promise **is an object representing the eventual completion (or failure) of an asynchronous operation and its resulting value**. A Promise can be in one of three states:

- **Pending**: Initial state, neither fulfilled nor rejected.
- **Fulfilled**: The operation is completed successfully.
- **Rejected**: The operation failed.

### Key Points:

1. **Constructor Syntax**: Created using `new Promise(executor)`

   ```javascript
   const myPromise = new Promise((resolve, reject) => {
     // Async operation here
   });
   ```

2. **Chaining**: `.then()` and `.catch()` methods can be chained to handle resolved or rejected states.

   ```javascript
   myPromise
     .then((result) => console.log(result))
     .catch((error) => console.error(error));
   ```

3. **Error Handling**: Use `.catch()` or `.finally()` to handle errors and cleanup.

   ```javascript
   myPromise
     .finally(() => console.log("Done"))
     .catch((error) => console.error(error));
   ```

4. **Built-in Methods**: `Promise.all()`, `Promise.race()`, `Promise.resolve()`, and `Promise.reject()` are useful static methods.
   ```javascript
   Promise.all([promise1, promise2])
     .then(([result1, result2]) => /* do something */);
   ```

### Code Examples:

1. **Creating a Promise**

   ```javascript
   const myPromise = new Promise((resolve, reject) => {
     const success = true; // Simulate success
     if (success) {
       resolve("Operation successful");
     } else {
       reject("Operation failed");
     }
   });
   ```

2. **Using `.then()` and `.catch()`**

   ```javascript
   myPromise
     .then((result) => {
       console.log(result); // Output: "Operation successful"
     })
     .catch((error) => {
       console.error(error); // Output: "Operation failed"
     });
   ```

3. **Using `Promise.all()`**

   ```javascript
   const promise1 = Promise.resolve(1);
   const promise2 = Promise.resolve(2);

   Promise.all([promise1, promise2]).then(([result1, result2]) => {
     console.log(result1, result2); // Output: 1 2
   });
   ```

4. **Async/Await Syntax**
   ```javascript
   async function fetchData() {
     try {
       const result = await myPromise;
       console.log(result); // Output: "Operation successful"
     } catch (error) {
       console.error(error); // Output: "Operation failed"
     }
   }
   fetchData();
   ```

### What did promises "replace"?

Promises offer a more structured, flexible, and readable way to handle asynchronous operations compared to callbacks and event listeners. They make it easier to handle errors and to write asynchronous code that is clean and maintainable.

Before promises, the primary mechanisms for handling asynchronous operations in JavaScript were:

1. **Callbacks**: A callback function is passed as an argument to another function and is executed after its parent function has completed.
2. **Event Listeners**: Certain types of objects dispatch events, and you can write listeners to respond to those events.

### Key Points:

1. **Callback Hell**: Deep nesting of callbacks can lead to unreadable and unmanageable code, often referred to as "Callback Hell" or the "Pyramid of Doom."

   ```javascript
   asyncFunction1(param1, function (result1) {
     asyncFunction2(result1, function (result2) {
       asyncFunction3(result2, function (result3) {
         // ... and so on
       });
     });
   });
   ```

2. **Event Listeners**: They are more suitable for certain types of asynchronous operations, but they can be cumbersome for others.
   ```javascript
   const xhr = new XMLHttpRequest();
   xhr.addEventListener("load", function () {
     // Do something with `xhr.responseText`
   });
   xhr.open("GET", "https://api.example.com/data");
   xhr.send();
   ```

### Code Example Showing Promise vs Callback:

**Using Callbacks**

```javascript
function fetchData(callback) {
  setTimeout(() => {
    callback("Data fetched");
  }, 1000);
}

fetchData((result) => {
  console.log(result); // Output: "Data fetched"
});
```

**Using Promises**

```javascript
function fetchData() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve("Data fetched");
    }, 1000);
  });
}

fetchData().then((result) => {
  console.log(result); // Output: "Data fetched"
});
```

## How do we use promises outside of asynch and await?

Using promises with `.then()`, `.catch()`, and `.finally()` gives you the ability to work with asynchronous operations in a structured manner.

Using promises without `async/await` involves methods like `.then()`, `.catch()`, and `.finally()`. Here's how to use each:

### Key Points:

1. **`.then()`:** Called when the Promise is resolved.

   ```javascript
   fetchData().then((data) => {
     console.log(data); // Do something with data
   });
   ```

2. **`.catch()`:** Called when the Promise is rejected.

   ```javascript
   fetchData().catch((error) => {
     console.error(error); // Handle the error
   });
   ```

3. **`.finally()`:** Always called, regardless of whether the Promise was resolved or rejected.
   ```javascript
   fetchData().finally(() => {
     console.log("Done"); // Always executed
   });
   ```

### Code Example:

**Basic Usage**

```javascript
const fetchData = () => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Change true to false to see catch in action
      if (true) {
        resolve("Data fetched");
      } else {
        reject("Failed to fetch data");
      }
    }, 1000);
  });
};

// Using then, catch, and finally
fetchData()
  .then((data) => console.log(data)) // Output: "Data fetched"
  .catch((error) => console.error(error))
  .finally(() => console.log("Done")); // Output: "Done"
```

**Chaining Promises**

```javascript
const fetchMoreData = (prevData) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve(prevData + " and more data");
    }, 500);
  });
};

fetchData()
  .then((data) => {
    console.log(data); // Output: "Data fetched"
    return fetchMoreData(data);
  })
  .then((moreData) => {
    console.log(moreData); // Output: "Data fetched and more data"
  })
  .catch((error) => {
    console.error(error);
  })
  .finally(() => {
    console.log("All done"); // Output: "All done"
  });
```

## What does immutable/mutable mean? What about in React?

## What is closure? Give examples.

## Why are block-scoped (rather than function-scope) variables not available after we have exited a function?

## Tell me everything about front-end caching (and caching in general)

## what is the difference between local and session storage?

## How to use Redis?

## What are cookies and what do we use them for?

## What is HTTP and REST?

## Which HTTP verbs are there and when are they used?

## Explain the lifecycles of a react component? (mounted, rerendered and unmounted)

## Tell me everything about useEffect?

## How do class components differ from functional components (not syntactically, in relation to state management)

## MOBX - how do we make react components observable? What are computed values? what are the things to look out for using MOBX and how do we improve its performance?
