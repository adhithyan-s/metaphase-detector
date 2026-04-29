from fastapi import APIRouter, HTTPException
from models.patient import Patient
from config.db import conn
from schemas.patient import patientEntity, patientsEntity

patient = APIRouter()

@patient.get("/patient")
async def find_all_patients():
    return patientsEntity(conn.metaphase.patient.find())

@patient.post("/patient")
def register_patient(patient: Patient):
    conn.metaphase.patient.insert_one(dict(patient))
    return {"message": "Patient registered successfully"}