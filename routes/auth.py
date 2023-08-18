from fastapi import APIRouter, Body, HTTPException
from config.db import conn
from models.index import users
from schemas.index import Auth
import hashlib

auth_login = APIRouter()

def md5_encode(text):
  md5_hash = hashlib.md5()
  md5_hash.update(text.encode('utf-8'))
  encoded_text = md5_hash.hexdigest()
  return encoded_text

@auth_login.post("/auth")
async def auth(username: str = Body(), password: str = Body()):
  found = conn.execute(users.select().where(users.c.user_name == username.lower())).fetchall()
  print(found)
  if found:
    if md5_encode(password) == found[0].pass_word:
      return {"detail": "Welcome Back, "+found[0].user_name+"!"}
    
    raise HTTPException(status_code=401, detail="Username/password is wrong!",)

  raise HTTPException(status_code=401, detail="Username/password is wrong!")