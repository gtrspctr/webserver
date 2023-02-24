from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    #return render_template("index.html")
    return "<h1>TEST</h1>"

@views.route("/")
@views.route("/<first>")
@views.route("/<first>/<path:rest>")
def unknown(first=None, rest=None):
    return render_template("unknown.html")

"""
@views.route("/profile")
def profile():
    args = request.args
    name = args.get("name")
    return render_template("index.html", name=name)

@views.route("/json")
def get_json():
    return jsonify({"name":"Bob", "age": "75"})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-home")
def go_home():
    return redirect(url_for("views.home"))
"""