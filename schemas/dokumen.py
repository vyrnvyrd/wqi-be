from pydantic import BaseModel

class Dokumen(BaseModel):
  file:str
  title: str