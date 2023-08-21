
/*
const funcProto = Object.getPrototypeOf(() => {});
console.log(Object.getOwnPropertyNames(funcProto));
 */

/* function Person(name) {
    this.name = name;
}

Person.prototype = {
    constructor: Person,
    isHuman: true,
};

const patrik = new Person('Patrik');
const bosse = new patrik.constructor('Bosse');

Person.prototype.speak = function() {
    console.log(`Hello my name is ${this.name}`);
}

 */

/* Array.prototype.myPush = function(value) {
    this[this.length] = value;
}

const arr = [1,2,3];
arr.myPush(4);
console.log(arr);
 */


class Person {
    static isHuman = true;
    constructor(name) {
        this.name = name;
    }
    static greet() {
        console.log('Hello');
    speak() {
        console.log(`Hello my name is ${this.name}`);
    }
}

const patrik = new Person('Patrik');
const bosse = new Person('Bosse');
patrik.speak();
console.log(patrik.isHuman);
