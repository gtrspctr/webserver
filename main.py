#!/usr/bin/env python
#from flask import request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from website import create_app
import json

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required.", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required.", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required.", required=True)

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.get(id=video_id)
        return result
    
    def put(self, video_id):
        abort_if_video_id_in_videos(video_id)
        args = video_put_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201
    
    def delete(self, video_id):
        abort_if_video_id_not_in_videos(video_id)
        del videos[video_id]
        return "Deleted " + str(video_id), 204

"""
with open("./users_data", "r") as infile:
    infile.read()
    users = json.loads(infile)

names = {"al": {"first_name": "Al",
                "last_name": "Robison",
                "age": 33,
                "gender": "male"},
         "juan": {"first_name": "Juan",
                  "last_name": "Gomez",
                  "age": 30,
                  "gender": "male"}}
"""

# Initialize webserver application
app = create_app()

# Create API
api = Api(app)
api.add_resource(Video, "/video/<int:video_id>")

# Create Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"

# Run webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)