#organisational
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask (__name__)

#####################
## Database Setup ###
#####################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

#####################

#####################
## Login Configs  ###
#####################
login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users.login' #users blueprint will have a view login


from companyblog.core.views import core
from companyblog.error_pages.handlers import error_pages
from companyblog.users.views import users

app.register_blueprint(core)
app.register_blueprint(error_pages)
app.register_blueprint(users)