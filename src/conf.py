import os

class Config:
    INFECTION_MONKEY_URL = os.getenv("INFECTION_MONKEY_URL") or "https://10.0.12.81:5000"
    INFECTION_MONKEY_USER = os.getenv("INFECTION_MONKEY_USER") or "admin"
    INFECTION_MONKEY_PASSWORD = os.getenv("INFECTION_MONKEY_PASSWORD") or "admin"

config = Config()