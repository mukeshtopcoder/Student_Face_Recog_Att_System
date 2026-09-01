import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    db_host: str = os.getenv("DB_HOST", "localhost")
    db_port: int = int(os.getenv("DB_PORT", "3306"))
    db_user: str = os.getenv("DB_USER", "root")
    db_password: str = os.getenv("DB_PASSWORD", "")
    db_name: str = os.getenv("DB_NAME", "cv_attendance")
    face_tolerance: float = float(os.getenv("FACE_TOLERANCE", "0.48"))
    face_model: str = os.getenv("FACE_MODEL", "hog")

settings = Settings()
