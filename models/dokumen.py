from sqlalchemy import Table, Column, String, TIMESTAMP, Text
from config.db import meta
from sqlalchemy.dialects.postgresql import UUID
import uuid

dokumen = Table(
  'dokumen', meta,
  Column('id', UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4),
  Column('file', Text, nullable=False),
  Column('created_at', TIMESTAMP, nullable=False)
)