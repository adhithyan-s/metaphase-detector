from pydantic import BaseModel
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    male = "male"
    female = "female"

class Patient(BaseModel):
    name: str
    address: str
    doctor_id: str
    age: int
    gender: Gender
    analysed: Optional[bool] = False
