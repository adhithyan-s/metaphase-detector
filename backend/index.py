from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.patient import patient

app = FastAPI(title="Metaphase Detector API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(patient)