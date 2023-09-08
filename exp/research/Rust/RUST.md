# Rust in context

<br>

| Feature           | Rust    | C           | C++             | Go       | Python      |
| ----------------- | ------- | ----------- | --------------- | -------- | ----------- |
| Statically typed  | Yes     | Yes         | Yes             | Yes      | No          |
| Garbage collected | No      | No          | No              | Yes      | No          |
| Memory safety     | Yes     | No          | Yes (with RAII) | No       | No          |
| Concurrency       | Yes     | Yes         | Yes             | Yes      | Yes         |
| Performance       | High    | High        | High            | High     | Good        |
| Learning curve    | Steep   | Steep       | Steep           | Moderate | Gentle      |
| Popularity        | Growing | Widely used | Widely used     | Growing  | Widely used |

<br>

**Unique features of Rust:**

- Ownership and borrowing system: Rust's ownership and borrowing system ensures memory safety by preventing dangling pointers and data races.
- Fearless concurrency: Rust's concurrency model is designed to be safe and easy to use, even for beginners.
- Macros: Rust has a powerful macro system that allows programmers to write concise and expressive code.

**Shared features of Rust, C, and C++:**

- Low-level control: Rust, C, and C++ allow programmers to have low-level control over their code, which can be useful for performance-critical applications.
- Portability: Rust, C, and C++ are all portable languages, which means that they can be used to write code that runs on a variety of platforms.
- Compiled languages: Rust, C, and C++ are all compiled languages, which means that they are converted into machine code before they are executed. This makes them faster than interpreted languages, such as Python.

**Shared features of Rust and Go:**

- Garbage collection: Rust and Go both have garbage collection, which means that programmers do not have to worry about managing memory manually.
- Concurrency: Rust and Go both support concurrency, which allows programmers to write code that can run multiple tasks at the same time.
- Modern features: Rust and Go are both modern languages that have many features that make them suitable for writing high-performance, concurrent applications.

**Which language is right for you?**

If you are looking for a language that is memory safe, has good performance, and is easy to learn, then Rust is a good choice.

If you are looking for a language that is widely used and has a large community, then C++ or Go are good choices.

<br>

## Ownership and borrowing system

It ensures memory safety by preventing dangling pointers/data races

```Rust
fn main() {
    let mut x = 5; // x is owned by the current scope

    let y = &x; // y borrows x

    // x is still valid here, because y is only borrowing it

    y = &10; // y is now borrowing 10, and x is no longer valid
}
```

<br>

## Fearless concurrency

The concurrency model in Rust is designed to be safe and easy to use. Ownership and borrowing can be used, as well as unsafe.

```Rust
fn main() {
    let mut x = 0; // x is shared between the two threads

    let t1 = thread::spawn(move || {
        x += 1;
    });

    let t2 = thread::spawn(move || {
        x += 1;
    });

    t1.join();
    t2.join();

    assert_eq!(x, 2);
}
```

<br>

## Macros

Rust enable users to write concise and expressive code. Macros are similar to functions, but they can be used to expand code at compile time.

```Rust
macro_rules! print_tuple {
    ($($e:expr),+) => {
        println!("(");
        $(print!("{}, ", $e);)+
        println!(")");
    }
}
```
