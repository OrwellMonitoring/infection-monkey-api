import os

class Config:
    INFECTION_MONKEY_URL = os.getenv("INFECTION_MONKEY_URL") or "https://localhost:5000"
    INFECTION_MONKEY_USER = os.getenv("INFECTION_MONKEY_USER") or "admin"
    INFECTION_MONKEY_PASSWORD = os.getenv("INFECTION_MONKEY_PASSWORD") or "adin"
    INFECTION_MONKEY_CONFIG = os.getenv("INFECTION_MONKEY_CONFIG") or "../config/monkey.conf"

config = Config()