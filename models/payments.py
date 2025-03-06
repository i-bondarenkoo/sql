from sqlalchemy import TIMESTAMP, Integer, String, ForeignKey, Table, Column, func
from models.base import Base

# # Таблица платежей
payments_table = Table(
    "payments",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("booking_id", ForeignKey("bookings.id"), nullable=False),
    Column("amount", Integer, nullable=False),
    Column("paid_at", TIMESTAMP, default=func.now()),
)
