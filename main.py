import pickle
import pandas as pd
from fastapi import FastAPI
from data_model import Water

app = FastAPI(
        title = 'Water Potalibilty Prediction',
        description = 'Predicting Water Portability'
    )

with open ('model.pkl','rb') as f:
    model = pickle.load(f)


@app.get('/')
def index():
    return 'Welcome to the Water Portability Prediction FastAPI'

@app.post('/predict')
def model_prediction(water: Water):
    sample = pd.DataFrame(
            {'ph': [water.ph],
            'Hardness':[ water.Hardness],
            'Solids': [water.Solids],
            'Chloramines': [water.Chloramines],
            'Sulfate': [water.Sulfate],
            'Conductivity': [water.Conductivity],
            'Organic_carbon': [water.Organic_carbon],
            'Trihalomethanes': [water.Trihalomethanes],
            'Turbidity': [water.Turbidity]}
            ) 

    predicted_value = model.predict(sample)

    if predicted_value == 1:

        return 'Water is Consumable'

    else:
        return 'Water is not Consumable'

