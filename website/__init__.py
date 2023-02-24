from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "alfjasghowrbn489h34g498h9*&H34glk%*Yg4"

    return app