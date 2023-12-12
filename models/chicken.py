import enum

from sqlalchemy import Integer, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

# Local Imports
from models.base import BaseModel


class Sex(enum.Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Chicken(BaseModel):
    farmer_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("farmer.id", ondelete="CASCADE"),
    )
    age: Mapped[int] = mapped_column(
        Integer, nullable=False,
    )
    sex: Mapped[Sex] = mapped_column(
        Enum(Sex), nullable=False,
    )
