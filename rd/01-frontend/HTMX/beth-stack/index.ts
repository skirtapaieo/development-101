
import { Elysia } from "elysia";
import { html } from "@elysiajs/html";
import as elements from ""
const emojis = ["🔥", "✨", "💥", "⚡", "🌈", "⭐", "☀️", "🌕", "☄️", "🚀"];

let message = "Hello World ";

for (const emoji of emojis) {
    message += emoji + " ";
}
const app = new Elysia()
    .use(html())
    .get("/", ({ html }) =>
        html(
            <BaseHTML>
            <body>
            { message }
            < /body>
            < /BaseHTML>
        )
    )
    .listen(3000);

console.log(
    `Elysia is running at http://${app.server?.hostname}:${app.server?.port}`
);

const BaseHtml = ({ children }: elements.Children) => `
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>THE BETH STACK</title>
  <script src="https://unpkg.com/htmx.org@1.9.3"></script>
  <script src="https://unpkg.com/hyperscript.org@0.9.9"></script>
  <link href="/styles.css" rel="stylesheet">
</head>

${children}
`;