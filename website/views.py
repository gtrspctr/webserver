from flask import Blueprint, render_template, request, jsonify, redirect, url_for, Response
from sqlalchemy.sql import func
from datetime import datetime
from .models import RemoteRequest
from .external_requests import lookup_geoip
from . import db

views = Blueprint("views", __name__)

# Index
# When a request is made here, it looks up and stores
# the request information
@views.route("/")
def home():
    request_ip = request.remote_addr
    request_geoip = lookup_geoip(request_ip)
    request_method = request.method
    request_agent = request.user_agent
    new_request = RemoteRequest(ip=str(request_ip),
                                isp=str(request_geoip["isp"]),
                                city=str(request_geoip["city"]),
                                country=str(request_geoip["country"]),
                                method=str(request_method),
                                agent=str(request_agent),
                                created_at=func.now())
    db.session.add(new_request)
    db.session.commit()
    
    return render_template("index.html")

# Page that displays the data in the db
@views.route("/request_log")
def score():
    return render_template("request_log.html")

# Swagger API documentation
@views.route("/apidocs")
def api_docs():
    return render_template("swaggerui.html")

# Queries all data in the db and displays in plain old json format
@views.route("/json")
def get_json():
    ids = RemoteRequest.query.all()
    data = []
    for id in ids:
        data.append(id.serialize())
    return jsonify(data)
