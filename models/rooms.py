from sqlalchemy import Integer, Table, Column, String
from models.base import Base

# # Таблица номеров
rooms_table = Table(
    "rooms",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("room_number", Integer, nullable=False, unique=True),
    Column("price_per_night", Integer, nullable=False),
    Column("status", String, nullable=False),  # Заменено Enum на String
)
