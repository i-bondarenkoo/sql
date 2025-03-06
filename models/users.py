from sqlalchemy import Table, Column, Integer, String
from models.base import Base

# Таблица пользователей
users_table = Table(
    "users",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("first_name", String(50), nullable=False),
    Column("last_name", String(50), nullable=False),
    Column("email", String(100), unique=True),
    Column("phone", String(128), unique=True, nullable=False),
)
