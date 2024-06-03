from fastapi import FastAPI
from app.api.endpoints.health import health
from app.api.endpoints.files import files

app = FastAPI(
    debug=True,
    title="Files Management API",
)

app.include_router(health.router)
app.include_router(files.router)

