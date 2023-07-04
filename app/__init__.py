from flask import Flask, request
from flask_restful import Resource, Api, reqparse


app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        # 初始化解析器
        parser = reqparse.RequestParser()
        parser.add_argument('account_id', type=str, location='form', required=True)
        parser.add_argument('ec', type=str, location='files')
        data = parser.parse_args()

        return {'hello': 'world'}

api.add_resource(HelloWorld, '/')