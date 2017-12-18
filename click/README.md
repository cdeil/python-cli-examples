# cli with click


Using `click.group`, that doesn't allow lazy-loading:

    python -m greet.cli

* http://click.pocoo.org/dev/quickstart/#nesting-commands
* https://github.com/pallets/click/tree/master/examples/repo

Using `click.MultiCommand`:

    python -m greet.cli_mc

* http://click.pocoo.org/dev/commands/#custom-multi-commands
* https://github.com/pallets/click/tree/master/examples/complex

The way this is implemented at the moment, this doesn't do lazy loading!

Maybe try this? https://github.com/click-contrib/click-plugins

For testing see:

* http://click.pocoo.org/dev/testing/

For Sphinx see:

* https://github.com/click-contrib/sphinx-click

