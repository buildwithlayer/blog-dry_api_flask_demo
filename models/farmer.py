from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

# Local Imports
from models.base import BaseModel
from models.chicken import Chicken
from models.crop import Crop


class Farmer(BaseModel):
    name: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )

    # --- RELATIONSHIPS ---
    chickens: Mapped[List[Chicken]] = relationship(
        "Chicken",
        cascade="all, delete",
    )
    crops: Mapped[List[Crop]] = relationship(
        "Crop",
        cascade="all, delete",
    )
