from fastapi import APIRouter
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

from .config import get_settings
from .service import make_greeting

router = APIRouter()

REQUESTS = Counter("app_requests_total", "Total HTTP requests", ["path"])

@router.get("/healthz")
def healthz():
    REQUESTS.labels(path="/healthz").inc()
    return {"status": "ok"}

@router.get("/greet")
def greet():
    REQUESTS.labels(path="/greet").inc()
    settings = get_settings()
    return make_greeting(settings["GREETING_TARGET"])

@router.get("/metrics")
def metrics():
    # Prometheus-format
    REQUESTS.labels(path="/metrics").inc()
    data = generate_latest()
    return data, 200, {"Content-Type": CONTENT_TYPE_LATEST}