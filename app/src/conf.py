import os

class Config:
    INFECTION_MONKEY_URL = os.getenv("INFECTION_MONKEY_URL") or "https://10.0.13.181:5000"
    INFECTION_MONKEY_USER = os.getenv("INFECTION_MONKEY_USER") or "admin"
    INFECTION_MONKEY_PASSWORD = os.getenv("INFECTION_MONKEY_PASSWORD") or "adin"
    INFECTION_MONKEY_CONFIG = os.getenv("INFECTION_MONKEY_CONFIG") or "../config/"
    BROWSER_PORT = os.getenv("BROWSER_PORT") or 4444
config = Config()