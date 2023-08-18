from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root:urankhade@localhost:3306/wqi")
meta = MetaData()
conn = engine.connect()