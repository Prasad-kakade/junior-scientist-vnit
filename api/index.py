import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from api import modelothon, mathamaze, jso, catapultikon, exquizit, arduinoexp, mun

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "").split(",") if os.environ.get("CORS_ORIGINS") else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(modelothon.router, prefix="/api")
app.include_router(mathamaze.router, prefix="/api")
app.include_router(jso.router, prefix="/api")
app.include_router(catapultikon.router, prefix="/api")
app.include_router(exquizit.router, prefix="/api")
app.include_router(arduinoexp.router, prefix="/api")
app.include_router(mun.router, prefix="/api")

# Serve static HTML pages from the public/ directory
app.mount("/", StaticFiles(directory="public", html=True), name="public")
