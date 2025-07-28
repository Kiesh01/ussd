# mpesa_utils.py

import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64

# Daraja API credentials (replace with your actual values)
MPESA_CONSUMER_KEY = 'saGKlOkn1FOGUGgcBtbrQMLSdslYsVdqAKYw4FdM0S5cC8zk'
MPESA_CONSUMER_SECRET = '1bogQLHNKBCSD8Ylx4f1ALqQbAtMaxQCiYmbGu79vaRTGPjBmdR26sZDX5D3btBD'
MPESA_SHORTCODE = '174379'
MPESA_PASSKEY = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"



def get_access_token():
    url = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    response = requests.get(url, auth=HTTPBasicAuth(MPESA_CONSUMER_KEY, MPESA_CONSUMER_SECRET))
    access_token = response.json().get('access_token')
    return access_token

def stk_push(phone_number, amount, account_reference, transaction_desc):
    access_token = get_access_token()

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    data_to_encode = MPESA_SHORTCODE + MPESA_PASSKEY + timestamp
    encoded_password = base64.b64encode(data_to_encode.encode()).decode('utf-8')

    stk_push_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
   
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        
    }

    payload = {
        "BusinessShortCode": MPESA_SHORTCODE,
        "Password": encoded_password,
        "Timestamp": timestamp,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": '254708374149',
        "PartyB": MPESA_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": "https://2d5ee83c7454.ngrok-free.app/fertilizer/callback",
        "AccountReference": account_reference,
        "TransactionDesc": transaction_desc,
        
    }

    response = requests.post(stk_push_url, json=payload, headers=headers)
    data = response.json()

    print("MPESA STK Push Response:", data)
    return data