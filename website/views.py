from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint("views", __name__)

@views.route("/")
def home():
    request_ip = request.remote_addr
    request_method = request.method
    request_agent = request.user_agent
    #request_browser = ""
    #request_os = ""
    #if "curl" not in str(request_agent):
    #    request_browser = request.headers["Sec-Ch-Ua"]
    #    request_os = request.headers["Sec-Ch-Ua-Platform"]
    print("Remote IP: " + str(request_ip))
    print("Remote Method: " + str(request_method))
    print("Remote Agent: " + str(request_agent))
    print()
    #if len(request_browser) > 0:
    #    print("Remote Browser: " + str(request_browser))
    #if len(request_os) > 0:
    #    print("Remote OS: " + str(request_os))
    return render_template("index.html")

@views.route("/scoreboard")
def score():
    return render_template("scoreboard.html")

#@views.route("/")
#@views.route("/<first>")
#@views.route("/<first>/<path:rest>")
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