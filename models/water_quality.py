from sqlalchemy import Table, Column, String, Text, Float, Integer, TIMESTAMP
from config.db import meta
from sqlalchemy.dialects.postgresql import UUID
import uuid

water_quality = Table(
  'water_quality', meta,
  Column('id', UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4),
  Column('nama_sumur', String(255), nullable=False),
  Column('id_kota', String(100), nullable=False),
  Column('nama_kota', String(255), nullable=False),
  Column('id_kecamatan', String(100), nullable=False),
  Column('nama_kecamatan', String(255), nullable=False),
  Column('id_kelurahan', String(100), nullable=False),
  Column('nama_kelurahan', String(255), nullable=False),
  Column('alamat', Text, nullable=False),
  Column('id_dokumen', UUID(as_uuid=True), nullable=False, default=uuid.uuid4),
  Column('zat_organik', Float, nullable=False),
  Column('tds', Float, nullable=False),
  Column('mangan', Float, nullable=False),
  Column('klorida', Float, nullable=False),
  Column('kekeruhan', Float, nullable=False),
  Column('fluorida', Float, nullable=False),
  Column('ph', Float, nullable=False),
  Column('kesadahan', Float, nullable=False),
  Column('sulfat', Float, nullable=False),
  Column('suhu', Float, nullable=False),
  Column('class_data', Integer, nullable=False),
  Column('created_at', TIMESTAMP, nullable=False)
)