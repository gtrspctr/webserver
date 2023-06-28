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

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video ID does not exist in database.")
        return result
    
    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video ID already exists in database.")
        video = VideoModel(
            id=video_id,
            name=args["name"],
            views=args["views"],
            likes=args["likes"]
        )
        db.session.add(video)
        db.session.commit()
        return video, 201
    
    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_patch_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video ID does not exist. Unable to PATCH.")
        
        if args["name"]:
            result.name = args["name"]
        if args["views"]:
            result.views = args["views"]
        if args["likes"]:
            result.likes = args["likes"]

        db.session.commit()
        return result
    
    def delete(self, video_id):
        abort_if_video_id_not_in_videos(video_id)
        del videos[video_id]
        return video, 201

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
#app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
#db = SQLAlchemy(app)

"""
class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={name}, views={views}, likes={likes})"
"""
#with app.app_context():
#    db.create_all()

# Run webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)