export function moveElementToEnd(arr: number[], toMove: number): number[] {
  let i = 0, j = arr.length - 1;

  while (i < j) {
    while (i < j && arr[j] === toMove) j--;
    if (arr[i] === toMove) [arr[i], arr[j]] = [arr[j], arr[i]];
    i++;
  }

  return arr;
}

