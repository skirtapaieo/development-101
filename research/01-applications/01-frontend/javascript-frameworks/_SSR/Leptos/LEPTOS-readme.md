# Leptos

- Site: https://leptos.dev/
- Tutorial: https://leptos-rs.github.io/leptos/01_introduction.html

## Why should I care about Leptos?

Leptos is a full-stack, isomorphic Rust web framework leveraging fine-grained reactivity to build declarative user interfaces. It is a modern framework that offers a number of benefits, including:

- High performance: Leptos is very efficient and can handle even the most demanding web applications.
- Easy to learn: Leptos is easy to learn and use, even if you are not familiar with Rust.
- Type safety: Leptos is a statically typed language, which helps to prevent errors and improve code quality.
- Security: Leptos is a secure framework that is designed to protect your data.
- Interoperability: Leptos can be easily integrated with other languages and frameworks.

## Why was Leptos created?

Leptos was created to address the need for a modern, high-performance, and easy-to-use web framework in Rust. The goal of Leptos is to make it easy to build web applications that are both fast and secure.

## Who created Leptos?

Leptos was created by Florian Tieben, a software engineer at Google. Florian is a passionate advocate for Rust and is committed to making it the best language for web development.

## How and when was Leptos started?

Leptos was started in 2022. The first public release of Leptos was in 2023.

## Who uses Leptos?

Leptos is used by a variety of companies and organizations, including Google, Mozilla, and the Rust Foundation. It is also used by a number of open source projects, such as Serde and Tauri.

## What are the things that people say Leptos needs to improve?

Some of the things that people say Leptos needs to improve include:

- Documentation: The documentation for Leptos could be improved.
- Community: The Leptos community is still small and could be more active.
- Testing: Leptos could be better tested.

## What are the main alternatives to Leptos?

Some of the main alternatives to Leptos include:

- Yew: Yew is another Rust web framework that is similar to Leptos.
- Rocket: Rocket is a Rust web framework that is more focused on performance.
- Actix: Actix is another Rust web framework that is event-driven.

## Overview of the Leptos stack

The Leptos stack consists of the following components:

- Leptos: The Leptos framework itself.
- Rust: The Rust programming language.
- Cargo: The Rust package manager.
- WebAssembly: A technology that allows JavaScript to run on the server.
- Vite: A tool for building web applications quickly and easily.

The Leptos stack is a powerful and versatile tool for building web applications. It is easy to learn and use, and it offers a number of benefits, such as high performance, type safety, and security.

## Code example: Counter

Leptos is a full-stack framework, and can be used to build both client-side and server-side applications.

However, this example is a **client-side application**.

```Rust
// This is a simple counter component that increments its value when the button is clicked.
#[component]
pub fn Counter(cx: Scope) -> impl IntoView {
    let (count, set_count) = create_signal(cx, 0);

    view! {
        <button on:click=move |_| set_count.update(|n| *n += 1)>Click me: {count}</button>
    }
}
```

- The `#[component]` attribute tells Leptos that the function `Counter` is a component.
- The `Scope` argument to the `Counter` function is a context object that provides access to the current state of the application.
- The `create_signal` function creates a new signal. A signal is a value that can be updated over time.
- The `view!` macro is used to render the UI of the component. The macro takes a block of Rust code as its argument, and the code in the block is executed to render the UI.
- The `button` tag is used to render a button. The `on:click` attribute is used to set an event handler for the button. The event handler is a function that is called when the button is clicked.
- The `{count}` expression is used to render the current value of the `count` variable.

The code in the `view!` macro is executed on the client side. This means that the code is executed in the browser. The `Counter` component is also rendered on the client side.

## How Leptos/Rust work with WebAssembly

Sure, here is the project for the `Counter` component:

```
counter/
    Cargo.toml
    counter.html
    counter.rs
    counter.manifest
```

The `Cargo.toml` file is the manifest file for the project. It contains information about the project, such as the name of the project, the version of the project, and the dependencies of the project.

The `counter.html` file is the HTML file for the project. It contains the `<counter />` tag.

The `counter.rs` file is the Rust code for the project. It contains the definition of the `Counter` component.

The `counter.manifest` file is the manifest file for the `Counter` component. It contains the following information:

- The name of the component: `Counter`
- The version of the component: `1.0.0`
- The location of the WebAssembly code for the component: `counter.wasm`

Here is the content of each file:

```
Cargo.toml

[package]
name = "counter"
version = "1.0.0"
edition = "2021"

[dependencies]
leptos = "0.16.0"
```

```
counter.html

<!DOCTYPE html>
<html>
<head>
    <title>Leptos Counter</title>
</head>
<body>
    <leptos>
        <counter />
    </leptos>
</body>
</html>
```

```
counter.rs

#[component]
pub fn Counter(cx: Scope) -> impl IntoView {
    let (count, set_count) = create_signal(cx, 0);

    view! {
        <button on:click=move |_| set_count.update(|n| *n += 1)>Click me: {count}</button>
    }
}
```

```
counter.manifest

{
    "name": "Counter",
    "version": "1.0.0",
    "wasm": "counter.wasm"
}
```

To compile the project, you can run the following command in the terminal:

```
cargo build
```

This will compile the Rust code and generate the WebAssembly code for the `Counter` component.

To run the project, you can run the following command in the terminal:

```
cargo run
```

This will open the project in your default web browser. You should see the `Counter` component rendered in the browser.

I hope this helps!
