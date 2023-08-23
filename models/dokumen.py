from sqlalchemy import Table, Column, Integer, Text
from config.db import meta
from sqlalchemy.dialects.postgresql import UUID
import uuid

dokumen = Table(
  'dokumens', meta,
  Column('id', Integer, nullable=True, primary_key=True),
  Column('file', Text, nullable=False),
)