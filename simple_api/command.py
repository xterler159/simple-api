import click
import uvicorn


@click.group()
def cli():
    pass


@click.command()
@click.option("--port", default=8100)
def start(port):
    PORT = int(port)
    app_entry_point = "simple_api.api.application:create_app"

    click.echo("Starting the development server...")
    uvicorn.run(app=app_entry_point, port=PORT, reload=True)


cli.add_command(start)
