export function threeNumberSum(arr: number[], target: number): number[][] {
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

