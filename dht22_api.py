from fastapi import FastAPI
from routes.dht22_routes import dht22

app = FastAPI()

app.include_router(dht22)