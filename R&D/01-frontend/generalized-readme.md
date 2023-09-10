# The concepts to think of

## The browser

- The request/s from the browser
- The data that is being sent
- HTML
- JavaScript
- Other - images, stylesheets

## Server-side vs client-side rendering

| Steps                        | Server-side Rendering (SSR)                                             | Client-side Rendering (CSR)                             | Static Site Generation (SSG)                       | SSR followed by Hydration                                                                                          |
| ---------------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Initial Request**          | User requests a webpage via the browser.                                | User requests a webpage via the browser.                | User requests a pre-generated page.                | User requests a webpage via the browser.                                                                           |
| **Server Processing**        | Server processes the request, runs backend code.                        | Server sends minimal HTML structure.                    | No processing; static content served.              | Server processes the request, runs backend code.                                                                   |
| **HTML Generation**          | Server generates full HTML based on templates/data.                     | JavaScript in browser generates content.                | HTML pages generated at build time.                | Server generates full HTML based on templates/data.                                                                |
| **Response to Browser**      | Server sends fully rendered HTML to the browser.                        | Browser displays initial HTML, then JS updates.         | Server sends static HTML file to browser.          | Server sends rendered HTML, then JS "hydrates" the view.                                                           |
| **Browser Parsing**          | Browser parses/displays the received HTML.                              | Browser parses initial HTML, processes JS.              | Browser parses/displays static HTML.               | Browser parses received HTML, processes JS for interactivity.                                                      |
| **Fetching Additional Data** | Might use AJAX for dynamic updates.                                     | JS often makes AJAX/API requests for data.              | Typically not required.                            | JS might make AJAX/API requests for further interactions/data.                                                     |
| **Updating the View**        | Requires new request for full page updates.                             | Can update parts of the view with JS.                   | Cannot update without regeneration.                | Can update specific parts with JS without full page reloads.                                                       |
| **Routing**                  | Managed on server (e.g., Express routes, Django URLs).                  | Managed in client by JS libraries (e.g., React-Router). | Pre-defined during build, limited dynamic routing. | Initially managed on server, then client-side libraries can take over (e.g., Next.js with its file-based routing). |
| **State Management**         | Managed on server (e.g., session variables, cookies).                   | Managed in client (e.g., Redux, Vuex).                  | Typically minimal; static generation.              | Hybrid. Server can provide initial state, then client manages with tools like Redux or Context API.                |
| **Meta Frameworks**          | -                                                                       | Create React App, Angular CLI, Vue CLI.                 | Jekyll, Hugo.                                      | Next.js for React, Nuxt.js for Vue, Sapper/SvelteKit for Svelte.                                                   |
| **Prominent Frameworks**     | Express.js (with template engines like EJS, Pug), Django, Ruby on Rails | React (standalone), Angular, Vue.js                     | Jekyll, Hugo, Next.js (with SSG), Gatsby           | Next.js, Nuxt.js, Sapper/SvelteKit                                                                                 |

## Astro, Qwik and SolidJS

| Steps                     | Server-side Rendering (SSR)                     | Client-side Rendering (CSR)                     | Static Site Generation (SSG)              | SSR followed by Hydration                                | Qwik                                      | Astro                                             | SolidJS                                         |
| ------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------- | -------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------- | ----------------------------------------------- |
| **Initial Request**       | User requests a webpage via the browser.        | User requests a webpage via the browser.        | User requests a pre-generated page.       | User requests a webpage via the browser.                 | User requests a webpage.                  | User requests a pre-generated page.               | User requests a webpage via the browser.        |
| **Server Processing**     | Server processes request, runs backend code.    | Server sends minimal HTML structure.            | No processing; static content served.     | Server processes request, runs backend code.             | Server processes for optimal data inline. | Partial processing; content served.               | Minimal initial structure, JS-driven content.   |
| **HTML Generation**       | Server generates full HTML from templates/data. | JS in browser generates content.                | HTML pages generated at build time.       | Server generates full HTML from templates/data.          | Optimized HTML with critical inline data. | Generate static HTML, hydrate as needed.          | JS in browser generates content.                |
| **Response to Browser**   | Server sends fully rendered HTML to browser.    | Browser displays initial HTML, then JS updates. | Server sends static HTML file to browser. | Server sends rendered HTML, then JS "hydrates" the view. | Sends optimized HTML to browser.          | Sends pre-rendered content, hydrates selectively. | Browser displays initial HTML, then JS updates. |
| ... (Same for other rows) | ...                                             | ...                                             | ...                                       | ...                                                      | ...                                       | ...                                               | ...                                             |
| **Prominent Frameworks**  | Express.js, Django, Ruby on Rails               | React, Angular, Vue.js                          | Jekyll, Hugo, Gatsby                      | Next.js, Nuxt.js, Sapper/SvelteKit                       | Qwik                                      | Astro                                             | SolidJS                                         |

## Vanilla JS ...

| Steps                     | Server-side Rendering (SSR)                     | Client-side Rendering (CSR)                     | Static Site Generation (SSG)              | SSR followed by Hydration                                | Qwik                                      | Astro                                             | SolidJS                                         | Vanilla JS                                            |
| ------------------------- | ----------------------------------------------- | ----------------------------------------------- | ----------------------------------------- | -------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- |
| **Initial Request**       | User requests a webpage via the browser.        | User requests a webpage via the browser.        | User requests a pre-generated page.       | User requests a webpage via the browser.                 | User requests a webpage.                  | User requests a pre-generated page.               | User requests a webpage via the browser.        | User requests a webpage via the browser.              |
| **Server Processing**     | Server processes request, runs backend code.    | Server sends minimal HTML structure.            | No processing; static content served.     | Server processes request, runs backend code.             | Server processes for optimal data inline. | Partial processing; content served.               | Minimal initial structure, JS-driven content.   | Server can send minimal structure or full content.    |
| **HTML Generation**       | Server generates full HTML from templates/data. | JS in browser generates content.                | HTML pages generated at build time.       | Server generates full HTML from templates/data.          | Optimized HTML with critical inline data. | Generate static HTML, hydrate as needed.          | JS in browser generates content.                | Browser processes and displays received HTML.         |
| **Response to Browser**   | Server sends fully rendered HTML to browser.    | Browser displays initial HTML, then JS updates. | Server sends static HTML file to browser. | Server sends rendered HTML, then JS "hydrates" the view. | Sends optimized HTML to browser.          | Sends pre-rendered content, hydrates selectively. | Browser displays initial HTML, then JS updates. | Server sends HTML, JS may or may not update the view. |
| ... (Same for other rows) | ...                                             | ...                                             | ...                                       | ...                                                      | ...                                       | ...                                               | ...                                             | ...                                                   |
| **Prominent Frameworks**  | Express.js, Django, Ruby on Rails               | React, Angular, Vue.js                          | Jekyll, Hugo, Gatsby                      | Next.js, Nuxt.js, Sapper/SvelteKit                       | Qwik                                      | Astro                                             | SolidJS                                         | - (Pure JavaScript)                                   |

## Vanilla JS vs React/Frameworks

https://frontendmasters.com/blog/vanilla-javascript-todomvc/