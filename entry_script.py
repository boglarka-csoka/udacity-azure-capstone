import joblib
import os
import json
import numpy as np

from azureml.core.model import Model

def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'),'logreg_model.pkl')
    model = joblib.load(model_path)

def run(data_raw):
    try:
        #data = json.load(open('data.json'))
        data = np.array(data_raw['data'])
        #data=data_raw['data']
        # Call predict() on each model
        result = model.predict(data)
        # You can return any JSON-serializable value.
        return {"prediction": result}
    except Exception as e:
        result = str(e)
        return result