
/**
 * Three Number Sum
 *
 * Solution:    Find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
 *
 * Problem:     Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum.
 *              The function should find all triplets in the array that sum up to the target sum and return a two-dimensional array of all these triplets.
 *              The numbers in each triplet should be ordered in ascending order, and the triplets themselves should be ordered in ascending order with respect to the numbers they hold.
 *              If no three numbers sum up to the target sum, the function should return an empty array.
 *
 * Input ex:    array, [12, 3, 1, 2, -6, 5, -8, 6], targetSum = 0
 * Output ex:   two-dimensiontal array, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
 *
 * Approaches:  Brute force approach: O(n^3) time | O(n) space, use: <50 elements, extremely slow for larger arrays
 *              Hashtable approach: O(n^2) time | O(n) space, use: 50-1000 elements
 *              Two-pointer approach: O(n^2) time | O(n) space, use: >1000 elements
 *
 * Complexity:  See above approaches
 *
 * Language:    Typescript, Zod (for input validation)
 *
*/

import { z } from 'zod';

const schema = z.object({
    array: z.array(z.number()),
    targetSum: z.number()
});

type Input = z.infer<typeof schema>;

export function threeSumBruteForce(input: Input): number[][] {
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

// Test cases for each algorithm

describe('Three Number Sum', () => {
    const testInput = { array: [12, 3, 1, 2, -6, 5, -8, 6], targetSum: 0 };
    const expectedOutput = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]];

    test('Brute force approach', () => {
        expect(threeSumBruteForce(testInput)).toEqual(expectedOutput);
    });

    test('Hash table approach', () => {
        expect(threeSumHashTable(testInput)).toEqual(expectedOutput);
    });

    test('Two-pointer approach', () => {
        expect(threeSumTwoPointer(testInput)).toEqual(expectedOutput);
    });
});

console.log("Hello via Bun!");