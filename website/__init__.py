from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from os import path

# Create and define database
db = SQLAlchemy()
db_name = "database.db"

current_dir = path.dirname(__file__)
parent_dir = path.dirname(current_dir)
db_dir = path.join(parent_dir, "instance")
db_path = path.join(db_dir, db_name)

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "alfjasghowrbn489h34g498h9*&H34glk%*Yg4"
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}'.format(db_path)
    app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    db.init_app(app)

    # Import and register blueprints
    from .views import views

    app.register_blueprint(views, url_prefix="/")

    # Import and register database
    from .models import RemoteRequest
    with app.app_context():
        db.create_all()
    
    # Import and register API
    from .api import api
    api.init_app(app)

    return app