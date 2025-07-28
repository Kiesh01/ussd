from flask import Blueprint, request, jsonify
from datetime import datetime
from pymongo import MongoClient




# Create the Blueprint
daraja_callback_bp = Blueprint("daraja_callback", __name__)

# MongoDB setup
client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
client.admin.command('ping')  # Check connection
db = client.Kalro_db
purchased = db.purchased


@daraja_callback_bp.route("/daraja/callback", methods=["POST"])
def daraja_callback():
    data = request.get_json(force=True)
    print("Headers:", request.headers)
    print("Content-Type:", request.content_type)
    print("Callback received:", data)

    try:
        callback = data['Body']['stkCallback']
        result_code = callback['ResultCode']
        checkout_request_id = callback['CheckoutRequestID']
        result_desc = callback['ResultDesc']

        # Update the matching purchase
        update_result = purchased.update_one(
            {"mpesa_checkout_request_id": checkout_request_id},
            {
                "$set": {
                    "status": "completed" if result_code == 0 else "failed",
                    "result_code": result_code,
                    "result_desc": result_desc,
                    "completed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
            }
        )

        print(f"Update matched {update_result.matched_count} document(s).")

    except Exception as e:
        print("Error processing callback:", str(e))

    return jsonify({"ResultCode": 0, "ResultDesc": "Callback received"})

