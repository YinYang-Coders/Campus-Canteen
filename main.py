import os
import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, request, g


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
db.commit()

@app.route('/')
@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/register')
def register():
	return render_template('register.html')

if __name__ == '__main__':
	app.run(debug = True)