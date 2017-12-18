def add_subcommand_hello(subparsers):
    parser = subparsers.add_parser('hello')
    parser.set_defaults(func=hello)


def hello(args):
    print('hello', args)
