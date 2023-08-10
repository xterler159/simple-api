import click


from simple_api.api.app import Application


@click.group()
def cli():
    pass


@click.command()
@click.option("--port", default=8100)
def start(port):
    PORT = int(port)
    click.echo("Starting the development server...")

    app = Application(port=PORT)
    app.start()


cli.add_command(start)
