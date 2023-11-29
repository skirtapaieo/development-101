
#!/bin/bash

# TransposeMatrix.ts
echo "export function transposeMatrix(matrix: number[][]): number[][] {
  const rows = matrix.length;
  const cols = matrix[0].length;
  const transposed: number[][] = Array.from({ length: cols }, () => Array(rows).fill(0));

  for (let i = 0; i < rows; ++i) {
    for (let j = 0; j < cols; ++j) {
      transposed[j][i] = matrix[i][j];
    }
  }

  return transposed;
}
" > TransposeMatrix.ts

# ThreeNumberSum.ts
echo "export function threeNumberSum(arr: number[], target: number): number[][] {
  arr.sort((a, b) => a - b);
  const triplets: number[][] = [];

  for (let i = 0; i < arr.length - 2; i++) {
    let left = i + 1, right = arr.length - 1;
    while (left < right) {
      const currentSum = arr[i] + arr[left] + arr[right];
      if (currentSum === target) {
        triplets.push([arr[i], arr[left], arr[right]]);
        left++;
        right--;
      } else if (currentSum < target) {
        left++;
      } else {
        right--;
      }
    }
  }
  return triplets;
}
" > ThreeNumberSum.ts

# SmallestDifference.ts
echo "export function smallestDifference(arr1: number[], arr2: number[]): [number, number] {
  arr1.sort((a, b) => a - b);
  arr2.sort((a, b) => a - b);
  let i = 0, j = 0;
  let smallest = Infinity, current = Infinity;
  let smallestPair: [number, number] = [0, 0];

  while (i < arr1.length && j < arr2.length) {
    const first = arr1[i], second = arr2[j];
    current = Math.abs(first - second);
    if (current < smallest) {
      smallest = current;
      smallestPair = [first, second];
    }
    if (first < second) i++;
    else j++;
  }
  return smallestPair;
}
" > SmallestDifference.ts

# MoveElementToEnd.ts
echo "export function moveElementToEnd(arr: number[], toMove: number): number[] {
  let i = 0, j = arr.length - 1;

  while (i < j) {
    while (i < j && arr[j] === toMove) j--;
    if (arr[i] === toMove) [arr[i], arr[j]] = [arr[j], arr[i]];
    i++;
  }

  return arr;
}
" > MoveElementToEnd.ts

echo "TypeScript files have been generated."
