import os
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sg2.controllers.router import router
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).parent

app = FastAPI(title="SG2 - Sistema Gestionador de Servicios Gastronomicos")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")
app.mount("/", StaticFiles(directory=str(BASE_DIR / "static"), html=True), name="static")

@app.get("/status")
def home():
    return {"status": "SG2 API funcionando"}
