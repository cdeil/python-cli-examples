import sys
from cliff.app import App
from cliff.command import Command
from cliff.commandmanager import CommandManager


class Hello(Command):
    """Say hello"""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument('name')
        return parser

    def take_action(self, args):
        print('Hello {}'.format(args.name))


class Bye(Command):
    """Say bye"""

    def get_parser(self, prog_name):
        parser = super().get_parser(prog_name)
        parser.add_argument('name')
        return parser

    def take_action(self, args):
        print('Bye {}'.format(args.name))


# Here we create a CommandManager and App directly
# To customize the CLI you have to sub-class those!

command_manager = CommandManager('greet')
command_manager.add_command('hello', Hello)
command_manager.add_command('bye', Bye)

app = App(
    description='Twitter command line application',
    version='0.1',
    command_manager=command_manager,
)

# Application needs to be run with command line to parse.
if __name__ == '__main__':
    app = App(
        description='Command line interface for the greet package',
        version='0.1',
        command_manager=command_manager,
    )
    sys.exit(app.run(sys.argv[1:]))
