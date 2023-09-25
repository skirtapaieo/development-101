
# Backend 

<br>

## Table of Contents

- [Back-end frameworks](#back-end-frameworks)
  - [Comment on Typescript and Type of Typing](#comment-on-typescript-and-type-of-typing)
- JavaScript Back-end Frameworks 
  - [Next.js](#nextjs)
    - [Principles](#principles)
    - [Why did Vercel develop it?](#why-did-vercel-develop-it)
    - [Comparison Next vs Express](#comparison-next-vs-express)
- [Python Back-end Frameworks](#python-back-end-frameworks)
  - [Overview](#overview)
  - [Flask vs Vanilla Python](#flask-vs-vanilla-python) 
- [Server-side rendering (SSR), Static site generation (SSG) or client side generation (CSG)](#server-side-rendering-ssr-static-site-generation-ssg-or-client-side-generation-csg)
  - [Decision tree for picking the right approach](#decision-tree-for-picking-the-right-approach)


## Back-end frameworks 

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

<br>

### Comment on Typescript and Type of Typing  

Python and Go are both statically-typed languages, which means they perform type checking at compile time, similar to TypeScript. However, they handle this in different ways and have different levels of strictness.

So, in short, while there is not a "TypeScript for Python" or "TypeScript for Go" in terms of being a superset language that adds static typing, both Python and Go do have their own static typing systems. Python's is optional and less strict, while Go's is mandatory and quite strict.

#### Python 

Python uses a system called "type hints" or "type annotations". This is optional typing, which means that you can choose whether or not to use it in your Python code. It was introduced in Python 3.5 as a means of achieving TypeScript-like static typing. Python type hints allow you to indicate the expected type of function arguments, return values, and variable assignments. However, these type hints are mostly used for development tools (like IDEs and linters) and don't affect the runtime behavior of the code. Python's type checking is not as strict as TypeScript's.

#### Go 
Go, on the other hand, is strongly statically-typed, and all variables have to be explicitly declared with their type. If you try to use a variable of one type where a different type is expected, the Go compiler will throw an error. This is quite similar to TypeScript, which also requires you to declare types for your variables and function arguments/return values, and checks types at compile time.

## JavaScript Backend Frameworks

### Next.js 

#### Principles 

Next.js is a popular React framework built by Vercel with several core principles and features that make it stand out. These include:

1. **Hybrid Static & Server Rendering**: Next.js offers flexible rendering modes, including static generation (SSG), server-side rendering (SSR), and incremental static regeneration (ISR). With this flexibility, you can choose the most suitable rendering strategy for each page according to its needs. This is a key principle and feature of Next.js.

2. **File System Routing**: Next.js follows a file-system based router built on the concept of pages. When a file is added to the 'pages' directory, it's automatically available as a route.

3. **Automatic Code Splitting**: This is an important feature for performance. Next.js will only load the JavaScript needed for the current page, instead of loading all the JavaScript at once. This leads to faster page loads.

4. **Built-in CSS and Sass Support, and support for any CSS-in-JS library**: Next.js comes with built-in CSS and Sass support. You can import CSS/Sass files from any React component.

5. **Hot Code Reloading**: Next.js automatically reloads the application in the browser whenever a file is saved in the text editor.

6. **API Routes**: Next.js provides a solution to build your API with serverless functions, which allows you to create a backend API endpoint inside a Next.js app. You can do this by creating a file inside the 'pages/api' directory.

7. **TypeScript Support**: Next.js provides an integrated TypeScript experience out of the box, with automatic TypeScript configuration and compilation.

8. **Fast Refresh**: Next.js includes Fast Refresh, which preserves component state and only updates the files you edit.

9. **Zero Configuration**: Next.js works out of the box with default configurations, but can also be customized for more complex use cases.

10. **Optimization and Bundling**: Next.js is optimized for production from the start, providing automatic static optimization and client-side data fetching. It also supports ES6 features and uses Webpack for bundling.
  
In essence, Next.js offers developers an advanced and versatile framework for building React applications, balancing ease of use with the flexibility to handle more complex use cases.

#### Why did Vercel develop it? 

Vercel (formerly Zeit) developed Next.js to solve the common challenges in setting up and configuring a React application, especially for production. Their goal was to provide a solution that enabled developers to quickly bootstrap a new project and also provided a clear and efficient way to build highly performant, SEO-friendly, production-ready applications. Here are some specific reasons:

In summary, Vercel developed Next.js to help developers build production-ready React applications with ease, speed, and scalability.


1. **Ease of Setup**: Setting up a production-ready React application can be complex and time-consuming. With Next.js, developers can get started right away with sensible defaults and conventions.

2. **Universal JavaScript**: Next.js allows developers to use JavaScript both on the client and the server. This simplifies development and improves performance by rendering pages on the server-side before sending them to the client.

3. **Performance**: By introducing features like automatic code-splitting and server-side rendering, Next.js aims to make it easier to build fast, highly performant web applications.

4. **Developer Experience**: With features like hot-module replacement, automatic routing based on the filesystem, and support for CSS and Sass, Next.js provides an excellent developer experience out of the box.

5. **Hybrid Static & Server Rendering**: To give developers the flexibility to choose the right rendering strategy for each page in their application, be it Static Site Generation (SSG), Server Side Rendering (SSR), or Incremental Static Regeneration (ISR).

6. **SEO-friendly**: Since Next.js supports server-side rendering, it's more SEO-friendly than client-side-rendered applications. It helps search engine crawlers to index the pages more effectively, resulting in better visibility on search engine results.

7. **Scalability**: Next.js, in combination with Vercel's hosting platform, is designed to scale effortlessly, meeting the needs of both small projects and large enterprise applications.

#### Comparison Next vs Express

Sure, let's compare the principles of Next.js and Express.js in a tabular form. 

|                             | Next.js                                                                                                                                                                                                                                                                                      | Express.js                                                                                                                                             |
|-----------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Ease of Setup**               | Very straightforward setup with less configuration. Provides an integrated toolset which simplifies the process of starting a new project.                                                                                                                           | Very flexible but requires manual configuration and setup. It doesn’t dictate a certain project structure.                                             |
| **Universal JavaScript**       | Supports Universal JavaScript (JavaScript that can run both on the client and the server). This simplifies development and can improve performance.                                                                                                              | Mainly for backend development. If universal JavaScript is needed, it would require additional configuration with a bundler like Webpack.             |
| **Performance**                | Built-in code splitting and server-side rendering for improving performance.                                                                                                                                                                                  | Very performant, but features like code splitting or server-side rendering need to be implemented manually.                                            |
| **Developer Experience**       | Excellent developer experience with features like hot-module replacement, automatic routing based on the filesystem, and built-in CSS/SASS support.                                                                                                             | Great flexibility and simplicity. Developers have total control over how they want to structure their application, but this requires more setup work. |
| **Hybrid Static & Server Rendering**  | Provides support for both static site generation (SSG), server-side rendering (SSR), and incremental static regeneration (ISR). This gives developers flexibility to choose the best rendering strategy for each page.                                         | Primarily a server-side rendering (SSR) framework. Static site generation would need to be manually implemented.                                       |
| **SEO-friendly**                | Because of its support for server-side rendering, Next.js is generally more SEO-friendly than single-page applications (SPAs) that are purely client-rendered.                                                                                                   | It can also serve SEO-friendly pages as it is a server-side rendering framework. However, if used in conjunction with a frontend framework like React, additional setup would be required for SEO optimization. |
| **Scalability**                 | Designed for scalability. It can be deployed to a serverless environment easily, especially on Vercel's own platform, enabling easy scaling.                                                                                                                     | Highly scalable but it requires manual scaling configuration, either through setting up load balancers or deploying to a PaaS provider.              |
| **Routing**                     | Automatic routing based on the file system. This means you do not need to manually set up your routes.                                                                                                                                                         | Requires manual setup for routing. However, this gives you a lot of flexibility in how you want to handle routing.                                     |
| **API routes**                  | Provides built-in support for API routes, which means you can build your frontend and API all in one place.                                                                                                                                                     | Express.js is a go-to solution for building APIs, providing a lot of flexibility in terms of how you structure and handle your API endpoints.         |
| **Integrated Toolset**         | Provides an integrated toolset for modern web development including pre-rendering, CSS-in-JS, hot module replacement etc.                                                                                                                                      | Express is unopinionated and minimalist - it does not come with integrated tools for things like hot module replacement or CSS-in-JS. You need to add them manually.  |
 
This table outlines the major differences between Next.js and Express.js. However, the best choice between the two depends largely on the specific requirements of the project. Express.js offers more flexibility and control, while Next.js provides more out-of-the-box features that can speed up development and improve productivity, especially for React projects.

## Python Back-end frameworks

### Overview 

Here is a simplified comparison of the underlying principles of Flask, Django, Pyramid, and FastAPI:

| Principle/Characteristic | Flask | Django | Pyramid | FastAPI |
|----------------------|-------|--------|---------|---------|
| Simplicity           | Yes   | Yes    | Yes     | Yes     |
| Flexibility          | Yes   | No     | Yes     | Yes     |
| Extensibility        | Yes   | Yes    | Yes     | Yes     |
| Batteries-Included   | No    | Yes    | No      | Partial |
| DRY (Don't Repeat Yourself) | No   | Yes    | Yes     | Yes     |
| Rapid Development    | Yes   | Yes    | Yes     | Yes     |
| High Performance     | No    | No     | No      | Yes     |
| Automatic Data Validation | No | Yes | Yes | Yes |
| Interactive API documentation | No | No | No | Yes |
| Asynchronous Programming Support | No | No | Yes | Yes |
| Security Features    | Yes   | Yes    | Yes     | Yes     |
| Testability          | Yes   | Yes    | Yes     | Yes     |
| Built-in ORM         | No    | Yes    | No      | No      |
| Support for RESTful APIs | Yes | Yes | Yes | Yes |

Notes: 

- For the Batteries-Included characteristic, Django offers a full suite of tools and features out of the box, whereas Flask, Pyramid, and FastAPI are more minimalistic and offer only a core set of features, though FastAPI does include more built-in features compared to Flask and Pyramid.
- For Automatic Data Validation, Django, Pyramid, and FastAPI provide these features, while Flask does not include them in its core but can be extended using libraries like WTForms or Marshmallow.
- For Interactive API documentation, only FastAPI includes automatic generation of interactive API documentation.
- For Asynchronous Programming Support, only Pyramid and FastAPI support it natively.
- For the Built-in ORM characteristic, Django provides a full-featured ORM, whereas Flask, Pyramid, and FastAPI do not include an ORM in their core package but can be easily integrated with external ORMs like SQLAlchemy.

Remember, these characteristics can be implemented in all these frameworks using the right extensions or coding practices. This table is designed to show what each framework includes or emphasizes out of the box.

<br> 

### Flask vs Vanilla Python 

Let's consider a simple example where we want to create a web server that responds to HTTP GET requests at the endpoint '/hello' with the message 'Hello, World!'. 

Here's how you might do it in "vanilla" Python, using only the built-in `http.server` module:

```python
# Vanilla Python with http.server
from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/hello':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        else:
            self.send_response(404)

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

run()
```

Now, let's consider how we might achieve the same functionality using Flask, which is a minimalist Python web framework:

```python
# Flask
from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(port=8000)
```

Here are some ways that using Flask improves upon the "vanilla" Python example:

1. **Simplicity**: The Flask code is significantly shorter and easier to understand. There's no need to manually handle HTTP headers, status codes, or server setup - Flask takes care of all of this behind the scenes.

2. **Flexibility**: It's easy to add new routes in Flask - just define a new function and use the `@app.route` decorator to specify the path. In the "vanilla" Python example, you'd need to modify the `do_GET` method each time you want to add a new route.

3. **Testability**: Flask provides built-in support for unit testing, which makes it easier to test your routes and ensure that they're working as expected. Testing a server written using `http.server` would require additional tools or libraries.

4. **Development Features**: Flask comes with features like automatic reloading during development, and detailed error pages, both of which can speed up the development process.

This example illustrates why using a web framework like Flask, Django, Pyramid, or FastAPI is typically more efficient than using "vanilla" Python for web development. Each of these frameworks offers its own set of features and advantages, but they all aim to make it easier and faster to develop reliable, production-ready web applications.

<br>

## Server-side rendering (SSR), Static site genereation (SSG) or client side generation (CSG)

When building a React/Next.js application, choosing when to use Server-Side Rendering (SSR), Static Site Generation (SSG), and Client-Side Rendering (CSR) is an important decision. Here are some guiding principles regarding these methods:

1. **Server-Side Rendering (SSR):**

- SSR is useful when you need the data from the server at the very initial page load.
- It's beneficial for SEO as the search engine crawlers receive a fully rendered HTML page.
- SSR is ideal for dynamic and user-specific data. If every request results in different data, SSR can help as it fetches and displays real-time data.
- Keep in mind that SSR can be computationally expensive since the server has to render a new HTML page for every new request.

2. **Static Site Generation (SSG):**

- SSG is useful when your website data doesn't change often. You can generate HTML at build time, resulting in fast page loads.
- It's excellent for SEO, similar to SSR, as fully-rendered pages are served.
- Next.js supports Incremental Static Regeneration (ISR), which allows you to update static content after you've built your site. It's beneficial for content that changes infrequently.
- Pages can be cached by a CDN, making them incredibly fast to serve.

3. **Client-Side Rendering (CSR):**

- CSR is ideal when your page content changes frequently or is very dynamic (e.g., a real-time data dashboard).
- With CSR, once the JavaScript bundle is loaded, navigation between pages is fast since only necessary data is requested from the server, not an entire new page.
- SEO can be a challenge with CSR because not all web crawlers can effectively process JavaScript. However, many modern search engines have improved their ability to index client-rendered sites.
- It may cause a delay in interactivity on slower networks or devices due to the size of JavaScript files.

Each rendering method has its advantages, and often, a modern web application will use a combination of these techniques depending on the specific needs of each page or component. Next.js's hybrid approach allows you to choose on a per-page basis.

### Decision tree for picking the right approach 

A simple decision tree for choosing between SSR, SSG, and CSR when using Next.js:

1. **Does your page show static content that doesn't change often?**

   - Yes: Use Static Site Generation (SSG).
   
     1.1. Does your static content need to be updated occasionally?
     
        - Yes: Use Incremental Static Regeneration (ISR).
        - No: Use standard SSG.
   
   - No: Move to question 2.

2. **Does your page need to fetch and display data that changes frequently or is user-specific on each request?**

   - Yes: Use Server-Side Rendering (SSR).
   - No: Move to question 3.

3. **Does your page have highly dynamic content that changes on the client side or have a lot of user interaction?**

   - Yes: Use Client-Side Rendering (CSR).
   - No: Consider re-evaluating your page requirements, as it seems there's no dynamic or static data. Perhaps pure HTML/CSS will suffice.

Remember, these choices aren't mutually exclusive, and often a combination is used. With Next.js's hybrid nature, you can choose to use SSG for some pages and SSR for others in the same application. Additionally, you can start with CSR and then fetch and render additional data server-side as needed. 

This decision tree is a simplified guide. In real applications, you'll need to consider factors like the frequency of data updates, SEO requirements, user experience, page performance, and more.
