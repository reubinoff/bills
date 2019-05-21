from flask_restful import Resource

from .. import api


class Users(Resource):
    def get(self):
        return {"moshe": "reubinoff"}


api.add_resource(Users, '/users')


# https://flask-restful.readthedocs.io/en/latest/quickstart.html
