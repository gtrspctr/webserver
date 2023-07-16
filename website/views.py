from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Response
from .models import RemoteRequest
from . import db

views = Blueprint("views", __name__)

@views.route("/")
def home():
    request_ip = request.remote_addr
    request_method = request.method
    request_agent = request.user_agent
    new_request = RemoteRequest(ip=str(request_ip),
                                method=str(request_method),
                                agent=str(request_agent))
    db.session.add(new_request)
    db.session.commit()
    
    return render_template("index.html")

@views.route("/scoreboard")
def score():
    return render_template("scoreboard.html")

@views.route("/json")
def get_json():
    ids = RemoteRequest.query.all()
    data = []
    for id in ids:
        data.append(id.serialize())
    return jsonify(data)