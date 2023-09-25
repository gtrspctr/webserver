from . import db
from .models import RemoteRequest
from .external_requests import lookup_geoip
from flask_restful import Resource, reqparse
from flask import request
from sqlalchemy.sql import func

class RemoteRequests(Resource):
    def submit_info(self):
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

    def get(self, req_id=None):
        # GET: query resource

        # Check if specific ID was requested
        if req_id:
            # ID was requested. Query db for that ID.
            id = RemoteRequest.query.get(req_id)

            # Check if requested ID exists
            if id:
                # ID exists. Return serialized data.
                return id.serialize(), 200
            else:
                # ID does not exist. Return message saying so.
                return {"message": "Requested ID not found in database."}, 404
        # Specific ID was not requested. Return all data.
        else:
            ids = RemoteRequest.query.all()
            return [id.serialize() for id in ids], 201

    def post(self):
        # POST: create resource

        # Create parser that verifies submitted data
        parser = reqparse.RequestParser()
        parser.add_argument("ip", type=str, required=True, help="Enter IP as a string.")
        parser.add_argument("isp", type=str, required=True, help="Enter ISP as a string.")
        parser.add_argument("city", type=str, required=True, help="Enter city as a string.")
        parser.add_argument("country", type=str, required=True, help="Enter country as a string.")
        parser.add_argument("method", type=str, required=True, help="Enter method as a string.")
        parser.add_argument("agent", type=str, required=True, help="Enter agent as a string.")
        args = parser.parse_args()

        # Submit new request data to database
        self.submit_info()

        # Submit POST request to database
        new_entry = RemoteRequest(
            ip=args["ip"],
            isp=args["isp"],
            city=args["city"],
            country=args["country"],
            method=args["method"],
            agent=args["agent"],
            created_at=func.now())
        db.session.add(new_entry)
        db.session.commit()

        return {"message": str("New IP created: " + args["ip"])}, 201
        
    def put(self, req_id):
        # PUT: replace resource

        # Check if ID exists in db
        id = RemoteRequest.query.get(req_id)
        if id:
            # ID exists. Parse data.
            parser = reqparse.RequestParser()
            parser.add_argument("ip", type=str, required=False, help="Enter IP as a string.")
            parser.add_argument("isp", type=str, required=False, help="Enter ISP as a string.")
            parser.add_argument("city", type=str, required=False, help="Enter city as a string.")
            parser.add_argument("country", type=str, required=False, help="Enter country as a string.")
            parser.add_argument("method", type=str, required=False, help="Enter method as a string.")
            parser.add_argument("agent", type=str, required=False, help="Enter agent as a string.")
            args = parser.parse_args()

            # Submit new request data to database
            self.submit_info()

            # Commit to db
            if args.get("ip"):
                id.ip = args["ip"]
            if args.get("isp"):
                id.isp = args["isp"]
            if args.get("city"):
                id.city = args["city"]
            if args.get("country"):
                id.country = args["country"]
            if args.get("method"):
                id.method = args["method"]
            if args.get("agent"):
                id.agent = args["agent"]
            id.created_at = func.now()
            db.session.commit()

            return {"message": "Fields replaced on ID: " + str(req_id)}, 200
        else:
            return {"message": "Requested ID not found in database."}, 404

    def patch(self, req_id):
        # PATCH: update resource

        # Check if ID exists in db
        id = RemoteRequest.query.get(req_id)
        if id:
            # ID exists. Parse data.
            parser = reqparse.RequestParser()
            parser.add_argument("ip", type=str, required=False, help="Enter IP as a string.")
            parser.add_argument("isp", type=str, required=False, help="Enter ISP as a string.")
            parser.add_argument("city", type=str, required=False, help="Enter city as a string.")
            parser.add_argument("country", type=str, required=False, help="Enter country as a string.")
            parser.add_argument("method", type=str, required=False, help="Enter method as a string.")
            parser.add_argument("agent", type=str, required=False, help="Enter agent as a string.")
            args = parser.parse_args()

            # Submit new request data to database
            self.submit_info()

            # Commit to db
            if args.get("ip"):
                id.ip = args["ip"]
            if args.get("isp"):
                id.isp = args["isp"]
            if args.get("city"):
                id.city = args["city"]
            if args.get("country"):
                id.country = args["country"]
            if args.get("method"):
                id.method = args["method"]
            if args.get("agent"):
                id.agent = args["agent"]
            id.created_at = func.now()
            db.session.commit()

            return {"message": "Fields updated on ID: " + str(req_id)}, 200
        else:
            return {"message": "Requested ID not found in database."}, 404

    def delete(self, req_id):
        # DELETE: delete resource

        # Submit new request data to database
        #self.submit_info()

        # Check if ID exists in db        
        id = RemoteRequest.query.get(req_id)
        if id:
            # ID exists. Delete data.
            db.session.delete(id)
            db.session.commit()
            return {"message": "ID " + str(req_id) + " deleted."}, 200
        else:
            return {"message": "Requested ID not found in database."}, 404