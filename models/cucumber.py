from sqlalchemy import Boolean, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

# Local Imports
from models.crop import Crop


class Cucumber(Crop):
    id: Mapped[int] = mapped_column(
        Integer,
        ForeignKey("crop.id", ondelete="CASCADE"),
        primary_key=True,
    )
    for_pickling: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    # --- METADATA ---
    __mapper_args__ = {"polymorphic_identity": "cucumber"}
