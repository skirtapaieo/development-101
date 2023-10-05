
/*

Two Number Sum.

Takes in a non-empty array - of distinct integers.
Also takes in an integer representing a target sum.

If any two numbers in the array sum up to the target sum, the function should return them in an array.

if no two number in the array sum up to the target sum, the function should return an empty array.

The target sum has to be obtained by summing two different integers in the array - you cannot add a singe integer to itself in order to obtain the target sum.

*/

export function twoNumberSum(array: number[], targetSum: number): number[] | [] {

    // sort array in ascending order
    array.sort((a, b) => a - b);
    console.log(array);
    // [ -4, -1, 1, 3, 5, 6, 8, 11 ]

    // initialize two pointers
    let leftPointer: number = 0;
    let rightPointer: number = array.length - 1;

    // loop through array until left pointer is less than right pointer

    while (leftPointer < rightPointer) {
        // Step 1: -4 + 11 = 7 ... 7 < 10 ... move left pointer up one
        // Step 2: -1 + 11 = 10 ... 10 === 10 ... return [ -1, 11 ]
        const currentSum: number = array[leftPointer] + array[rightPointer];

        // if the sum of the two pointers is equal to the target sum, return the two numbers in an array
        if (currentSum === targetSum) {
            return [array[leftPointer], array[rightPointer]];
        }
        // if current sum is less than target sum, move left pointer up one
        else if (currentSum < targetSum) {
            leftPointer++;
        }
        // if current sum is greater than target sum, move right pointer down one
        else if (currentSum > targetSum) {
            rightPointer--;
        }
    }
    // if no two numbers sum up to the target sum, return an empty array
    return [];
}

console.log(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10));


