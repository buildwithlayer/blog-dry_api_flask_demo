from enum import Enum
from typing import Optional, Type, Dict

from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Integer, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, Relationship

# Local Imports
from config import db


class BaseMeta(object):
    include_relationships = True


class BaseModel(db.Model):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True,
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, nullable=False, server_default=func.now(), onupdate=func.now(),
    )

    # --- METADATA ---
    __abstract__ = True

    __schema__ = None

    @classmethod
    def get_relationship(cls, attr_name: str) -> Optional[Relationship]:
        attr = getattr(cls, attr_name)
        prop = getattr(attr, "property", None)
        if prop is None or not isinstance(prop, Relationship):
            return None
        return prop

    @classmethod
    def nest_attribute(cls, attr_name: str, prop: Relationship, schema_kwargs: dict):
        many = getattr(prop, "collection_class", None) is not None
        entity = getattr(prop, "entity", None)
        nested_class = getattr(entity, "class_", None)
        if not hasattr(nested_class, "make_schema"):
            raise TypeError(f"Unexpected nested type [{type(nested_class).__name__}]")

        schema_kwargs[attr_name] = fields.Nested(
            nested_class.make_schema()(many=many)
        )

    @classmethod
    def get_enum(cls, attr_name: str) -> Optional[Type[Enum]]:
        attr = getattr(cls, attr_name)
        attr_type = getattr(attr, "type", None)
        if attr_type is None:
            return None

        return getattr(attr_type, "enum_class", None)

    @classmethod
    def enum_attribute(cls, attr_name: str, enum_class: Type[Enum], schema_kwargs: dict):
        schema_kwargs[attr_name] = fields.Enum(enum_class)

    @classmethod
    def make_schema(cls, overrides: Optional[Dict[str, fields.Field]] = None) -> type(SQLAlchemyAutoSchema):
        if cls.__schema__ is not None:
            return cls.__schema__

        if overrides is None:
            overrides = dict()

        meta_kwargs = {
            "model": cls,
        }
        meta_class = type("Meta", (BaseMeta,), meta_kwargs)

        schema_kwargs = {
            "Meta": meta_class
        }
        schema_name = f"{cls.__name__}Schema"

        for attr_name in cls.__dict__:
            if attr_name in overrides:
                schema_kwargs[attr_name] = overrides[attr_name]
            elif (prop := cls.get_relationship(attr_name)) is not None:
                cls.nest_attribute(attr_name, prop, schema_kwargs)
            elif (enum_class := cls.get_enum(attr_name)) is not None:
                cls.enum_attribute(attr_name, enum_class, schema_kwargs)

        cls.__schema__ = type(schema_name, (SQLAlchemyAutoSchema,), schema_kwargs)
        return cls.__schema__
