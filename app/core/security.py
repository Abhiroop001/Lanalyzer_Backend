from passlib.context import CryptContext
from jose import jwt
from app.config import settings
from datetime import datetime, timedelta

# Configure Passlib with bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using bcrypt.
    Bcrypt only supports up to 72 bytes, so truncate if necessary.
    """
    if len(password.encode("utf-8")) > 72:
        password = password[:72]
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a password against its hash.
    Truncate if longer than 72 bytes to match bcrypt behavior.
    """
    if len(password.encode("utf-8")) > 72:
        password = password[:72]
    return pwd_context.verify(password, hashed)

def create_token(data: dict) -> str:
    """
    Create a JWT access token with 24h expiry.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
