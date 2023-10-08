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

