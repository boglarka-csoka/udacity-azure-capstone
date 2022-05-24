import joblib
import os
import json
import numpy as np

from azureml.core.model import Model

def init():
    global model
    #model=ws.models['hyperparam_best_model']
    #model_path=model.download(exist_ok=True)
    model_path =os.path.join(os.getenv("AZUREML_MODEL_DIR"), "logreg_model.pkl") #Model.get_model_path(model_name='logreg_model.pkl')
    model = joblib.load(model_path)

def run(data_raw):
    try:
        #data = json.load(open('data.json'))
        data = np.array(json.loads(data_raw)['data']) #.tolist()
        #data=data_raw['data']
        # Call predict() on each model
        result = model.predict(data)
        # You can return any JSON-serializable value.
        return {"prediction": result}
    except Exception as e:
        result = str(e)
        return result