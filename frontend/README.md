# Index

This file needs cleanup - it is as messy as the subject :-)

- [Historical approaches](#historical-approaches)
  - [The evolution of the web](#the-unprincipled-evolution-of-the-web)
- [Design systems](#design-systems)
- [Core principles of the Internet and the web](#core-principles-of-the-internet-and-the-web)
  - [1 Universality](#1-universality)
  - [1.1 Responsive Design](#11-responsive-design)
  - [1.2 Accessibility](#12-accessibility)
    - [1.2.1 Accessibility from design perspective](#121-accessibility-from-design-perspective)
- [A Microfrontent experiment (in index.html)](#a-microfrontent-experiment-in-indexhtml)
- [Web-based front-end approaches](#web-based-front-end-approaches)
  - [The three general approaches](#the-three-general-approaches)
    - [Static-site generation (SSG)](#static-site-generation-ssg)
    - [Server-side rendering (SSR](#server-side-rendering-ssr)
    - [Client-side rendering (CSR)](#client-side-rendering-csr)
    - [Back-end for front-end](#back-end-for-front-end)
  - [Overview](#overview-1)
  - [React principles](#react)
  - [Vue](#vue)
  - [Svelte](#svelte)
  - [Angular](#angular)
  - [vanilla JavaScript](#vanilla-javascript)
- [Mobile-approaches](#mobile-approaches)
  - [React Native](#react-native)
  - [Flutter](#flutter)
  - [Swift/iOS](#swift-ios)
  - [Kotlin/Android](#kotlin-android)
- [Desktop approaches](#desktop-approaches)
  - [Electron](#electron)
- [JavaScript Framework comparison (Svelte/Vue/React)](#javascript-framework-comparison-sveltevuereact)
  - [Overview](#overview)
  - [React](#react)
  - [Vue](#vue)
  - [Svelte](#svelte)
- [React, principles and benefits](#react-principles-and-benefits)
- [Algoexpert - Spaghetti Recipe](#algoexpert-spaghetti-recipe)
- [Algoexpert - Blog Post](#algoexpert-blog-post)
- [Algoexpert - Rainbow circles (JavaScript)](#algoexpert-rainbow-circles-javascript)

## How come the landscape is so fragmented/decentralized?

The landscape of front-end development has indeed become fragmented, with various libraries, frameworks, and tools emerging over time. Several reasons can explain why large tech companies like Microsoft and Google haven't produced a single "complete" development environment that covers all aspects of the modern front-end stack:

1. **Diverse Needs**: Different projects have different requirements. A single solution that aims to address all possible use cases might become bloated and lose the flexibility required by individual projects.

2. **Innovation and Evolution**: The web evolves rapidly. Tools and technologies can quickly become obsolete or be superseded by superior solutions. This dynamism has led to a natural progression where newer solutions emerge to address limitations in existing ones.

3. **Community-Driven Development**: The open-source nature of many web technologies has allowed individual developers and smaller teams to contribute and create new solutions. This democratized ecosystem means innovations can come from anywhere, not just major tech companies.

4. **Economic & Strategic Interests**: Major companies often have specific strategic or economic interests in pushing certain technologies. For example, Google backs Angular and contributes to Chromium (which powers many browsers like Chrome and Edge), while Facebook created React.

5. **Interoperability Over Monopoly**: While it's feasible for a tech giant to attempt creating an all-in-one solution, promoting interoperability between tools might be more beneficial for the web ecosystem. The Web is inherently decentralized, and fostering an environment where tools can work together can be more advantageous than a monolithic approach.

6. **Existing Integrated Solutions**: While not covering every aspect of front-end development, there are solutions like Microsoft's Visual Studio (and Visual Studio Code) or Google's Firebase that do offer integrated tools for various aspects of development.

7. **Adoption Concerns**: Launching a new, comprehensive tool doesn't guarantee adoption. Developers tend to use tools they are familiar with, that have strong community support, or that they feel are the best fit for their specific needs. Convincing the global developer community to switch to a new all-in-one solution would be a monumental challenge.

8. **Maintenance and Evolution**: Maintaining a monolithic, all-inclusive solution would be a huge undertaking. As different parts of the web ecosystem evolve at different rates, keeping such a system updated, bug-free, and cutting-edge would be incredibly challenging.

While the fragmentation can seem overwhelming, it also illustrates the vibrancy and innovation of the web development community. Developers have a wealth of tools to choose from, allowing them to select the best ones for their specific needs. That said, there's always a possibility that more integrated solutions will emerge in the future as the landscape continues to evolve.

## End-to-end approach rev 3

The following tools is part of the toolset in front-end:

1. **Sentry**: Sentry is an error tracking tool that helps developers monitor and fix issues in real-time. It integrates with various programming languages and platforms.

   - **Category**: Error Monitoring & Tracking

2. **Hotjar**: Hotjar provides insights into user behaviors on websites through heatmaps, session recordings, and surveys.

   - **Category**: User Behavior Analytics & Feedback

3. **Detectify**: Detectify is a web security scanner that automates the process of checking web applications for vulnerabilities and security issues.

   - **Category**: Web Security & Vulnerability Scanning

4. **Storybook**: Storybook is a tool for developing and showcasing UI components in isolation. It supports various frontend frameworks and libraries.
   - **Category**: UI Component Development & Documentation

These tools each serve different purposes in the development, maintenance, and optimization of web applications. Grouping them gives a clearer picture of their primary roles within the broader landscape of web development tools.

## End-to-end-approach rev 2

Of course! Let's integrate back-end as a service (BaaS), end-to-end (E2E) testing, and search solutions into the web stack table.

### Comprehensive Front-end and Back-end Web Stack:

| Layer                                | Technology/Concept                 | Description                                                                | Initial Innovation                             | Major Dependencies                                   |
| ------------------------------------ | ---------------------------------- | -------------------------------------------------------------------------- | ---------------------------------------------- | ---------------------------------------------------- |
| Base Layer                           | HTML                               | Structure of the web page.                                                 | 1990s                                          | —                                                    |
| Styling                              | CSS                                | Appearance and design.                                                     | Late 1990s                                     | —                                                    |
| Interactivity                        | JavaScript                         | Allows dynamic interactions.                                               | 1995                                           | —                                                    |
| UI Libraries                         | React, Vue, Angular, Svelte        | Build interactive UIs.                                                     | 2000s onwards                                  | JS (React depends on JSX, Angular on TypeScript)     |
| CSS Frameworks                       | Bootstrap, Tailwind, Bulma         | Predefined styles and components.                                          | 2010s                                          | CSS, often with JS enhancements                      |
| Specific/Specialized UI Libraries    | Material UI, Chakra UI, Ant Design | Offer specific design systems/components.                                  | 2010s                                          | Typically JS libraries like React or Vue             |
| Meta Frameworks/Full Stack Solutions | Next.js, Nuxt, SvelteKit, Astro    | Offer integrated solutions, SSR, and more.                                 | 2010s onwards                                  | Base libraries (e.g., Next.js -> React, Nuxt -> Vue) |
| Package Managers                     | npm, Yarn                          | Manage & organize libraries and dependencies.                              | 2010s                                          | Node.js                                              |
| Task Runners & Bundlers              | Webpack, Rollup, Parcel            | Process, bundle & optimize code and assets.                                | 2010s                                          | Node.js                                              |
| Transpilers                          | Babel, TypeScript                  | Convert newer code standards to older ones.                                | 2010s                                          | JS                                                   |
| Responsive Design                    | Media Queries, Bootstrap           | Ensure sites work on various devices and screens.                          | Early 2010s                                    | CSS (Bootstrap requires JS for certain components)   |
| SPAs                                 | React Router, Vue Router           | Seamless transitions without full page reloads.                            | Mid 2010s                                      | React, Vue                                           |
| State Management                     | Redux, Vuex                        | Manage and organize data flow in applications.                             | Mid 2010s                                      | React (Redux), Vue (Vuex)                            |
| Web Components                       | Polymer, StencilJS                 | Encapsulate and reuse components across projects.                          | Mid 2010s                                      | JS                                                   |
| Static Site Generators               | Jekyll, Gatsby                     | Pre-build pages for improved performance.                                  | Early 2010s                                    | Ruby (Jekyll), React (Gatsby)                        |
| SSR                                  | Next.js, Nuxt                      | Render pages on the server for performance & SEO.                          | Mid 2010s                                      | React (Next.js), Vue (Nuxt)                          |
| PWAs                                 | Service Workers, Manifest          | Enhance web apps with native-like capabilities.                            | Mid 2010s                                      | JS                                                   |
| **BaaS**                             | Firebase, Supabase, AWS Amplify    | Provide back-end capabilities without managing server-side infrastructure. | 2010s                                          | Varies; Firebase (JS SDK), Supabase (PostgreSQL, JS) |
| **E2E Testing**                      | Cypress, Playwright                | Automated testing simulating real user behavior.                           | 2010s                                          | JS                                                   |
| **Search Solutions**                 | Algolia, Elasticsearch             | Provide fast and reliable search capabilities.                             | 2010s (Algolia in 2012, Elasticsearch in 2010) | JS for client integration, Java (Elasticsearch)      |

This table integrates back-end as a service (BaaS), end-to-end (E2E) testing, and search solutions into the prior web stack. Remember, these categories often overlap, and tools might span multiple categories or be used in different ways based on the project's requirements.

## End-to-end approach rev 1

Note: Astro and Qwik are missing

### 1. UI Libraries / Frameworks:

These provide a set of components and often styles to build interactive user interfaces.

| Library/Framework | Supports TypeScript?           | Major Dependencies | Core Principles                       |
| ----------------- | ------------------------------ | ------------------ | ------------------------------------- |
| Material UI       | Yes                            | React              | Components for material design        |
| Chakra UI         | Yes                            | React              | Modular, accessible component library |
| Mantine           | Yes                            | React              | High customization, dark theme        |
| Gestalt           | Yes                            | React              | Pinterest's design language           |
| PrimeReact        | Yes                            | React              | Rich UI component suite               |
| Evergreen         | Yes                            | React              | Polished, flexible components         |
| Arco Design       | Yes (with @arco-design/vue-ts) | Vue                | Enterprise-level design language      |
| Fluent            | Yes                            | React              | Microsoft's Fluent Design             |
| Radix             | Likely Yes                     | React              | Primitives for UI design              |
| Semi UI           | Likely Yes                     | React              | Enterprise UI components              |
| Ant Design        | Yes                            | React              | Enterprise-level components           |

### 2. CSS Frameworks:

These provide styling utilities without the inclusion of JavaScript components.

| Framework | Core Principles                                           |
| --------- | --------------------------------------------------------- |
| Bootstrap | Responsive grid, UI components                            |
| Tailwind  | Utility-first CSS framework                               |
| Bulma     | Modern, responsive framework                              |
| UI kit    | Lightweight, modular front-end kit                        |
| Windy     | Likely a misname, WindiCSS is utility-first like Tailwind |
| Spectre   | Lightweight, responsive                                   |
| Milligram | Minimalist CSS framework                                  |
| Mini      | Minimalist responsive grid                                |
| Picnic    | Lightweight, no dependencies                              |
| Skeleton  | Bare-bones grid system                                    |

### 3. Specific UI Libraries:

These are more specialized UI toolsets.

| Library  | Supports TypeScript? | Major Dependencies | Core Principles             |
| -------- | -------------------- | ------------------ | --------------------------- |
| Daisy UI | Yes                  | Tailwind CSS       | Extendable component plugin |

### 4. Meta Frameworks / Full Stack Solutions:

These are built on top of base libraries/frameworks and offer a more comprehensive solution.

| Framework  | Supports TypeScript? | Major Dependencies | Core Principles                  |
| ---------- | -------------------- | ------------------ | -------------------------------- |
| Svelte Kit | Yes                  | Svelte             | Hybrid static & server rendering |
| Next.js    | Yes                  | React              | Static & server-side rendering   |
| Nuxt       | Yes                  | Vue                | Static & server-side rendering   |
| Astro      | Yes                  | ---                | Deliver the least amount of JS   |
| Qwik       | Yes                  | ---                | Optimize for loading speed       |

### 5. Base UI Libraries:

| Library | Supports TypeScript? | Core Principles       |
| ------- | -------------------- | --------------------- |
| Svelte  | Yes                  | Reactive components   |
| Vue     | Yes                  | Reactive data-binding |
| React   | Yes                  | Component-based UI    |

### 6. Backend Frameworks:

| Framework     | Language     | Core Principles                                     |
| ------------- | ------------ | --------------------------------------------------- |
| Django        | Python       | Batteries-included web framework                    |
| Laravel       | PHP          | Elegant syntax, MVC web application framework       |
| .NET          | C#, F#, etc. | Platform for building various types of applications |
| Flask         | Python       | Lightweight, micro web framework                    |
| Ruby on Rails | Ruby         | Convention over configuration, MVC                  |

### 7. End-to-End Testing:

| Tool      | Supports TypeScript? | Core Principles                 |
| --------- | -------------------- | ------------------------------- |
| Playwrite | Yes                  | Browser automation              |
| Cypress   | Yes                  | Fast, easy, reliable testing    |
| Vi Test   | Unknown              | Not sure, may need more details |

### 8. Search:

| Tool    | Type                | Core Principles           |
| ------- | ------------------- | ------------------------- |
| Algolia | Search-as-a-Service | Instant search experience |

### 9. Backend-as-a-Service:

| Service  | Supports TypeScript? | Core Principles                                   |
| -------- | -------------------- | ------------------------------------------------- |
| Firebase | Yes                  | Real-time NoSQL database, authentication, hosting |
| Supabase | Yes                  | Open-source Firebase alternative                  |

### 10. Databases:

| Database | Type             | Core Principles                                         |
| -------- | ---------------- | ------------------------------------------------------- |
| MySQL    | Relational       | Widely-used open-source database                        |
| Prisma   | Database Toolkit | Type-safe database access, auto-generated query builder |

## Historical approaches

A few examples of front-end development:

- 1985 - [Writing first windows-based application in GEM using C](https://github.com/skirtapaieo/frontend-101/blob/main/oldschool/helloworld-TOS.c)
- 1995 - [Java applets](https://github.com/skirtapaieo/frontend-101/blob/main/oldschool/Java-applet.java)
- 1997 - Server-side rendering - https://github.com/skirtapaieo/frontend-101/blob/main/VBscript.asp
- 1998 - Pre-CSS layouts using Tables and Pixels - https://github.com/skirtapaieo/frontend-101/blob/main/simple-layout-tables-pixels.html
- 2003 - Introduction of AJAX (Asynchronous JavaScript and XML) https://github.com/skirtapaieo/frontend-101/blob/main/AJAX-example.html
- 2015 - Responsive design - Sketch and Javascript https://github.com/skirtapaieo/frontend-101/blob/main/AJAX-example.html
- 2016 - Micro-frontends (scaling front-ends) - ...
- 2019 - Design systems -
- 2019 - Real-time, 3D gameas using Babylon.js -

| Year    | Concept                                             | Example                                                |
| ------- | --------------------------------------------------- | ------------------------------------------------------ |
| 1984    | GUI on Apple Macintosh (Macintosh System)           | Icons, windows, menus, and mouse interaction           |
| 1985    | GUI on Atari ST (TOS)                               | Graphical User Interface with desktop-like controls    |
| 1990    | Introduction of the World Wide Web (WWW)            | Hypertext Markup Language (HTML)                       |
| 1993    | Server-side rendering (CGI)                         | Common Gateway Interface (CGI) scripts                 |
| 1995    | Introduction of Java Applets                        | Embedding Java programs in web pages                   |
| 1995    | Dynamic client-side interaction (AJAX)              | XMLHttpRequest for asynchronous data retrieval         |
| 1996    | Introduction of CSS (Cascading Style Sheets)        | Separation of presentation from HTML                   |
| 1997    | Introduction of IIS (Internet Information Services) | Web server software for hosting websites               |
| 1998    | Introduction of VBScript                            | Client-side scripting language for web browsers        |
| 1999    | Introduction of Perl                                | General-purpose scripting language for web development |
| 2000    | Introduction of PHP                                 | Server-side scripting language for web development     |
| 2002    | Single-page applications (SPAs)                     | Gmail (AJAX-based email client)                        |
| 2005    | JavaScript frameworks (jQuery)                      | Simplified DOM manipulation and event handling         |
| 2007    | Introduction of iOS (Objective-C)                   | Native mobile app development for Apple devices        |
| 2008    | Introduction of Android (Java)                      | Native mobile app development for Android devices      |
| 2009    | HTML5 specification                                 | Semantic elements, video/audio, canvas                 |
| 2010    | CSS3 specification                                  | Transitions, transforms, media queries                 |
| 2013    | Introduction of React.js                            | Component-based UI development                         |
| 2014    | Introduction of Swift (iOS)                         | Modern programming language for iOS development        |
| 2015    | Introduction of Vue.js                              | Progressive and lightweight JavaScript framework       |
| 2017    | Progressive Web Apps (PWAs)                         | Web applications with native-like capabilities         |
| 2019    | Serverless architecture                             | Serverless functions (AWS Lambda, Azure Functions)     |
| 2020    | AI/ML integration in web development                | Machine learning models in browser applications        |
| 2021    | Continued advancements in web standards             | HTML6 proposals, Web Components                        |
| 1995    | Introduction of Java (Java Servlets, JSP)           | Server-side Java for web development                   |
| Present | Ongoing innovations and emerging technologies       | WebAssembly, WebRTC, GraphQL, PWAs                     |
| Present | Continued advancements in mobile app development    | Kotlin (Android), Swift (iOS)                          |

<br>

### The evolution of the web - high-level

| Year  | Tools for Layout & Design              | Tools for Content Management                  | Tools for Interactivity              | Design Component/Systems            | Analytics & UX                             |
| ----- | -------------------------------------- | --------------------------------------------- | ------------------------------------ | ----------------------------------- | ------------------------------------------ |
| 1990s | HTML, Tables, Pixels                   | Basic Text Editors, templates in databases    | Animated GIFs, Java Applets          | N/A                                 | N/A                                        |
| 2000s | CSS Frameworks, Dreamweaver, Flash     | Early CMS Platforms (e.g., WordPress)         | ActiveX, Flash, JavaScript Libraries | N/A                                 | Basic Web Analytics                        |
| 2010s | Responsive Design, CSS Grid, Bootstrap | Advanced CMS Platforms (e.g., Drupal, Joomla) | HTML5, CSS3, jQuery, Ajax            | Design Frameworks (e.g., Bootstrap) | Advanced Analytics, User Testing           |
| 2020s | CSS Flexbox, CSS Grid, Tailwind CSS    | Headless CMS, Contentful, Prismic             | Three.js, Babylon.js, WebAssembly    | Design Systems (e.g., Material UI)  | Advanced Analytics, A/B Testing, UX Design |

### More rendering patterns

Here's a table summarizing the various front-end rendering patterns for web applications, their key principles, tools commonly used, and approximate first appearance timeline.

| Timeline | Pattern                                  | Principles                                                                         | Tools                                                              |
| -------- | ---------------------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------ |
| 1991     | 1. Static Websites                       | Pre-built HTML files served directly. No dynamic rendering. Simple and performant. | HTML, CSS, JavaScript, Jekyll and Hugo                             |
| 2005     | 2. Single Page Websites                  | Dynamic rendering on the client side using JavaScript, and one (not multiple) page | jQuery, AngularJS, Backbone.js                                     |
| 2009     | 3. SSR (Server-Side Rendering)           | Rendered on the server. Faster initial page load. Good for SEO. MPA+SPA            | Node.js, Express.js, Next.js, ASP.NET, PHP                         |
| 2010     | 4. SSG (Static Site Generation)          | Build time rendering. Good performance and SEO. Limited dynamic content.           | Jekyll, Hugo, Next.js, Gatsby                                      |
| 2020     | 5. Incremental Static Regeneration       | Update static content post-deployment without full rebuild. SSG+SSR                | Next.js                                                            |
| 2010     | 6. Hydration                             | Initial SSR for fast load, followed by client-side rendering for interactivity.    | React, Vue.js                                                      |
| 2018     | 7. Partial Hydration                     | Only specific parts of the app are made interactive, reducing load time.           | Astro, Marko                                                       |
| 2021     | 8. Islands                               | Mix of SSR and client-side rendering. Each component decides its own rendering.    | Astro, Island Architecture                                         |
| 2022     | 9. Streaming SSR (Server-Side Rendering) | Server sends HTML to the browser in chunks, speeding up time to first byte.        | React 18+, Vue 3.0+, Next 13?                                      |
| 2023     | 10. Resumability                         | The ability to pause server-side rendering, deliver HTML to client, and resume.    | Frameworks supporting streaming SSR like React 18+, Qwik framework |

Please note that the timeline is approximate and may vary depending on the specific use case or development ecosystem. Also, some of the tools mentioned under each category can support multiple rendering patterns, such as Next.js, which supports SSR, SSG, and Incremental Static Regeneration.

## Core principles of the Internet and the web

The core principles of the internet and the web, as established by their inventors and early architects, can be summarized as follows:

1. **Openness**: The internet was designed as an open platform where everyone is free to connect, communicate, and share information. It's based on open standards that everyone can use.

2. **Decentralization**: The internet is a decentralized network. This means there is no central control point or governing body. This design principle is one of the reasons why the internet is resilient and hard to fully shut down.

3. **Interoperability**: The internet and the web are built on standard protocols and technologies. This ensures that all parts of the network can work together, and that the web works the same way no matter what device or software you're using.

4. **Universality**: From the perspective of the World Wide Web, a key principle is that any type of information can be shared and linked to from anywhere. This led to the creation of URLs and HTTP.

5. **Scalability**: The internet and web were designed to scale, i.e., to grow in size and complexity without requiring a redesign of the whole system.

6. **Fault Tolerance**: The internet was designed to be robust and reliable, capable of routing around damage or faults without losing data.

7. **End-to-End Principle**: This principle states that the network itself should remain simple and that complexity should be handled at the endpoints (i.e., by users' devices). This allows the network to carry any type of data, and new applications can be developed without the need to alter the core of the internet.

8. **Net Neutrality**: This principle states that all traffic on the internet should be treated equally. It prevents internet service providers from favoring certain types of content or services.

9. **Accessibility**: As for the World Wide Web, Tim Berners-Lee stated that "The power of the Web is in its universality. Access by everyone regardless of disability is an essential aspect". The web should be accessible to all individuals, regardless of their hardware, software, language, location, or ability.

These principles have guided the development and growth of the internet and the web, and while some of them face challenges today due to technological, political, and commercial pressures, they remain fundamental to the nature of the internet and web.

## 1 Universality

the principle of universality, in the context of the web, signifies that anyone, anywhere, should be able to access and use the web, regardless of their physical or mental abilities, the devices they're using, their language, culture, or geographical location. This principle can be broken down into several related principles or areas:

- Accessibility: The web should be accessible to all individuals, including those with disabilities. This involves ensuring that web content is accessible to individuals with various types of disabilities, including visual, auditory, physical, speech, cognitive, language, learning, and neurological disabilities.

- Responsive Design: Given the proliferation of different types of devices (desktops, laptops, tablets, mobile phones, etc.), the web should be designed in such a way that it can respond and adapt to different screen sizes and orientations. Responsive web design is an approach to design that makes web pages render well on a variety of devices and window or screen sizes.

- Internationalization and Localization: The web is a global platform, and as such, it should be accessible regardless of language or culture. Internationalization is the design and development of a product, application or document content that enables easy localization for target audiences that vary in culture, region, or language.

- Cross-Browser Compatibility: The web should work the same way regardless of the browser or operating system used. This means that web technologies should be designed to be compatible with a variety of web browsers, including older versions.

- Device Independence: This refers to the ability of a website or web application to be used on any device. This goes beyond responsive design to include other forms of internet devices such as smart TVs, wearables, or IoT devices.

- Connectivity Independence: With the rise of service workers, websites can now be designed to work offline or on low quality networks. This means that the web is universally accessible regardless of the user's connection status or quality.

All these principles support the overall idea of universality and aim to ensure that the web is a platform that everyone can use, irrespective of their circumstances or the technology they have access to.

### 1.1 Responsive Design

https://github.com/skirtapaieo/frontend-101/blob/main/responsive-design/responsive.html

Responsive design is an approach in web design aimed at making websites render well on a variety of devices and window or screen sizes. This methodology is essential for creating an optimal viewing and interaction experience, which can significantly impact user satisfaction and engagement.

The main principles of responsive design are:

1. **Fluid Grids**: This principle is based on the use of proportional measurements, like percentages, instead of fixed units like pixels. The layout adjusts to the screen size by the percentage it's set to. For instance, if a column is set to be 50% of the page width, it will maintain this proportion regardless of the screen size. This results in a smooth and seamless adaptation of the design.

2. **Flexible Images**: Images in a responsive design are flexible and scale according to the size of the viewport. The aim is to ensure that images are not larger than their containing element. For instance, setting an image's max-width to 100% means that an image will never exceed the width of its container, thereby avoiding overflow and distortion on smaller screens.

3. **Media Queries**: Media queries are a cornerstone of responsive design. They allow the application of different CSS styles to different devices based on characteristics, such as screen resolution, orientation (portrait or landscape), and screen size. For instance, a media query can be used to increase the font size when a website is viewed on a larger screen, or adjust the layout when viewed in portrait or landscape mode.

4. **Mobile First**: This principle advocates designing the website for the smallest screen first and then progressively enhancing the design for larger screens. It's a strategy that addresses the growing use of mobile devices to access the web. An example of this would be designing a layout, typography, and navigation suitable for a small, touch-based interface, and then adding elements or features for larger, mouse-based interfaces.

5. **Progressive Enhancement**: This principle involves designing the basic content and functionality first and then progressively adding more nuanced and sophisticated layers of presentation and features on top. For example, a website might first be designed with basic HTML and CSS, and then advanced CSS, JavaScript, and other technologies might be added to enhance the user experience on devices that support these technologies.

Remember, the goal of responsive design is not just to make the website "work" on different devices, but to ensure a great user experience regardless of the device being used.

### 1.2 Accessibility

https://github.com/skirtapaieo/frontend-101/blob/main/accessibility.md

Using the above example, in the context of accessibility:

Looking at the given code, it does follow some general accessibility practices but could be improved in other areas:

- **Use of alt attribute**: The image has an alt attribute which is very good. This attribute provides alternative text for those who can't see images. However, the value "An example image" is not very descriptive. It should ideally contain a brief description of the image.

- **Semantics**: The code doesn't use semantic HTML elements. Semantic elements like `<header>', <footer>, <section>, <article>, and <nav> ` make it easier for both people and machines (like search engines and screen readers) to understand the content structure. Consider replacing `<div>` tags with semantic HTML where appropriate.

- **Font size**: The code specifies font sizes in pixels which is not ideal for accessibility. Instead, relative units like em or rem should be used to make the site more flexible for users who need or prefer larger text.

- **Color contrast**: The code doesn't specify color, which means that it will default to browser settings. In practice, it's important to ensure that text and background colors have sufficient contrast for readability, especially for users with visual impairments.

- **Keyboard Navigation**: There is no specific code here for keyboard navigation (like specifying tabindex). Keyboard navigation is critical for users who can't use a mouse.

#### 1.2.1 Accessibility from design perspective

Figma, a popular collaborative interface design tool, supports a variety of plugins to help designers create more accessible designs. Here's a brief overview of the ones you mentioned:

1. **A11y - Annotation Kit**: This Figma plugin helps designers communicate accessibility specifications to developers by allowing them to annotate their designs with WCAG (Web Content Accessibility Guidelines) 2.1 requirements. The plugin comes with a set of components that can be added to the designs to indicate things like color contrast, keyboard focus, and other important accessibility elements.

2. **Twitter's Accessibility Annotation Library**: Created by Twitter's design team, this Figma library helps designers add accessibility annotations directly into their design files. These annotations can guide developers to create products that are inclusive and accessible to everyone.

3. **Axe - Axe for Designers**: Developed by Deque Systems, Axe for Designers is a plugin for Figma that checks your designs for accessibility issues while you're still in the design phase. It can detect issues related to color contrast, missing text alternatives, incorrect hierarchy, and much more, helping to catch and resolve accessibility problems before they make it into the development stage.

These tools are extremely valuable in creating more inclusive designs and should be an integral part of the design process for any team committed to accessibility. Remember, it's easier (and less expensive) to address accessibility issues during the design phase than after development has been completed.

Please note, while these tools can help identify many potential accessibility issues, they are not exhaustive, and manual checks and user testing should also be included in the design and development process.

## Design systems

https://github.com/skirtapaieo/frontend-101/blob/main/design-system.md

## A Microfrontent experiment (in index.html)

started with a very basic example without any JavaScrit framework/library or router, no separate development or deployment pipeline. To load the content into a content area based on people clicking on navigation links - we had to add a simple router that basically reacts to capture the click, fetch the content and update the page. Note: It doesn't work yet. Just wanted to try it out.

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Micro-frontend Experiment</title>
    <link rel="stylesheet" href="css/styles.css">
    <script>
        window.addEventListener('popstate', loadContent);

        document.addEventListener('DOMContentLoaded', function () {
            document.querySelector('nav').addEventListener('click', function (event) {
                if (event.target.tagName === 'A') {
                    event.preventDefault();
                    history.pushState(null, '', event.target.href);
                    loadContent();
                }
            });

            loadContent();
        });

        function loadContent() {
            fetch(location.pathname)
                .then(function (response) {
                    if (response.ok) {
                        return response.text();
                    } else {
                        throw new Error('Failed to load content: ' + response.status);
                    }
                })
                .then(function (data) {
                    document.querySelector('#content').innerHTML = data;
                })
                .catch(function (error) {
                    console.error(error);
                });
        }
    </script>
</head>
<body>
    <header>
        <h1>Micro-frontend Experiment</h1>
    </header>

    <nav>
        <ul>
            <li><a href="/spaghetti-recipe/index.html">Team 1 - Spaghetti Recipe</a></li>
            <li><a href="/blog-post/index.html">Team 2 - Blog Post</a></li>
            <li><a href="/rainbow-circles/index.html">Team 3 - Rainbow Circles</a></li>
        </ul>
    </nav>

    <main id="content">
        <!-- Content of the micro-frontend will be loaded here -->
    </main>

    <footer>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Sed nisi.</p>
    </footer>
</body>
</html>

```

<br>

## Web-based front-end approaches

### The general approaches

There are primarily three types of techniques commonly used in web development:

#### Static Site Generation (SSG)

- Static Site Generation involves pre-rendering the entire website at build time, generating static HTML, CSS, and JavaScript files for each page. These static files are then served to the client without requiring server-side processing for each request.
- SSG is well-suited for content-heavy websites where the content doesn't change frequently. It offers fast loading times and improved performance as the server doesn't need to regenerate the pages for each user request.
- Popular frameworks that support SSG include Gatsby, Next.js (with its "export" feature), and Nuxt.js.

#### Server-Side Rendering (SSR)

- Server-Side Rendering involves rendering React or other frontend components on the server and sending the fully rendered HTML to the client.
- When a user requests a page, the server fetches the data, processes it, renders the React components, and returns the complete HTML to the client.
- SSR is useful when you need dynamic content or personalized data to be available on the page at load time. It also improves SEO since search engine crawlers can see the fully rendered content.
- Frameworks like Next.js, Nuxt.js, and After.js provide built-in SSR capabilities for React and Vue.js applications.

#### Client-Side Rendering (CSR)

- Client-Side Rendering involves sending a minimal HTML page with JavaScript bundles to the client. The JavaScript code then fetches data from APIs and renders the components on the client-side, updating the DOM dynamically.
- CSR is useful for highly interactive and dynamic web applications where content is frequently changing or personalized to each user.
- The initial load time may be slower compared to SSR or SSG because the browser needs to fetch and execute JavaScript before rendering the content.
- React, Vue.js, and other modern frontend libraries are commonly used for CSR.

#### Back-end for front-end

The Back-End for Front-End (BFF) is considered to be a hybrid architectural pattern that combines both server-side and client-side elements.

The BFF pattern introduces a dedicated back-end layer specifically designed to cater to the needs of a particular front-end application. It acts as an intermediary between the front-end and the main back-end services, providing a customized and optimized interface for the front-end.

Here's how the BFF pattern fits into the architectural landscape:

- Client-Side Element: The BFF pattern aligns with the client-side element because it serves as the back-end layer directly interacting with the front-end. From the perspective of the front-end application, the BFF acts as a server-side API that the front-end can communicate with. It exposes API endpoints or serverless functions that the front-end can call to request data or perform actions.

- Server-Side Element: The BFF pattern also aligns with the server-side element because it handles business logic, data processing, and interactions with databases or external services. It performs the necessary server-side tasks to fulfill the requests coming from the front-end and returns the appropriate responses.

- Hybrid Layer: The BFF acts as an intermediary layer between the front-end and the main back-end services. It provides an additional level of abstraction that customizes the data and services exposed to the front-end, while still relying on the main back-end services for the core business logic and data management.

- Separation of Concerns: The BFF pattern helps in separating the concerns of the front-end and the main back-end, making it easier to manage and maintain the two separately. This separation improves code organization, scalability, and security, as the front-end and back-end teams can work independently and focus on their specific domains.

- Optimization and Performance: By having a dedicated back-end layer for a specific front-end, the BFF can optimize data format, caching, and communication to best suit the needs of the front-end, improving performance and user experience.

- Flexibility and Independence: The BFF pattern allows different front-end applications (e.g., web, mobile, desktop) to have their own custom back-end layer, tailored to their specific requirements, without affecting the main back-end services.

Overall, the Back-End for Front-End pattern combines aspects of both server-side and client-side architecture, acting as a hybrid layer that serves as an interface between the front-end and the main back-end services. It is a valuable architectural approach to enhance front-end development, improve performance, and enable greater flexibility in managing complex web applications.

### Main advantages and use cases

- SSG is ideal for content-heavy websites where content is relatively static, as it provides excellent performance and SEO benefits.
- SSR is useful when you need dynamic content, personalized data, or want to ensure that search engines can crawl the fully rendered content.
- CSR is suitable for highly interactive applications that require real-time updates and dynamic content based on user interactions.

Developers can choose the appropriate SSR technique based on the specific requirements of their project, the nature of the content, and the desired user experience. Some frameworks, like Next.js and Nuxt.js, offer a combination of both SSR and SSG, allowing developers to choose the most suitable rendering technique on a per-page basis.

### React principles

https://github.com/skirtapaieo/frontend-101/blob/main/react.md

### Overview 1

| Principle                   | React                                      | Vue                     | Svelte                                   | Angular                    | Vanilla JavaScript                       |
| --------------------------- | ------------------------------------------ | ----------------------- | ---------------------------------------- | -------------------------- | ---------------------------------------- |
| Declarative Programming     | Yes                                        | Yes                     | Yes                                      | Yes                        | No                                       |
| Component-Based             | Yes                                        | Yes                     | Yes                                      | Yes                        | No                                       |
| Unidirectional Data Flow    | Yes                                        | Yes                     | Yes                                      | Yes                        | No                                       |
| Virtual DOM                 | Yes                                        | Yes                     | No                                       | No                         | No                                       |
| Reactive Updates            | Yes                                        | Yes                     | Yes                                      | Yes                        | No                                       |
| Templating                  | JSX                                        | Vue Templates           | Svelte Templates                         | Angular Templates          | Manual DOM Manipulation                  |
| Directives                  | No                                         | Yes                     | Yes                                      | Yes                        | No                                       |
| Two-Way Data Binding        | No                                         | Yes                     | Yes                                      | Yes                        | No                                       |
| Dependency Tracking         | No                                         | Yes                     | Yes                                      | Yes                        | No                                       |
| Store Management (State)    | Redux, MobX, etc.                          | Vuex                    | No built-in store, but easy to integrate | RxJS and NgRx              | Manual State Management                  |
| Reactivity                  | Reactivity libraries like RxJS can be used | Vue's reactivity system | Svelte's reactivity system               | Angular's RxJS observables | No built-in reactivity                   |
| Scoped Styles               | Yes                                        | Yes                     | Yes                                      | Yes                        | No                                       |
| Component Lifecycle Hooks   | Yes                                        | Yes                     | Yes                                      | Yes                        | No                                       |
| Transition and Animation    | Yes                                        | Yes                     | Yes                                      | Yes                        | Manual CSS Animation/JavaScript Handling |
| Rich Ecosystem              | Yes                                        | Yes                     | Yes                                      | Yes                        | Limited                                  |
| Community                   | Strong                                     | Great                   | Growing                                  | Large                      | N/A                                      |
| Native                      | React Native                               | N/A                     | N/A                                      | N/A                        | N/A                                      |
| CLI                         | Create React App                           | Vue CLI                 | SvelteKit CLI                            | Angular CLI                | N/A                                      |
| Adoption                    | Widely adopted                             | Rapidly growing         | Emerging                                 | Well-established           | N/A                                      |
| Performance                 | Excellent                                  | Good                    | Excellent                                | Good                       | N/A                                      |
| Bundle Size                 | Moderate                                   | Moderate                | Smallest                                 | Larger                     | N/A                                      |
| Ease of Learning            | Moderate                                   | Easy                    | Easy                                     | Moderate                   | N/A                                      |
| Comprehensive Documentation | Extensive                                  | Comprehensive           | Comprehensive                            | Comprehensive              | N/A                                      |

### Overview 2

Lets check out three different frameworks - React, Vue and Svelte.

|                             | React                                                                                                                            | Vue.js                                                                                                                 | Svelte                                                                                                                                                           |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Learning Curve**          | High. JSX and the whole React ecosystem (like Redux) can take time to grasp.                                                     | Medium. Provides a gentle learning curve and is easier to get started with than React.                                 | Low. Arguably the easiest to learn out of these three, with more emphasis on plain JavaScript and less boilerplate.                                              |
| **Performance**             | Fast. But can suffer if not optimized properly (like using PureComponent, shouldComponentUpdate, etc.).                          | Fast. Similar to React, but includes automatic performance optimizations.                                              | Very fast. Svelte compiles your code to tiny, standalone JavaScript modules at build time, unlike React and Vue, which do the bulk of their work in the browser. |
| **Community and Ecosystem** | Large. Many resources and third-party libraries available. Supported by Facebook.                                                | Growing. Backed by a strong community. A healthy balance between official and community plugins.                       | Smaller. The youngest of the three, so the community is still growing. Fewer resources and libraries.                                                            |
| **Flexibility**             | Very flexible. React is more of a library than a framework, which means it can be more lightweight but might require more setup. | Balanced. Vue.js is a progressive framework, meaning it can be used in part of an application or for a complete build. | Less flexible. Svelte is less flexible in terms of usage within existing projects, but this is by design—it's an intentional trade-off for performance.          |
| **Use Case**                | Best for large-scale applications with active development where performance is a concern.                                        | Best for applications that require a balance of flexibility, ease of use, and performance.                             | Best for smaller projects where start-up performance is the most important factor, or for including in larger projects as a widget or component.                 |

### React

#### Click on Button

A simple example of a component that increments a counter when the button is clicked:

```jsx
import React, { useState } from "react";

function Counter() {
  const [counter, setCounter] = useState(0);

  return (
    <div>
      <p>Counter: {counter}</p>
      <button onClick={() => setCounter(counter + 1)}>Increment</button>
    </div>
  );
}

export default Counter;
```

### Decrement/incement/reset Button

```jsx
import React, { useState } from "react";

function Counter() {
  const [counter, setCounter] = useState(0);

  return (
    <div>
      <p>Counter: {counter}</p>
      <button onClick={() => setCounter(counter + 1)}>Increment</button>
      <button onClick={() => setCounter(counter - 1)}>Decrement</button>
      <button onClick={() => setCounter(0)}>Reset</button>
    </div>
  );
}

export default Counter;
```

### Vue

```vue
<template>
  <div>
    <p>Counter: {{ counter }}</p>
    <button @click="counter++">Increment</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      counter: 0,
    };
  },
};
</script>
```

```vue
<template>
  <div>
    <p>Counter: {{ counter }}</p>
    <button @click="increment">Increment</button>
    <button @click="decrement">Decrement</button>
    <button @click="reset">Reset</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      counter: 0,
    };
  },
  methods: {
    increment() {
      this.counter++;
    },
    decrement() {
      this.counter--;
    },
    reset() {
      this.counter = 0;
    },
  },
};
</script>
```

### Svelte

```svelte
<script>
  let counter = 0;
</script>

<div>
  <p>Counter: {counter}</p>
  <button on:click={() => counter++}>Increment</button>
</div>
```

```svelte
<script>
  let counter = 0;

  function increment() {
    counter++;
  }

  function decrement() {
    counter--;
  }

  function reset() {
    counter = 0;
  }
</script>

<div>
  <p>Counter: {counter}</p>
  <button on:click={increment}>Increment</button>
  <button on:click={decrement}>Decrement</button>
  <button on:click={reset}>Reset</button>
</div>

```

## Mobile approaches

### React Native

Facebook's open-source framework for building mobile applications using JavaScript and React. https://github.com/skirtapaieo/frontend-101/blob/main/mobile-desktop/react-native-hello.js

### Flutter

Google's UI toolkit for building natively compiled applications for mobile, web, and desktop from a single codebase. https://github.com/skirtapaieo/frontend-101/blob/main/mobile-desktop/flutter-hello.dart

### Swift/iOS

These are the native development languages and frameworks for iOS. Offer comprehensive support for platform specific features, but not cross-platform.
https://github.com/skirtapaieo/frontend-101/blob/main/mobile-desktop/swift-hello.swift

### Kotlin/Android

These are the native development languages and frameworks for Android. Offer comprehensive support for platform specific features, but not cross-platform.
https://github.com/skirtapaieo/frontend-101/blob/main/mobile-desktop/kotlin-hello.js

## Desktop approaches

### Electron

This allows you to build desktop apps with JavaScript, HTML, and CSS. Apps like Visual Studio Code, Slack, and GitHub Desktop are built with Electron. https://github.com/skirtapaieo/frontend-101/blob/main/mobile-desktop/electron.js

## Algoexpert - Spaghetti Recipe

Pretty straight forward

## Algoexpert - Blog Post

Pretty straight forward

## Algoexpert - Rainbow circles (JavaScript)

Not so straight forward :-)
