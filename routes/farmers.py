from apiflask import HTTPError, APIBlueprint

# Local Imports
from models.farmer import Farmer
from schemas.farmer import FarmerSchema

farmers_bp = APIBlueprint(
    "farmers", __name__, enable_openapi=True
)


@farmers_bp.get("/<int:farmer_id>")
@farmers_bp.output(FarmerSchema)
def get_farmer_by_id(farmer_id: int):
    farmer = Farmer.query.where(Farmer.id == farmer_id).first()
    if farmer is None:
        raise HTTPError(404, message="Farmer not found")
    return farmer
