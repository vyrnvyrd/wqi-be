from pydantic import BaseModel

class Dokumen(BaseModel):
  id:str
  file:str
  created_at:str