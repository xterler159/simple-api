import click

from dotenv import load_dotenv, dotenv_values

from simple_api.api.app import Application

load_dotenv()


@click.group()
def cli():
    pass


@click.command()
def start():
    PORT = int(dotenv_values().get("PORT"))
    click.echo("Starting the development server...")

    app = Application(port=PORT)
    app.start()


cli.add_command(start)
