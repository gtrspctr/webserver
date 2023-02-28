from flask import Flask
from flask_restful import Api, Resource
from werkzeug.middleware.proxy_fix import ProxyFix

class HelloWorld(Resource):
    def get(self):
        return {"data":"HelloWorld"}
    
    def put(self):
        pass

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "alfjasghowrbn489h34g498h9*&H34glk%*Yg4"
    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
    api = Api(app)
    api.add_resource(HelloWorld, "/helloworld")

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app

