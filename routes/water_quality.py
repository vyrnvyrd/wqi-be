from fastapi import APIRouter, HTTPException, Body
from fastapi_pagination import Page, paginate
from config.db import conn
from models.index import water_quality, datasets, dokumen
from schemas.index import Water_Quality, Water_Quality_List
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from starlette.responses import FileResponse

water_quality_api = APIRouter()

def classify_machine_learning(df, new_data_body):
  # data pre-processing
  column_to_drop = 'nama_lokasi'
  df = df.drop(columns=[column_to_drop])
  column_to_drop = 'indeks_pencemaran'
  df = df.drop(columns=[column_to_drop])

  X = df.drop(columns=['class'])
  y = df['class']

  #feature selection - corellation coeficient
  correlations = X.corrwith(y)
  correlations = correlations.abs().sort_values(ascending=False)
  K = 10
  selected_features = correlations.index[:K]

  # train model
  X_train, X_test, y_train, y_test = train_test_split(X[selected_features], y, test_size=0.2, random_state=200)
  model = RandomForestClassifier(
    n_estimators=300,
    criterion='gini',
    max_depth=11,
    min_samples_split=2,
    min_samples_leaf=3,
    min_weight_fraction_leaf=0.0,
    max_features='sqrt',
    max_leaf_nodes=None,
    min_impurity_decrease=0.0,
    bootstrap=True,
    oob_score=False,
    n_jobs=-1,
    random_state=200,
    verbose=0,
    warm_start=False,
    class_weight='balanced')
  model.fit(X_train, y_train)

  # Load and preprocess new data
  data_dict = {
    'organik': new_data_body.zat_organik,
    'zat_padat_terlarut': new_data_body.tds,
    'mangan': new_data_body.mangan,
    'chlorida': new_data_body.klorida,
    'kekeruhan': new_data_body.kekeruhan,
    'fluorida': new_data_body.fluorida,
    'pH': new_data_body.ph,
    'total_hardness': new_data_body.kesadahan,
    'sulfat': new_data_body.sulfat,
    'suhu': new_data_body.suhu
  }

  # Create a DataFrame from the dictionary
  new_x_test = pd.DataFrame([data_dict])
  new_pred = model.predict(new_x_test)

  return new_pred[0]

@water_quality_api.get("/water_quality", tags=["Water Quality"], response_model=Page[Water_Quality_List], description="Get all water quality")
async def get_list_water_quality():
  result = conn.execute(water_quality.select()).fetchall()
  return paginate(result)

@water_quality_api.get("/water_quality/{id}", tags=["Water Quality"], description="Get water quality by id")
async def get_water_quality_by_id(id: int):
  result = conn.execute(water_quality.select().where(water_quality.c.id == id)).fetchall()
  if not result:
    raise HTTPException(status_code=404)
  result_dokumen = conn.execute(dokumen.select().where(dokumen.c.id == result[0].id_dokumen)).fetchall()
  data_detail = result[0]._mapping
  data_file = result_dokumen[0]._mapping
  return {
    'data': data_detail,
    'file': data_file
  }

@water_quality_api.get("/water_quality/download/{id}", tags=["Water Quality"], description="Download water quality")
async def download_saved_file(id: int):
    result_dokumen = conn.execute(dokumen.select().where(dokumen.c.id == id)).fetchall()
    if not result_dokumen:
      raise HTTPException(status_code=404)
    print(result_dokumen)
    return FileResponse(path=result_dokumen[0].file)

@water_quality_api.post("/water_quality", tags=["Water Quality"], description="Post new water quality")
async def post_water_quality(data: Water_Quality):
  try:
    result = conn.execute(datasets.select()).fetchall()
    new_data = data
    df = pd.DataFrame(result, columns=[
      'nama_lokasi',
      'zat_padat_terlarut',
      'kekeruhan',
      'besi',
      'fluorida',
      'total_hardness',
      'chlorida',
      'mangan',
      'nitrat',
      'nitrit',
      'pH',
      'seng',
      'sulfat',
      'senyawa_aktif_biru_metilen',
      'organik',
      'suhu',
      'bakteri_koli',
      'indeks_pencemaran',
      'class'
    ])
    new_class = classify_machine_learning(df, new_data)

    conn.execute(water_quality.insert().values(
      nama_sumur=new_data.nama_sumur,
      id_kota=new_data.id_kota,
      nama_kota=new_data.nama_kota,
      id_kecamatan=new_data.id_kecamatan,
      nama_kecamatan=new_data.nama_kecamatan,
      id_kelurahan=new_data.id_kelurahan,
      nama_kelurahan=new_data.nama_kelurahan,
      alamat=new_data.alamat,
      id_dokumen=new_data.id_dokumen,
      zat_organik=new_data.zat_organik,
      tds=new_data.zat_organik,
      mangan=new_data.mangan,
      klorida=new_data.klorida,
      kekeruhan=new_data.kekeruhan,
      fluorida=new_data.fluorida,
      ph=new_data.ph,
      kesadahan=new_data.kesadahan,
      sulfat=new_data.sulfat,
      suhu=new_data.suhu,
      class_data=new_class
    ))
    conn.commit()

    return {
      'detail': 'Success!'
    }
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
