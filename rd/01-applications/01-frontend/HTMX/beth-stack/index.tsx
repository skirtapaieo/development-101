import { Elysia, t } from "elysia";
import { html } from "@elysiajs/html";
import * as elements from "typed-html";

const emojis = ["🔥", "✨", "💥", "⚡", "🌈", "⭐", "☀️", "🌕", "☄️", "🚀"];

let message = "Hello World ";

for (const emoji of emojis) {
    message += emoji + " ";
}
const app = new Elysia()
    .use(html())
    .get("/", ({ html }) =>
        html(
            <BaseHtml>
                <body
                    class="flex w-full h-screen justify-center items-center"
                    hx-get="/todos"
                    hx-trigger="load"
                    hx-swap="innerHTML">
                    <h1>
                        {message}
                    </h1>
                </body>
            </BaseHtml>
        )
    )
    .post("/clicked", () => <div class="flex w-full text-blue-600 justify-center items-center">im from server</div>)
    .get("/todos", () => <TodoList todos={db} />)
    .listen(3000);

type Todo = {
    id: number;
    content: string;
    completed: boolean;
}

const db: Todo[] = [
    { id: 1, content: "learn the beth stack", completed: true },
    { id: 2, content: "learn vim", completed: false }
]

function TodoItem({ content, completed, id }: Todo) {
    return (
        <div class="flex flex-row space-x-3">
            <p>{content}</p>
            <input type="checkbox" checked={completed} />
            <button class="text-red-500">X</button>
        </div>
    )
}

function TodoList({ todos }: { todos: Todo[] }) {
    return (
        <div>
            {todos.map((todo) => (
                <TodoItem {...todo} />
            ))}
        </div>
    );
}

const BaseHtml = ({ children }: elements.Children) => `
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The BETHst stack</title>
  <script src="https://unpkg.com/htmx.org@1.9.6" integrity="sha384-FhXw7b6AlE/jyjlZH5iHa/tTe9EpJ1Y55RjcgPbjeWMskSxZt1v9qkxLJWNJaGni" crossorigin="anonymous"></script>
  <script src="https://unpkg.com/hyperscript.org@0.9.11"></script>
  <script src="https://cdn.tailwindcss.com"></script>
  <link href="/styles.css" rel="stylesheet">
</head>

${children}
`;

console.log(
    `Elysia is running at http://${app.server?.hostname}:${app.server?.port}`
);

