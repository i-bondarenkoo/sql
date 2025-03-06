from sqlalchemy import Integer, String, ForeignKey, Table, Column, Date
from models.base import Base

# Таблица бронирований
booking_table = Table(
    "bookings",
    Base.metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", ForeignKey("users.id"), nullable=False),
    Column("room_id", ForeignKey("rooms.id"), nullable=False),
    Column("start_date", Date, nullable=False),
    Column("end_date", Date, nullable=False),
    Column("status", String, nullable=False),  # Заменено Enum на String
)
