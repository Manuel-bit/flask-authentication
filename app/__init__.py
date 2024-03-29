from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_name):

  app = Flask(__name__)

  #initializing configuarations
  app.config.from_object(config_options[config_name])

  #initialisisng blueprints
  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  #initialising flask extensions
  db.init_app(app)


  return app