from flask import request, jsonify, make_response
from flask_restful import Resource
import os
import random
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import numpy as np
from efficientnet.tfkeras import EfficientNetB4
print(tf.version.VERSION)


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
            # print(tf.__version__)
            # print(keras.__version__)
            


        except:
            upload_status = "error in uploading file in server!!"     
            error_code=404
        res = make_response(
                    jsonify({
                        'upload_status': upload_status,
                        'file_id': my_file.filename
                        
                    }), error_code)

        return res




class RunModel(Resource):
    def __init__(self):
        pass

    def get(self):
        pass

    def post(self):
        
        req = request.get_json()
        file_id = req['file_id']
        dir_loc = os.path.dirname(os.path.abspath(__file__))
        abs_path = os.path.join(dir_loc, "static", file_id)
        print("Loading model\n")
        model = load_model(os.path.join(dir_loc, "static","efficientnet.h5"))
        # model = tf.keras.models.load_model("cassava.hdf5")
        print("model loaded\n")
        error_code=200
        try:
            test_datagen = ImageDataGenerator(rescale = 1/255)
            # print("Hello")
            # print(os.path.join(dir_loc, "static","cassava.hdf5"))
            # model = tf.keras.models.load_model(os.path.join(dir_loc, "static","cassava.hdf5"))
            # print("Hello momdel")
            vals = ["Cassava Bacterial Blight (CBB)",
                      "Cassava Brown Streak Disease (CBSD)", 
                      "Cassava Green Mottle (CGM)",
                      "Cassava Mosaic Disease (CMD)",
                      "Healthy"]

            # vals = ["Disease1", "Disease2", "Disease3", "Disease4", "Disease5", "Disease6"]
            test_generator = test_datagen.flow_from_directory(
                dir_loc, 
                target_size = (512,512),
                color_mode = "rgb",
                class_mode="categorical",
                batch_size = 1 )
            pred = model.predict(test_generator)
            # print(pred)
            result = str(vals[np.argmax(pred)])

            run_status = "model prediction successful"
            # result=random.randrange(20,8000,6)

        except:
            run_status = "error in running model file on server!!"     
            error_code=404
        res = make_response(
                    jsonify({
                        'run_status': run_status,
                        'result':result,
                        
                        
                    }), error_code)

        return res