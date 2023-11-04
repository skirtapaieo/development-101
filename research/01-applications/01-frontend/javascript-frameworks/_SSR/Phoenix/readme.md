# Phoenix

http://www.phoenixframework.org

## How it started

Phoenix was created by Chris McCord, a software developer with experience in Ruby and Ruby on Rails.

The framework was initially released in 2014. McCord wanted to bring the ease and productivity of Ruby on Rails into a system that could handle a much higher volume of connections with lower latency.

This led him to the Elixir programming language, which runs on the Erlang virtual machine (BEAM). BEAM is known for its real-time capabilities, fault-tolerance, and ability to handle a large number of simultaneous connections efficiently.

## Why Phoenix was created?

- Scalability and performance
- Real-time features
- Productivity
- Fault-tolerande/hot code swapping
- Rich ecosystem

## Who uses what?

Some well-known companies that are known to be using Elixir, Erlang, or Phoenix.

While these companies have used these technologies, the scope and context of their use can vary. It may be for a specific service, for high-demand systems, or for newer services that are being tested for scalability and performance.

### Elixir

1. **Pinterest**: Uses Elixir for its notification system to handle millions of events per day.
2. **Adobe**: Utilizes Elixir in the Adobe Experience Manager as a Cloud Service.
3. **Slack**: Utilizes Elixir to handle a large number of concurrent users and operations.
4. **Financial Times**: Uses Elixir for its recommendation engine.

### Erlang

1. **Ericsson**: Erlang was originally developed here, and it continues to be used in many telecommunication solutions.
2. **WhatsApp**: Built its messaging back end with Erlang to handle millions of simultaneous connections.
3. **T-Mobile**: Uses Erlang in their SMS and authentication systems.
4. **Amazon**: Amazon SimpleDB, a distributed database, has components written in Erlang.

### Phoenix (Elixir-based)

1. **Bleacher Report**: Used Phoenix to improve performance while reducing server costs significantly.
2. **Poki**: An online gaming platform that moved to Phoenix to handle millions of users.
3. **Podium**: Uses Phoenix for handling real-time features in its business messaging platform.

## Overview of the Phoenix stack

- Phoenix is the web framework - routing, controllers, views, templates, channels for real-time communication
- Elixir - programming language that Elixir is written in (runs on Erland VM, BEAM)
- BEAM - Bogdan, Björns, Erlang, Abstract, Machine, a virtual machine.
- Ecto - database wrapper and query generator used in Phoenix (includes DSL for queries)
- Mix - build tool for project creation, compilation, testing, custom tasks
- Hex - package manager in Erland ecosystem, default pm for Elixir
- Plug - a specification for composable modules, used in phoenix for creatin middleware
- Brunch/Webpack - build engines
- Cowboy - HTTP server
- Channels - allows real-time communication between client and server, often over WebSockets
- Telemetry - observability library, used to gather performance and event-data, for debugging/monitoring
- Surface - Allowing to build interactive and real-time user interface declaratively
