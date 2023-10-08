/**
 * Name:        <Name>
 *
 * Problem:    <Problem
 *
 * Details:    <Details
 *
 * Variations:  <Variations>
 *
 * Solutions:   <Solutions
 *
 * Language:    <Language>
 *
 * Performance: <Performance>
 *
 * Dependencies: <Dependencies>
 *
 * Validation:  <Validation>
 *
 * Edge cases:  <Edge cases>
 *
 * Test cases:  <Test Cases>
 *
 * Input ex:    <Input Example
 *
 * Output ex:   <Output example>
 *
 * Comments:    Typedoc: https://typedoc.org/
 *
 * Author:      Patrik Svensson, https://github.com/skirtapaieo
 *
*/



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