import click
import io

from datetime import datetime

import toudou.models.models as models
import toudou.services.services as services


@click.group()
def cli():
    pass


@cli.command()
def init_db():
    models.init_db()


@cli.command()
@click.option("-t", "--task", prompt="Your task", help="The task to remember.")
@click.option("-d", "--due", type=click.DateTime(), default=None, help="Due date of the task.")
def create(task: str, due: datetime):
    models.create_todo(task, due=due)

@cli.command()
@click.argument('csv_file', type=click.File('r'))
def import_csv(csv_file: io.TextIOWrapper):
    services.import_from_csv(csv_file.read())

@cli.command()
def export_csv():
    services.export_to_csv()

@cli.command()
@click.option("--id", required=True, type=click.INT, help="Todo's id.")
def get(id: int):
    click.echo(models.get_todo(id))

@cli.command()
def get_all():
    click.echo(models.get_todos())


@cli.command()
@click.option("--id", required=True, type=click.INT, help="Todo's id.")
@click.option("-c", "--complete", required=True, type=click.BOOL, help="Todo completed")
@click.option("-t", "--task", prompt="Your task", help="The task to remember.")
@click.option("-d", "--due", type=click.DateTime(), default=None, help="Due date of the task.")
def update(id: int, complete: bool, task: str, due: datetime):
    models.update_todo(id, task, complete, due)


@cli.command()
@click.option("--id", required=True, type=click.INT, help="Todo's task.")
def delete(id: int):
    models.delete_todo(id)
