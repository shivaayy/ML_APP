# python package requirments
flask
flask-restful
flask-cors
tensorflow
efficientnet
numpy



Steps to run:

1.  `pip install -r requirements.txt`

2. download the efficientnet model from any ONE of the following links:
    1. https://www.kaggle.com/siddalore/cassava-efficientnetb7
    2. https://www.kaggle.com/siddalore/efficientnetb4-with-cutmix-mixup-gridmask#Running-model
    3. https://www.kaggle.com/siddalore/resnet50-with-cutmix-mixup-gridmask?rvi=1

 and place it in `./server/static` directory.

_make sure the name of the model file matches the name in the model_api file. Default name of the model imported is `efficientnet.h5`_

3. Navigate to directory `/server`. Start server using `python server.py`

4. Open Frontend client by opening the `src/index.html` file in the browser.

5. Upload image in the frontend client.

6. Click on run model.

7. Wait for inference to complete.

See the results!

The time it takes for the model to predict will be given in the terminal.
