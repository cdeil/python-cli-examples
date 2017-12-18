import logging
import argparse

log = logging.getLogger(__name__)


def main(args=None):

    parser = argparse.ArgumentParser(prog='greet', description='I can say hello and bye!')
    parser.add_argument(
        '--loglevel', default='info', help='Log level',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
    )
    subparsers = parser.add_subparsers(help='Sub-commands')

    from .hello import add_subcommand_hello
    add_subcommand_hello(subparsers)

    from .bye import add_subcommand_bye
    add_subcommand_bye(subparsers)

    # Parse all command line arguments
    args = parser.parse_args(args)

    # Call the desired subcommand function
    args.func(args)
    # print(args)
    print('this is main')

    logging.basicConfig(level=args.loglevel.upper())

    log.debug('some debug')
    log.info('some info')
    log.warning('some warning')

    return 0
