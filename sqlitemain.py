import os
import sqlite3
from flask import Flask, render_template, flash, redirect, url_for, request, g
from wtforms import Form, BooleanField, StringField, validators, PasswordField
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form

app = Flask(__name__)
db = SQLAlchemy(app)

#CONFIG
CSRF_ENABLED = True
SECRET_KEY = 'something secret'
SESSION_TYPE = 'filesystem'
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app1.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#Model
db = sqlite3.connect('app.db')
print "opened database successfully";
cur = db.cursor()
cur.execute('''DROP TABLE user''')
cur.execute('''CREATE TABLE user(id INTEGER PRIMARY KEY, name TEXT, password TEXT)''')
db.commit()

#Forms
class RegistrationForm(Form):
	username = StringField('Username', [validators.InputRequired()])
	password = PasswordField('New Password', [validators.InputRequired()])

class SignInForm(Form):
    username = StringField('Username', [validators.InputRequired()])
    password = PasswordField('New Password', [validators.InputRequired()])

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        with sqlite3.connect('app.db') as con:
            cur = con.cursor()
            cur.execute("""SELECT name FROM user where name='self.username.data'""")
            check = cur.fetchone()
        if check is None:
            self.username.errors.append('Unknown Username')
            return False

        if not check.check_password(self.password.data):
            self.password.errors.append('Invalid Password')
            return False

        self.check = check
        return True           



@app.route('/', methods=['GET', 'POST'])
def login():
    form = SignInForm(csrf_enabled = False)
    if request.method == 'POST' and form.validate():
        return redirect(url_for('hello'))
    return render_template("loginform.html", title = 'Sign In', form=form)    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(csrf_enabled = False)
    if request.method == 'POST' and form.validate():
        with sqlite3.connect('app.db') as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user (name, password) VALUES (?,?)",(form.username.data, form.password.data))
            con.commit()
        return redirect(url_for('hello'))
    return render_template('registerform.html', title = 'Sign Up', form = form)

@app.route('/hello')
def hello():
    return "Welcome to Campus Canteen"

if __name__ == '__main__':
	app.run(debug = True)