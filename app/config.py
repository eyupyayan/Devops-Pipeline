import os

def get_settings():
    return {
        "APP_NAME": os.getenv("APP_NAME", "devops-lab"),
        "GREETING_TARGET": os.getenv("GREETING_TARGET", "Batman"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "info"),
    }