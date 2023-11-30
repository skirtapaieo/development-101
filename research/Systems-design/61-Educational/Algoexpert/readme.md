# Algoexpert platform

### Clarifying questions

- Functional.
  - Are we designing the full platform or a part? (functionality/use cases) Only the core user flow where you end up at the website, going through questions, marking "questions" as complete or in progress, writing running code in various languages, the code will be tested and you either get ok or no
  - In the algoexpert part, there are content parts, but there is also an **engine of some kind that manages 9 languages**, test cases, etc, that seems to be the core of the platform.
  - It is a content platform, but How many changes/week? . A few every week, so not a large issue. Most likely the work on every course, the video content and so ...
- Non-functional
  - Load from users? 100,000 visits from users/week
  - Availability? not a big problem ...
  - performance? feel responsive ...

#### Additional questions

Sure, let's look at AlgoExpert's current design as of my knowledge cutoff in September 2021 to provide the best responses to these questions. Please note, the platform may have evolved since then, and my answers may no longer reflect the current state of the platform.

| Category                         | Questions                                                                                                                   | AlgoExpert's Current Implementation                                                                                                                                                                                  |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| User Requirements                | 1. Who exactly are we building this platform for?                                                                           | AlgoExpert is primarily targeted towards software engineering candidates preparing for technical interviews.                                                                                                         |
|                                  | 2. What kinds of content and features should the platform have?                                                             | AlgoExpert offers a comprehensive set of coding interview problems, video explanations, and text-based solutions.                                                                                                    |
|                                  | 3. What level of difficulty should the coding questions have?                                                               | AlgoExpert covers a wide range of difficulty levels, catering to users at different stages of their preparation.                                                                                                     |
|                                  | 4. What types of instructional materials should we include?                                                                 | AlgoExpert provides both video explanations and text-based solutions for each problem.                                                                                                                               |
|                                  | 5. Which programming languages should we support?                                                                           | As of September 2021, AlgoExpert supports several popular programming languages including Python, JavaScript, Java, C++, C#, and more.                                                                               |
|                                  | 11. Should the platform provide features to track a user's progress over time?                                              | AlgoExpert offers a progress tracker to help users keep track of their progress through the problem set.                                                                                                             |
|                                  | 12. How will the platform ensure accessibility and inclusivity for users of different backgrounds and with different needs? | AlgoExpert ensures accessibility by providing text-based solutions in addition to video explanations. Further details specific to inclusivity and accessibility initiatives were not available as of September 2021. |
| Product Design and Functionality | 6. What should the user interface look like?                                                                                | AlgoExpert has a user-friendly interface with a built-in code editor where users can write, test, and debug their code.                                                                                              |
|                                  | 7. How will users' solutions be evaluated?                                                                                  | AlgoExpert provides automated test cases that users can run against their code for immediate feedback.                                                                                                               |
|                                  | 8. Should the platform include features for users to collaborate with each other?                                           | As of September 2021, AlgoExpert does not include features for direct user collaboration such as forums or chat rooms.                                                                                               |
| Business Model                   | 9. What should the platform's subscription model be?                                                                        | AlgoExpert operates on a paid subscription model. They offer a one-time payment for lifetime access to their resources as of September 2021.                                                                         |
| Technical Requirements           | 10. How do we plan to scale the platform as the user base grows?                                                            | Specific details on AlgoExpert's scaling strategies are not publicly available. However, being a web-based platform, they likely use scalable cloud infrastructure.                                                  |
| Security and Privacy             | 13. What considerations should we make to ensure the platform is secure and respects user privacy?                          | AlgoExpert has a privacy policy in place that details how they collect, use, and protect user data. They likely follow industry standard security practices to protect their platform and user data.                 |

### The coding platform

| Feature                   | HackerRank's CodeChecker   | JDoodle        | Sphere Engine   | Glot.io       | CompileBox    | Remoteinterview.io  |
| ------------------------- | -------------------------- | -------------- | --------------- | ------------- | ------------- | ------------------- |
| Sandboxing                | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Multiple Languages        | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Resource Limitations      | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Input/Output Handling     | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Error Handling            | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| Evaluation                | No\*                       | No\*           | No\*            | No\*          | No\*          | No\*                |
| Scalability               | Yes                        | Yes            | Yes             | Yes           | Yes           | Yes                 |
| ------------------------- | -------------------------- | -------------- | --------------- | ------------- | ------------- | ------------------- |
| Total 'Yes' Counts        | 6                          | 6              | 6               | 6             | 6             | 6                   |

\* While these services handle code execution, they typically do not perform evaluation of the solution against a set of test cases. That part usually needs to be managed by your platform - you would call their API to run the code and then evaluate the output yourself.

As for guessing which platform AlgoExpert is using, it's a tough call without insider knowledge. As an AI model trained by OpenAI, I don't have access to real-time or proprietary data.

As of my last training cut-off in September 2021, AlgoExpert hasn't publicly stated which method they use. It's plausible they could have developed their own in-house solution given their scale and specific requirements. The advantage of an in-house solution is that it allows for full control over the environment, including customization and scaling based on their particular needs.

If they're using a third-party service, it would likely be one that offers robust features and wide language support, but it's impossible to say definitively which one. Please reach out to AlgoExpert directly for the most accurate information.

### Description of the areas

A coding execution environment is the server-side component where the user-submitted code is actually executed and evaluated. It is also known as a code execution engine. Here's a more detailed look at the process and considerations involved in setting up this environment:

1. **Sandboxing:** One of the most critical aspects of the code execution environment is sandboxing, which is a security mechanism for separating running programs. It isolates the user-submitted code execution in a separate environment to ensure that any malicious code doesn't harm your system or access sensitive data.

2. **Supporting Multiple Languages:** The environment needs to support all the programming languages you plan to offer on your platform. This involves installing the required compilers or interpreters for each language on your server and creating a system that selects the correct one based on the user's chosen language.

3. **Resource Limitations:** User-submitted code can potentially consume a lot of system resources or even fall into an infinite loop. To prevent a single user from consuming all your server resources, you need to impose limitations on execution time, memory usage, and possibly other resources like disk usage or network access.

4. **Input and Output Handling:** The environment needs to provide the input data to the user's code and capture the output for evaluation. This might involve setting up a file system in the sandbox environment or redirecting the standard input/output streams of the code execution process.

5. **Error Handling:** If the user's code has an error, you need to capture this and provide helpful feedback. This involves capturing compiler/interpreter error messages and exceptions thrown during execution.

6. **Evaluation:** After running the code, you need to compare the output to the expected output to determine if the solution is correct. This might be as simple as a string comparison, or it might involve some more complex logic if there are multiple valid solutions.

7. **Scalability:** Depending on the number of users and the complexity of the problems, code execution could be a very resource-intensive task. You need to design your environment with scalability in mind. This could involve distributing the load across multiple servers, using cloud services that can auto-scale based on load, or queuing code execution tasks and processing them in the background.

If building such an environment sounds too complex or resource-intensive, there are third-party services like JDoodle, Sphere Engine, or HackerRank's CodeChecker that provide APIs for running code in multiple languages. These services handle all the complexities mentioned above and can save you a significant amount of development time and resources. However, they come with ongoing costs and the risk of relying on a third-party service.

Whether you choose to build your own environment or use a third-party service largely depends on your specific requirements, resources, and risk tolerance. Both options have their pros and cons and should be carefully considered.

### A list of platforms

1. [HackerRank's CodeChecker](https://www.hackerrank.com/)
2. [JDoodle](https://www.jdoodle.com/)
3. [Sphere Engine](https://www.sphere-engine.com/)
4. [Glot.io](https://glot.io/)
5. [CompileBox](https://github.com/remoteinterview/compilebox)
6. [RemoteInterview.io](https://www.remoteinterview.io/)

Platforms like Palm or GTP would be a supplement to these platforms.
