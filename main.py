from fastapi import FastAPI, Body
from routers import items
import models.classifier as clf
from joblib import load
from models.iris import Iris

app = FastAPI()

app.include_router(items.router)


@app.on_event('startup')
async def load_model():
    clf.model = load('models/iris_dt_v1.joblib')


@app.post('/predict', tags=["predictions"])
async def get_prediction(iris: Iris):
    data = dict(iris)['data']
    prediction = clf.model.predict(data).tolist()

    return {"prediction": prediction}


@app.get("/")
async def root():
    return {"message": "Hello DataScience Applications!"}
