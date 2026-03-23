from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes_feedback import router as feedback_router
from app.api.routes_health import router as health_router
from app.core.config import settings
from sqlalchemy.exc import OperationalError
from app.core.database import Base, engine
from app.models.feedback import Feedback  # Ensure model is registered in metadata.


app = FastAPI(title=settings.app_name)

app.add_middleware(
    
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    # For Step 1 we create tables automatically to keep setup simple.
    # Later steps (Docker/K8s) will use migrations.
    try:
        Base.metadata.create_all(bind=engine)
    except OperationalError as exc:
        # Keep the service running so you can hit /health and debug config,
        # while /feedback endpoints will fail until DB creds are correct.
        print(f"[startup] Could not connect to PostgreSQL: {exc}")


@app.get("/")
def root():
    return {"message": "Feedback API is running"}


app.include_router(health_router)
app.include_router(feedback_router)

