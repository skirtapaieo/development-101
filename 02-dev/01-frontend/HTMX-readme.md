# HTMX

A library that allows you to access AJAX, WebSockets, Service-side events, **without having to write JavaScript**. I enables making partial page updates in HTML.

## Key principles

- Progressive enhancement - it allows you to enhance your existing HTML progressively. You can start adding dynamic behavior without rewriting your entire app.
- Keep it simple - by simply using HTML-attributes HTMX aims to be as simple as possible
- Minimalistic - HTMX is very lightweight, ensuring your web application remains fast

<br>

## Client-side (HTML+HTMX)

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HTMX Example</title>
    <script src="https://unpkg.com/htmx.org@1.4.1"></script> <!-- Including HTMX -->
</head>
<body>
    <button hx-get="/getContent" hx-target="#contentDiv">Load Content</button>
    <div id="contentDiv"></div>
</body>
</html>
```

## Server-Side

### JavaScript (Express.js)

```JavaScript

const express = require('express');
const app = express();
const PORT = 3000;

app.get('/getContent', (req, res) => {
    res.send("Hello from HTMX!");
});

app.listen(PORT, () => {
    console.log(`Server started on http://localhost:${PORT}`);
});

```

### Python

```Python
from flask import Flask

app = Flask(__name__)

@app.route('/getContent')
def get_content():
    return "Hello from HTMX!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

```

### Go

```Go
package main

import (
	"fmt"
	"net/http"
)

func getContent(w http.ResponseWriter, r *http.Request) {
	fmt.Fprint(w, "Hello from HTMX!")
}

func main() {
	http.HandleFunc("/getContent", getContent)
	http.ListenAndServe(":3000", nil)
}

```

Timeline of the Web according to HTMX:

1. **Web 1.0** (Initial phase):

   - Dominated by only HTML without JavaScript (JS).

2. **Web 2.0** (Starts in 2005):

   - Rise of Single Page Applications (SPA) and JSON.
   - Numerous sites like Drupal and Wordpress emerged. These sites utilized JS and concepts like AJAH/AJAJ, but largely adhered to regular HTML from Web 1.0.
   - Emphasis on re-creating Flash applications using just HTML, CSS, and JS.

3. **2010-2012**:

   - Browsers began to support and implement HTML5, CSS3, and ES5 along with JSON.parse.
   - Introduction of the history API that allowed URLs to be changed without having to reload the entire page. Before this, there was a reliance on #! links.

4. **2015**:

   - Peak of traditional web frameworks like Drupal, Wordpress, Django, and Rails.
   - Surge in mobile app popularity brought forth a question on the relevance of the web.

5. **Circa 2020**:
   - Overwhelming use of JS, JSON, and API became the norm.
   - Server frameworks started adapting to an environment where HTML was primarily for applications.
   - Introduction of frameworks and tools like Blazor, Phoenix LiveView, Laravel Livewire, and HTMX.

Other Key Points:

- Web applications with Java and ActiveX existed before JavaScript became prominent.
- Early JS apps relied more on HTML and XML instead of JSON.
- The history of the web seems to run in two parallel directions. One focuses on websites with server-side logic and minimal JS, staying true to the original web. The other leans towards providing a more "app-like" experience.
- Despite the evolution and competition from native apps, HTML remains a strong and preferred medium for delivering apps.

In essence, while technology and platforms have evolved over the years, the integral role of HTML in web development remains evident.

<br>

## HTMX and other approaches

| Steps                     | Server-side Rendering (SSR)                     | Client-side Rendering (CSR)                     | SSR followed by Hydration                                | Qwik                                      | Astro                                             | SolidJS                                         | Vanilla JS                                            | HTMX                                                       |
| ------------------------- | ----------------------------------------------- | ----------------------------------------------- | -------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------------- | ---------------------------------------------------------- |
| **Initial Request**       | User requests a webpage via the browser.        | User requests a webpage via the browser.        | User requests a webpage via the browser.                 | User requests a webpage.                  | User requests a pre-generated page.               | User requests a webpage via the browser.        | User requests a webpage via the browser.              | User requests a webpage via the browser.                   |
| **Server Processing**     | Server processes request, runs backend code.    | Server sends minimal HTML structure.            | Server processes request, runs backend code.             | Server processes for optimal data inline. | Partial processing; content served.               | Minimal initial structure, JS-driven content.   | Server can send minimal structure or full content.    | Server processes request, sends HTML with HTMX attributes. |
| **HTML Generation**       | Server generates full HTML from templates/data. | JS in browser generates content.                | Server generates full HTML from templates/data.          | Optimized HTML with critical inline data. | Generate static HTML, hydrate as needed.          | JS in browser generates content.                | Browser processes and displays received HTML.         | Server generates full HTML, enhanced with HTMX.            |
| **Response to Browser**   | Server sends fully rendered HTML to browser.    | Browser displays initial HTML, then JS updates. | Server sends rendered HTML, then JS "hydrates" the view. | Sends optimized HTML to browser.          | Sends pre-rendered content, hydrates selectively. | Browser displays initial HTML, then JS updates. | Server sends HTML, JS may or may not update the view. | Server sends HTML. Dynamic updates via HTMX directives.    |
| ... (Same for other rows) | ...                                             | ...                                             | ...                                                      | ...                                       | ...                                               | ...                                             | ...                                                   | ...                                                        |
| **Prominent Frameworks**  | Express.js, Django, Ruby on Rails               | React, Angular, Vue.js                          | Next.js, Nuxt.js, Sapper/SvelteKit                       | Qwik                                      | Astro                                             | SolidJS                                         | - (Pure JavaScript)                                   | HTMX                                                       |
