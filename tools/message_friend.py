import requests

def message_friend(emotion: str):
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    PHONE_NUMBER_ID = "YOUR_PHONE_NUMBER_ID"

    url = f"https://graph.facebook.com/v23.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "messaging_product": "whatsapp",
        "to": "923001234567",  # recipient in international format
        "type": "text",
        "text": {
            "body": (
                "Emergency alert: Ali asked that you be notified. "
                "Please check on them as soon as possible."
            )
        },
    }

    response = requests.post(
        url,
        headers=headers,
        json=payload,
        timeout=30,
    )

    print("Status:", response.status_code)
    print("Response:", response.json())
    return response

