from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_cors import CORS
import model_api

app = Flask(__name__)
api = Api(app)
CORS(app)

# route for uploading file on server
api.add_resource(model_api.UploadImage, '/upload/')



if __name__ == "__main__":
    app.run(debug=True)