from flask_restful import Api
from .resources import RemoteRequests

# Initialize the API and give it an endpoint
api = Api()
api.add_resource(RemoteRequests, "/api/requests", "/api/requests/<int:req_id>")