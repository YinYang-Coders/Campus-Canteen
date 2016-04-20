import os
import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, request, g
from wtforms import Form, BooleanField, StringField, validators

app = Flask(__name__)

#CONFIG
CSRF_ENABLED = True
SECRET_KEY = 'secret'

#Model
db = sqlite3.connect('mydb')
cursor = db.cursor()
cursor.execute('''DROP TABLE users''')
cursor.execute('''
	CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
						password TEXT)
''')

#Forms
class RegistrationForm(Form):
	username = StringField('Username', [validators.InputRequired()])
	password = StringField('Password', [validators.InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def login():
	return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
	app.run(debug = True)