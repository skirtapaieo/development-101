
# Backend 

## Overview 

Almost any back-end framework, works with any front-end framework - suggestions based on what is commonly used in the community 

| Language | Framework | Type | Description | Optimal Front-End |
|---|---|---|---|---|
| JavaScript | Express.js | Traditional | A minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. | Angular, React, Vue |
| JavaScript | Nest.js | Traditional | A framework for building efficient, scalable Node.js server-side applications. It uses progressive JavaScript, is built with and fully supports TypeScript, and combines elements of OOP, FP, and FRP. | Angular, React, Vue |
| JavaScript | Koa.js | Traditional | A next-generation web framework for Node.js created by the team behind Express.js. It aims to be a smaller, more expressive, and more robust foundation for web applications and APIs. | Angular, React, Vue |
| JavaScript | Next.js | SSR | A React framework with server-side rendering and path-based routing. | React |
| JavaScript | Nuxt.js | SSR | A Vue.js framework with server-side rendering and path-based routing. | Vue.js |
| Go | Gin Gonic | Traditional | A web framework written in Go. It features a martini-like API with much better performance, up to 40 times faster. | React, Angular, Vue |
| Go | Echo | Traditional | A high performance, extensible, minimalist web framework for Go. | React, Angular, Vue |
| Go | Revel | Traditional | A high-productivity web framework for the Go language that does not require any setup. | React, Angular, Vue |
| Python | Django | Traditional | A high-level Python web framework that encourages rapid development and clean, pragmatic design. | React, Angular, Vue |
| Python | Flask | Traditional | A micro web framework written in Python. | React, Angular, Vue |
| Python | Pyramid | Traditional | A small, fast, down-to-earth, open source Python web framework. | React, Angular, Vue |
| Python | FastAPI | Traditional | A modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. | React, Angular, Vue |

### Comment on Typescript and Type of Typing  

Python and Go are both statically-typed languages, which means they perform type checking at compile time, similar to TypeScript. However, they handle this in different ways and have different levels of strictness.

Python uses a system called "type hints" or "type annotations". This is optional typing, which means that you can choose whether or not to use it in your Python code. It was introduced in Python 3.5 as a means of achieving TypeScript-like static typing. Python type hints allow you to indicate the expected type of function arguments, return values, and variable assignments. However, these type hints are mostly used for development tools (like IDEs and linters) and don't affect the runtime behavior of the code. Python's type checking is not as strict as TypeScript's.

Go, on the other hand, is strongly statically-typed, and all variables have to be explicitly declared with their type. If you try to use a variable of one type where a different type is expected, the Go compiler will throw an error. This is quite similar to TypeScript, which also requires you to declare types for your variables and function arguments/return values, and checks types at compile time.

So, in short, while there is not a "TypeScript for Python" or "TypeScript for Go" in terms of being a superset language that adds static typing, both Python and Go do have their own static typing systems. Python's is optional and less strict, while Go's is mandatory and quite strict.
