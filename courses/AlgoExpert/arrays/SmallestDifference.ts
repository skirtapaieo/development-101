export function smallestDifference(arr1: number[], arr2: number[]): [number, number] {
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

