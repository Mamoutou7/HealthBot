from fastapi import FastAPI
from app.api.routes_healthbot import router


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    Returns:
        FastAPI: Configured FastAPI instance.
    """

    app = FastAPI(
        title="HealthBot AI",
        version="1.0.0"
    )

    app.include_router(router, prefix="/api")

    return app


app = create_app()