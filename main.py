from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {"data": "Hello World!"}

api.add_resource(HelloWorld, "/helloworld")

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
