
Hey there.

## Reboot as software developer!

In the past six years at Digitalkompaniet, I've led up to 30 teams at companies like Telenor, Hemnet, Delaval, NetOnNet, and SJ, focusing on management over hands-on development.The end oof 2022 marked a turning point for me, with significant advancements in AI.

I started doing courses and research, which I documented here (development-101) and more playful things in another repository (play-101). I also have private repos where I do startup and client work.

Since March, I have started to do commercial work for clients, my first thing was a performance framework using Python, Puppeteer, Lighthouse that tested the performance of 10 competitors, from 3 different locations across Europe and summarizing "everything" about their performance on all of their pages.

So a little bit about this repo:


## Embracing simplicity in Coding (in private repos)

Most of my coding is done in private repos for customers, and what you find here are quick and dirty, non-production, examples, assignments, quick "touch and feel" of some library and so on. But below is an example of an assigment in AlgoExpert, below that a simple MVP (a CLI-based AI assistant) - and my most used Bash script :-)


### MVP/CLI-based AI assistant

```Python
import openai
from dotenv import load_dotenv
import os
import json
import yaml

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# load the yaml file with people's CV's
with open("persons-10.yaml", "r") as f:
    persons = yaml.safe_load(f)
# bprint(f"Loaded CV Data: {str(persons)[:50]}")  # Print to verify file loaded

ascii_art = """
 ______    _ __         ___   ____
/_  __/___(_) /  ___   / _ | /  _/
 / / / __/ / _ \/ -_) / __ |_/ /
/_/ /_/ /_/_.__/\__/ /_/ |_/___/
"""
initial_system_message = f"{ascii_art}"
print(
    f"{initial_system_message}\nWelcome to Tribe MVP.\nYou are using the organization module.\n\n"
)  # Print to verify initial system message

initial_system_message += str(persons)
conversation_history = [{"role": "system", "content": initial_system_message}]


def chat_with_gpt(prompt):
    global conversation_history  # Declare it global so we can modify it

    # Add user's message to the conversation history
    conversation_history.append({"role": "user", "content": prompt})

    # Generate a response using the conversation history
    response = openai.ChatCompletion.create(
        model="gpt-4", messages=conversation_history
    )

    # Extract and return the assistant's reply
    assistant_reply = response.choices[0].message["content"].strip()

    # Add assistant's reply to the conversation history
    conversation_history.append({"role": "assistant", "content": assistant_reply})

    return assistant_reply


GREEN = "\033[0;32m"
RED = "\033[0;31m"
RESET = "\033[0m"

if __name__ == "__main__":
    while True:
        user_input = input(f"{GREEN}Patrik:{RESET} ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break

        response = chat_with_gpt(user_input)
        print(f"{RED}Tribe-AI:{RESET} {response}")
```

### A Bash-script

I have a hangup that I want to keep control on the amout of code I do to make sure that things don't grow out of hand.

```Bash
#!/bin/bash

# Initialize the line count to 0
total_lines=0

# Initialize the other variable to 50 for lines in other types of files
other=0

# Loop through each .js, .ts, or .yaml file in the /src directory and its subdirectories
while read -r file; do
  # Count the lines in each file
  lines=$(wc -l < "$file")
  echo "$file has $lines lines"

  # Add to total line count
  total_lines=$((total_lines + lines))
# Yaml: done < <(find ../ -type f \( -name "*.js" -o -name "*.ts" -o -name "*.yaml" \))

# No Yaml:
done < <(find ../ -type f \( -name "*.js" -o -name "*.ts" \))

# Add the 'other' lines to the total line count
total_lines=$((total_lines + other))

# Display total line count
echo "Total lines of code: $total_lines"

```


### Depth-fist assignment at AlgoExpert

Here is quite a different sample, where I had done some assignments Algoexpert before this (Depth First Search) assignment, and I think I wanted a way to think through the problem, the variants, and to document the code and try to write some test cases which ends up looking overcommented. And it is only half done to become production worthy - it lacks error handling in the "node" classes - but I took out the algorithm part and passed the assignment, which was one of the main goals in this case:


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












## Continuous learning through courses (/courses)

I started using AlgoExpert years ago to sharpen my technical interview skills, especially for roles at top tech firms like Google and Facebook. AlgoExpert has since evolved, offering 6 courses and extensive learning in algorithms and data structure, systems design, front-end, blockchain/crypto, and machine learning. I've signed up for all courses and most of them are done now. My language focus has been on JavaScript and Python - but you also learn a little about React, Go, Solidity, HTML and CSS.

### Product Management and UX (in private repos and clients)

The focus is software development butin any software development approach, product management and UX are key, both creating cross-functional organizations and harmonized "toolchains". I've successfully launched products with outstanding UX and technology, like at DeLaval, where we developed cloud platforms and products using AWS IoT solutions and a proprietary edge server. I have worked as CTO/CPO, and I have done UX design for clients. I am proficient in Figma and Storybook, I've worked with design systems in Vue and React, collaborating with in-house teams and agencies. The most recent thing that I have learned about is accessibility. I have done reactive programming since 2014 (Meteor).

## Systems design and architecture (/research/systems-design)

My expertise in systems architecture stems from working on telecom systems with complex models and large-scale RFQ processes at companies like Ericsson and Huawei. I enhanced this knowledge through AlgoExpert's systems design course, adding exercises from various sectors like social media, streaming, team collaboration, finance, real estate, and education.

My designs, often used for interviews or discussions, focus on user experience, service architecture, APIs, and information models. My experience covers a broad range of areas, including front-end, back-end, infrastructure, and data pipelines, though these are usually too advanced for typical systems design.

Most of the system designs are made in less than 30 minutes, in some cases I took more time to research a special topic. Most systems design have a lot in similar, but almost all advanced solutions have one or more unique features, that is well worth to invest in.

## Infrastructure increasingly important (research/infrastructure)

With a 15-year history on AWS, I've played a key role in cloud infrastructure, including introducing Azure at Tele2 and migrating Hemnet to AWS. My experience also covers SRE, DevOps, and cost optimization. I've explored modern web development tools like Next.js through Vercel. I use this directory to research topics that I am curious about.

## Tools

I've use tools like VSC, GitHub/Git, and WSL/Ubuntu. My expertise spans front-end development, microfrontend teams, and various languages including Go, Python, TypeScript and JavaScript. I'm also experienced in database management (RDBMS and SQL) with a focus on data-first approaches. Here's an early version of the CLI-based application:

