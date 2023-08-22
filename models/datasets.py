from sqlalchemy import Table, Column, String, Float, Integer, TIMESTAMP
from config.db import meta
from sqlalchemy.dialects.postgresql import UUID
import uuid

datasets = Table(
  'datasets', meta,
  Column('nama_lokasi', String(255), nullable=False),
  Column('zat_padat_terlarut', Float, nullable=False),
  Column('kekeruhan', Float, nullable=False),
  Column('besi', Float, nullable=False),
  Column('fluorida', Float, nullable=False),
  Column('total_hardness', Float, nullable=False),
  Column('chlorida', Float, nullable=False),
  Column('mangan', Float, nullable=False),
  Column('nitrat', Float, nullable=False),
  Column('nitrit', Float, nullable=False),
  Column('ph', Float, nullable=False),
  Column('seng', Float, nullable=False),
  Column('sulfat', Float, nullable=False),
  Column('senyawa_aktif_biru_metilen', Float, nullable=False),
  Column('organik', Float, nullable=False),
  Column('suhu', Float, nullable=False),
  Column('bakteri_koli', Float, nullable=False),
  Column('indeks_pencemaran', Float, nullable=False),
  Column('class_data', Integer, nullable=False)
)