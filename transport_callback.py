from flask import Blueprint, request, jsonify
from datetime import datetime
from pymongo import MongoClient



# Create Blueprint
transport_callback_bp = Blueprint("transport_callback", __name__)

# MongoDB setup
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
client.admin.command('ping')
db = client.Kalro_db
transport_payments = db.purchased

@transport_callback_bp.route("/transport/callback", methods=["POST"])
def transport_callback():
    data = request.get_json(force=True)
    print("Headers:", request.headers)
    print("Content-Type:", request.content_type)
    print("transport Callback received:", data)

    try:
        callback = data['Body']['stkCallback']
        result_code = callback['ResultCode']
        checkout_request_id = callback['CheckoutRequestID']
     

        # Update the matching purchase
        update_result = transport_payments.update_one(
            {"transport_checkout_request_id": checkout_request_id},
            {
                "$set": {
                    "transport_checkout_status": "completed" if result_code == 0 else "declined",
                    "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )

        print(f"Update matched {update_result.matched_count} document(s).")

    except Exception as e:
        print("Error processing callback:", str(e))

    return jsonify({"ResultCode": 0, "ResultDesc": "Callback received"})


