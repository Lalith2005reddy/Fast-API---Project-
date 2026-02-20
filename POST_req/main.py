from fastapi import FastAPI, Path, Query, HTTPException
from typing import Annotated, Literal
from pydantic import BaseModel,Field, field_validator
import json

app = FastAPI()

class Patient(BaseModel):

    id : Annotated[str, Field(..., description='ID of patient', examples=['P001'])]
    name : str
    city : str
    age : int
    gender : str
    height : float
    weight : float

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data