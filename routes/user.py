from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User

user = APIRouter()

@user.get("/")
async def read_data():
  return conn.execute(users.select()).fetchall()