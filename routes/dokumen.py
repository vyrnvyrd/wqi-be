from fastapi import APIRouter, HTTPException
from config.db import conn
from models.index import dokumen
from schemas.index import Dokumen
import base64

dokumen_api = APIRouter()

def is_base64(s):
  try:
    decoded = base64.b64decode(s)
    encoded = base64.b64encode(decoded)
    return encoded == s.encode()
  except:
    return False

@dokumen_api.post("/dokumen", tags=["Dokumen"], description="Post new document")
async def post_dokumen(data: Dokumen):
  if (is_base64(data.file)):
    decoded_content = base64.b64decode(data.file)
    file_path = f"file/{data.title}"

    with open(file_path, "wb") as f:
      f.write(decoded_content)

    result = conn.execute(dokumen.insert().values(
      file=file_path
    ))
    conn.commit()
    inserted_id = result.lastrowid
    return {
      "id": inserted_id
    }
  
  raise HTTPException(status_code=400)
