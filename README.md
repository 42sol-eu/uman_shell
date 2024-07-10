# README: uman-shell, providing modern shell commands
<!--used for PyPI -->

> **NOTE:**
> also see ./README.adoc[extended README]

## Motivation

Shells are still using abbreviated commands like `ls`, `cat`, `chmod` and `grep`,
which are quick to write but harder to learn.

> `uman-shell` aims to provide a wellformed, unabreviated shell syntax for the most important commands.

Scripting in the shell gets cryptic very fast and is therefore hard to maintain.

> `uman-shell` uses Python for scripting providing a more modern way of automating tasks on the shell.

Error handling on the shell is hard, especially when building pipelines and in testing scripts.

> `uman-shell` not only provides the Python debugger but also Pythons other error handling and testing capacities.

Shell automations work with the active folder (`working directory`) as a context.
In my opinion the context is harder to manager in a shell script.

> `uman-shell` provides context managers (via `with`-block) to write more concise code.

It is hard to work with configuration files, escpecially yaml and toml in bash scripts.
Often it depends on environment variables.

> `uman-shell` uses Pythons capabilities to easily utilize file configurations in automations.


## Goals


TODO: add conent to readme.md