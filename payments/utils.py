import base64
from datetime import datetime
import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth

def get_mpesa_access_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET

    response = requests.get(url, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print("🔴 Failed to get M-Pesa access token:", response.text)
        raise Exception("Failed to get M-Pesa access token")

def send_stk_push_request(order):
    try:
        access_token = get_mpesa_access_token()
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        password = base64.b64encode(
            (settings.MPESA_SHORTCODE + settings.MPESA_PASSKEY + timestamp).encode()
        ).decode('utf-8')

        headers = {
            "Authorization": f"Bearer {access_token}",
            "Content-Type": "application/json"
        }

        payload = {
            "BusinessShortCode": settings.MPESA_SHORTCODE,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": int(order.get_total_cost()),  # make sure this works
            "PartyA": "254708374149",  # Sandbox test number only
            "PartyB": settings.MPESA_SHORTCODE,
            "PhoneNumber": "254708374149",
            "CallBackURL": settings.MPESA_CALLBACK_URL,
            "AccountReference": f"ORDER{order.id}",
            "TransactionDesc": "Order Payment"
        }

        response = requests.post(
            "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest",
            headers=headers,
            json=payload
        )

        data = response.json()
        print("📦 STK Push Response:", data)  # Debug output

        if data.get("ResponseCode") == "0":
            print("✅ STK push initiated successfully.")
            return True
        else:
            print("❌ STK push failed with response:", data)
            return False

    except Exception as e:
        print("⚠️ Error during STK push:", str(e))
        return False
