import os
import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, request, g
from wtforms import Form, BooleanField, StringField, validators
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form

app = Flask(__name__)
db = SQLAlchemy(app)

#CONFIG
CSRF_ENABLED = True
SECRET_KEY = 'secret'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), index = True, unique = True)
    password = db.Column(db.String(64), index = True)

#Forms
class RegistrationForm(Form):
	username = StringField('Username', [validators.InputRequired()])
	password = StringField('Password', [validators.InputRequired()])


@app.route('/', methods=['GET', 'POST'])
def login():
	return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled = False)
    if form.validate_on_submit():
        return redirect('/hello')
    return render_template('registerform.html', title = 'Sign Up', form = form)

@app.route('/hello')
def hello():
    return "Welcome to Campus Canteen"

if __name__ == '__main__':
	app.run(debug = True)