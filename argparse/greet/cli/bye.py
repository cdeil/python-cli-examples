def add_subcommand_bye(subparsers):
    parser = subparsers.add_parser('bye')
    parser.set_defaults(func=bye)


def bye(args):
    print('bye', args)
