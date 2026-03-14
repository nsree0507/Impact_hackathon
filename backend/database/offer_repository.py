from datetime import datetime
from backend.database.mongo_connection import get_database


def save_offer(offer_data: dict):
    """
    Save generated offer into MongoDB
    """

    db = get_database()
    offers_collection = db["offers"]

    offer_data["created_at"] = datetime.utcnow()

    result = offers_collection.insert_one(offer_data)

    return str(result.inserted_id)


def get_customer_offers(customer_id: str):
    """
    Fetch stored offers for a customer
    """

    db = get_database()
    offers_collection = db["offers"]

    offers = list(
        offers_collection.find(
            {"customer_id": customer_id},
            {"_id": 0}
        )
    )

    return offers
