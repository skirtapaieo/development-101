

/* const arr = [5,7,3,0];

const double = num => num * 2; // implicit return
const doubled = arr.map(double);{
    return value * 2;
});

console.log(doubled); */

/* const arr = [5,7,3,0];

const[first,second] = arr;
// const first = arr[0];
// const second = arr[1];

console.log(arr); */

/* const arr = [5,7,3,0];

const person = {
    name: 'Neha',
    website: 'algoexpert.io',
};

const {name: firstName, ...rest } = person;
console.log(firstName);
console.log(rest); */

/* const arr = [5,7,3,0];

function add(x,y) {
    return x + y);
}

add(...arr);
 */

/* const arr = [1,2,3,4];
const arr2 = [5,6,7];
const combined = [0, ...arr, ...arr2, 8, 9, 10];
 */

/* const arr = [1,2,3,4];

function logParams(x, ...rest) {
    console.log(x, rest);
}

logParams(...arr); */


/* const name= 'Neha';

console.log(`Hello ${name}`); */

/* const person = {
    company: {
        website: 'algoexpert.io',
    }

    console.log(person?.company?.website ?? 'foo');
 */

const shouldRunCode = true;

function logWorld() {
    console.log('world');
}

shouldRunCode && logWorld();