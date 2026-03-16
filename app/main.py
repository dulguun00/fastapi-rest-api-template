from fastapi import FastAPI

from app.api.routes import auth, items
from app.db.session import Base, engine
from app.models import item, user


app = FastAPI(title="FastAPI REST API Template")

Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(items.router, prefix="/items", tags=["items"])


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
