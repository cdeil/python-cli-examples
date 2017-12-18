from collections import OrderedDict
import importlib
import click

# Here we're doing an explicit listing of available sub-commands.
# But we could also gather this list automatically using any collection
# method we like, e.g. grepping source code files or some registration pattern
# like e.g. class decorator or a metaclass.
commands = OrderedDict([
    ('hello', dict(module='hello', function='hello', description='Say hello')),
    ('bye', dict(module='bye', function='bye', description='Say goodbye')),
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
