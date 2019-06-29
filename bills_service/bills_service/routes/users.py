from flask_restful import Resource
from bills_service import api
import logging


class Users(Resource):
    def get(self):
        logging.debug("asd")
        return {"moshe": "reubinoff"}


api.add_resource(Users, '/users')


# https://flask-restful.readthedocs.io/en/latest/quickstart.html
