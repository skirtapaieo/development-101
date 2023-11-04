# Infrastructure

# Cloud for HTMX/Golang application

A deployment of a HTMX/Go application:

| Infrastructure Component       | Azure                                           | AWS                                     | Google Cloud Platform                    |
| ------------------------------ | ----------------------------------------------- | --------------------------------------- | ---------------------------------------- |
| **Compute/Backend**            | Azure Kubernetes Service (AKS)                  | Amazon Elastic Kubernetes Service (EKS) | Google Kubernetes Engine (GKE)           |
| **Load Balancer**              | Azure Load Balancer + Azure Application Gateway | AWS Elastic Load Balancing (ELB)        | Google Cloud Load Balancer               |
| **Web Hosting/Static Content** | Azure Blob Storage with Static Website          | Amazon S3 with Static Website Hosting   | Google Cloud Storage with Static Website |
| **Content Delivery Network**   | Azure CDN                                       | Amazon CloudFront                       | Google Cloud CDN                         |
| **Scaling**                    | Managed by AKS                                  | Managed by EKS                          | Managed by GKE                           |
| **Monitoring & Logging**       | Azure Monitor + Log Analytics                   | Amazon CloudWatch                       | Google Cloud Monitoring + Logging        |

## Notes:

1. **Compute/Backend**: Kubernetes is recommended because it is well-suited for containerized applications, like one written in Go, and it's known for scalability and manageability. Both AKS (Azure), EKS (AWS), and GKE (Google Cloud) manage and orchestrate your Kubernetes infrastructure.

2. **Load Balancer**: It's essential when expecting a lot of users to distribute the incoming traffic. Each platform provides its native load balancing solutions which integrate well with their Kubernetes services.

3. **Web Hosting/Static Content**: Since HTMX largely depends on HTML attributes, you'll be dealing with mainly static content. All three cloud platforms offer scalable storage solutions that can also serve static websites.

4. **Content Delivery Network (CDN)**: A CDN is crucial for performance, especially when serving users globally. It ensures that your static content (like HTML, CSS, and JS files) is served from locations closer to the end user.

5. **Scaling**: With Kubernetes, scaling (both manual and auto-scaling) is handled by the platform itself, ensuring your application can handle thousands of users.

6. **Monitoring & Logging**: All three cloud platforms offer monitoring and logging solutions. They'll help you track application performance, user metrics, and troubleshoot issues.

Given the above setup, you'll deploy your Go application as a container on Kubernetes. Your HTMX-based frontend will be hosted as static content in the respective storage solutions, and it will communicate with your Go backend. The CDN will ensure fast content delivery, while the load balancer will distribute the incoming traffic to your backend. The Kubernetes service in each platform will manage the scaling.

## Visualizing infrastructure

There are several tools and methodologies available that allow users to define, generate, or visualize infrastructure as code (IaC) or using specific notations:

1. **Infrastructure as Code (IaC)**:

   - **Terraform**: An open-source IaC software tool that provides a consistent CLI workflow to manage numerous cloud services. Terraform scripts can be written in HashiCorp Configuration Language (HCL). You define what resources you want, and Terraform will create/update them in the correct order.
   - **AWS CloudFormation**: Allows you to define AWS infrastructure using JSON or YAML templates.
   - **Azure Resource Manager (ARM) Templates**: Define Azure resources using JSON.
   - **Google Cloud Deployment Manager**: Uses YAML for resource definition in GCP.
   - **Pulumi**: A modern IaC tool that lets you define infrastructure using general-purpose programming languages like TypeScript, Python, Go, or C#.

2. **Visualization from IaC**:

   - Some IaC tools or third-party integrations can generate visual representations of your infrastructure based on your code/templates:
     - **Terraform**: While not built-in, tools like `terraform graph` (which creates a visual graph of Terraform resources) or third-party tools like `Blast Radius` can be used.
     - **CloudCraft**: Allows you to import your AWS infrastructure (although it's more manual than automatic visualization from IaC).

3. **Notation and Diagramming**:

   - **The AWS Well-Architected Tool**: Provides a set of consistent designs and best practices, with templates available.
   - **Archimate**: A technical standard for IT architecture visualization. There are tools like Archi that allow for creating such diagrams.
   - **AWS, Azure, and GCP Icon Sets**: All three cloud providers offer sets of icons for use in diagramming tools, so you can visually represent each service accurately.

4. **DSL (Domain-Specific Language) for Diagrams**:

   - **CDK for Terraform**: Allows you to define Terraform infrastructure using TypeScript or Python, essentially providing a higher-level abstraction over HCL.
   - **AWS CDK (Cloud Development Kit)**: Lets you define AWS resources using familiar programming languages. It provides higher-level constructs, making it easier than working directly with CloudFormation templates.
   - **Diagrams**: A python library that lets you define cloud infrastructure diagrams using Python code. It supports multiple cloud providers.

5. **Pre-made Templates**:
   - Both AWS and Azure provide Quick Start templates or solutions that provide pre-made CloudFormation and ARM templates for common architectures.
   - GCP offers similar solutions with their Cloud Foundation Toolkit.

The approach you choose largely depends on your preferences, the complexity of your setup, and how often you expect changes. Some prefer the flexibility and power of IaC with tools like Terraform or CloudFormation, while others might prioritize visualization and use tools like CloudCraft or the AWS Well-Architected Tool. There's no one-size-fits-all; the landscape is vast, and the right tools often depend on specific project needs.

## Smaller, simpler approaches than the Big 3 Cloud vendors

There are several platforms and vendors that aim to simplify deployment, hosting, and scaling of web applications, often abstracting away much of the underlying infrastructure management. Here are some popular ones:

1. **Vercel**:

   - **Purpose**: Primarily known for hosting frontend web applications and static sites.
   - **Features**: Offers a global CDN, automatic HTTPS, continuous deployment from Git, serverless functions, and more.
   - **Best For**: Projects based on Next.js (although it supports other frameworks too).

2. **Netlify**:

   - **Purpose**: A platform for building, deploying, and hosting web applications and static sites.
   - **Features**: Continuous deployment from Git, serverless functions, built-in CDN, form handling, identity/authentication services, and more.
   - **Best For**: Static site generators like Jekyll, Hugo, Gatsby, etc., and frontend frameworks like React, Vue, Angular.

3. **Render**:

   - **Purpose**: Provides hosting for web apps, static sites, backend apps, databases, and more.
   - **Features**: Continuous deployment, pull request previews, automatic HTTPS, managed databases, private networking.
   - **Best For**: Full-stack applications with frontend and backend components.

4. **Heroku**:

   - **Purpose**: A cloud platform as a service (PaaS) supporting several programming languages.
   - **Features**: Git-based deployments, a marketplace of add-ons for databases, caching, logging, error tracking, etc.
   - **Best For**: Backend applications, APIs, web applications with backend logic.

5. **Firebase Hosting**:

   - **Purpose**: Offers fast, secure, and reliable hosting for web applications.
   - **Features**: Serves content over a CDN, provides automatic SSL, supports serverless with Cloud Functions, offers realtime databases and authentication.
   - **Best For**: SPA (Single Page Applications) and mobile app backends.

6. **DigitalOcean App Platform**:

   - **Purpose**: Platform as a Service (PaaS) offering by DigitalOcean.
   - **Features**: Git-based deployment, auto-scaling, HTTPS, container-based applications.
   - **Best For**: Web apps, APIs, static sites, and container-based applications.

7. **Begin**:
   - **Purpose**: A platform to build and deploy serverless apps.
   - **Features**: Git integration, built on top of AWS (especially AWS Lambda).
   - **Best For**: Serverless applications and architectures.

These platforms primarily cater to developers looking for a more straightforward deployment process, abstracting away many infrastructure decisions and tasks.

They can be more cost-effective for small to medium-sized applications due to their pricing structures and the avoided overhead of managing infrastructure directly.

However, larger, more complex applications, or those with specific infrastructure needs, may still benefit from a more traditional or custom cloud-based setup.

## Comparison of infrastructure approaches

| Category                             | Pros                                                                                                  | Cons                                                                                  |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **Full-Featured Cloud Environments** | - Versatility<br>- Scalability<br>- Managed Services<br>- Security<br>- Integration<br>- Global Reach | - Complexity<br>- Cost<br>- Vendor Lock-in                                            |
| **Simpler Cloud Platforms**          | - Simplicity<br>- Speed<br>- Optimized for Use Cases<br>- Managed<br>- Cost-Effective                 | - Less Control<br>- Scope Limitation<br>- Vendor Lock-in                              |
| **Self-Managed/On-Premise**          | - Full Control<br>- Optimization<br>- Cost Structure<br>- Security                                    | - Maintenance Overhead<br>- Upfront Costs<br>- Scalability<br>- Redundancy Challenges |
| **Hybrid Solutions**                 | - Balanced Control<br>- Optimization<br>- Flexibility                                                 | - Complexity<br>- Cost Monitoring<br>- Integration Challenges                         |
