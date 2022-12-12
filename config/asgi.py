import os
from importlib.util import find_spec

from django.apps import apps
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.wsgi import WSGIMiddleware
from fastapi.staticfiles import StaticFiles

# Export Django settings env variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
apps.populate(settings.INSTALLED_APPS)

# This endpoint imports should be placed below the settings env declaration
# Otherwise, django will throw a configure() settings error
from config.fast_api_router import router as fast_api_router
#
# Get the Django WSGI application we are working with
django_wsgi_app = get_wsgi_application()

# This can be done without the function, but making it functional
# tidies the entire code and encourages modularity
def get_application() -> FastAPI:
    # Main Fast API application
    app = FastAPI(
        title="Fast API Django Pet Store",
        openapi_url="/fast-api/openapi.json",
        docs_url=f"/fast-api/docs",
        debug=settings.DEBUG
    )

    # Set all CORS enabled origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include all api endpoints
    app.include_router(fast_api_router, prefix="/fast-api")

    app.mount(f"/web", WSGIMiddleware(django_wsgi_app))
    # Set Up the static files and directory to serve django static files
    app.mount("/static", StaticFiles(directory=settings.STATIC_ROOT), name="static")

    return app


app = get_application()
