from flask import  Flask, request, Response, jsonify
from pymongo import MongoClient
import datetime
from daraja_callback import daraja_callback_bp
from transport_callback import transport_callback_bp
from fertilizer_callback import fertilizer_callback_bp
from mpesa_util import lipa_na_mpesa_online
from trans_util import stkpush
from fert_util import stk_push
from datetime import datetime


app = Flask(__name__)
app.register_blueprint(daraja_callback_bp)
app.register_blueprint(transport_callback_bp)
app.register_blueprint(fertilizer_callback_bp)


# MongoDB setup
try:
    client = MongoClient("mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000")
    client.admin.command('ping')  # Check connection
    db = client.Kalro_db
    users = db.users
    sales = db.sales
    purchased=db.purchased

except Exception as e:
    print(f"Error connecting to MongoDB: {e}")
    users = None
    sales = None

# Your static data (same as before) — unchanged
locations = {
    "1": "Naivasha", "2": "Kitale", "3": "Thika", "4": "Muguga South", "5": "Mtwapa",
    "6": "Meru", "7": "Marsabit", "8": "Kibos", "9": "Kericho", "10": "Marigat"
}

offers = {
    "1": {"name": "DAP 18:46:00 10Kg", "price": 160},
    "2": {"name": "NPK 23:23:00 10Kg", "price": 660},
    "3": {"name": "CAN 26%N 10Kg", "price": 980},
    "4": {"name": "CAN 26%N 25Kg", "price": 2200},
    "5": {"name": "CAN 26%N 50Kg", "price": 3850},
    "6": {"name": "DAP 18:46:00 50Kg", "price": 6500},
    "7": {"name": "NPK 17:17:17 50Kg", "price": 6700}
}

produce = {
    "1": "Tomatoes",
    "2": "Cabbage",
    "3": "Onions",
    "4": "Sukumawiki",
    "5": "Spinach",
    "6": "Rice"
}

# Buy options
buy_options = {
    "1": {  # Tomatoes
        "1": {"qty": "50Kg", "price": 1},
        "2": {"qty": "100Kg", "price": 17000},
        "3": {"qty": "150Kg", "price": 25500}
    },
    "2":{ # cabbages
         "1": {"qty": "50Kg", "price": 2000},
         "2": {"qty": "100Kg", "price": 4000},
         "3": {"qty": "150Kg", "price": 6000}

    },
    "3":{ #onions
        "1": {"qty": "50Kg", "price": 6000},
        "2": {"qty": "100Kg", "price": 12000},  # fixed
        "3": {"qty": "150Kg", "price": 18000}
    },
    "4":{ #sukumawiki
        "1": {"qty": "50Kg", "price": 2500},
        "2": {"qty": "100Kg", "price": 5000},
        "3": {"qty": "150Kg", "price": 7500}
    
    },
    "5":{ #spinach
            "1": {"qty": "50Kg", "price": 15000},
            "2": {"qty": "100Kg", "price": 30000},
            "3": {"qty": "150Kg", "price": 45000}

    },
    "6":{ #rice
         "1": {"qty": "50Kg", "price": 7000},
         "2": {"qty": "100Kg", "price": 14000},
         "3": {"qty": "150Kg", "price": 21000}

    }
    # ... other produce definitions omitted for brevity, but follow same structure
}

# Sell options (starting with Tomatoes only for now)
sell_options = {
    "1": {  # Tomatoes
        "1": {"qty": "1Kg", "price": 170},
        "2": {"qty": "2Kg", "price": 340},
        "3": {"qty": "4Kg", "price": 680},
        "4": {"qty": "8Kg", "price": 1360},
        "5": {"qty": "16Kg", "price": 2240}
    },
    "2":{ #cabbages
        "1": {"qty": "1Kg", "price": 40},
        "2": {"qty": "2Kg", "price": 80}, 
        "3": {"qty": "4Kg", "price": 160}, 
        "4": {"qty": "8Kg", "price": 320}, 
        "5": {"qty": "16Kg", "price": 640}
        },
    "3":{ #onions
        "1": {"qty": "1Kg", "price": 100}, 
        "2": {"qty": "2Kg", "price": 200}, 
        "3": {"qty": "4Kg", "price": 400}, 
        "4": {"qty": "8Kg", "price": 800}, 
        "5": {"qty": "16Kg", "price": 1600}

    },
    "4":{ #sukumawiki
        "1": {"qty": "1Kg", "price": 50},
        "2": {"qty": "2Kg", "price": 100}, 
        "3": {"qty": "4Kg", "price": 200}, 
        "4": {"qty": "8Kg", "price": 400}, 
        "5": {"qty": "16Kg", "price": 800}
    },
    "5":{
        "1": {"qty": "1Kg", "price": 100}, 
        "2": {"qty": "2Kg", "price": 200}, 
        "3": {"qty": "4Kg", "price": 400}, 
        "4": {"qty": "8Kg", "price": 800}, 
        "5": {"qty": "16Kg", "price": 1600}
    },
    "6":{
        "1": {"qty": "1Kg", "price": 140}, 
        "2": {"qty": "2Kg", "price": 280}, 
        "3": {"qty": "4Kg", "price": 560}, 
        "4": {"qty": "8Kg", "price": 1120}, 
        "5": {"qty": "16Kg", "price": 2240}
    }

}

@app.route("/ussd", methods=["GET", "POST"])
def ussd():
    session_id = request.values.get("sessionId", "")
    service_code = request.values.get("serviceCode", "")
    phone_number = request.values.get("phoneNumber", "").strip().replace("+", "")
    text = request.values.get("text", "").strip()

    user_responses = text.split("*")
    level = len(user_responses)
    user_doc = users.find_one({"phone": phone_number})
    is_registered = user_doc is not None
    response = ""

    if text == "":
        if is_registered:
            response = (
                "CON Welcome back to KALRO!\n"
                "1. Log in\n"
                "2. Exit"
            )
        else:
            response = (
                "CON Welcome to KALRO.\n"
                "1. Register\n"
                "2. Exit"
            )

    elif is_registered and user_responses[0] == "1":  # Log in flow
        if level == 1:
            response = "CON Enter your 4-digit PIN:"
        elif level == 2:
            if user_responses[1] == user_doc.get("pin"):
                response = (
                    "CON Main Menu:\n"
                    "1. Seed & Fertilizer Offers\n"
                    "2. Buy Farm Produce\n"
                    "3. Sell Farm Produce\n"
                    "4. Transport Request."
                )
            else:
                response = "END Incorrect PIN."
        elif level >= 3:
            option = user_responses[2]

            # --- Seed & Fertilizer Offers ---
            if option == "1":
                # Level 3 -> display main offers menu
                if level == 3:
                    response = (
                        "CON Select an input:\n"
                        "1. DAP 18:46:00 10Kg - 160\n"
                        "2. NPK 23:23:00 10Kg - 660\n"
                        "3. CAN 26%N 10Kg - 980\n"
                        "4. CAN 26%N 25Kg - 2200\n"
                        "5. CAN 26%N 50Kg - 3850\n"
                        "00. More"
                    )
                elif level == 4:
                    choice = user_responses[3]
                    if choice == "00":
                        response = (
                            "CON More Offers:\n"
                            "6. DAP 18:46:00 50Kg - 6500\n"
                            "7. NPK 17:17:17 50Kg - 6700\n"
                            "00. Back"
                        )
                    elif choice in offers:
                        item = offers[choice]
                        response = (
                            f"CON You selected {item['name']} @ Ksh {item['price']}.\n"
                            "Would you like delivery for KES 350?\n"
                            "1. Yes\n"
                            "2. No"
                        )
                    else:
                        response = "END Invalid selection."
                elif level == 5 and user_responses[3]=="00":
                    # More offers selection
                    choice = user_responses[4]
                    if choice =="00":
                        #Go back to main main

                        response = (
                            "CON Select an input:\n"
                            "1. DAP 18:46:00 10Kg - 160\n"
                            "2. NPK 23:23:00 10kG - 660\n"
                            "3. CAN 26%N 10Kg - 980\n"
                            "4. CAN 26%N 25Kg - 2200\n"
                            "5. CAN 26%N 50Kg - 3850\n"
                            "00. More"
                        )
                    elif choice in offers:
                        item = offers[choice]
                        response = (

                            f"CON You selected {item['name']} @ Ksh {item['price']}.\n"
                            "Would you like delivery for KES 350?\n"
                            "1. Yes\n"
                            "2. No"
                        )
                    else:
                        response = "END Invalid selection."
                elif (
                            (level ==5 and user_responses[3] in offers) or
                            (level ==6 and user_responses[3]=="00" and user_responses[4] in offers)
                        ):
                    if level ==5:
                        choice = user_responses[3]
                        transport_choice = user_responses[4]
                    else:
                        choice = user_responses[4]
                        transport_choice = user_responses[5]

                    if choice not in offers:
                        response = "END Invalid input selection"
                    else:
                        item = offers[choice]
                        base_price = item["price"]
                        name = item["name"]

                        if transport_choice == "1":
                            transport_cost = 350
                            total_cost = base_price + transport_cost
                            transport_status = "included"
                            desc = f"Purchase of {name} with delivery"

                        elif transport_choice == "2":
                            transport_cost = 0
                            total_cost = base_price
                            transport_status = "declined"
                            desc = f"Purchase of {name} without delivery"
                        else:
                            response = "END Invalid selection."
                            return Response(response, mimetype="text/plain")
                        
                        #STK Push
                        mpesa_response = stk_push(
                            phone_number= phone_number,
                            amount=total_cost,
                            account_reference=name,
                            transaction_desc=desc,
                        )
                        if mpesa_response.get("ResponseCode")=="0":
                            purchased.insert_one({
                                "phone": phone_number,
                                "produce":name,
                                "quantity":"1Kg",
                                "price": base_price,
                                "transport_cost":transport_cost,
                                "total_cost": total_cost,
                                "transaction_desc": desc,
                                "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                "mpesa_checkout_request_id": mpesa_response.get("CheckoutRequestID"),
                                "mpesa_merchant_request_id": mpesa_response.get("MerchantRequestID"),
                                "mpesa_response_description": mpesa_response.get("ResponseDescription"),
                                "status":"pending",
                                "transport_checkout_status":transport_status
                            })
                            response = f"END STK Push sent for KES {total_cost}. Complete payment on your phone."
                        else:
                            response = "END Payment initiation failed. Try again later."
                    # --- Buy Farm Produce ---
            elif option == "2":
                if level == 3:
                    response = "CON Select produce:\n" + "\n".join([f"{k}. {v}" for k, v in produce.items()])
                elif level == 4:
                    prod_id = user_responses[3]
                    if prod_id in buy_options:
                        opts = buy_options[prod_id]
                        response = "CON Select quantity:\n" + "\n".join([f"{k}. {v['qty']} - Ksh {v['price']}" for k, v in opts.items()])
                    else:
                        response = "END Invalid produce."
                elif level == 5:
                        prod_id, qty_id = user_responses[3], user_responses[4]
                        opts = buy_options.get(prod_id, {})
                        if qty_id in opts:
                            item = opts[qty_id]
                            name = produce[prod_id]
                            response = (
                                f"CON Buy {item['qty']} {name} @ Ksh {item['price']}.\n"
                                "Would you like delivery at KES 350?\n"
                                "1. Yes\n"
                                "2. No"
                            )
                        else:
                            response = "END Invalid quantity."
                elif level == 6:

                    # User has answered the delivery question
                    prod_id, qty_id, transport_choice = user_responses[3], user_responses[4], user_responses[5]
                    opts = buy_options.get(prod_id, {})
                    item = opts.get(qty_id)
                    name = produce.get(prod_id)

                    # Safety check
                    if not item or not name:
                        response = "END Could not process your request. Try again later."
                    else:
                        base_price = item["price"]
                        if transport_choice == "1":
                            # Delivery requested
                            transport_cost = 0
                            total_cost = base_price + transport_cost
                            callbackurl = "https://2d5ee83c7454.ngrok-free.app/daraja/callback"

                            mpesa_response = lipa_na_mpesa_online(
                                phone_number=phone_number,
                                amount=total_cost,
                                account_reference=f"{name}_{item['qty']}",
                                transaction_desc=f"Purchase of {item['qty']} {name} with delivery",
                                callback= callbackurl
                              
                            )

                            if mpesa_response.get("ResponseCode") == "0":
                                # Record the pending sale + delivery
                                purchased.insert_one({
                                    "phone": phone_number,
                                    "produce": name,
                                    "quantity": item["qty"],
                                    "price": base_price,
                                    "transport_cost": transport_cost,
                                    "total_cost": total_cost,
                                    "transaction_desc": f"Purchase of {item['qty']} {name}",
                                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                    "mpesa_checkout_request_id": mpesa_response.get("CheckoutRequestID"),
                                    "mpesa_merchant_request_id": mpesa_response.get("MerchantRequestID"),
                                    "mpesa_response_description": mpesa_response.get("ResponseDescription"),
                                    "status": "pending",
                                    "transport_checkout_status": "included"
                                })
                                response = (
                                    f"END STK Push sent for KES {total_cost}. "
                                    "Complete payment on your phone. Delivery will be arranged."
                                )
                            else:
                                response = "END Payment initiation failed. Try again later."

                        elif transport_choice == "2":
                            # No delivery—pickup only
                            callbackurl = "https://2d5ee83c7454.ngrok-free.app/daraja/callback"
                            mpesa_response = lipa_na_mpesa_online(
                                phone_number=phone_number,
                                amount=base_price,
                                account_reference=f"{name}_{item['qty']}",
                                transaction_desc=f"Purchase of {item['qty']} {name} without delivery",
                                callback = callbackurl
                            )

                            if mpesa_response.get("ResponseCode") == "0":
                                purchased.insert_one({
                                    "phone": phone_number,
                                    "produce": name,
                                    "quantity": item["qty"],
                                    "price": base_price,
                                    "transport_cost": 0,
                                    "total_cost": base_price,
                                    "transaction_desc": f"Purchase of {item['qty']} {name}",
                                    "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                                    "mpesa_checkout_request_id": mpesa_response.get("CheckoutRequestID"),
                                    "mpesa_merchant_request_id": mpesa_response.get("MerchantRequestID"),
                                    "mpesa_response_description": mpesa_response.get("ResponseDescription"),
                                    "status": "pending",
                                    "transport_checkout_status": "declined"
                                })
                                response = (
                                    f"END STK Push sent for KES {base_price}. "
                                    "Complete payment on your phone. Pick up at your nearest KALRO center."
                                )
                            else:
                                response = "END Payment initiation failed. Try again later."

                        else:
                            response = "END Invalid selection."

            elif option == "3":
                if level == 3:
                    response = (
                        "CON Select produce to sell:\n"
                        "1. Tomatoes\n2. Cabbage\n3. Onions\n4. Sukumawiki\n5. Spinach\n6. Rice"
                    )

                elif level == 4:
                    prod_id = user_responses[3]
                    if prod_id in sell_options:
                        options = sell_options[prod_id]
                        response = "CON Select quantity:\n" + "\n".join(
                            [f"{k}. {v['qty']} - Ksh {v['price']}" for k, v in options.items()]
                        )
                    else:
                        response = "END Invalid produce selection."

                elif level == 5:
                    prod_id, qty_id = user_responses[3], user_responses[4]
                    produce_map = {
                        "1": "Tomatoes", "2": "Cabbage", "3": "Onions",
                        "4": "Sukumawiki", "5": "Spinach", "6": "Rice"
                    }

                    if prod_id in sell_options and qty_id in sell_options[prod_id]:
                        item = sell_options[prod_id][qty_id]
                        name = produce_map.get(prod_id, "Produce")
                        response = (
                            f"CON Confirm sale:\n{name} - {item['qty']} for Ksh {item['price']}\n"
                            "1. Confirm\n2. Cancel"
                        )
                    else:
                        response = "END Invalid selection."

                elif level == 6:
                    confirm = user_responses[5]
                    prod_id, qty_id = user_responses[3], user_responses[4]
                    item = sell_options.get(prod_id, {}).get(qty_id)
                    produce_map = {
                        "1": "Tomatoes", "2": "Cabbage", "3": "Onions",
                        "4": "Sukumawiki", "5": "Spinach", "6": "Rice"
                    }
                    name = produce_map.get(prod_id, "Produce")

                    if confirm == "1" and item:
                        sales.insert_one({
                            "phone": phone_number,
                            "produce": name,
                            "quantity": item["qty"],
                            "expected_price": item["price"],
                            "status": "available",
                            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        })
                        response = f"END Sale recorded for {item['qty']} {name} at Ksh {item['price']}."
                    else:
                        response = "END Sale cancelled."

                        

                                 #Transport logic
            elif  option == "4": 
                if level == 3:
                    
                    pending_items = list(purchased.find({
                        "phone": phone_number,
                        "status":"completed",
                        "transport_checkout_status":"declined"
                    }))
                    item_count = len(pending_items)

                    if item_count == 0:
                        response = "END You have no completed purchases awaiting delivery."
                    else:
                        if item_count == 1:
                            transport_cost = 1
                        elif 1 < item_count < 5:
                            transport_cost = 500
                        elif 5 <= item_count < 10:
                            transport_cost = 700
                        else:
                            transport_cost = 1250

                        lines = [f"CON You have {item_count} item(s) pending delivery:"]
                        for idx, item in enumerate(pending_items, start=1):
                            prod = item.get("produce", "Item")
                            qty = item.get("quantity", "Qty")
                            lines.append(f"{idx}. {prod} - {qty}")

                        lines.append(f"\nDelivery cost: KES {transport_cost}\n1. Pay now \n2. Cancel")

                        response = "\n".join(lines) 
                    
                elif level == 4 and user_responses[2] =="4":
                    transport_choice = user_responses[3]

                    pending_items = list(purchased.find({
                        "phone":phone_number,
                        "status":"completed",
                        "transport_checkout_status":"declined"
                    }))
                    item_count = len(pending_items)

                    if item_count == 0:
                        response = "END No pending deliveries found."

                    elif transport_choice == "1":
                        #determine transport cost
                        if item_count == 1:
                            transport_cost = 1
                        elif 1 < item_count < 5:
                            transport_cost= 500
                        elif 5 <= item_count < 10:
                            transport_cost = 700
                        else:
                            transport_cost = 1250

                        

                        mpesa_response = stkpush(
                            phone_number= phone_number,
                            amount=transport_cost,
                            account_reference="TransportRequest",
                            transaction_desc="Transport payment for produce delivery",
                       
                        
                        )

                        if mpesa_response.get("ResponseCode")=="0":
                            for item in pending_items:
                                purchased.update_one(
                                    {"_id":item["_id"]},
                                    {"$set":{
                                        "transport_checkout_status":"declined",
                                        "transport_checkout_request_id":mpesa_response.get("CheckoutRequestID"),
                                        "transport_request_time":datetime.now().strftime('Y-%m-%d %H:%M:%S'),
                                        "transport_item_count":item_count,
                                        "transport_cost":transport_cost
                                    }}
                                )
                            response = "END STK PUSH sent. Complete payment to arrange delivery."
                        else:
                            response = "END Payment initiation failed. Try again later."
                    elif transport_choice == "2":
                        response = "END Transport request cancelled. You can pick up from your nearest KALRO center."
                    else:
                        response = "END Invalid selection."
                


           
            
  
          
        
             

    elif not is_registered:
        if user_responses[0] == "1":  # Register flow
            if level == 1:
                response = "CON Enter your name:"
            elif level == 2:
                response = "CON Select your location:\n" + "\n".join([f"{k}. {v}" for k, v in locations.items()])
            elif level == 3:
                if user_responses[2] in locations:
                    response = "CON Create a 4-digit PIN:"
                else:
                    response = "END Invalid location."
            elif level == 4:
                name, location_key, pin = user_responses[1], user_responses[2], user_responses[3]
                if location_key in locations:
                    users.insert_one({
                        "phone": phone_number,
                        "name": name,
                        "location": locations[location_key],
                        "pin": pin
                    })
                    response = f"END Registration successful. Welcome, {name}!"
                else:
                    response = "END Invalid location."
        else:
            response = "END Thank you for visiting KALRO."

    else:
        response = "END Invalid input."

    return Response(response, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True)