# Phoenix

# Introduction

We have this little stack of technologies:

- Erlang (needs installation, with Scoop or Chocolatey, like ver 26)
- Elixir (like 1.15)

## Erlang

Programming lanugage used to build massively scalable, fault-tolerant systems.
Originally developed by Ericsson, for telco, but used broadly today.

- Concurrency model - actor model, with lightweight processes communicating through message passing
- Fault-tolerance - has a let it crash philosophy, with supervisor that can restart processes when they fail, ensuring system robustness
- BEAM - the virtual machine, optimized for running concurrent and distributed systems

## Elixir

A functional, concurrent, general purpose language that runs on BEAM

- Ruby-like syntax
- Designed for building scalable and maintainable applications
- Comes with great tools that helps create, manage and test applications

## Phoenix Framework

Is a web framework built on Elixir

- Often compared to Ruby on Rails, but offers better concurrency/efficiency
- Provides: routing, views, controllers, and database integration
- With channels it provides a way to add real-time functionality to applications

## Phoenix LiveWire

A Feature in Phoenix Framework that enables rich, real-time experiences with server-rendered HTML.
You can build interactive real-time application, without a lot of JavaScript.
