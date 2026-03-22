import os, json
import firebase_admin
from firebase_admin import credentials, firestore

# Load JSON string from environment variable
firebase_credentials_json = os.getenv("FIREBASE_CREDENTIALS_JSON")

if firebase_credentials_json:
    creds_dict = json.loads(firebase_credentials_json)
    cred = credentials.Certificate(creds_dict)

    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)

    db = firestore.client()
else:
    raise RuntimeError("FIREBASE_CREDENTIALS_JSON not set in environment")
