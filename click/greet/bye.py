import click


@click.command()
@click.argument('name')
def bye(name):
    """Say bye"""
    print(f'Bye {name}')
