# -*- coding: utf-8 -*-
"""
Created on Fri May  7 23:49:11 2021

@author: yasasmi
"""

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from PhoneUsageIP import PhoneUsageIP
import numpy as np
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open("phone_usage_model_pickle","rb")
mp=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Behaviour Analysis': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_depression(data:PhoneUsageIP):
    data = data.dict()
    print(data)
    
    Age=data['Age']
    Gender=data['Gender']
    No_Of_Social_Media_Apps=data['No_Of_Social_Media_Apps']
    Social_Media_App_Usage=data['Social_Media_App_Usage']
    Gaming_App_usage=data['Gaming_App_usage']
    Night_Time_Use=data['Night_Time_Use']

    print(mp.predict([[Age,Gender,No_Of_Social_Media_Apps,Social_Media_App_Usage,Gaming_App_usage,Night_Time_Use]]))
    prediction = mp.predict([[Age,Gender,No_Of_Social_Media_Apps,Social_Media_App_Usage,Gaming_App_usage,Night_Time_Use]])
    if(prediction[0] == 0):
        prediction="Not Depressed"
    elif(prediction[1] == 1):
        prediction="mild"
    elif(prediction[2] == 2):
        prediction="modarate"    
    else:
        prediction="high"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload