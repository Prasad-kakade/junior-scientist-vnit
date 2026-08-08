from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import all route files directly from the api folder
from api import modelothon, mathamaze, jso, catapultikon, exquizit, arduinoexp, mun

app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Junior Scientist API is Live!"}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
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
