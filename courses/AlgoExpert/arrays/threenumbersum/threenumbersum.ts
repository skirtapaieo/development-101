
/**
 * Three Number Sum
 *
 * Problem:     Find all triplets in the array - that sum up to the target sum - and return a two-dimensional array - of all these triplets.
 *
 *              Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
 *              The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
 *              The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
 *              If no three numbers sum up to the target sum, the function should return an empty array.
 *
 * Solutions:   Brute force approach: O(n^3) time | O(n) space, use: <50 elements, extremely slow for larger arrays
 *              Hashtable approach: O(n^2) time | O(n) space, use: 50-1000 elements
 *              Two-pointer approach: O(n^2) time | O(n) space, use: >1000 elements
 *
 * Input ex:    array, [12, 3, 1, 2, -6, 5, -8, 6], targetSum = 0
 * Output ex:   two-dimensiontal array, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
 *
 * Misc:        Using Zod for validation/inferring types
 *              Making a range of test (inpu/output) cases, and testing the function
 *
*/

import { z } from 'zod';

const schema = z.object({
    array: z.array(z.number()),
    targetSum: z.number()
});

type Input = z.infer<typeof schema>;

export function threeSumBruteForce(input: Input): number[][] | [] {
    const { array, targetSum } = input;
    const triplets: number[][] = [];
    for (let i = 0; i < array.length; i++) {
        for (let j = i + 1; j < array.length; j++) {
            for (let k = j + 1; k < array.length; k++) {
                if (array[i] + array[j] + array[k] === targetSum) {
                    let triplet = [array[i], array[j], array[k]];
                    triplet.sort((a, b) => a - b);
                    triplets.push(triplet);
                }
            }
        }
    }
    return triplets;
}


export function threeSumHashTable(input: Input): number[][] {
    const { array, targetSum } = input;
    const triplets: number[][] = [];
    for (let i = 0; i < array.length - 1; i++) {
        const seen: Set<number> = new Set();
        for (let j = i + 1; j < array.length; j++) {
            const complement = targetSum - array[i] - array[j];
            if (seen.has(complement)) {
                let triplet = [array[i], array[j], complement];
                triplet.sort((a, b) => a - b);
                triplets.push(triplet);
            } else {
                seen.add(array[j]);
            }
        }
    }
    return triplets;
}

export function threeSumTwoPointer(input: Input): number[][] {
    const { array, targetSum } = input;
    const triplets: number[][] = [];
    array.sort((a, b) => a - b);
    for (let i = 0; i < array.length - 2; i++) {
        let left = i + 1;
        let right = array.length - 1;
        while (left < right) {
            const currentSum = array[i] + array[left] + array[right];
            if (currentSum === targetSum) {
                triplets.push([array[i], array[left], array[right]]);
                left++;
                right--;
            } else if (currentSum < targetSum) {
                left++;
            } else if (currentSum > targetSum) {
                right--;
            }
        }
    }
    return triplets;
}


// Test Function
function testFunction(name: string, func: (input: Input) => number[][], input: Input, expected: number[][]): void {
    const result = func(input);
    console.log(`${name} Test: ${JSON.stringify(result) === JSON.stringify(expected) ? "PASSED" : "FAILED"}`);
    console.log(`Expected: ${JSON.stringify(expected)}`);
    console.log(`Received: ${JSON.stringify(result)}`);
    console.log("------------");
}

// Test cases

// Your function implementations go here
// threeSumBruteForce, threeSumHashTable, threeSumTwoPointer

// Define test cases
const testCases = [
    {
        input: { array: [12, 3, 1, 2, -6, 5, -8, 6], targetSum: 0 },
        expected: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]],
    },
    {
        input: { array: [1, 2, 3], targetSum: 6 },
        expected: [[1, 2, 3]],
    },
    {
        input: { array: [1, 2, 3], targetSum: 7 },
        expected: [],
    },
    {
        input: { array: [8, 10, -2, 49, 14], targetSum: 57 },
        expected: [[-2, 10, 49]],
    },
    {
        input: { array: [12, 3, 1, 2, -6, 5, 0, -8, -1], targetSum: 0 },
        expected: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5], [-1, 0, 1]],
    },
    {
        input: { array: [12, 3, 1, 2, -6, 5, 0, -8, -1, 6], targetSum: 0 },
        expected: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5], [-1, 0, 1]],
    },
    {
        input: { array: [12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], targetSum: 0 },
        // expected: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5], [-5, 0, 5], [-1, 0, 1]],
        expected: [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]]

    },
    {
        input: { array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], targetSum: 18 },
        // expected: [[3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]],
        expected: [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]


    },
    {
        input: { array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], targetSum: 32 },
        expected: [[8, 9, 15]],
    },
    {
        input: { array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], targetSum: 33 },
        expected: []
    },
    {
        input: { array: [1, 2, 3, 4, 5, 6, 7, 8, 9, 15], targetSum: 5 },
        expected: [],
    }
];

// Run test cases
testCases.forEach((testCase, i) => {
    console.log(`Running test case ${i + 1}`);
    console.log(`Input: ${JSON.stringify(testCase.input)}`);

    const outputBruteForce = threeSumBruteForce(testCase.input);
    const outputHashTable = threeSumHashTable(testCase.input);
    const outputTwoPointer = threeSumTwoPointer(testCase.input);

    console.log(`Output using Brute Force: ${JSON.stringify(outputBruteForce)}`);
    console.log(`Output using Hash Table: ${JSON.stringify(outputHashTable)}`);
    console.log(`Output using Two Pointer: ${JSON.stringify(outputTwoPointer)}`);

    console.log(`Expected: ${JSON.stringify(testCase.expected)}`);
    console.log('---');
});



