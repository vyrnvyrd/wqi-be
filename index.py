from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.index import user, auth_login, dokumen_api, water_quality_api
from fastapi_pagination import add_pagination
import paho.mqtt.client as mqtt

app = FastAPI()

add_pagination(app)

origins = [
  "http://localhost.tiangolo.com",
  "https://localhost.tiangolo.com",
  "http://localhost",
  "http://localhost:8080",
  "http://localhost:3000",
  "http://localhost:3001",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

app.include_router(user)
app.include_router(auth_login)
app.include_router(dokumen_api)
app.include_router(water_quality_api)