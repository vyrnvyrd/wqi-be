from fastapi import APIRouter, HTTPException
from config.db import conn
from models.index import dokumen
from schemas.index import Dokumen
import base64

dokumen_api = APIRouter()

def is_base64(s):
  try:
    print(base64.b64decode(s))
    decoded = base64.b64decode(s)
    print('here', decoded)
    encoded = base64.b64encode(decoded)
    print('here', encoded)
    print('here', encoded == s.encode())
    return encoded == s.encode()
  except:
    return False

@dokumen_api.post("/", tags=["Dokumen"], description="Post new document")
async def post_dokumen(data: Dokumen):
  print(is_base64(data.file))
  if (is_base64(data.file)):
    result = conn.execute(dokumen.insert().values(
      file=data.file
    ))
    conn.commit()
    inserted_id = result.lastrowid
    return {
      "id": inserted_id
    }
  
  raise HTTPException(status_code=400)
