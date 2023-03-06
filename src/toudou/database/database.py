from sqlalchemy import *

import toudou.models.models as model

engine = create_engine("sqlite:///src/toudou/database/todo.db", echo=False)
metadata_obj = MetaData()

todo_table = Table (
    "todos",
    metadata_obj,
    Column("id", Integer, primary_key=True),
    Column("task", String(1000), nullable=False),
    Column("complete", Boolean, nullable=False),
    Column("due", DateTime, nullable=True)
)

def init() -> None:
    metadata_obj.create_all(engine)

def save(todo) -> None:
    stmt = insert(todo_table).values(
        task=todo.task,
        complete=todo.complete,
        due=todo.due
    )

    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

def read(read=None):
    if(read==None):
        stmt = select(todo_table)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return result.all()
    else:
        stmt = select(todo_table).where(todo_table.c.id == read)
        with engine.connect() as conn:
            result = conn.execute(stmt)
            return result.all()

def remove(task: int) -> None:
    stmt = (
            delete(todo_table).
            where(todo_table.c.id == task)
            )
    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()

def update_todo(todo) -> None:
    print(todo)
    stmt = (
        update(todo_table).
        where(todo_table.c.id == todo.id).
        values(
            task=todo.task,
            complete=todo.complete,
            due=todo.due  
            )
        )

    with engine.connect() as conn:
        result = conn.execute(stmt)
        conn.commit()