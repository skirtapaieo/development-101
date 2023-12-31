
/*

Two Number Sum.


Takes in a non-empty array - of distinct integers.

Also takes in an integer representing a target sum.

If any two numbers in the array sum up to the target sum, the function should return them in an array.

if no two number in the array sum up to the target sum, the function should return an empty array.

The target sum has to be obtained by summing two different integers in the array - you cannot add a singe integer to itself in order to obtain the target sum.

*/

export function twoNumberSum(array: Number[], targetsum: Number): Number[] | [] {

    const hashTable: { [key: number]: boolean } = {};

    for (const number of array) {
        // Step 1: 10 - 3 = 7 ... 7 in hashTable? ... no ... add 3 to hashTable
        // Step 2: 10 - 5 = 5 ... 5 in hashTable? ... no ... add 5 to hashTable
        // Step 3: 10 - -4 = 14 ... 14 in hashTable? ... no ... add -4 to hashTable
        // Step 4: 10 - 8 = 2 ... 2 in hashTable? ... no ... add 8 to hashTable
        // Step 5: 10 - 11 = -1 ... -1 in hashTable? ... no ... add 11 to hashTable
        // Step 6: 10 - 1 = 9 ... 9 in hashTable? ... no ... add 1 to hashTable
        // Step 7: 10 - -1 = 11 ... 11 in hashTable? ... yes ... return [ 11, -1 ]

        const potentialMatch: number = targetsum - number;
        if (potentialMatch in hashTable) {
            return [potentialMatch, number];
        } else {
            hashTable[number] = true;
        }
    }
}

console.log(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10));
