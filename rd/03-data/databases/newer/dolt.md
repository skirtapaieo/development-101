
# Dolt

[Site URL](https://www.dolthub.com/)
[Tutorial URL](https://docs.dolthub.com/)

## Why should I care of Dolt?

Dolt is a SQL database that has Git features. You can commit, branch, merge, clone, and push and pull just like a Git repository.

## Who created Dolt?

Dolt is developed by DoltHub, a company co-founded by Brian Hendriks and Tim Sehn.

## Why the name Dolt?

The name "Dolt" is a play on "Git for Data."

## Why Dolt was created?

Dolt was created to provide version control features to database management, making it easier for developers to track changes and collaborate.

## How and when was Dolt started?

Dolt was started in 2019 by DoltHub.

## Who uses Dolt?

It's used by developers, data engineers, and data scientists who want Git-like version control for their databases.

## What are the things that people say Dolt needs to improve?

- Query performance on large datasets.
- Lack of some SQL features compared to more established DBMSs.

## What are the main alternatives to Dolt (include URLs)?

- Git ([Git](https://git-scm.com/))
- Traditional SQL Databases like MySQL ([MySQL](https://www.mysql.com/))

## Overview of the Dolt stack

Dolt uses a MySQL-compatible SQL engine and has built-in Git features.

# Using the tool Dolt

## How to install Dolt using CLI

\`\`\`bash
sudo curl -L https://github.com/dolthub/dolt/releases/latest/download/install.sh | bash
\`\`\`

## How to configure Dolt

\`\`\`bash
dolt config --global --add user.email "you@example.com"
dolt config --global --add user.name "Your Name"
\`\`\`

## Give a simple example of how to use Dolt

\`\`\`bash
dolt init
\`\`\`

## Give a more complex and full example of what you can do with Dolt

\`\`\`bash
dolt clone <repository>
dolt checkout -b new_branch
dolt table import -u table_name table.csv
dolt commit -m "Added a new table"
dolt push origin new_branch
\`\`\`
