import os
from flask import Flask, render_template, g, session, url_for, request
from flask.ext.mail import Mail
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.user import login_required, UserManager, UserMixin, SQLAlchemyAdapter

app = Flask(__name__)

@app.route('/')
def Hello():
	return "Hello World"

if __name__ == '__main__':
	app.run(debug = True)