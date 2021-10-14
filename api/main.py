from pydantic import BaseModel
from fastapi import FastAPI, Depends, HTTPException, status
from typing import Optional
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.encoders import jsonable_encoder
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from starlette.responses import RedirectResponse
from models import Features
from data_preparation import prepare_data

import pickle
import csv 
import json
import random

api = FastAPI(
    title='My Exam'
)
security = HTTPBasic()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

with open("./users.json", "r") as f:
    users = json.load(f)

with open("./data/model.pkl", "rb") as f:
    model = pickle.load(f)

def check_credentials(credentials: HTTPBasicCredentials = Depends(security)):

    user = list(filter(lambda u: u["username"] == credentials.username, users))

    if not len(user):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    user = user[0]

    if user["password"] != credentials.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username

@api.get("/")
def redirect_to_docs():

    return RedirectResponse(url="/docs")

@api.post("/prediction")
def make_prediction(data: Features, username: str = Depends(check_credentials)):

    df = prepare_data(data)
    proba = round(model.predict_proba(df)[0][1], 4)
    prediction = int(model.predict(df)[0])

    return {"Prediction": prediction, "proba": proba}

