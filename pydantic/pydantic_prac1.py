from pydantic import BaseModel,EmailStr, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name : Annotated[str, Field(max_length=50, title='Name of Patient',description='Gives names of Patient',examples=['Nitish','Amith sha'])]
    email : EmailStr
    age : int = Field(gt=0, lt=120)
    weight : Annotated[float,Field(gt=0,strict=True)]
    married : Annotated[Optional[bool], Field(default=None, description="Marriage status")]
    allergies : Annotated[Optional[List[str]], Field(max_length=5,default=None)]
    contact_details : Dict[str,str]

patient_info = {'name': 'nitish', 'age': '30', 'weight' : "75.25", 'married':True, 'allergies': ['pollen','dust'], 'contact_details': {'email':'abcd@gmail.com','phone':'9949800087'},'email':'katraj@gmail.com'}

patient1  = Patient(**patient_info)  #Unpack a dictionary into keyword arguments

'''  ** -> Unpack a dictionary into keyword arguments'''

def insert_patient_data(patient : Patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.contact_details)
    print(patient.allergies)
    print('inserted')

insert_patient_data(patient1)