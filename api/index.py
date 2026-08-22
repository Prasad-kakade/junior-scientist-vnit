import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import modelothon, mathamaze, jso, catapultikon, exquizit, arduinoexp, mun ,image

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.environ.get("CORS_ORIGINS", "").split(",") if os.environ.get("CORS_ORIGINS") else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# List of all your routers
routers = [
    modelothon.router,
    mathamaze.router,
    jso.router,
    catapultikon.router,
    exquizit.router,
    arduinoexp.router,
    mun.router,
    image.router
]

# Register each router WITH and WITHOUT the /api prefix so Vercel never 404s
for r in routers:
    app.include_router(r)