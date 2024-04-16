from flask import Flask
from flask_moment import Moment
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from os import path
from .config import *

# Create and define database
db = SQLAlchemy()
db_name = "database.db"

# Define filepaths
current_dir = path.dirname(__file__)
parent_dir = path.dirname(current_dir)
static_dir = path.join(current_dir, 'static')
db_dir = path.join(parent_dir, "instance")
db_path = path.join(db_dir, db_name)
swagger_dir = path.join(static_dir, "swagger")
swagger_path = path.join(swagger_dir, "swagger.json")

# Create application
def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = config.SECRET_KEY                                            # Secret key for session cookies
    app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI.format(db_path)  # Location/type of db
    app.config["DEBUG"] = config.DEBUG                                                      # Debug mode on for dev, off for prod
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)         # Used to interpret data from the proxy (Nginx in this case)
    db.init_app(app)
    moment = Moment(app)

    # Import and register webpage blueprints
    from .views import views
    app.register_blueprint(views, url_prefix="/")

    # Import and register database
    from .models import RemoteRequest
    with app.app_context():
        db.create_all()     # Only creates db if it doesn't already exist
    
    # Import and register API
    from .api import api
    api.init_app(app)

    return app