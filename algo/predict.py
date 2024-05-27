import os
import pickle
from .constant import person_data as person
import pandas as pd
def predict(map):
        person_data=person
        current_dir = os.path.dirname(os.path.realpath(__file__))
        model_pkl_file = os.path.join(current_dir, "iris_classifier_model.pkl")
        with open(model_pkl_file, 'rb') as file:  
            model1 = pickle.load(file)
        for key in map.keys():
              if key in person_data:
                person_data[key] = map[key]
        person_data=pd.DataFrame([person_data])
        y_pred = model1.predict(person_data)
        print(y_pred)
        return y_pred[0]
        