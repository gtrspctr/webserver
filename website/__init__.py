from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix
from flask_sqlalchemy import SQLAlchemy
from os import path

"""
class HelloWorld(Resource):
    def get(self, name, age):
        return {"name":name,"age":age}
    
    def post(self):
        return "Hello!"
"""
db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "alfjasghowrbn489h34g498h9*&H34glk%*Yg4"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    db.init_app(app)

    """
    # API
    api = Api(app)
    api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:age>")
    """

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    #from .models import User, Note
    #create_database(app)

    return app


def create_database(app):
    if not path.exists('website/' + DB_NAME):
        print(path)
        db.create_all(app)
        print("Created database.")
