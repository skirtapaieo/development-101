
/**
 * Depth-first search
 *
 * Problem:    Traverse a graph by going as deep as possible, if possible, before backtracking
 *
 * Details:     You a given a Node class that has a name and an array of optional children nodes.
 *              When put together, nodes form an acyclic tree-like structure.
 *              Implement the depthFirstSearch method on the Node class.
 *              It takes in and empty array.
 *
 * Scenarios:   Size of input, structure of graph, available memory, available time
 *
 * Solutions:   Recursive approach: O(v + h) time | O(v) space,
 *                  size of input: smaller lists, more readable
 *                  structure of graph: for trees, not for graphs with cycles
 *              Iterative approach: O(v + e) time | O(v) space,
 *                  size of input: for larger lists, more performant
 *                  structure of graph: for tree and graphs with cycles
 *              Generator function approach: O(v + e) time | O(v) space,
 *                  size of input: for larger lists, more performant
 *                  structure of graph: for trees
 *              Custom data structure approach: O(v + e) time | O(v) space,
 *                  size of input: for even larger lists, more performant
 *                  structure of graph: for tree and graphs with cycles
 *
 * Input ex:   graph = A
                    /  |  \
                    B   C   D
                / \     / \
                E   F   G   H
                    / \   \
                    I   J   K
 * Output ex:   ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
 *
*/

export class Node {
    name: string;
    children: Node[];

    constructor(name: string) {
        this.name = name;
        this.children = [];
    }

    addChild(name: string) {
        this.children.push(new Node(name));
        return this;
    }

    // Recursive approach
    depthFirstSearcRecursive(array: string[]): string[] {
        array.push(this.name); // add current node to array (i.e. current root node)
        for (const child of this.children) { // Loop through children
            child.depthFirstSearchRecursive(array); // Recursively call function on each child, and sets each child as root node when it calls itself
        }
        return array; // when all children have been traversed, return array
    }

    // Iterative approach
    depthFirstSearchIterative(array: string[]): string[] {
        const stack: Node[] = [this]; // Initialize stack with root node
        while (stack.length > 0) { // Loop while stack is not empty
            const current = stack.pop()!; // Pop last element from stack
            array.push(current.name); // Add popped element to array
            for (let i = current.children.length - 1; i >= 0; i--) { // Loop through children in reverse order
                stack.push(current.children[i]);
            }
        }
        return array;
    }

    // Generator function approach
    *depthFirstSearchGenerator(): Generator<string, void, unknown> {
        yield this.name;
        for (const child of this.children) {
            yield* child.depthFirstSearchGenerator();
        }
    }

    // Custom data structure approach
    depthfirstSearchCustom(): string[] {
        const array: string[] = [];
        const stack: CustomStack = new CustomStack();
        stack.push(this);
        while (!stack.isEmpty()) {
            const current = stack.pop()!;
            array.push(current.name);
            for (let i = current.children.length - 1; i >= 0; i--) {
                stack.push(current.children[i]);
            }
        }
        return array;
    }

}

const graph1 = new Node("A")
    .addChild("B")
    .addChild("C")
    .addChild("D")
    .children[0]
    .addChild("E")
    .addChild("F")
    .parent.children[2]
    .addChild("G")
    .addChild("H")
    .parent.children[1]
    .addChild("I")
    .addChild("J")
    .parent.children[2]
    .addChild("K");

console.log(graph1.depthFirstSearch()); // ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

const graph2 = new Node("A")
    .addChild("B")
    .addChild("C")
    .children[0]
    .addChild("D");

console.log(graph2.depthFirstSearch()); // ["A", "B", "D", "C"]

const graph3 = new Node("A")
    .addChild("B")
    .addChild("C")
    .addChild("D")
    .addChild("E")
    .parent.children[1]
    .addChild("F");

console.log(graph3.depthFirstSearch()); // ["A", "B", "C", "F", "D", "E"]

const graph4 = new Node("A")
    .addChild("B")
    .addChild("C")
    .children[0]
    .addChild("D")
    .parent.children[1]
    .addChild("E")
    .addChild("F")
    .children[0]
    .addChild("G");

console.log(graph4.depthFirstSearch()); // ["A", "B", "D", "C", "E", "F", "G"]

const graph5 = new Node("A")
    .addChild("B")
    .addChild("C")
    .addChild("D")
    .addChild("E")
    .addChild("F")
    .children[0]
    .addChild("G")
    .parent.parent.children[1]
    .addChild("H")
    .addChild("I")
    .addChild("J")
    .children[0]
    .addChild("K")
    .parent.parent.children[3]
    .addChild("L")
    .parent.children[1]
    .addChild("M")
    .addChild("N")
    .parent.children[5]
    .addChild("O")
    .addChild("P")
    .addChild("Q")
    .addChild("R")
    .children[0]
    .addChild("S")
    .parent.parent.children[7]
    .addChild("T")
    .addChild("U")
    .parent.children[8]
    .addChild("V")
    .children[0]
    .addChild("W")
    .parent.children[1]
    .addChild("X")
    .parent.children[2]
    .addChild("Y")
    .parent.children[3]
    .addChild("Z");

console.log(graph5.depthFirstSearch()); // ["A", "B", "G", "F", "K", "E", "D", "L", "C", "M", "N", "H", "S", "U", "P", "T", "V", "W", "X", "Y", "Z", "Q", "R", "O"]


