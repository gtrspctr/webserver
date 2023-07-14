#!/usr/bin/env python
#from flask import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from website import create_app
import json
from os import path

# Define directory
current_dir = path.dirname(__file__)
db_dir = path.join(current_dir, "database")
db_path = path.join(db_dir, "database.db")
db_uri = "sqlite:///{}".format(db_path)

# Request parser for PUT method
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required.", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required.", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required.", required=True)

# Request parser for PATCH method
video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str, help="Name of the video is required.")
video_patch_args.add_argument("views", type=int, help="Views of the video is required.")
video_patch_args.add_argument("likes", type=int, help="Likes of the video is required.")

# Initialize webserver application
app = create_app()

# Create API
#api = Api(app)
#api.add_resource(Video, "/video/<int:video_id>")

# Run webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)