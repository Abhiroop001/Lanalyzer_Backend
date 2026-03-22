from passlib.context import CryptContext
from jose import jwt
from app.config import settings
from datetime import datetime, timedelta

# Use Argon2 instead of bcrypt
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using Argon2.
    Argon2 supports long passwords without the 72-byte limit.
    """
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """
    Verify a password against its Argon2 hash.
    """
    return pwd_context.verify(password, hashed)

def create_token(data: dict) -> str:
    """
    Create a JWT access token with 24h expiry.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(hours=24)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
