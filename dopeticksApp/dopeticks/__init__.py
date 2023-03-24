from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app = Flask(__name__)

# Set a secret key to prevent against modifying cookies and XSS requests on forms
app.config['SECRET_KEY'] = '16de15a4bf6314e0badd358db742206261ccee1b5222fb8e'
# format for the URI is postgresql://{user}:{password}@{RDS endpoint}/{db name, default is postgres}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresmaster:1NewPass!@dopeticks-db-v02.chcal2ivuvcc.us-west-2.rds.amazonaws.com:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()
bcrypt = Bcrypt(app)
loginManager = LoginManager(app)
loginManager.login_view = 'login'			# Flask function that brings user back to login page if they haven't logged in
loginManager.login_message_category = 'info'		# Makes pretty - Assigns Bootstraps' "info" category styling to login-related messages

from dopeticks import routes

