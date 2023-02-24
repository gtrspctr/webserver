#!/usr/bin/env python

"""
from flask import Flask
from website.views import views
from website import create_app
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)
app.register_blueprint(views, url_prefix="/")

# Routes
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
"""

from website import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)