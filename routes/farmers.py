from apiflask import HTTPError, APIBlueprint
from marshmallow import Schema, fields

# Local Imports
from models.farmer import Farmer


farmers_bp = APIBlueprint(
    "farmers", __name__, enable_openapi=True
)


class FarmerOut(Schema):
    id = fields.Integer(required=True)
    created_at = fields.DateTime(required=True)
    updated_at = fields.DateTime(required=True)
    name = fields.String(required=True)


@farmers_bp.get("/<int:farmer_id>")
@farmers_bp.output(FarmerOut)
def get_farmer_by_id(farmer_id: int):
    farmer = Farmer.query.where(Farmer.id == farmer_id).first()
    if farmer is None:
        raise HTTPError(404, message="Farmer not found")
    return farmer
