
interface TreeNode {
    value: number;
    left?: TreeNode;
    right?: TreeNode;
}

function twoNumberSum(root: TreeNode, targetSum: number): Number[] | [] {

    const stack: TreeNode[] = [root];
    const set: Set<number> = new Set();

    while (stack.length > 0) {
        const node = stack.pop()!;
        if (node === undefined || node === null) {
            continue;
        }

        if (set.has(targetSum - node.value)) {
            return [node.value, targetSum - node.value];
        }

        set.add(node.value);
        stack.push(node.left!);
        stack.push(node.right!);
    }
    return [];
}

function buildBinarySearchTree(numbers: number[]): TreeNode | null {
    if (numbers.length === 0) {
        return null;
    }

    const sortedNumbers = numbers.slice().sort((a, b) => a - b);

    function buildTree(start: number, end: number): TreeNode | null {
        if (start > end) {
            return null;
        }

        const mid = Math.floor((start + end) / 2);
        const node: TreeNode = { value: sortedNumbers[mid] };
        node.left = buildTree(start, mid - 1);
        node.right = buildTree(mid + 1, end);
        return node;
    }

    return buildTree(0, sortedNumbers.length - 1);
}

const numbers = [3, 5, -4, 8, 11, 1, -1, 6];
const targetSum = 10;

const root = buildBinarySearchTree(numbers);
const result = twoNumberSum(root!, targetSum);

console.log(result); // [11, -1]