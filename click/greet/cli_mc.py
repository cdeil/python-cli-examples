from collections import OrderedDict
import importlib
import click

commands = OrderedDict([
    ('hello', dict(module='hello', function='hello')),
    ('bye', dict(module='bye', function='bye')),
])


class CLI(click.MultiCommand):
    def list_commands(self, ctx):
        return list(commands)

    def get_command(self, ctx, name):
        module = importlib.import_module('greet.' + commands[name]['module'])
        return getattr(module, commands[name]['function'])


cli = CLI(help='Command line interface for the greet package')

if __name__ == '__main__':
    cli()
