import click


@click.group()
def cli():
    """I can say hello and bye!"""
    pass


from .hello import hello
cli.add_command(hello)
