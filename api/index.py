from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from pathlib import Path

from api import modelothon, mathamaze, jso, catapultikon, exquizit, arduinoexp, mun

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = Path(__file__).resolve().parent.parent


@app.get("/")
def read_root():
    return FileResponse(BASE_DIR / "index.html")


app.include_router(modelothon.router, prefix="/api")
app.include_router(mathamaze.router, prefix="/api")
app.include_router(jso.router, prefix="/api")
app.include_router(catapultikon.router, prefix="/api")
app.include_router(exquizit.router, prefix="/api")
app.include_router(arduinoexp.router, prefix="/api")
app.include_router(mun.router, prefix="/api")