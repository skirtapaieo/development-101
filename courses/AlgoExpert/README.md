# Algoexpert

Course aimed at helping software engineers prepare for algorithmic coding interviews at top tech companies like Google, Facebook, Amazon, and Microsoft.
It entails 195 coding questions, in various categories and levels. It is about 100+ hours of video explanations, data structure crash course and space-time complexity analysis.

The categories:
- Arrays
- Binary Search Trees
- Binary Trees
- Dynamic Programming
- Famous Algorithms
- Graphs
- Greedy Algorithms
- Heaps
- Linked Lists
- Recursion
- Searching
- Sorting
- Stacks
- Strings
- Tries

It think the course is very good. I tried to focus on learning JavaScript, a little bit of Typescript, I tried to think about conceptual solutions, adding pseudocode, before coding when I did the exercises. I also tried to start use JSDoc, terminology, Zod (for validations), test, scenarios, alternative solutions.

There are many routes of improving courses like Algoexpert - at the same time the exercises become a little complex. See code example below for some ideas. I also asked ChatGPT to make a code review - see below the code. I haven't addressed the issues. For interview purposes the course is most likely effective if you go through all the material and all exercises.

## Example: Depth First Search (Graph)

```Javascript
/**
 * Name:        Depth First Search
 *
 * Problem:    Traverse a graph by going as deep as possible, if possible, before backtracking
 *
 * Details:     You a given a Node class that has a name and an array of optional children nodes.
 *              When put together, nodes form an acyclic tree-like structure.
 *              Implement the depthFirstSearch method on the Node class.
 *              It takes in and empty array.
 *
 * Variations:  Size of input, structure of graph, available memory, available time
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
 * Language:    TypeScript/JavaScript
 *
 * Performance: Partly mentioned in solutions
 *
 * Dependencies: None (except for TypeScript/JavaScript)
 *
 * Validation:  Zod: https://github.com/colinhacks/zod#introduction (not used)
 *
 * Edge cases:  Empty input, invalid input, null values, cycles, disconnected components
 *
 * Test cases:  Yes (7) Basic_Tree_Structure, Single_Child_At_Each_Node, Nested_Children, Large_Tree,
 *              Empty_Graph, Disconnected_Components, Invalid_Input_Test, Null_Value_Test, Single_Node
 *
 * Input ex:    graph = A
                    /  |  \
                    B   C   D
                / \     / \
                E   F   G   H
                    / \   \
                    I   J   K
 *
 * Output ex:   ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]
 *
 * Comments:    Typedoc: https://typedoc.org/
 *
 * Author:      Patrik Svensson, https://github.com/skirtapaieo
 *
*/


/**
 * Node class
 */
export class Node {
    name: string;
    children: Node[];

    /**
     * Constructor
     * @param name - Name of the node
     */
    constructor(name: string) {
        this.name = name;
        this.children = [];
    }

    /**
     * Add a child to the node
     * @param name - Name of the child node
     * @returns {Node} - this
     */
    addChild(name: string) {
        this.children.push(new Node(name));
        return this;
    }

    /**
     * Depth-First Search using a recursive approach
     * @param array - Array to populate with node names during the traversal
     * @returns {string[]} - Array with traversed node names
     * @remarks Test_Cases: Basic_Tree_Structure, Single_Child_At_Each_Node, Nested_Children, Large_Tree
     */
    depthFirstSearchRecursive(array: string[]): string[] {
        array.push(this.name); // add current node to array (i.e. current root node)
        for (const child of this.children) { // Loop through children
            child.depthFirstSearchRecursive(array); // Recursively call function on each child, and sets each child as root node when it calls itself
        }
        return array; // when all children have been traversed, return array
    }

    /**
     * Depth-First Search using an iterative approach
     * @param array - Array to populate with node names during traversal
     * @returns {string[]} - Array with traversed node names
     * @remarks Test_Cases: Basic_Tree_Structure, Single_Child_At_Each_Node, Nested_Children, Large_Tree, Disconnected_Components
     */
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

    /**
     * Depth-First Search using a generator function
     * @yields {string} - Yields node names during traversal
     * @remarks Test_Cases: Basic_Tree_Structure, Single_Child_At_Each_Node, Nested_Children
     */
    *depthFirstSearchGenerator(): Generator<string, void, unknown> {
        yield this.name;
        for (const child of this.children) {
            yield* child.depthFirstSearchGenerator();
        }
    }

    /**
     * Depth-First Search using a custom data structure
     * @returns {string[]} - Array with traversed node names
     * @remarks Test_Cases: Basic_Tree_Structure, Single_Child_At_Each_Node, Nested_Children, Large_Tree, Disconnected_Components
     */
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

// Test Case 1: Basic_Tree_Structure
// Remarks: Basic tree with 4 main nodes and a few children.
/* const graph1 = new Node("A")
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
console.log(graph1.depthFirstSearchRecursive([])); // ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"] */
const graph1 = new Node("A");
const childB = graph1.addChild("B");
const childC = graph1.addChild("C");
const childD = graph1.addChild("D");
const childE = childB.addChild("E");
const childF = childB.addChild("F");
const childG = childD.addChild("G");
const childH = childD.addChild("H");
const childI = childC.addChild("I");
const childJ = childC.addChild("J");
const childK = childD.addChild("K");

console.log(graph1.depthFirstSearchRecursive([])); // ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

// Test Case 2: Single_Child_At_Each_Node
// Remarks: Each node has only a single child.
const graph2 = new Node("A")
    .addChild("B")
    .addChild("C")
    .children[0]
    .addChild("D");
console.log(graph2.depthFirstSearchRecursive([])); // ["A", "B", "D", "C"]

// Test Case 3: Nested_Children
// Remarks: Some nodes have nested children.
const graph3 = new Node("A")
    .addChild("B")
    .addChild("C")
    .addChild("D")
    .addChild("E")
    .parent.children[1]
    .addChild("F");
console.log(graph3.depthFirstSearchRecursive([])); // ["A", "B", "C", "F", "D", "E"]

// Test Case 4: Large_Tree
// Remarks: A large tree with multiple layers of children.
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
console.log(graph4.depthFirstSearchRecursive([])); // ["A", "B", "D", "C", "E", "F", "G"]

// Test Case 5: Empty_Graph
// Remarks: Testing an empty graph, should return an empty array.
const graph5 = new Node("");
console.log(graph5.depthFirstSearchRecursive([])); // []

// Test Case 6: Disconnected_Components
// Remarks: Nodes that are not directly connected to the root.
const graph6 = new Node("A");
const disconnectedNode = new Node("Z");
console.log(graph6.depthFirstSearchRecursive([])); // ["A"]

// Test Case 7: Invalid_Input_Test
// Remarks: Trying to add an invalid node name (an empty string) as a child.
try {
    const graph7 = new Node("A").addChild("");
} catch (e) {
    console.log(e.message); // "Invalid name for child"
}

// Test Case 8: Null_Value_Test
// Remarks: Trying to pass null as a node name.
try {
    const graph8 = new Node(null as unknown as string);
} catch (e) {
    console.log(e.message); // "Invalid name"
}

// Test Case 9: Single_Node
// Remarks: Testing with a graph that has a single node.
const graph9 = new Node("A");
console.log(graph9.depthFirstSearchRecursive([])); // ["A"]

console.log(graph5.depthFirstSearch()); // ["A", "B", "G", "F", "K", "E", "D", "L", "C", "M", "N", "H", "S", "U", "P", "T", "V", "W", "X", "Y", "Z", "Q", "R", "O"]
```

## ChatGPT code review

Conducting a code review involves several aspects, including correctness, style, performance, and maintainability. Below is a review based on these aspects.

### Correctness

- **Method Signatures**: The provided methods follow the proper signature for depth-first search, starting from the root node and traversing to the children.
- **Test Cases**: It appears that most of the edge cases and variations of input are well thought out and covered by the test cases.
- **Handling of Non-Existence**: The `!` operator in TypeScript (non-null assertion operator) is used to assert that `stack.pop()` will not return `undefined`. This is not safe and should be handled more carefully.
- **Disconnection and Cycles**: There is no handling of disconnected nodes or cycles in the graph, which could lead to incorrect results or infinite loops.

### Style

- **Documentation**: The code is well-documented, which is excellent for maintainability. However, more detailed comments about the expected behavior within methods could be useful.
- **Consistency**: The coding style is consistent, with appropriate naming conventions for variables and functions.
- **Use of TypeScript**: The code takes advantage of TypeScript features such as type annotations, which improves readability and maintainability.

### Performance

- **Complexity**: The algorithmic complexity is briefly described, but no detailed analysis is provided for the best, average, and worst cases.
- **Memory Usage**: The recursive method could lead to a stack overflow if the tree is very deep. This is an important consideration for large inputs.
- **Iterative vs. Recursive**: The iterative approach is typically more performant due to the lack of function call overhead.

### Maintainability

- **Extensibility**: The `Node` class can be easily extended to include additional properties or methods.
- **Hard-coded Tests**: The test cases are hard-coded within the file, which is not scalable. It would be better to separate tests from the implementation and use a testing framework.

### Additional Observations

- **Custom Data Structure**: There is a mention of a custom data structure (`CustomStack`), but it is not defined anywhere in the provided code.
- **Generator Function**: The generator function is a nice touch and could be useful in scenarios where you want to process nodes as they are visited without storing the entire result.
- **Error Handling**: There is an attempt to handle invalid inputs in the test cases, but the `Node` class itself doesn't seem to validate the input.

### Recommendations

- Implement proper error handling and input validation in the `Node` class's constructor and methods.
- Consider avoiding the use of the non-null assertion operator and handle potential `undefined` values explicitly.
- Add handling for cycles and disconnected nodes if applicable.
- Consider using a testing framework for more robust and scalable tests.
- Define and include the `CustomStack` implementation or remove references if it is not used.
- Analyze and discuss the space and time complexity in more detail, particularly considering the depth of the tree.

Overall, the provided code is a good starting point for a depth-first search implementation, but it should be further refined for robustness, especially concerning error handling and potentially complex graph structures.

