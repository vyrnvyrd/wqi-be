from sqlalchemy import Table, Column, String
from config.db import meta
from sqlalchemy.dialects.postgresql import UUID
import uuid

users = Table(
    'users', meta,
    Column('id', UUID(as_uuid=True), primary_key=True, nullable=False, default=uuid.uuid4),
    Column('user_name', String(255), nullable=False),
    Column('pass_word', String(255), nullable=False)
)