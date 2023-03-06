import csv
import dataclasses
import io
import datetime as dt

from datetime import datetime

from toudou.models.models import create_todo, get_todos, Todo
from toudou.database.database import read

today = dt.date.today()
filename = f"{today.strftime('%Y-%m-%d')}.csv"

def export_to_csv():
    todos = read()
    with open("src/toudou/csv/"+filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Écriture de l'en-tête
        writer.writerow(['task', 'completed', 'due'])

        # Écriture des données de chaque tâche
        for todo in todos:
            writer.writerow([
                todo[1], 
                todo[2], 
                todo[3].strftime('%Y-%m-%d %H:%M:%S') if todo[3] else ''
            ])

def import_from_csv(data: str) -> None:
    with io.StringIO(data) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        for row in csv_reader:
            #print(bool(str(row["completed"])))
            create_todo(task=row["task"],due=datetime.fromisoformat(row["due"]) if row["due"] else None,complete = True if row["completed"].strip().lower() == "true" else False)
