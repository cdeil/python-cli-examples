import click


@click.group()
def cli():
    """Command line interface for the greet package"""
    pass


from .hello import hello
cli.add_command(hello)

from .bye import bye
cli.add_command(bye)

if __name__ == '__main__':
    cli()
