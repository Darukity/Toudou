import os
import pickle
import uuid

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

import toudou.database.database as database


@dataclass
class Todo:
    id: int
    task: str
    complete: bool
    due: Optional[datetime]


def init_db() -> None:
    database.init()


def create_todo(task: str,complete: bool = False,due: Optional[datetime] = None) -> None:
    todo = Todo(uuid.uuid4().int, task=task, complete=complete, due=due)
    database.save(todo)


def get_todo(id: int) -> Todo:
    return database.read(id)


def get_todos() -> list[Todo]:
    return database.read()


def update_todo(id: int,task: str,complete: bool,due: Optional[datetime]=None) -> None:
    if get_todo(id):
        todo = Todo(id, task=task, complete=complete, due=due)
        database.update_todo(todo)


def delete_todo(id: int) -> None:
    database.remove(id)