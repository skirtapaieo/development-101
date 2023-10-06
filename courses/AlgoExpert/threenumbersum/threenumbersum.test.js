
import { threeSumBruteForce, threeSumHashTable, threeSumTwoPointer } from './threenumbersum';

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
