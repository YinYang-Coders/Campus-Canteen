import os
from flask import Flask, render_template, g, session, url_for, request
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

app = Flask(__name__)

#CONFIG
class ConfigClass(object):
    # Flask settings
    SECRET_KEY =              os.getenv('SECRET_KEY',       'THIS IS AN INSECURE SECRET')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL',     'sqlite:///basic_app.sqlite')
    CSRF_ENABLED = True

    # Flask-Mail settings
    MAIL_USERNAME =           os.getenv('MAIL_USERNAME',        'vortexhackathon@outlook.com')
    MAIL_PASSWORD =           os.getenv('MAIL_PASSWORD',        'ABC@123456')
    MAIL_DEFAULT_SENDER =     os.getenv('MAIL_DEFAULT_SENDER',  '"Campus Canteen" <vortexhackathon@outlook.com>')
    MAIL_SERVER =             os.getenv('MAIL_SERVER',          'smtp.live.com')
    MAIL_PORT =           int(os.getenv('MAIL_PORT',            '25'))
    MAIL_USE_SSL =        int(os.getenv('MAIL_USE_SSL',         True))

    # Flask-User settings
    USER_APP_NAME        = "Campus Canteen"                # Used by email templates




@app.route('/')
@app.route('/login')
@login_required
def login_page():
	return('login.html', title = 'Sign In')