from fastapi import APIRouter
from backend.services.geofence_service import check_geofence
from backend.services.recommendation_service import get_recommendations
from backend.services.offer_service import generate_offer

router = APIRouter()


@router.post("/check-location")
def check_location(data: dict):

    customer_id = data["customer_id"]
    lat = data["latitude"]
    lon = data["longitude"]

    geofence_result = check_geofence(lat, lon)

    if not geofence_result["inside"]:
        return {
            "message": "User outside store area",
            "distance": geofence_result["distance"]
        }

    # Generate recommendations
    recommendations = get_recommendations(customer_id)

    # Generate offers
    offers = generate_offer(recommendations)

    return {
        "message": "User inside store area",
        "distance": geofence_result["distance"],
        "offers": offers
    }
