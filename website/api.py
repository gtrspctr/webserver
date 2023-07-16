from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from .resources import RemoteRequests

api = Api()

api.add_resource(RemoteRequests, "/api/requests", "/api/requests/<int:id>")