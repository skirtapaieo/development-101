const Hello = () =>
  div(
    p("Hello"),
    ul(li("World"), li(a({ href: "https://vanjs.org" }, "VanJS")))
  );
