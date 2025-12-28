from app.core.config import SECRET_KEY, ALGORITHM
from datetime import datetime, timedelta
from jose import jwt, JWTError



ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    print("JWT CREATE SECRET:", SECRET_KEY)
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


