import os
from flask.ext.wtf import Form
from flask import Flask, render_template, g, session, url_for, request, render_template_string
from flask.ext.mail import Mail
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from wtforms import StringField, BooleanField, TextAreaField, PasswordField, validators
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

class RegisterForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

#DATABASE
class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_name = db.Column(db.String(64), index=True, unique=True)
	password = StringField(db.String(64), index=True)

db.create_all()



@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_page():
	form = LoginForm(csrf_enabled = False)
	return render_template("login.html")

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(csrf_enabled = False)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

# Start development web server
if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)