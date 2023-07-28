import click
from simple_api.api.app import Application


@click.group()
def cli():
    pass


@click.command()
def run():
    click.echo("Starting the development server...")
    app = Application(port=8000)
    app.start()


cli.add_command(run)
