 

# Programming languages and tools 

<br>
<br>

# Index

- [Programming languages and tools](#programming-languages-and-tools)
  - [Production-ready code](#production-ready-code)
  - [Back-end languages](#back-end-languages)
  - [Programming Paradigms](#programming-paradigms)
  - [Test-driven development](#test-driven-development)
- [Python](#python)
   - [The Python Stack](#the-python-stack) 
   - [The Foundations of Python](#the-foundations-of-python)
     - [Standard Libraries - Python vs JavaScript](#standard-libraries-Python-vs-JavaScript)
   - [Refreshing Python on Programming Expert](#refreshing-python-on-programming-expert)
   - [Python, Zen and Pep 484](#python-zen-and-pep-484)
   - [PEP 20 (Zen of Python)](#pep-20-zen-of-python)
   - [Python and typing](#python-and-typing)
     - [Python, type hints and static type checking](#python-type-hints-and-static-type-checking)
     - [Examples of Python without type hints](#examples-of-python-without-type-hints)
     - [Examples of Python with type hints](#examples-of-python-with-type-hints)
   - [Tools that might help writing more Pythonic code](#tools-that-might-help-writing-more-pythonic-code)
   - [Popular Python Packages (their optimizations, and Mojo)](#popular-python-packages-their-optimizations-and-mojo)
   - [How to approach learning the most popular libraries](#how-to-approach-learning-the-most-popular-libraries)
   - [What other skills are needed?](#what-other-skills-are-needed)
- [Golang](#go)
- [JavaScript](#javascript)
  - [Typescript](#typescript) 
- [New Languages](#new-languages)
  - [Mojo](#mojo)
  - [Zig](#zig)
- [VS Code, Replit, Vercel](#vs-code-replit-vercel)


# Production-ready code 

## Python Example 

The following code is one of 100's of excercises in "Programming Expert (using Python).  

```
def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)
```

And the following code has been improved in several ways to make it production-ready: 

```
import logging
from typing import List, Optional

def compare_lists(lst1: Optional[List] = None, lst2: Optional[List] = None) -> int:
    """
    Return the number of unique elements common to two lists.

    Args:
        lst1: The first list. If not provided, an empty list will be used.
        lst2: The second list. If not provided, an empty list will be used.

    Returns:
        The number of unique elements that are common to `lst1` and `lst2`.

    Raises:
        TypeError: If either argument is not a list or contains unhashable types.
    """
    
    # Ensure input arguments are of correct type
    if lst1 is None:
        lst1 = []
    if lst2 is None:
        lst2 = []

    if not isinstance(lst1, list):
        raise TypeError(f'Expected lst1 to be a list, got {type(lst1).__name__}')
    if not isinstance(lst2, list):
        raise TypeError(f'Expected lst2 to be a list, got {type(lst2).__name__}')
    
    # Convert to sets and find intersection
    try:
        lst1_set = set(lst1)
        lst2_set = set(lst2)
    except TypeError as e:
        raise TypeError('Both lists should contain only hashable items') from e

    set_intersection = lst1_set.intersection(lst2_set)

    # Log the result
    logging.info("Lists compared. Found %d common unique elements.", len(set_intersection))
    
    return len(set_intersection)

```

The following are the improvements: 
- Function Signature: The function signature now includes type hints (Optional[List] and int). This provides additional information about expected input types and the return type, which can help with understanding the function's purpose and behavior. It also aids in static type checking if a tool like mypy is used.

- Default Arguments: Instead of using mutable default arguments (lst1=[], lst2=[]), which can lead to unexpected behavior, we default to None and assign an empty list inside the function if the argument is None. This ensures that each call to the function gets a brand-new empty list if no list is provided.

- Error Handling: We've added explicit checks to make sure lst1 and lst2 are of the correct type (i.e., lists). If they are not, the function raises a TypeError. This is an example of "fail fast", where problems are detected and reported as soon as possible.

- Try/Except Block: When creating sets from the lists, the function now catches TypeErrors, which could occur if a list contains unhashable elements. The new exception message provides a clearer explanation of the problem.

- Logging: A logging statement has been added at the end of the function. This provides a record of the function's operation, which can be useful for understanding the flow of a program and debugging. Note that the logging level is INFO, so this will only appear if the logging level is set to INFO or lower.

- Docstring: The function now includes a docstring, which describes its purpose, arguments, return value, and exceptions. This can help other developers understand how the function is supposed to be used and what it does.

- Explicit is better than implicit: Each step of the operation is now clearly delineated and commented. This makes the code easier to read and understand. The function's logic hasn't changed, but the added clarity and explicitness improve maintainability.

- All these improvements make the function more robust, easier to understand, and easier to debug, which are important qualities for production-ready code.

<br> 


# Back-end languages 

A table of a variety of back-end languages: 

| Features/Properties     | Go             | TypeScript         | Node.js           | Java         | .NET              | Ruby               |
|-------------------------|----------------|--------------------|-------------------|--------------|-------------------|-------------------|
| Type System             | Static         | Static             | Dynamic           | Static       | Static            | Dynamic            |
| Compilation             | Compiled       | Transpiled         | Interpreted       | Both (JIT)   | Both (JIT)        | Interpreted        |
| Performance             | High           | Moderate           | Moderate          | High         | High              | Moderate           |
| Concurrency             | Built-in       | Event-driven       | Event-driven      | Multithreading (manual) | Multithreading (manual) | Green-threading (manual) |
| Syntax                  | Simple         | More complex       | More complex      | More complex | More complex      | Simple             |
| Package Management      | Go Modules     | npm                | npm               | Maven/Gradle | NuGet             | RubyGems (Bundler) |
| Learning Curve          | Moderate       | High               | High              | High         | High              | Moderate           |
| Ecosystem               | Robust         | Very Large         | Very Large        | Very Large   | Very Large        | Large              |
| Use Cases               | System programming, Microservices, CLI tools | Web development, APIs, Real-time applications | Web development, APIs, Real-time applications | Enterprise applications, Android Apps, Web applications | Web and Desktop applications, Microservices, Cloud-based apps | Web development (Especially with Rails) |
| Object-Oriented         | Struct-based   | Yes, class-based   | Yes, prototype-based | Yes, class-based | Yes, class-based | Yes, class-based  |

Please note that while Ruby is an object-oriented language, it's dynamically typed and interpreted, and its performance isn't as high as some other languages. However, its simplicity and the productivity of the Ruby on Rails framework make it popular for web development.


<br>

# Programming paradigms 


## High-level table 

| Paradigm | Description | Python Support | Examples in Other Languages |
| --- | --- | --- | --- |
| **Imperative** | The programmer instructs the computer on what steps to take to solve a problem. It focuses on describing how a program operates. | Yes | C, Go, Machine Code |
| **Declarative** | The programmer tells the computer what the desired result is without having to describe step by step. It focuses on what the program should accomplish. | Partial (List Comprehensions, SQL Queries with SQLite) | SQL, HTML, CSS |
| **Object-Oriented** | Organizes software design around data, or objects, rather than functions and logic. | Yes | Java, C++ |
| **Functional** | Treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. | Partial (Support for higher-order functions, lambdas, and list comprehensions) | Haskell, Lisp |
| **Procedural** | A type of imperative programming where the program is built from procedures (or subroutines) which should ideally operate on data without side effects. | Yes | C, Pascal, CUDA |
| **Event-Driven** | The flow of the program is determined by events such as user actions, sensor outputs, or messages from other programs. | Yes (Frameworks like Django, Flask) | JavaScript |
| **API/Service Oriented** | This isn't a programming paradigm in a traditional sense. It's more of a design pattern focused on the interaction between different software platforms through well-defined interfaces or APIs. | Yes (Django Rest Framework, Flask) | Various (Any language can be used to implement or consume APIs) |
| **Domain-Specific** | Languages or tools designed for specific tasks in a particular domain. | Partial (Certain libraries or tools, like RegEx or SQL querying through SQLite) | SQL, CSS, Shell scripting |
| **Parallel** | The execution of concurrent tasks in the context of different cores or processors. | Partial (Multiprocessing and Threading modules, but Python's Global Interpreter Lock can be a limitation) | CUDA, C (with OpenMP) |
| **Concurrent** | Deals with the simultaneous execution of more than one sequence of operations. | Partial (Multiprocessing, Threading, asyncio for asynchronous I/O) | Java, Go |
| **Component-Based** | Building software application from modular components, each providing different functionality. | Yes (Python modules and packages provide component-based design) | JavaScript (React) |
| **Reflexive** | Programs can inspect, change structure, and execute program instructions on the fly. | Yes (Python's reflection capabilities with functions like getattr, hasattr) | JavaScript, Java |
| **Generative** | Programs can write other programs, or modify themselves while running. | Partial (Python can generate code, but it's not as integral a part of the language as in some others) | Lisp, Prolog |

## Comparing Python and JavaScript 

| Paradigm | Description | Python Support | JavaScript Support |
| --- | --- | --- | --- |
| **Imperative** | The programmer instructs the computer on what steps to take to solve a problem. It focuses on describing how a program operates. | Yes | Yes |
| **Declarative** | The programmer tells the computer what the desired result is without having to describe step by step. It focuses on what the program should accomplish. | Partial (List Comprehensions, SQL Queries with SQLite) | Partial (HTML manipulation with DOM API, Array methods like `map`, `filter`, `reduce`) |
| **Object-Oriented** | Organizes software design around data, or objects, rather than functions and logic. | Yes | Yes (Prototypical and with `class` syntax from ES6) |
| **Functional** | Treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. | Partial (Support for higher-order functions, lambdas, and list comprehensions) | Yes (First-class functions, Array methods like `map`, `filter`, `reduce`) |
| **Procedural** | A type of imperative programming where the program is built from procedures (or subroutines) which should ideally operate on data without side effects. | Yes | Yes |
| **Event-Driven** | The flow of the program is determined by events such as user actions, sensor outputs, or messages from other programs. | Yes (Frameworks like Django, Flask) | Yes (Core concept, especially in client-side JS and Node.js) |
| **API/Service Oriented** | This isn't a programming paradigm in a traditional sense. It's more of a design pattern focused on the interaction between different software platforms through well-defined interfaces or APIs. | Yes (Django Rest Framework, Flask) | Yes (Fetching data from server, interacting with RESTful services) |
| **Domain-Specific** | Languages or tools designed for specific tasks in a particular domain. | Partial (Certain libraries or tools, like RegEx or SQL querying through SQLite) | Partial (Domain-Specific Libraries or tools) |
| **Parallel** | The execution of concurrent tasks in the context of different cores or processors. | Partial (Multiprocessing and Threading modules, but Python's Global Interpreter Lock can be a limitation) | No (Due to single-threaded nature of JS, but Web Workers can be used for thread-like behavior) |
| **Concurrent** | Deals with the simultaneous execution of more than one sequence of operations. | Partial (Multiprocessing, Threading, asyncio for asynchronous I/O) | Yes (Async/Await, Callbacks, Promises for asynchronous I/O) |
| **Component-Based** | Building software application from modular components, each providing different functionality. | Yes (Python modules and packages provide component-based design) | Yes (Modules, and component-based libraries/frameworks like React) |
| **Reflexive** | Programs can inspect, change structure, and execute program instructions on the fly. | Yes (Python's reflection capabilities with functions like getattr, hasattr) | Yes (Objects and functions can be inspected and modified at runtime) |
| **Generative** | Programs can write other programs, or modify themselves while running. | Partial (Python can generate code, but it's not as integral a part of the language as in some others) | Partial (JavaScript can generate and evaluate code strings, but it's generally discouraged due to security and debugging difficulties) |

## Code examples 

| Paradigm | Python Support | Python Example | JavaScript Support | JavaScript Example |
| --- | --- | --- | --- | --- |
| **Imperative** | Yes | `x = 7; print(x)` | Yes | `let x = 7; console.log(x);` |
| **Declarative** | Partial | `[x**2 for x in range(10) if x%2 == 0]` | Partial | `[1, 2, 3, 4].map(x => x * 2).filter(x => x%2 === 0);` |
| **Object-Oriented** | Yes | `class A: pass` | Yes | `class A {}` or `function A() {}` |
| **Functional** | Partial | `(lambda x: x*2)(10)` | Yes | `(x => x*2)(10)` |
| **Procedural** | Yes | `def procedure(): pass; procedure()` | Yes | `function procedure() {}; procedure()` |
| **Event-Driven** | Yes | `import tkinter as tk; root = tk.Tk(); button = tk.Button(root, text="Click me"); button.pack(); root.mainloop()` | Yes | `document.querySelector('button').addEventListener('click', () => console.log('Clicked!'));` |
| **API/Service Oriented** | Yes | `import requests; requests.get('https://api.github.com')` | Yes | `fetch('https://api.github.com').then(response => response.json()).then(data => console.log(data));` |
| **Domain-Specific** | Partial | `import re; re.match(r'\d+', '123')` | Partial | `/\d+/.exec('123');` |
| **Parallel** | Partial | `from multiprocessing import Pool; with Pool() as p: print(p.map(int, ['1', '2', '3']))` | No | `// Not supported natively` |
| **Concurrent** | Partial | `import asyncio; async def main(): pass; asyncio.run(main())` | Yes | `async function main() {}; main();` |
| **Component-Based** | Yes | `import math; math.sqrt(4)` | Yes | `import React from 'react'; function Component() {return <div>Component</div>};` |
| **Reflexive** | Yes | `class A: pass; hasattr(A, 'attribute')` | Yes | `let obj = {}; 'property' in obj;` |
| **Generative** | Partial | `exec('print("Hello, World!")')` | Partial | `eval('console.log("Hello, World!")');` |


## Test-driven development 

Test-Driven Development (TDD) is a software development approach where tests are written before the code that fulfills those tests. The typical TDD cycle can be summarized as "Red - Green - Refactor":

1. **Red**: Write a failing test for a piece of functionality you want to implement.
2. **Green**: Write just enough code to make the test pass.
3. **Refactor**: Improve the code while keeping the test green (i.e., the code passes the test).

When it comes to architecture and design in TDD, they're still very important, but they're considered in a different way compared to traditional software development methods. Instead of designing the entire architecture upfront, TDD encourages developers to let the architecture emerge and evolve organically as the codebase grows and changes. The refactoring stage, which is an integral part of TDD, helps in shaping and refining the design over time.

However, it doesn't mean there's no design in TDD. Here's how you might approach design in TDD:

- **Understand the Problem Domain**: Before writing tests, you need a good understanding of the problem you're trying to solve and the domain in which you're working. This understanding will inform your tests and your design decisions. 

- **Simple Design**: TDD encourages developers to start with the simplest design that could possibly work and let the architecture of the system evolve as more tests are added.

- **Refactoring**: Each time you get a test to pass, you have an opportunity to refactor the code and improve the design. This continuous refactoring helps in maintaining a clean, robust, and flexible architecture. 

- **Design Patterns**: When you're refactoring, you'll often find that certain design patterns can help to structure your code better. Knowing these patterns and understanding when to apply them is a key skill in TDD.

- **SOLID Principles**: Following SOLID principles (Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) will lead to a more maintainable and flexible design. These principles often naturally emerge when practicing TDD.

- **Listen to the Tests**: If you find your tests are hard to write, it's often a sign that your design isn't quite right. Maybe a class has too many responsibilities or the dependencies between classes are too complicated. Listening to these "test smells" can guide your design decisions.

So, in TDD, the architecture and design are constantly being revised and improved throughout the development process rather than being completely designed upfront. The continuous feedback from the tests helps to shape the design and guide it towards a clean, maintainable, and flexible architecture.

### TDD in Python

Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: first the developer writes a failing automated test case that defines a desired improvement or new function, then produces code to pass that test and finally refactors the new code to acceptable standards. TDD is well-supported in Python through a variety of tools and libraries.

Here are some commonly used testing libraries in Python:

1. **unittest**: This is the standard library testing framework that comes bundled with Python. It supports test automation, sharing of setup and shutdown code for tests, aggregation of tests into collections, and independence of the tests from the reporting framework.

2. **pytest**: This is a popular third-party library that provides a powerful and flexible framework for testing Python code. It supports running unittest, doctest, and nose test cases, and provides many advanced features like fixtures, parameterized testing, and plugins.

3. **doctest**: Another standard library module, doctest lets you write tests as part of your documentation. You include some example usage of your code in your docstrings, and doctest can extract these examples and run them as tests.

4. **mock**: Part of the standard library (as of Python 3.3), mock allows you to replace parts of your system under test and make assertions about how they have been used.

5. **hypothesis**: This is a third-party library for property-based testing, an advanced form of testing where you specify properties that your code should have, and Hypothesis generates test cases that try to disprove these properties.

6. **tox**: Tox is a tool for automating testing in multiple Python environments, making it easier to test your code against different Python versions and interpreter implementations.

7. **coverage**: Coverage.py is a tool for measuring code coverage of Python programs, helping to identify which parts of your code might not be tested.

Using these tools, you can build a comprehensive suite of automated tests for your Python code, supporting a test-driven development approach. Automated testing can help you catch bugs early, gain confidence when refactoring, and ensure that your code is behaving as expected.

<br>


# Python 

## The Python "Stack" 

Here's a "stack-like" structure:

1. **Python Language:** The high-level, interpreted programming language known for its simplicity and readability. It's specified by a series of documents known as Python Enhancement Proposals (PEPs). The language includes its syntax, grammar, and core concepts like variables, data types, control flow constructs, functions, and classes.

2. **Python Interpreter:** An interpreter is a program that reads and executes Python code. The official and most widely used interpreter is CPython, which is written in C. Other interpreters include Jython (Python for Java platform), PyPy (Python written in a subset of Python itself), etc.

3. **Python Compiler:** Python is an interpreted language, but that doesn't mean it doesn't involve compilation. Python source code is first compiled to bytecode which is a lower-level representation of your program. This bytecode is then interpreted by the Python interpreter (CPython's case, the Python Virtual Machine). This compilation step is often invisible to the user but is a key part of the process.

4. **Python Standard Library:** The Python standard library is a vast collection of modules that provides cross-platform functionality for a wide range of common tasks, such as file I/O, system calls, threading, networking, and much more. This library is part of any standard Python distribution.

5. **Python Built-In Functions and Types:** These are functions and types like `print()`, `len()`, `int`, `list`, `dict`, etc., which are always available in Python without needing to import any module.

6. **Third-Party Libraries/Modules/Extensions:** These are additional libraries/modules/extensions that are not included in the standard Python distribution but can be installed and used to extend Python's functionality. They can be found on PyPI and installed with pip.

7. **Python Scripts/Modules:** These are .py files containing Python code, which can define functions, classes, and variables, and can also include runnable code. The module name is the file name without the `.py` suffix.

8. **Python Packages:** A way of organizing related Python modules into a directory hierarchy. In essence, it's a directory that contains Python modules and a special `__init__.py` file.

I hope this provides a helpful high-level view of the different components that make up Python!

<br>

## The foundations of Python 

There are many foundational topics to learn: 
- The Python Language reference - syntax and semantics - Lexical analysis, Data model, Execution model, Import system, Expressions, Simple/compound statements, top-level components
- Python Standard Library - built-in functions, constants, types, exceptions, text processing, binary data services, data types, numeric and mathematical, functional, file and directory, etc ...
- **"Fluent Python"** by Luciano Ramalho: This book offers a deep dive into how Python works under the hood. It covers advanced topics such as metaclasses, descriptors, decorators, and understanding the data model of Python.

<br>

### Standard Libraries: Python vs JavaScript 

|                | Python Standard Library  | JavaScript Standard Library |
|----------------|-------------------------|-----------------------------|
| **Purpose**    | Python's standard library is expansive, offering a wide variety of modules that can handle everything from file I/O, web scraping, email, regular expressions, and more. It has a strong emphasis on ease of use. | JavaScript's standard library is smaller and more minimalistic, focusing primarily on functions needed for web development such as DOM manipulation, event handling, and AJAX requests. |
| **Built-in Functions** | Python's standard library has a variety of built-in functions for complex data manipulation, mathematical operations, object-oriented programming, and more. | JavaScript's built-in functions are generally focused on manipulating web page content and event handling. It also has Math and Date libraries for basic computations and date/time manipulation. |
| **Data Structures** | Python has built-in support for advanced data structures like dictionaries, tuples, and sets, and the standard library has modules for operations on these. | JavaScript primarily uses objects and arrays for complex data. It does have newer data structures like Maps and Sets but their use is not as prevalent. |
| **File I/O** | Python's standard library has extensive support for file I/O operations with modules like `os`, `shutil`, and `pathlib`. | JavaScript's standard library doesn't include file I/O due to the security model of browsers, but Node.js provides these capabilities. |
| **Networking** | Python has strong support for networking protocols in its standard library, with modules like `socket`, `http.client`, `ftplib`, and `smtplib`. | JavaScript's standard library itself doesn't support networking protocols, but web APIs like `fetch` and `XMLHttpRequest` and Node.js modules handle these needs. |
| **Database** | Python's standard library includes the `sqlite3` module for interacting with SQLite databases. | JavaScript doesn't have direct database handling in its standard library, but can interact with databases via external libraries or web APIs. |

<br>

## Production-ready code 

The following code is one of 100's of excercises in "Programming Expert (using Python).  

```
def compare_lists(lst1=[], lst2=[]):
    lst1_set = set(lst1)
    lst2_set = set(lst2)
    set_intersection = lst1_set.intersection(lst2_set)

    return len(set_intersection)
```

And the following code has been improved in several ways to make it production-ready: 

```
import logging
from typing import List, Optional

def compare_lists(lst1: Optional[List] = None, lst2: Optional[List] = None) -> int:
    """
    Return the number of unique elements common to two lists.

    Args:
        lst1: The first list. If not provided, an empty list will be used.
        lst2: The second list. If not provided, an empty list will be used.

    Returns:
        The number of unique elements that are common to `lst1` and `lst2`.

    Raises:
        TypeError: If either argument is not a list or contains unhashable types.
    """
    
    # Ensure input arguments are of correct type
    if lst1 is None:
        lst1 = []
    if lst2 is None:
        lst2 = []

    if not isinstance(lst1, list):
        raise TypeError(f'Expected lst1 to be a list, got {type(lst1).__name__}')
    if not isinstance(lst2, list):
        raise TypeError(f'Expected lst2 to be a list, got {type(lst2).__name__}')
    
    # Convert to sets and find intersection
    try:
        lst1_set = set(lst1)
        lst2_set = set(lst2)
    except TypeError as e:
        raise TypeError('Both lists should contain only hashable items') from e

    set_intersection = lst1_set.intersection(lst2_set)

    # Log the result
    logging.info("Lists compared. Found %d common unique elements.", len(set_intersection))
    
    return len(set_intersection)

```

The following are the improvements: 
- Function Signature: The function signature now includes type hints (Optional[List] and int). This provides additional information about expected input types and the return type, which can help with understanding the function's purpose and behavior. It also aids in static type checking if a tool like mypy is used.

- Default Arguments: Instead of using mutable default arguments (lst1=[], lst2=[]), which can lead to unexpected behavior, we default to None and assign an empty list inside the function if the argument is None. This ensures that each call to the function gets a brand-new empty list if no list is provided.

- Error Handling: We've added explicit checks to make sure lst1 and lst2 are of the correct type (i.e., lists). If they are not, the function raises a TypeError. This is an example of "fail fast", where problems are detected and reported as soon as possible.

- Try/Except Block: When creating sets from the lists, the function now catches TypeErrors, which could occur if a list contains unhashable elements. The new exception message provides a clearer explanation of the problem.

- Logging: A logging statement has been added at the end of the function. This provides a record of the function's operation, which can be useful for understanding the flow of a program and debugging. Note that the logging level is INFO, so this will only appear if the logging level is set to INFO or lower.

- Docstring: The function now includes a docstring, which describes its purpose, arguments, return value, and exceptions. This can help other developers understand how the function is supposed to be used and what it does.

- Explicit is better than implicit: Each step of the operation is now clearly delineated and commented. This makes the code easier to read and understand. The function's logic hasn't changed, but the added clarity and explicitness improve maintainability.

- All these improvements make the function more robust, easier to understand, and easier to debug, which are important qualities for production-ready code.

### PEP20 and the code 

PEP 20, known as the Zen of Python, is a collection of 19 "guiding principles" for writing computer programs in the Python language. Let's see how these principles apply to the improved code:

Beautiful is better than ugly.
The function is structured clearly and cleanly, making it aesthetically pleasing to a developer's eye.

Explicit is better than implicit.
The function explicitly checks the input types and whether they contain hashable elements. It also has explicit type hints.

Simple is better than complex.
The function does one specific task and does it simply and directly, without any unnecessary complexity.

Complex is better than complicated.
The function doesn't have any unnecessary complexity or complications. It's straightforward and easy to understand.

Flat is better than nested.
The function doesn't have nested control structures. It's quite flat, making it easy to read and understand.

Sparse is better than dense.
The code isn't overly dense. Each step is clear, and there's plenty of white space.

Readability counts.
The function has been written with readability in mind. It includes comments, clear variable names, and a well-written docstring.

Special cases aren't special enough to break the rules.
The function doesn't have any special cases. It treats all input the same way.

Although practicality beats purity.
The function is practical and doesn't adhere to any kind of "purity". It does what's needed to get the job done.

Errors should never pass silently.
The function includes error handling to ensure that errors do not pass silently.

Unless explicitly silenced.
The function does not silence any errors.

In the face of ambiguity, refuse the temptation to guess.
The function doesn't make any assumptions about the input. It checks that the input is of the correct type and contains hashable elements.

There should be one-- and preferably only one --obvious way to do it.
The function uses the standard way of finding the intersection of two sets in Python.

Although that way may not be obvious at first unless you're Dutch.
This is a humorous reference to Python's creator, Guido van Rossum, who is Dutch.

Now is better than never.
The function does what it needs to do now, without procrastinating or delaying.

Although never is often better than right now.
The function doesn't rush to return a result before it's ready. It takes the necessary steps in the necessary order.

If the implementation is hard to explain, it's a bad idea.
The function is easy to explain, which indicates that it's well-implemented.

If the implementation is easy to explain, it may be a good idea.
Again, the function is easy to explain, which suggests that it's a good implementation.

Namespaces are one honking great idea -- let's do more of those!
This isn't directly applicable to the function, but it's always a good idea to use namespaces appropriately in larger Python programs. In this case, the function does properly keep its variables in its local namespace.

Overall, the function seems to align well with the principles of PEP 20.

### Power of 10 and the code

The "Power of Ten" rules by Gerard J. Holzmann of NASA's Jet Propulsion Laboratory are very specific and were intended for C programming in ultra high-integrity systems, such as spacecraft. However, some rules are general good practices for most languages. Let's see how these principles apply to the improved code:

1. **Rule 1: Restrict all code to very simple control flow constructs.**
   This function does follow this rule. It's very straightforward with a simple control flow.

2. **Rule 2: Give all loops a fixed upper-bound.**
   This function doesn't use any loops, so it naturally satisfies this rule.

3. **Rule 3: Do not use dynamic memory allocation after initialization.**
   This rule is more relevant for languages like C that have manual memory management. Python handles memory allocation automatically, but we can interpret this rule as advising against unnecessary creation of new objects. The function does create new sets from the input lists, which is necessary for its purpose.

4. **Rule 4: No function should be longer than what can be printed on a single sheet of paper.**
   This function is quite short and easily fits on a single printed page, satisfying this rule.

5. **Rule 5: The assertion density of the code should average to a minimum of two assertions per function.**
   This rule isn't strictly followed in the function, as it doesn't use Python's `assert` statement. However, it does check for errors and raise exceptions, which can serve a similar purpose in some contexts.

6. **Rule 6: Data objects must be declared at the smallest possible level of scope.**
   This rule is followed in the function. All variables are local to the function and are declared close to where they are used.

7. **Rule 7: The return value of non-void functions must be checked by each calling function, and the validity of parameters must be checked inside each function.**
   The function does check the validity of its parameters. As for the return value, that's up to the calling code.

8. **Rule 8: The use of the preprocessor must be limited to file inclusion and simple macro definitions.**
   This rule is specific to C and doesn't apply to Python.

9. **Rule 9: The use of pointers should be restricted.**
   This rule is also specific to C and doesn't apply to Python.

10. **Rule 10: All code must be compiled with all compiler warnings enabled. The use of lint-like tools should also be part of the standard development process.**
    This rule can be applied to Python in the form of using tools like `pylint` or `flake8` for static analysis, and fixing any warnings or errors they report. The function doesn't have any obvious issues that would be flagged by such tools.

Remember, while these rules are a good guideline, they're not universally applicable to every language or project. It's important to consider the context and purpose of the code.

### Applying code quality tools on code 

you can use various code quality tools for Python to check for potential issues. While I can't run these tools in this current environment, I can guide you on how you could run them in your local setup. Here's a brief overview of some popular tools and how to use them:

- pylint: Pylint is a tool that checks for errors in Python code, tries to enforce a coding standard and looks for code smells. You can install it with pip (pip install pylint) and then run it on your python file like so: pylint your_file.py.

- flake8: Flake8 is a tool for enforcing style consistency across Python projects. It includes checks provided by other tools like PyFlakes and pycodestyle. Install it with pip (pip install flake8) and run it with: flake8 your_file.py.

- mypy: Mypy is an optional static type checker for Python. Since your code uses type annotations, mypy can be useful to ensure these are correct. Install it with pip (pip install mypy) and run it like so: mypy your_file.py.

- Black: Black is an uncompromising code formatter. It auto-formats your code to make it clean and consistent with the PEP 8 style guide. Install it with pip (pip install black) and run it with: black your_file.py.

- Bandit: Bandit is a tool designed to find common security issues in Python code. Install it with pip (pip install bandit) and run it like so: bandit your_file.py.

After running each of these tools on your Python file, they will provide you with a report detailing any issues they've found. Some will also provide suggested fixes.



<br>
<br>

## Refreshing Python on Programming Expert

Learning basics of Python at Algoexpert, partly as a restart/refresh and partly to be able to start write Mojo. 

### Fundamentals 

- Data types
- Comments
- Variables and printing
- Console input
- Arithmetic operations
- Type conversions
- Conditions
- Compound conditions
- Conditionals
- Lists
- Strings
- Tuples
- For loops
- While loops
- **Slices**
- Dictionaries
- Sets
- Exceptions
- Functions
- Mutability
- Scope
- Math
- Sorting
- Misc syntax

### Object-oriented programming 

- Classes
- Methods
- Properties
- Class methods and attributes
- Stabic Methods
- Inheritance
- Abstract classes
- Interfaces
- Operator overloading 

### Advanced programming 

- Modules and packages
- Files
- Args and Kwargs
- Lambda functions
- Map and filter
- Function closures
- Decorators
- Iterators
- Generators
- Compilers and interpreters
- Threads and processes
- Python global Interpreter
- Threads
- Asynchronous programming 

### software design principles

  #### Divide and conquer
  
  #### Cohesion

 In the context of software design, the various types of cohesion refer to how different elements of a program or system work together. Different types of cohesion describe different levels of organization and cooperation among these elements. Here's an overview of the types you mentioned, along with examples:

1. **Functional Cohesion:** This is the strongest type of cohesion in which the degree of cohesion is highest. Elements are part of a module because they all contribute to a single well-defined task. Example: A function in a program that calculates the area of a circle. 

    ```python
    def calculate_area(radius):
        return 3.14 * (radius**2)
    ```

2. **Sequential Cohesion:** This type of cohesion occurs when parts of a module are grouped because the output from one element serves as the input to another element. Example: A function that reads from a file and processes the read data.

    ```python
    def read_and_process(file_name):
        with open(file_name, 'r') as file:
            data = file.read()
        # The following line is a placeholder for data processing
        processed_data = data.upper()
        return processed_data
    ```

3. **Communicational Cohesion:** This type of cohesion exists when parts of a module are grouped because they operate on the same data (i.e., they share a data structure). Example: A class that performs various operations on the same instance variable.

    ```python
    class Circle:
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * (self.radius ** 2)

        def circumference(self):
            return 2 * 3.14 * self.radius
    ```

4. **Procedural Cohesion:** Elements are grouped together, which must be executed in a particular order in which they relate to each other procedurally i.e., the order of execution is important.

    ```python
    def make_tea():
        boil_water()
        add_tea_leaves()
        steep_tea()
        serve_tea()
    ```

5. **Temporal Cohesion:** Elements of the module are organized such that they are processed at a similar point in time. They are used for initialization, cleanup, etc.

    ```python
    def startup():
        load_configurations()
        establish_database_connections()
        initialize_system_logs()
        start_services()
    ```

6. **Logical Cohesion:** A module has logical cohesion if there is some logical relationship between the activities of the module, and the complex logic is controlled by control variables passed to the module. A good example of logical cohesion would be a function that executes a different mathematical operation (add, subtract, multiply, divide) based on a parameter.

    ```python
    def execute_operation(x, y, operator):
        if operator == '+':
            return x + y
        elif operator == '-':
            return x - y
        elif operator == '*':
            return x * y
        elif operator == '/':
            return x / y
        else:
            return None
    ```

7. **Utility Cohesion (Coincidental Cohesion):** This is the lowest type of cohesion. It occurs when parts of a module are grouped arbitrarily. That is, the parts have no significant relationship (other than perhaps they have been grouped in the same module).

    ```python
    class Utilities:
        @staticmethod
        def read_file(file_name):
            with open(file_name, 'r') as file:
                data = file.read()
            return data

        @staticmethod
        def calculate_area(radius):
            return 3.14 * (radius ** 2)
    ```

These two methods are grouped together in a utility class but they don't share a logical relationship.

8. **Layer Cohesion:** A layered system is composed of a number of layers, each providing services to the layer above it. So, the way that classes and functions are organized in layers can also be an example of cohesion. For example, in a MVC (Model-View-Controller) structure, each layer has its specific tasks:

    - Model: Data handling
    - View: User Interface (UI)
    - Controller: Handles user requests and manipulates the model

In Python, this might look something like this:

```python
class Model:
    data = []

    def add_data(self, new_data):
        self.data.append(new_data)

class View:
    def display_data(self, data):
        for item in data:
            print(item)

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def add_and_display_data(self, new_data):
        self.model.add_data(new_data)
        self.view.display_data(self.model.data)
```

  
In this example, each class in a different layer has its own specific tasks, maintaining a good level of cohesion within each layer.

 ##### Coupling

Coupling refers to the degree of interdependence between things. In programming, it is typically desirable to reduce coupling. There are many different types of coupling:

- Content: a component secretly modifies the internal data of another component.
- Stamp: an argument type of a method is an application class.
- Routine Call: A routine calling another routine.
- Type Use: Use of globally defined data types.
- Inclusion/Import: importing unnecessary components.
- External: a dependency on something outside of the scope of the system like an operating system, shared library, hardware etc.


#### Over de-coupling (micro-services) 

One of the potential downsides of a pure microservices architecture is that it can be "over-decoupled," leading to some complications.

While the goal of a microservices architecture is to create services that are loosely coupled and can evolve independently, this can sometimes be taken to an extreme, resulting in a system where services are so independent that it becomes challenging to maintain overall system integrity. 

Here are some challenges that can arise from an over-decoupled microservices architecture:

1. **Network Overhead and Latency:** Each microservice communicates over the network, which can introduce latency and potentially reduce performance, particularly when many services need to communicate to perform a single operation.

2. **Data Consistency:** Ensuring data consistency across services can be difficult, especially since each microservice has its own separate database.

3. **Complexity:** Managing, deploying, and monitoring a large number of services can be more complex than dealing with a monolithic application.

4. **Inter-Service Communication:** There's a need for a well-defined, robust communication mechanism between services to handle inter-service requests and responses.

5. **Distributed System Complexity:** Implementing a distributed system, like a microservices architecture, introduces complexities inherent in distributed computing, such as network partitioning, distributed transactions, and more.

Therefore, while a microservices architecture can provide significant benefits in terms of scalability and development speed, it's important to consider these potential challenges when deciding whether to adopt this architectural style. Over-decoupling can lead to a loss of the benefits that come from having an integrated, cohesive system, so it's crucial to strike the right balance between coupling and decoupling in a system's architecture.


  #### Abstraction, etc
  
  - Reusability
  - Reuse
  - Flexibility
  - Obsolescensce
  - Portability
  - Testability
  - Defensibility 

### Software engineering tools 

### Programming with Go 

### Projects 



## Python, Zen and Pep 484 

The PEP 20, written in 2004 by Tim Peters, do not mentiong typing or hinting, which was introduced in 2015 through PEP 484. 

## PEP 20 (Zen of Python) 

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

## Python and typing  

|                   | Statically-Typed  | Dynamically-Typed |
|-------------------|:-----------------:|:-----------------:|
| Strongly-Typed    | C++, C#, Java, Rust, Go, TypeScript | Python, Ruby |
| Weakly-Typed      | - | JavaScript, PHP, Perl |

### Python, type hints and static type checking 

| Timeframe   | Python Default | Python with Type Hints | Python with Static Type Checking |
|-------------|----------------|------------------------|----------------------------------|
| Compile Time | Python's interpreter compiles the source code into bytecode. No type checking is performed at this stage. | Python's interpreter compiles the source code into bytecode. No type checking is performed at this stage, type hints are ignored by the interpreter. | Tools like Mypy can be used to perform static type checking based on type hints, catching potential type errors before runtime. |
| Runtime | Python is dynamically typed, meaning types are checked at runtime. If an operation is performed on incompatible types, Python will raise a TypeError. | Python remains dynamically typed, meaning types are checked at runtime. Type hints do not enforce type checking at runtime, but they provide additional information that can be used by certain tools. | Python remains dynamically typed. Even with static type checking, type errors can still occur at runtime if they are not caught by the static type checker (for instance, if part of the code is not type-annotated). |
| Enforcement | Python enforces dynamic typing at runtime by raising a TypeError when an operation is performed on incompatible types. | Python does not enforce type hints at runtime. They are more like guidelines to the developer and static analysis tools. | Tools like Mypy enforce type hints at compile time, but this is not a built-in feature of Python itself. At runtime, Python's enforcement remains dynamic. |


#### Examples of Python without type hints 

While type hinting and static type checking tools have many advantages, they do come with some potential downsides:

- Increased Complexity: Adding type hints to your code can make it more complex and potentially harder to read, especially for people who are not used to seeing type hints in Python code. This can be particularly true when using more complex type hints, like those involving generics or custom classes.

- Development Time: It takes extra time to write out the type hints, especially in a large codebase. If you are not using a static type checker or other tools that take advantage of the type hints, this time might be better spent on other things.

- Flexibility: One of the strengths of Python is its dynamic typing, which allows for a great deal of flexibility. By adding type hints and enforcing them with static type checking, you are opting into a more rigid style of coding that reduces this flexibility.

- Maintenance: Type hints need to be maintained just like any other part of your code. If the types of your variables change, you'll need to update the type hints as well.

- Learning Curve: If you're new to static typing or type hinting, there can be a learning curve to understanding how to properly use and interpret them. This is particularly true for more complex type hints.

- Tooling Overhead: Using static type checking tools and other code quality tools adds another layer of complexity to your development process. You have to configure and maintain these tools, and they can sometimes give false positives or negatives, which can be frustrating.

Despite these potential downsides, many developers find that the benefits of type hinting and static type checking — like improved code clarity, better tooling support, and catching errors earlier — outweigh the costs. However, whether or not to use these features can depend on your specific situation, such as the size and complexity of your codebase, your team's familiarity with type hints, and the requirements of your project.

```
# Variable without typing
x = 10

# Function without typing
def add(a, b):
    return a + b

# Calling the function
result = add(5, 3)
print(result)  # Outputs: 8
```


#### Examples of Python with type hints 

Even without using a static type checker, type hints in Python can still provide several benefits:

- Readability: Type hints can make your code easier to understand. When you or other developers read the code, the type hints can provide immediate understanding about what type of values a function expects and what it will return.

- Self-documenting code: Type hints act as a form of documentation that stays up-to-date with the code. It's very helpful for API development where knowing the expected input and output types is crucial.

- IDE Support: Many modern integrated development environments (IDEs) and code editors support type hints for features like code-completion, refactoring, and error highlighting. This can help catch potential bugs early in the development process and improve developer productivity.

- Reduced Debugging Time: While they do not eliminate the need for unit testing, type hints can help identify certain types of issues early on, before the code is run or tests are executed.

- Maintainability: As a project grows, type hints become increasingly valuable. They can make refactoring easier, help you navigate through the code base, and make it easier for new developers to understand the existing code.

Remember, Python's type hints are optional and are not enforced at runtime. This means you can gradually introduce them into a code base, adding them to the most critical parts of the program first, without having to commit to using them everywhere. This flexibility is one of the strengths of Python's approach to typing.

```
from typing import List, Tuple

# Variable with typing
x: int = 10

# Function with typing
def add(a: int, b: int) -> int:
    return a + b

# Calling the function
result = add(5, 3)
print(result)  # Outputs: 8

# List with typing
numbers: List[int] = [1, 2, 3]

# Tuple with typing
coordinate: Tuple[float, float] = (10.5, 20.5)

```

### Tools that might help writing more Pythonic code 

- Python Linting: VS Code provides built-in support for Python linting, which can help identify potential errors and non-Pythonic code. You can configure your preferred linter in the VS Code settings. Common choices include pylint and flake8.

- AutoPEP8: autopep8 is a tool that automatically formats Python code to conform to the PEP 8 style guide. It can be integrated into VS Code and can automatically format your code whenever you save a file.

- Black: Black is a more opinionated code formatter than autopep8. It takes away some of the formatting choices to provide a uniform style across the codebase. It can also be integrated with VS Code and has gained a lot of popularity in the Python community.

- Mypy: Mypy is a static type checker for Python. If you're using type annotations, Mypy can check that your types are correct according to your annotations.

- VS Code Python extension: The Python extension for VS Code, provided by Microsoft, has built-in support for linting, IntelliSense (code completions), code formatting, and more.


#### Popular Python Packages (their optimizations, and Mojo) 

| Python Library | Description | Typical Enterprise Roles | Typical Optimizations | Mojo Optimizations | Core Concepts |
|----------------|-------------|--------------------------|-----------------------|-------------------|---------------|
| NumPy | Fundamental package for numerical computations | Data Scientists, Machine Learning Engineers, Quantitative Analysts | Uses pre-compiled C code for array operations | Not Applicable | Array operations, Broadcasting, Vectorization |
| Pandas | High-performance, easy-to-use data structures and data analysis tools | Data Scientists, Data Analysts, Machine Learning Engineers | Built on top of NumPy, uses Cython for critical paths | Not Applicable | DataFrame operations, Data wrangling |
| Matplotlib | Plotting library for creating static, animated, and interactive visualizations | Data Scientists, Data Analysts, Machine Learning Engineers | Performance-sensitive parts are in C/C++ | Not Applicable | Data visualization, Plotting |
| Scikit-Learn | Provides simple and efficient tools for machine learning and data mining | Data Scientists, Machine Learning Engineers | Uses Cython for critical code paths | Not Applicable | Machine Learning, Model selection and evaluation |
| TensorFlow | End-to-end open-source platform for machine learning | Machine Learning Engineers, Data Scientists, AI Researchers | Acceleration using GPUs and TPUs, efficient C++ backend | Not Applicable | Neural networks, Tensor operations, GPU computing |
| PyTorch | Open-source machine learning library for Python | Machine Learning Engineers, Data Scientists, AI Researchers | Supports GPU acceleration, efficient C++ backend | Not Applicable | Neural networks, Tensor operations, Auto-differentiation |
| Keras | User-friendly neural network library | Machine Learning Engineers, Data Scientists | Uses TensorFlow as its backend, benefiting from TensorFlow's optimizations | Not Applicable | Neural networks, Deep learning |
| SciPy | Library used for scientific and technical computing | Data Scientists, Machine Learning Engineers, Quantitative Analysts | Built on top of NumPy, parts are in C or Fortran | Not Applicable | Scientific computing, Optimization, Linear algebra |
| Seaborn | Statistical data visualization library | Data Scientists, Data Analysts | Built on top of Matplotlib, relies on its optimizations | Not Applicable | Data visualization, Statistical graphics |
| Flask | Lightweight and easy-to-use framework for developing web applications | Web Developers, Back-end Developers | Can be served with robust WSGI servers like Gunicorn or uWSGI | Not Applicable | Web development, RESTful APIs, HTTP protocols |
| Django | High-level Python web framework for developing secure and maintainable websites | Web Developers, Back-end Developers | Uses middleware classes, caching can be applied at multiple levels | Not Applicable | Web development, ORM, Middleware, MVC |
| BeautifulSoup | Library for parsing HTML and XML documents, often used for web scraping | Data Scientists, Data Analysts, Web Developers | Can use lxml's parser which is written in C | Not Applicable | HTML/XML parsing, Web scraping |
| Requests | Simple and elegant HTTP library to send HTTP requests | Web Developers, Back-end Developers, Data Scientists | Using sessions can make multiple requests faster | Not Applicable | HTTP requests, RESTful APIs |
| Pygame | Set of Python modules designed for writing video games | Game Developers, Software Developers | Can use Pygame's functionality with Pygame_SDL2 | Not Applicable | Game development, Event handling, Game physics |
| NLTK | Library for working with human language data | Data Scientists, NLP Engineers, AI Researchers | Performance can be improved by using alongside libraries like NumPy | Not Applicable | Natural Language Processing, Text analytics, Linguistic structure |
| Spacy | Open-source library for Natural Language Processing | Data Scientists, NLP Engineers, AI Researchers | Written in Cython, specifically designed to be fast, support for parallel processing | Not Applicable | Natural Language Processing, Text analytics, Linguistic structure |


##### How to approach learning the most popular libraries 

| Python Library | Recommended Resources | Learning Tips |
|----------------|----------------------|---------------|
| NumPy | [NumPy Official Documentation](https://numpy.org/doc/stable/), [NumPy course from Kaggle](https://www.kaggle.com/learn/numpy), [Python Numpy Tutorial from CS231n](https://cs231n.github.io/python-numpy-tutorial/) | Start with understanding the basics of array manipulation. Experiment with array operations, slicing, indexing, and broadcasting |
| Pandas | [10 minutes to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html), [Pandas course from Kaggle](https://www.kaggle.com/learn/pandas), [Python for Data Analysis by Wes McKinney](https://www.oreilly.com/library/view/python-for-data/9781491957653/) | Learn basic data manipulation operations like filtering, grouping, merging, reshaping data. Practice by analyzing datasets |
| Matplotlib | [Matplotlib Official Tutorials](https://matplotlib.org/stable/tutorials/index.html), [Python Plotting With Matplotlib (Guide) from Real Python](https://realpython.com/python-matplotlib-guide/) | Start with basic plots like line, bar and scatter plots. Gradually move to more complex plots and customization |
| Scikit-Learn | [Scikit-Learn Official User Guide](https://scikit-learn.org/stable/user_guide.html), [Introduction to Machine Learning with Python by Andreas C. Müller & Sarah Guido](https://www.oreilly.com/library/view/introduction-to-machine/9781449369880/) | Start with basic concepts like model fitting, prediction, validation, and then explore various machine learning algorithms. Try to implement these algorithms on datasets |
| TensorFlow | [TensorFlow Official Tutorials](https://www.tensorflow.org/tutorials), [TensorFlow for Deep Learning by Bharath Ramsundar and Reza Bosagh Zadeh](https://www.oreilly.com/library/view/tensorflow-for-deep/9781491980446/) | Start with the basic operations, then move onto building simple models and training them. Gradually progress towards complex models |
| PyTorch | [PyTorch Official Tutorials](https://pytorch.org/tutorials/), [Deep Learning with PyTorch by Eli Stevens, Luca Antiga, and Thomas Viehmann](https://www.manning.com/books/deep-learning-with-pytorch) | Similar to TensorFlow, start with the basics and gradually move on to more complex topics. The book provides a more detailed and practical approach |

##### What other skills are needed? 

Before you start with these libraries, you should have a solid understanding of Python programming. Here are some central concepts:

1. **Python Fundamentals**: Basics such as variables, data types, loops, conditionals, functions, and error handling.

2. **Data Structures**: Understanding of lists, tuples, sets, dictionaries, and how to manipulate them.

3. **Object-Oriented Programming (OOP)**: Classes, objects, inheritance, and polymorphism are core concepts in Python and many libraries.

4. **File I/O**: How to read from and write to files, which is particularly useful for data handling.

5. **Understanding of Libraries/Modules**: How to import and use Python libraries or modules.

6. **Exception Handling**: Understanding of how to catch and handle exceptions.

As for computer science courses, these would be beneficial:

1. **Intro to Computer Science**: This course lays the foundation and teaches basics of programming and computational thinking.

2. **Data Structures and Algorithms**: This is essential for understanding how to organize, store, and retrieve data efficiently.

3. **Databases**: Knowing how to interact with databases can be beneficial as many data science tasks involve retrieving data from databases.

4. **Statistics**: While not a computer science course per se, understanding statistics is crucial for data analysis and machine learning.

5. **Machine Learning**: A course on the basics of machine learning would be beneficial before diving into libraries like Scikit-Learn, TensorFlow, and PyTorch.

6. **Linear Algebra**: This is essential for understanding many data science and machine learning algorithms.

Remember, while these courses are beneficial, they are not strictly necessary to start learning these libraries. You can always pick up the necessary skills as you go along, especially if you're more interested in practical applications. Self-study through online resources can be just as effective, if not more so, than formal coursework.

<br>

## Go 

<br>

## JavaScript 

### Typescript

<br>

## New languages 

### Mojo

Modular is an integrated, composable, suite of tools that simplifies your AI infrastructure so your team can develop, deploy and innovate faster. 

Mojo is a new programming language, for "AI developers", a superset of of Python, with the performance of C. 

#### MLIR 


<br>
<br>

### Zig

<br>
<br>
<br>

## VS Code, Replit, Vercel 

Attribute         | Replit                                     | Vercel                                              | VS Code
------------------|--------------------------------------------|-----------------------------------------------------|----------------------------------
Category          | Online code editor and compiler             | Deployment and hosting platform                     | Local code editor
Language Support  | Supports multiple languages like Python, JavaScript, C++, etc. | Primarily used with JavaScript and related technologies like Next.js, but can support other languages | Supports multiple languages and has extensions for even more
Collaboration     | Offers real-time collaborative editing       | Collaboration through version control (git)          | Live Share extension allows for real-time collaboration
Deployment        | Has built-in hosting for web apps           | Specializes in hosting and deployment, with a focus on front-end projects | Does not provide hosting; used for development
Debugging         | Basic debugging features                    | Does not offer debugging; for deployment and hosting | Advanced debugging features available through extensions
Pricing           | Free for basic use, with paid tiers for more resources and private repls | Free for basic use, with paid tiers for more features and resources | Free
Use Case          | Good for quick prototyping and teaching     | Good for deploying static websites and serverless functions | Full-fledged development environment for various use cases

<br>
<br>

