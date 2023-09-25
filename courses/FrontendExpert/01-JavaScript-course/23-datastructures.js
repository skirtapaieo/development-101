// Data Structures

// Stack

const stack = [];
stack.push("google.com");
stack.push("instagram.com");

console.log(stack.pop());

// Queue

const queue = [];
queue.push("google.com");
queue.push("instagram.com");

console.log(queue.shift()); // use pop!

// Map

const map = new Map();
map.set("google.com", 123);
map.set("instagram.com", 456);

console.log(map.get("google.com"));

const iter = map.entries();
console.log(iter.next());
console.log(iter.next());
console.log(iter.next());

// Set

// WeakMap

// Weak Set

// Linked list
