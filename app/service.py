from datetime import datetime, timezone

def make_greeting(target: str) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    msg = f"Hello, {target}!"
    return {"message": msg, "time_utc": now}