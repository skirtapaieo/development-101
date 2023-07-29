# design-101


# Minimal design system

  - [What is it?](#what-is-it)
  - [Approach](#approach)
    - [1. Set Brand Guidelines](#1-set-brand-guidelines)
      - [1.1 Brand Guidelines/Rules](#11-brand-guidelinesrules)
      - [1.2 Best Practices](#12-best-practices)
      - [1.3 Tools](#13-tools)
    - [2. Define The System](#2-define-the-system)
    - [3. Create The Design Components](#3-create-the-design-components)
    - [4. Create UI Components](#4-create-ui-components)


## What is it? 

A design system is a collection of standards for design and front end code. It serves as a guide to help teams design and build digital products more efficiently and consistently. Here are some elements that a design system typically consists of:

- Style Guide: This includes the brand's color palette, typography, grid systems, spacing, and more. It sets the visual language of the brand.

- UI Components / Patterns Library: This is a library of reusable interface elements like buttons, form fields, modals, navigation menus, and more. They are built according to the style guide and often includes variations to suit different situations.

- Usage Guidelines: For each component and pattern, there should be clear instructions on when and how to use them. This can include do's and don'ts, design principles, and more.

- Iconography and Imagery: Icons and images used in the products. These need to be consistent with the style guide and contribute to the overall user experience.

- Voice and Tone Guidelines: This covers how the brand communicates with users through text. It can include copywriting guidelines, grammar and punctuation rules, and examples.

- Code Snippets: These are pre-written pieces of code that developers can reuse. They ensure that the code for each component remains consistent across the products.

- Documentation: Thorough documentation that details how to use the design system, how to contribute to it, and how it's organized. This is an important resource for both designers and developers.

- Design Tools and Resources: These can include downloadable design files, templates, or even design tool plugins that make it easy for designers to use the design system.

The specific components and depth of a design system can vary based on the needs and size of the organization. It is also a living document, constantly evolving as the brand and products evolve.

## Approach 


### 1 Set Brand guidelines  

The foundation is part strategy and part design. 

#### 1.1 Brand guidelines/rules

You need to manage a few rules and guidelines related to how your brand works:  

- Brand story 
- Logo usage
- Color palette 
- Typography 
- Imagery 
- Voice and tone 
- Print and digital application 

#### 1.2 Best practices 

There are some basic best practices: 

- Including essential elements (above)
- Provide clear instructions 
- Use real examples 
- Keep it flexible 
- Keep it updated 

#### 1.3 Tools 

| Tool | Purpose | Usability | Collaboration | Cost | Online/Offline |
| --- | --- | --- | --- | --- | --- |
| Adobe Suite | Comprehensive design tool for creating all sorts of brand assets. | Steeper learning curve but offers robust features. | Limited real-time collaboration; primarily individual work. | Paid. Various subscription options based on requirements. | Both, but primarily Offline. |
| Canva | User-friendly design tool, with templates for brand assets. | Very easy to use, even for beginners. | Good real-time collaboration features. | Free version available, paid for more features. | Online. |
| Google Docs/Slides | For creating simple and straightforward guidelines. | Very easy to use. | Excellent real-time collaboration features. | Free. | Online. |
| Figma/Sketch | Digital design tool for UI/UX and brand assets. | Moderate learning curve. | Excellent real-time collaboration features in Figma. Sketch has limited collaboration. | Figma: Free for individuals, paid for teams. Sketch: Paid. | Figma: Online. Sketch: Offline. |
| Frontify | Professional brand management platform for creating and sharing brand guidelines. | Moderate learning curve. | Excellent real-time collaboration features. | Paid. | Online. |


### 2 Define the system

Define a few principles including: 

- Typography 
- Colors 
- Spacing and Layout
- Button styles
- Form styles 

### 3 Create the Design components 

Using Figma for example, you can create a wide array of components, for each principle, like styles, colors and other elements. 

- Clarify requirements and scope 
- Create a style guid 
- Build (design) components 
- Prepare a Figma library 
- Use version control (Github) 

### C4 reate UI components 

Using Storybook for example, can help you address to challenges with components, stories, browsers, viewports and additional requirements related to, for example, accessibility

![text](https://storybook.js.org/0930d02ee2c69e80e8eb796e8be8981c/multiverse.png)

- Build components in Storybook 
- Create stories in storybook 
- Docucment the components 
- Create a CI/CD pipeline 

