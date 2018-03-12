import logging


from flask_restplus import Resource
from app.restplus import api

log = logging.getLogger(__name__)
ns = api.namespace('test', description='Tests')


@ns.route('/')
class Test(Resource):
    @staticmethod
    def get():
        response_dict = {"test": "test_string", "test_2": "test_string"}
        return response_dict
