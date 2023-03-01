#!/usr/bin/env python
#from flask import request
from flask_restful import Api, Resource, reqparse, abort
from website import create_app
import json

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required.", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video is required.", required=True)
video_put_args.add_argument("likes", type=int, help="Likes of the video is required.", required=True)

videos = {}

def abort_if_video_id_not_in_videos(video_id):
    if video_id not in videos:
        abort(404, message="Video ID is not valid.")

def abort_if_video_id_in_videos(video_id):
    if video_id in videos:
        abort(409, message="Video already exists with that ID.")

class Video(Resource):
    def get(self, video_id):
        abort_if_video_id_not_in_videos(video_id)
        return videos[video_id]
    
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

# Run webserver
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)