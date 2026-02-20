from fastapi import FastAPI, Path, Query, HTTPException
from pydantic import BaseModel
import json

app = FastAPI()

class Patient(BaseModel):
    name : int

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)

    return data