from flask import Flask
from flask_sqlalchemy import SQLAlchemy	# Manages database sync
from flask_bcrypt import Bcrypt			# Hashes passwords so that they are secure
from flask_login import LoginManager	# Manages logins/cookies



application = Flask(__name__)

# Set a secret key to prevent against modifying cookies and XSS requests on forms
application.config['SECRET_KEY'] = '16de15a4bf6314e0badd358db742206261ccee1b5222fb8e'
# format for the URI is postgresql://{user}:{password}@{RDS endpoint}/{db name, default is postgres}
#application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresmaster:Jele2789!@dopeticks-db-v04.c5utz0tlt1mg.us-west-2.rds.amazonaws.com:5432/postgres'
# application.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresmaster:Jele2789!@dopeticks-db-v04.c5utz0tlt1mg.us-west-2.rds.amazonaws.com:5432/postgres'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)
application.app_context().push()
bcrypt = Bcrypt(application)
loginManager = LoginManager(application)
loginManager.login_view = 'users.login'			# Flask function that brings user back to login page if they haven't logged in
loginManager.login_message_category = 'info'		# Makes pretty - Assigns Bootstraps' "info" category styling to login-related messages

from dopeticks.users.routes import users
from dopeticks.tasks.routes import tasks
from dopeticks.main.routes import main


application.register_blueprint(users)
application.register_blueprint(tasks)
application.register_blueprint(main)