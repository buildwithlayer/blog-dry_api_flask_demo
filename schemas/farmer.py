from marshmallow import fields

# Local Imports
from models.farmer import Farmer
from schemas.crop import CropSchema

FarmerSchema = Farmer.make_schema(
    overrides={"crops": fields.Nested(CropSchema(), many=True)}
)
