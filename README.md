# python-cli-examples

Examples exploring Python command line interface (CLI) packages.

## What I want

This is not a complete overview of ways to create CLIs in Python,
just something rather specific.

Here's what I want:

* A single command line tool, lots of sub-commands.
  Like `git` which has subcommands `git status`, `git commit`, ...
* The cli is part of a Python package, exposed both via a
  setuptools entry point and `__main__.py`, i.e.
* Just calling the main cli should print some help, i.e.
  a list of main cli arguments and available subcommands
  (like how `git` and `git --help` print the same thing).
* Code organisation: ideally the code for each sub-command can be
  a separate Python file. Having "lazy loading", i.e. import only
  for the subcommand that is executed, would be nice, but is not
  a hard requirement.
* Logging should be handled once only on the main command, avoid
  repetitive and boilerplate code on subcommands.
* It should be easy to write tests for each command,
  including asserts on return code, stdout and stdin
* It should be possible to get a list of available subcommands,
  as well as the arguments for a given command, without actually
  executing the command. Without any actual argument parsing or
  command execution occurring.
*
* CLI documentation generation as part of Sphinx docs

I do not need:

* A plugin mechanism where users or other packages can add or
  extend commands in my package.
* Passing arguments for the main command to the subcommands.
* An interactive way to prompt for arguments, like the FTOOLs do.
  (although this could probably be implemented nicely using

## Contents

As an example, we'll create a simple cli called `greet` in a package
called `greet` that has two subcommands: `hello` and `bye`, using
the following Python cli packages:

* https://docs.python.org/3/library/argparse.html
  * This is the Python std library solution. Used e.g. by `conda`.
* http://click.pocoo.org/dev/
  * From Arnim Ronacher. Used e.g. by Flask (see http://flask.pocoo.org/docs/dev/cli/)
  * The front page says "arbitrary nesting of commands" and "supports lazy loading of subcommands at runtime"
    which is what we want here, and what is hard with argparse.
* https://docs.openstack.org/cliff/latest/
  * From Dough Hellman. Used by OpenStack.
* http://traitlets.readthedocs.io/en/stable/config.html#command-line-arguments
  * Used by ipython for configuration and cli
  * Also used by ctapipe (see https://cta-observatory.github.io/ctapipe/api/ctapipe.core.Tool.html
    and https://cta-observatory.github.io/ctapipe/core/index.html), and this investigation
    is for what to use for http://gammapy.org/ and we want to collaborate with ctapipe.

## References

* https://github.com/gammapy/gammapy/pull/1235

## Testing

To test, we suggest you use a virtual environment for each of the solutions presented here.
For example to work on the one in the `argparse` folder:

    cd argparse
    python -m venv venv
    . venv/bin/activate
    python -m pip install -e .
    greet --help
    python -m greet --help
    python -m pytest -v
