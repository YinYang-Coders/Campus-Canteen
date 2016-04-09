import os
from flask.ext.wtf import Form
from flask import Flask, render_template, g, session, url_for, request, render_template_string
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import StringField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask.ext.login import login_user, logout_user, current_user, \
    login_required

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
db = SQLAlchemy(app)

#CONFIG
CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#FORMS
class LoginForm(Form):
    user_name = StringField('user_name', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])

#DATABASE
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(64), index=True, unique=True)
	password = StringField(db.String(64), index=True)




@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = LoginForm()
	return render_template("login.html")

# Start development web server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)