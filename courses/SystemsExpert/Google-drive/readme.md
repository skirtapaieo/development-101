# Google drive (and Dropbox, Onedrive, iCloud)

# 1 - Initial questions

## 2 - Background / the why

- Cloud storage and synchronization was pioneered by Dropbox
- To store files in the cloud, backup, synchronize, and share
- Integration with Googles other service
- Added security features
- Introduced in 2012

## 3 - Scope for the design

- Only storage aspect - personal drive - upload, folders, download, synchronization, sharing ...
- Not all features - not related products like Google docs, sheets, slides, drawings, desktop version, company, starred, recently added

### Usage insights

- The system is for 1 billion users - and 15 GB/user - i.e 15,000 PB, and with backup 30,000 PB, i.e. exabyte scale, 30 EB
- There are incremental back-ups, deduplication, compression and other methods

### Architecture

- Front-end
- Back-end
- Data pipeline
- Infrastructure
- Additional - security, protocols, algorithms, costs, team size

## 4 - Prior experiences

- Much simpler storage solutions
- Mainly a user of various storage solutions (Dropbox, Microsoft Onedrive, Apple iCloud)
- Usage of S3 for various static content ...
- Yocto for embedded system
- File systems ...

## 5 - A little bit of storage research

### Background to the distributed system

- Dropbox initially started using AWS S3
- As they grew they needed more control over their infrastructure
- Around 2015 they undertook a massive project (Magic Pocket) to migrate a majority of their user data - by 2016 90% of the data was moved to their new solution
- Distributed block-based file system, spreads data across multiple physical locations, adding redundancy and fault tolerance
- Custom hardware - fined tunes for their need of disks to match workload
- Optimized network - reduce latency, byt building a high-speed, low latency network to connect their data centers
- Cost-efficiency, flexibility and control

### Deep-dive into the main units (harddrives)

The insights below, gives and indication that to store 30 TB, 1,5 million harddrives would be used.

1. **Shingled Magnetic Recording (SMR)**: In a blog post from 2016, Dropbox mentioned that they were one of the earliest and largest adopters of SMR drive technology, which allows for greater data density and is typically used for archival storage.

2. **Custom-Built Infrastructure**: As part of their move away from AWS, Dropbox built custom hardware tailored to their specific needs. While they've mentioned this custom hardware in general terms, they haven't provided granular specifications.

3. **Industry Trends**: By 2021, data centers of large tech companies often used hard drives ranging from 10TB to 20TB, with some even going higher as technology progressed. Given Dropbox's scale, it would make sense for them to use high-capacity drives to maximize storage density and efficiency in their data centers. However, the exact capacity they would choose would depend on various factors, including cost, performance, reliability, and specific workload requirements.

4. **Multiple Drive Types**: Large-scale storage solutions typically use a combination of different drive types to balance cost and performance. While high-capacity HDDs might be used for the bulk storage of user files, faster SSDs might be used for caching, metadata storage, and other tasks requiring rapid access.

For the exact specifics on their drive sizes or the latest configurations they might be using, you'd likely need direct information from Dropbox or wait for any new disclosures they might make in future tech talks, blog posts, or white papers.

## Techniques for reducing storage

These won't be exact real-world scenarios but should give you an idea of how each method can lead to storage savings:

| Technique                         | Estimated Storage Savings (%) | Example Scenario                                                                                                                                                         |
| --------------------------------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Deduplication                     | 30%                           | 10 users upload the same 10MB presentation file. Instead of using 100MB of storage, only 10MB is used because the file is stored once and then referenced for each user. |
| Compression                       | 20%                           | A 100MB text file, when compressed, occupies only 80MB, thus saving 20MB of storage space.                                                                               |
| Shingled Magnetic Recording (SMR) | 10%                           | A traditional hard drive might store 10TB of data, but with SMR, it can store 11TB on the same physical disk.                                                            |
| Erasure Coding                    | 15%                           | Instead of keeping 3 full replicas of data for redundancy (300% storage use), erasure coding might achieve the same redundancy with only 115% storage use.               |
| Regular Data Cleanup              | 5%                            | Users delete files sending them to the trash. If Dropbox automatically clears the trash after 30 days, they could reclaim that storage space.                            |
| Tiered Storage                    | 0%                            | A frequently accessed file is moved from an SSD (expensive) to an HDD (cheaper) after a month of inactivity, saving costs but not storage space.                         |
| Monitoring & Predictive Analysis  | 0%                            | By predicting a drive's failure, data is moved before the drive fails, preventing data loss but not necessarily saving storage space.                                    |

The above scenarios are generalized examples. Actual outcomes depend on numerous factors including the specific algorithms used, the nature of the data, user behaviors, and technological advancements in storage solutions.

## 6 - Actual design

I would start thinking about the stack, which is very complicated. Clearly mainly a low-level "infrastructure" project.

### APIs, services and technologies

| Layer # | Layer Name                             | Representative API/Services for Operations                                 | Main Technology                                         |
| ------- | -------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------- |
| 10      | **Frontend/UI**                        | Web UI: `GET /home`, Desktop Client UI, Mobile App UI                      | React, Swift (iOS), Kotlin (Android)                    |
| 9       | **CI/CD**                              | Jenkins: `POST /job/upload-job/build`                                      | Jenkins, GitLab CI, Docker                              |
| 8       | **Monitoring & Logging**               | Prometheus: `GET /metrics`, ELK: `GET /logs/{file_id}`                     | Prometheus, ELK Stack (Elasticsearch, Logstash, Kibana) |
| 7       | **Security**                           | OAuth2: `POST /token`, TLS/SSL for all operations                          | OAuth2, TLS/SSL, Let's Encrypt                          |
| 6       | **User-Facing Services & APIs**        | `POST /file/upload`, `POST /folder/create`, `GET /file/download/{file_id}` | Nginx, Flask, Express.js                                |
| 5       | **Database & Caching**                 | PostgreSQL: `INSERT INTO files`, Redis: `GET cache:{file_id}`              | PostgreSQL, Redis, Cassandra                            |
| 4       | **Service Layer**                      | gRPC: `UploadFileService`, `DownloadFileService`                           | gRPC, HTTP/2, RabbitMQ                                  |
| 3       | **Networking**                         | SDN: `Route /datacenter1/file/upload`                                      | SDN (OpenFlow), VPN, HAProxy                            |
| 2       | **Orchestration & Cluster Management** | Kubernetes: `Deploy UploadService`, Docker: `Run FileSyncContainer`        | Kubernetes, Docker, etcd                                |
| 1       | **Data Protection and Optimization**   | Erasure Coding service, Deduplication service                              | Erasure Coding, Zstandard, LZ4                          |
| 0       | **Cluster & Distributed File Systems** | Ceph: `PUT object/file`, `GET object/file`                                 | Ceph, GlusterFS, Hadoop HDFS                            |
| -1      | **Storage Management**                 | LVM: `lvcreate`, Software RAID: `mdadm --create`                           | LVM, mdadm (Software RAID)                              |
| -2      | **Operating System & Filesystem**      | Linux system calls: `open()`, `write()`, `read()`                          | Linux (e.g., CentOS, Ubuntu), ext4 Filesystem           |
| -3      | **Hardware Layer**                     | Direct disk I/O, Network packet routing                                    | Custom Servers, HDDs/SSDs, Cisco Routers                |

Keep in mind that the choice of technology can vary depending on the specific requirements, the scale of operations, and the architectural decisions made by a company. The above list provides a general idea based on popular and widely-used technologies.

### Information model

Certainly! Below is a tabulated version of the information model for a Dropbox-like system:

| **Entity**      | **Attributes**                                                                                                                             | **Relationships**                                                                                                                      |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- |
| **User**        | - UserID (PK) <br> - Username <br> - Email <br> - Password (hashed) <br> - AccountType                                                     | 1. One-to-Many to **File** <br> 2. One-to-Many to **Folder** <br> 3. One-to-Many to **ActivityLog** <br> 4. One-to-Many to **Sharing** |
| **File**        | - FileID (PK) <br> - UserID (FK) <br> - FileName <br> - FileSize <br> - UploadDate <br> - LastModifiedDate <br> - FileHash <br> - FilePath | 1. Many-to-One to **User** <br> 2. One-to-Many to **Sharing** <br> 3. Many-to-One to **Folder**                                        |
| **Folder**      | - FolderID (PK) <br> - UserID (FK) <br> - FolderName <br> - CreationDate <br> - ParentFolderID (Self-FK) <br> - FolderPath                 | 1. Many-to-One to **User** <br> 2. Hierarchical to **Folder** <br> 3. One-to-Many to **File**                                          |
| **Sharing**     | - SharingID (PK) <br> - FileID (FK) <br> - SharedWithUserID (FK) <br> - SharingDate <br> - Permissions                                     | 1. Many-to-One to **User** <br> 2. Many-to-One to **File**                                                                             |
| **ActivityLog** | - LogID (PK) <br> - UserID (FK) <br> - Action <br> - ActionDate <br> - TargetFileID (FK) <br> - TargetFolderID (FK)                        | 1. Many-to-One to **User** <br> 2. Many-to-One to **File** <br> 3. Many-to-One to **Folder**                                           |

This table outlines the entities, their attributes, and their relationships. Keep in mind that this is a simplified version and real-world systems like Dropbox would have a more complex data model.

## The team building it

Here's an enhanced table that includes layer numbers and a realistic initial headcount estimate for a startup.

It's worth noting that in a startup setting, individuals often wear multiple hats and might span several role.

One would definitely not start with building own infrastructure but rather take the route that Dropbox took, using S3.

| **Role**                            | **Main Skills/Expertise**                                 | **Supported Layer**                                | **Layer Number** | **Estimated Headcount**                   |
| ----------------------------------- | --------------------------------------------------------- | -------------------------------------------------- | ---------------- | ----------------------------------------- |
| **Frontend Developer**              | HTML, CSS, JavaScript, React/Redux, Vue.js, Angular       | Frontend/UI                                        | 10               | 2-3                                       |
| **Mobile App Developer**            | Swift, Kotlin, Flutter, React Native                      | Frontend/UI                                        | 10               | 2 (1 for iOS, 1 for Android)              |
| **UI/UX Designer**                  | Wireframing, prototyping, user research, Figma, Sketch    | Frontend/UI                                        | 10               | 1                                         |
| **Backend Developer**               | Python, Node.js, Java, database design, RESTful API, gRPC | User-Facing Services & APIs, Service Layer         | 6, 4             | 2-3                                       |
| **Database Administrator/Engineer** | SQL, NoSQL, database tuning                               | Database & Caching                                 | 5                | 1                                         |
| **DevOps Engineer**                 | CI/CD, Docker, Kubernetes, Terraform                      | CI/CD, Orchestration & Cluster Management          | 9, 2             | 1-2                                       |
| **System Administrator**            | Linux/UNIX, shell scripting, server hardware management   | Operating System & Filesystem, Hardware Layer      | -2, -3           | 1                                         |
| **Network Engineer**                | Network design, TCP/IP, VPNs, SDN                         | Networking                                         | 3                | 1                                         |
| **Security Engineer**               | Threat analysis, encryption protocols, OAuth              | Security                                           | 7                | 1                                         |
| **Cloud Engineer**                  | AWS, Azure, Google Cloud, cloud architecture              | Infrastructure, Orchestration & Cluster Management | 0, 2             | 1                                         |
| **Data Engineer**                   | Data modeling, ETL, Hadoop, Spark                         | Data Pipeline, Service Layer                       | 4                | 1                                         |
| **Data Scientist**                  | Machine learning, predictive analytics                    | Data Pipeline                                      | 4                | 0-1 (might not be initial priority)       |
| **Data Analyst**                    | SQL, data visualization, business intelligence            | Data Pipeline                                      | 4                | 1                                         |
| **Product Manager**                 | Product lifecycle management, stakeholder communication   | Across all layers (strategy/planning)              | All              | 1                                         |
| **QA Engineer**                     | Test planning, test automation, quality assurance         | Across all layers (testing/verification)           | All              | 1-2                                       |
| **Technical Writer**                | Documentation, user guides, API documentation             | Across all layers (documentation)                  | All              | 0-1 (might come later as product matures) |
| **Project Manager/Scrum Master**    | Agile methodologies, sprint planning                      | Across all layers (coordination/planning)          | All              | 1                                         |

This setup suggests a total of approximately 20-30 initial members, but this can vary greatly based on the startup's scope, ambition, and resources.
