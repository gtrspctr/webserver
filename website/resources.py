from flask_restful import Resource

class RemoteRequests(Resource):
    def get(self):
        # Handle request: get resource
        print("Hello!")
        
        #pass
        return {"message": "Hi!"}, 201

    def post(self):
        # Handle request: create resource
        pass

    def put(self):
        # Handle request: replace resource
        pass

    def patch(self):
        # Handle request: update resource
        pass

    def delete(self):
        # Handle request: delete resource
        pass