from pydantic import BaseModel

class Water_Quality(BaseModel):
  nama_sumur:str
  id_kota:str
  nama_kota:str
  id_kecamatan:str
  nama_kecamatan:str
  id_kelurahan:str
  nama_kelurahan:str
  alamat:str
  id_dokumen:int
  zat_organik:float
  tds:float
  mangan:float
  klorida:float
  kekeruhan:float
  fluorida:float
  ph:float
  kesadahan:float
  sulfat:float
  suhu:float

class Water_Quality_List(BaseModel):
  id:int
  nama_sumur:str
  alamat:str
  class_data:int

class Water_Quality_Detail(BaseModel):
  id:int
  nama_sumur:str
  id_kota:str
  nama_kota:str
  id_kecamatan:str
  nama_kecamatan:str
  id_kelurahan:str
  nama_kelurahan:str
  alamat:str
  id_dokumen:int
  zat_organik:float
  tds:float
  mangan:float
  klorida:float
  kekeruhan:float
  fluorida:float
  ph:float
  kesadahan:float
  sulfat:float
  suhu:float