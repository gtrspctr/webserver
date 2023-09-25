from flask_restful import Api
from .resources import RemoteRequests

api = Api()
api.add_resource(RemoteRequests, "/api/requests", "/api/requests/<int:req_id>")