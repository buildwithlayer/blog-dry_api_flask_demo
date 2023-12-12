from typing import Dict

from marshmallow_oneofschema import OneOfSchema

# Local Imports
from models.crop import Crop
from schemas.cucumber import CucumberSchema
from schemas.tomato import TomatoSchema


class CropSchema(OneOfSchema):
    type_schemas: Dict[str, str] = {
        "cucumber": CucumberSchema,
        "tomato": TomatoSchema,
    }

    type_field_remove = False

    def get_obj_type(self, obj: Crop):
        return obj.type
