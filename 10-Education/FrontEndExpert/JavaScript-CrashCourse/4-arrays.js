
// const arr = [1,2,3]

/* console.log(arr[0]) // 1

console.log(arr.length) // 3

for (let i = 0; i < arr.length; i++) {
    console.log(arr[i])
}

arr.forEach(function(value, index) {
    console.log(value, index, this);
}, {num : 10}); */

/* const mappedArr = arr.map(function(value, index) {
    console.log(value, index, this);
    return value + index + this.num;
}, {num : 10});

console.log(mappedArr);
 */

/* const mappedArr = arr.filter(function(value, index) {
    return value > this.num;
}, {num : 1});

console.log(arr);
console.log(mappedArr); */

/* const mappedArr = arr.reduceRight(function(accumulator, currentValue) {
    return accumulator - currentValue;
}, {num : 0});

console.log(mappedArr); */

const arr = [5,7,3,0];



















arr.sort(compareNumbers);

function compareNumbers(firstNumber, secondNumber) {
    if (firstNumber === 3) {
        return -1;
    }
    if (secondNumber === 3) {
        return 1;
    }
    return firstNumber - secondNumber;
}

console.log(arr);
