from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

# Local Imports
from models.crop import Crop


class Tomato(Crop):
    id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("crop.id", ondelete="CASCADE"),
        primary_key=True,
    )
    diameter: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    # --- METADATA ---
    __mapper_args__ = {"polymorphic_identity": "tomato"}
