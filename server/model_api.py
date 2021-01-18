from flask import request, jsonify, make_response
from flask_restful import Resource
import os

class UploadImage(Resource):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        
        my_file = request.files["inpFile"]

        dir_loc = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.join(dir_loc, "static", my_file.filename)
        error_code=200
        try:
            
            my_file.save(abs_path)
            upload_status = "file uploaded"

        except:
            upload_status = "error in uploading file in server!!"     
            error_code=404
        res = make_response(
                    jsonify({
                        'upload_status': upload_status,
                        
                    }), error_code)

        return res