import bcrypt
from .database import execute

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, password_hash: str) -> bool:
    return bcrypt.checkpw(password.encode(), password_hash.encode())

def authenticate(username: str, password: str):
    rows = execute("SELECT username, password_hash, role FROM users WHERE username=%s AND is_active=TRUE", (username,), True)
    if rows and verify_password(password, rows[0]["password_hash"]):
        return {"username": username, "role": rows[0]["role"]}
    return None
