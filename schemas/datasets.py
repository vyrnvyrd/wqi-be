from pydantic import BaseModel

class Datasets(BaseModel):
  nama_lokasi:str
  zat_padat_terlarut:float
  kekeruhan:float
  besi:float
  fluorida:float
  total_hardness:float
  chlorida:float
  mangan:float
  nitrat:float
  nitrit:float
  ph:float
  seng:float
  sulfat:float
  senyawa_aktif_biru_metilen:float
  organik:float
  suhu:float
  bakteri_koli:float
  indeks_pencemaran:float
  class_data:int