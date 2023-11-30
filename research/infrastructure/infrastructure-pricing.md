
# Infrastructure

## Pricing

Pricing for Edge Computing, Serverless Computing, and Docker-based services can vary widely based on the cloud provider, the specific services used, and the requirements of the application.

|  | Edge Computing | Serverless Computing | Docker-based Computing |
|---|---|---|---|
| Hardware Costs | Usually Yes | No | No (Unless On-Prem) |
| Compute Costs | Yes | Yes (But granular) | Yes |
| Storage Costs | Possibly | Yes | Yes |
| Networking Costs | Usually Yes | Yes | Yes |
| Complexity | Medium-High | Low | Medium-High |
| Scalability | Limited | High | High |

# Providers

Here's a merged table - includes both the major cloud providers and the niche players.

| Provider       | Edge Computing      | Serverless Computing | Docker-based Computing    | VMs             | Bare-Metal         |
|----------------|---------------------|----------------------|---------------------------|-----------------|--------------------|
| AWS            | Wavelength, Snow Family| Lambda             | ECS, EKS                  | EC2             | EC2 Bare Metal     |
| Azure          | Edge Zones, IoT Edge| Azure Functions     | AKS                        | Azure VMs       | Dedicated Host     |
| Google         | IoT Edge, Anthos    | Cloud Functions     | GKE                        | Compute Engine  | N/A                |
| IBM            | Edge Application Manager| Cloud Functions   | Cloud Kubernetes Service  | Virtual Servers | Bare Metal Servers |
| Fastly         | Compute@Edge        | N/A                  | N/A                        | N/A             | N/A                |
| Cloudflare     | Cloudflare Workers  | N/A                  | N/A                        | N/A             | N/A                |
| Akamai         | Edge Compute        | N/A                  | N/A                        | N/A             | N/A                |
| StackPath      | Edge Computing      | N/A                  | N/A                        | N/A             | N/A                |
| Vercel         | N/A                 | Serverless Functions | N/A                        | N/A             | N/A                |
| Netlify        | N/A                 | Netlify Functions    | N/A                        | N/A             | N/A                |
| Zeit Now       | N/A                 | Now Functions        | N/A                        | N/A             | N/A                |
| Alibaba Cloud  | N/A                 | Function Compute     | Alibaba Container Service  | ECS             | N/A                |
| DigitalOcean   | N/A                 | N/A                  | Managed Kubernetes         | Droplets        | N/A                |
| Linode         | N/A                 | N/A                  | Linode Kubernetes Engine   | Linode Instances| N/A                |
| Red Hat        | N/A                 | N/A                  | OpenShift                  | N/A             | N/A                |
| Rancher        | N/A                 | N/A                  | Kubernetes Management      | N/A             | N/A                |
| Packet         | N/A                 | N/A                  | N/A                        | N/A             | Bare Metal Cloud   |
| OVHcloud       | N/A                 | N/A                  | N/A                        | N/A             | Bare-Metal Servers |
| Hetzner        | N/A                 | N/A                  | N/A                        | N/A             | Dedicated Servers  |

This table provides a comprehensive overview of what each provider offers in terms of Edge Computing, Serverless Computing, Docker-based Computing, VMs, and Bare-Metal Servers.
