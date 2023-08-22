from fastapi import APIRouter
from config.db import conn
from models.index import dokumen
from schemas.index import Dokumen

dokumen = APIRouter()

@dokumen.post("/")
async def post_dokumen():
  return {}