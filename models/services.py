from sqlalchemy import TIMESTAMP, Integer, String, ForeignKey, Table, Column
from models.base import Base

# # Таблица дополнительных услуг
services_table = Table(
    "services",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("booking_id", ForeignKey("bookings.id"), nullable=False),
    Column("service_name", String, nullable=False),
    Column("price", Integer, nullable=False),
)
