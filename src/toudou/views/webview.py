from flask import Flask, render_template, redirect, request, send_file

import toudou.database.database as database
import toudou.models.models as model
import toudou.services.services as services
import datetime as dt
import os

from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view')
def view():
    return render_template('view.html', todos=database.read())

@app.route('/view/delete/<id>')
def delete(id=None):
    database.remove(id)
    return redirect('/view')

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['input_name']
        completed = False
        due = request.form['input_date']
        try:
            model.create_todo(name, complete=completed, due=datetime.strptime(due, '%Y-%m-%d'))
        except ValueError:
            model.create_todo(name, complete=completed)
        # Ajouter le nouveau todo à la base de données ici
        return redirect('/view')
    else:
        return render_template('add.html', datetime=datetime.now())

@app.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id=None):
    if request.method == 'POST':
        name = request.form['input_name']
        if 'completed' in request.form:
            completed = True
        else:
            completed = False
        due = request.form['input_date']
        try:
            model.update_todo(id, name, complete=completed, due=datetime.strptime(due, '%Y-%m-%d'))
        except ValueError:
            model.update_todo(id, name, complete=completed)
        return redirect('/view')
    else:
        if(id==None):
            return redirect('/view')
        else:
            return render_template('edit.html', todo=database.read(id), datetime=datetime.now())

@app.route('/download-csv')
def download_csv():
    today = dt.date.today()
    filename = f"{today.strftime('%Y-%m-%d')}.csv"
    services.export_to_csv()
    return send_file('../csv/'+filename, as_attachment=True)