import click


@click.command()
@click.argument('name')
def hello(name):
    """Say hello"""
    print(f'Hello {name}')
