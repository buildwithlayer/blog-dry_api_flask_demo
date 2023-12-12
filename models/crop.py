from sqlalchemy import String, Integer, Float, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# Local Imports
from models.base import BaseModel


class Crop(BaseModel):
    farmer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("farmer.id", ondelete="CASCADE"), nullable=False,
    )
    type: Mapped[str] = mapped_column(
        String, nullable=False,
    )
    days_to_mature: Mapped[int] = mapped_column(
        Integer, nullable=False,
    )
    acres: Mapped[float] = mapped_column(
        Float, nullable=False,
    )

    # --- METADATA ---
    __mapper_args__ = {
        "polymorphic_identity": "crop",
        "polymorphic_on": "type",
    }
