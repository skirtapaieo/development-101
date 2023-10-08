
/**
 * Name:        Juice Bottling
 *
 * Problem:    Determine the optimal way to bottle the juice such that it maximizes revenue.
 *
 * Details:    Given an array of integers "prices" of length n, each index in this array
 *             corresponds to the price of that amount of juice.
 *             Return a list of all of the juice quantities required in ascending order.
 *
 * Variations:  Varying lengths and values of the input array "prices".
 *
 * Solutions:   Dynamic Programming: O(n^2) time | O(n) space
 *                 size of input: works for moderate-sized arrays
 *                 revenue maximization: most effective for this specific problem
 *
 * Language:    TypeScript
 *
 * Performance: Time complexity is quadratic (O(n^2)) and space complexity is linear (O(n)).
 *
 * Dependencies: None
 *
 * Validation:  None
 *
 * Edge cases:  First value in the prices array will always be 0, and all other values are positive.
 *
 * Test cases:  Test cases are provided below the code snippet.
 *
 * Input ex:    [0, 1, 3, 2]
 *
 * Output ex:   [1, 2]
 *
 * Comments:    Typedoc: https://typedoc.org/
 *
 * Author:      Your Name Here, https://github.com/your-github-username
 *
*/

export function juiceBottling(prices: number[]): number[] {
    const numSizes = prices.length - 1; // n - 1 units of juice
    const maxProfit = new Array(numSizes + 1).fill(0);
    const dividingPoints = new Array(numSizes + 1).fill(0);

    for (let size = 1; size <= numSizes; size++) {
        for (let dividingPoint = 1; dividingPoint <= size; dividingPoint++) {
            const possibleProfit = maxProfit[size - dividingPoint] + prices[dividingPoint];

            if (possibleProfit > maxProfit[size]) {
                maxProfit[size] = possibleProfit;
                dividingPoints[size] = dividingPoint;
            }
        }
    }

    const solution: number[] = [];
    let currentDividingPoint = numSizes;
    while (currentDividingPoint > 0) {
        solution.push(dividingPoints[currentDividingPoint]);
        currentDividingPoint -= dividingPoints[currentDividingPoint];
    }

    // Sort the solution in ascending order
    return solution.sort((a, b) => a - b);
}

// Test Cases
console.log(juiceBottling([0, 1])); // [1]
console.log(juiceBottling([0, 1, 3])); // [1, 1]
console.log(juiceBottling([0, 2, 3])); // [1, 1]
console.log(juiceBottling([0, 2, 3, 4])); // [1, 2]
console.log(juiceBottling([0, 2, 5, 6])); // [2, 2]
console.log(juiceBottling([0, 2, 5, 6, 7])); // [2, 3]
console.log(juiceBottling([0, 2, 5, 6, 11])); // [3, 4]
