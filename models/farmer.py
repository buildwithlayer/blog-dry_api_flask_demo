from sqlalchemy import Integer, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

# Local Imports
from config import db, marsh


class Farmer(db.Model):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
    )
    name: Mapped[str] = mapped_column(
        String, nullable=False,
    )


class FarmerSchema(marsh.SQLAlchemyAutoSchema):
    class Meta:
        model = Farmer
