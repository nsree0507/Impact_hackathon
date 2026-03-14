from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from backend.services.recommendation_service import get_recommendations
from backend.services.offer_service import generate_offer
from backend.services.loyalty_service import get_loyalty_status
from firebase.push_notification import send_push_notification


router = APIRouter(
    prefix="/customer",
    tags=["Customer Services"]
)


# -------------------------------
# Notification Request Model
# -------------------------------
class NotificationRequest(BaseModel):
    token: str


# -------------------------------
# Get Customer Offers
# -------------------------------
@router.get("/{customer_id}/offers")
def get_customer_offers(customer_id: str):

    try:
        recommended_products = get_recommendations(customer_id)

        offers = []

        for product in recommended_products:
            offer = generate_offer(customer_id, product)
            offers.append(offer)

        return {
            "customer_id": customer_id,
            "offers": offers
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
# Get Loyalty Status
# -------------------------------
@router.get("/{customer_id}/loyalty")
def customer_loyalty(customer_id: str):

    try:
        loyalty_status = get_loyalty_status(customer_id)

        return {
            "customer_id": customer_id,
            "loyalty_status": loyalty_status
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -------------------------------
# Send Test Notification
# -------------------------------
@router.post("/send-test-notification")
def send_test_notification(request: NotificationRequest):

    try:
        response = send_push_notification(
            token=request.token,
            title="🎉 Smart Retail Offer",
            body="20% OFF on Cookies near your store!"
        )

        return {
            "message": "Notification sent successfully",
            "firebase_response": response
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
