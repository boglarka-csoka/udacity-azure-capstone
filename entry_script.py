import joblib
import json
import numpy as np

from azureml.core.model import Model

def init():
    global model
    model_path = Model.get_model_path(model_name='hyperparam_best_model')
    model = joblib.load(model_path)

def run(data):
    try:
        #data = json.load(open('data.json'))
        #data = np.array(data)
        
        # Call predict() on each model
        result = model.predict(data)

        # You can return any JSON-serializable value.
        return {"prediction": result}
    except Exception as e:
        result = str(e)
        return result