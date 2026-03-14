from fastapi import APIRouter
from backend.database.mongo_connection import get_database

router = APIRouter(prefix="/admin", tags=["Admin Services"])


# -----------------------------------
# View Transactions
# -----------------------------------
@router.get("/transactions")
def get_transactions():

    db = get_database()
    transactions = list(db["transactions"].find({}, {"_id": 0}))

    return {
        "total_transactions": len(transactions),
        "data": transactions
    }


# -----------------------------------
# Add Transaction
# -----------------------------------
@router.post("/add-transaction")
def add_transaction(transaction: dict):

    db = get_database()
    db["transactions"].insert_one(transaction)

    return {"message": "Transaction added successfully"}


# -----------------------------------
# Sales Summary
# -----------------------------------
@router.get("/sales-summary")
def sales_summary():

    db = get_database()

    pipeline = [
        {
            "$group": {
                "_id": None,
                "total_sales": {"$sum": "$price"},
                "total_transactions": {"$sum": 1}
            }
        }
    ]

    result = list(db["transactions"].aggregate(pipeline))

    return result


# -----------------------------------
# Top Products
# -----------------------------------
@router.get("/top-products")
def top_products():

    db = get_database()

    pipeline = [
        {
            "$group": {
                "_id": "$product",
                "total_sold": {"$sum": "$quantity"}
            }
        },
        {"$sort": {"total_sold": -1}},
        {"$limit": 5}
    ]

    result = list(db["transactions"].aggregate(pipeline))

    return result


# -----------------------------------
# Customer Segments
# -----------------------------------
@router.get("/customer-segments")
def customer_segments():

    db = get_database()

    pipeline = [
        {
            "$group": {
                "_id": "$customer_id",
                "total_spent": {"$sum": "$price"}
            }
        },
        {"$sort": {"total_spent": -1}}
    ]

    result = list(db["transactions"].aggregate(pipeline))

    return result
