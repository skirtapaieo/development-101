# Design and UX

## Currently

- Design/SEO/performance review of industry leaders (client)
  - Programmatically automated lighthouse, webpagetests, pagespeed to measure SEO, Accessibility and Performance
  - With unligthouse or similar approach the review can be made for all parts of a site
  - To continuously review metrics for SEO, Accessibility and other indices/KPIs

## What about AI and design?

- ChatGPT - ex for personas, competitor analysis
- MidJourney - moodboards, icons, content, and other assets
- Adobe Creative - added AI to some of the tools
- UIzard - scans design sketches and transforms them to digital designs

## Recently

- Led program that built a design system using Figma, Storybook and component libraries (React/Vue)
- User session tracking (HotJar)
- Front-end security (Detectify)
- Analytics (Google Analytics, Tag Management)
- User performance and error tracking (Sentry)
- Security reviews (Detectify)

## Further back

- Balances 100s of cross-functional teams - with product, ux, developers and other expertise
- Participated in branding-centrix startups with branding and design agencies
- Led technical parts of design systems and have a very good understanding of various approaches
- I can participate hands-on if necessary (Figma (sketch), Adobe Creative Suite)
- Usability testing (both qualitative and quantitative)

## About approaches

**Startups** often need to move quickly and have less structured processes, which is why low-cost and flexible methods like sketching, wireframing, and digital prototyping tend to be highly applicable. Startups may also benefit from Lean UX, which focuses on learning and iterating quickly. Design systems may be less applicable in early stages because they require a significant investment to set up and are most beneficial when design consistency is needed across a large number of pages or components, which may not yet be the case for startups.

**Scaleups** are in a stage where they're growing rapidly but also trying to formalize processes to maintain consistency and efficiency. They can benefit from all the approaches, but design systems become particularly important to maintain design consistency as the product and team grow.

**Enterprises** have more established processes and larger teams, which can make it beneficial to have formal design systems in place. They often have the resources to invest in thorough user-centered design practices and can afford the time to create high-fidelity prototypes. Simpler methods like sketching and designing in your head may be less applicable due to the need for clear communication and documentation in larger teams.

| **Design Approach**                           | **Startup** | **Scaleup** | **Enterprise** |
| --------------------------------------------- | ----------- | ----------- | -------------- |
| Sketching/Paper Prototyping                   | High        | Medium      | Low            |
| Wireframing                                   | High        | High        | High           |
| Digital Prototyping (Figma, Sketch, Adobe XD) | High        | High        | High           |
| Designing in the Browser/HTML Prototyping     | Medium      | High        | High           |
| Design Systems                                | Low         | High        | High           |
| Mental Modeling/Designing in Your Head        | High        | Medium      | Low            |
| User-Centered Design (UCD)                    | High        | High        | High           |
| Design Thinking                               | High        | High        | High           |
| Lean UX                                       | High        | High        | Medium         |

## Future Target? Design systems

A design system is a collection of standards for design and front end code. It serves as a guide to help teams design and build digital products more efficiently and consistently. Here are some elements that a design system typically consists of:

- Style Guide: This includes the brand's color palette, typography, grid systems, spacing, and more. It sets the visual language of the brand.
- UI Components / Patterns Library: This is a library of reusable interface elements like buttons, form fields, modals, navigation menus, and more. They are built according to the style guide and often includes variations to suit different situations.
- Usage Guidelines: For each component and pattern, there should be clear instructions on when and how to use them. This can include do's and don'ts, design principles, and more.
- Iconography and Imagery: Icons and images used in the products. These need to be consistent with the style guide and contribute to the overall user experience.
- Voice and Tone Guidelines: This covers how the brand communicates with users through text. It can include copywriting guidelines, grammar and punctuation rules, and examples.
- Code Snippets: These are pre-written pieces of code that developers can reuse. They ensure that the code for each component remains consistent across the products.
- Documentation: Thorough documentation that details how to use the design system, how to contribute to it, and how it's organized. This is an important resource for both designers and developers.
- Design Tools and Resources: These can include downloadable design files, templates, or even design tool plugins that make it easy for designers to use the design system.

The general approach:

- The foundation is part strategy and part design.
- brand guidelines - story, logo usage, color palette, typography, imagery, voice and tone, print and digital
- Use a good range of tools ..
- details - spacing, layout, buttom styles, form styles

## Create the Design components

Using Figma for example, you can create a wide array of components, for each principle, like styles, colors and other elements.

- Clarify requirements and scope
- Create a style guid
- Build (design) components
- Prepare a Figma library
- Use version control (Github)

### Create UI components

Using Storybook for example, can help you address to challenges with components, stories, browsers, viewports and additional requirements related to, for example, accessibility

![text](https://storybook.js.org/0930d02ee2c69e80e8eb796e8be8981c/multiverse.png)

- Build components in Storybook
- Create stories in storybook
- Docucment the components
- Create a CI/CD pipeline
