import os, json
from dotenv import load_dotenv
from google.oauth2 import service_account
from google.cloud import firestore

load_dotenv()

class Settings:
    APP_NAME = "AI Legislative Analyzer"
    VERSION = "1.0.0"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    SECRET_KEY = os.getenv("SECRET_KEY", "Sukanya")
    ALGORITHM = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES = 60
    SCALEDOWN_API_KEY = os.getenv("SCALEDOWN_API_KEY")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    FIREBASE_CREDENTIALS_JSON = os.getenv("FIREBASE_CREDENTIALS_JSON")  # JSON string
    UPLOAD_DIR = "uploads"
    MAX_FILE_SIZE_MB = 50
    MAX_DOCUMENT_TOKENS = 200000

settings = Settings()

# Parse credentials
creds_dict = json.loads(settings.FIREBASE_CREDENTIALS_JSON)
credentials = service_account.Credentials.from_service_account_info(creds_dict)

db = firestore.Client(credentials=credentials, project=creds_dict["project_id"])
