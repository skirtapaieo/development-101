export function transposeMatrix(matrix: number[][]): number[][] {
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


/**
 * Name: Transpose Matrix (In-place)
 * Problem: Given a square matrix, transpose it. That is, flip the matrix over its main diagonal.
 */

export function transposeMatrixInPlace(matrix: number[][]): void {
  const n = matrix.length;

  for (let i = 0; i < n; ++i) {
    for (let j = i + 1; j < n; ++j) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]; // Swap elements
    }
  }
}

// Test case
const mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]];
transposeMatrixInPlace(mat);
console.log(mat);  // Output should be [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

