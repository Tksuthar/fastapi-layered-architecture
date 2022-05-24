from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from application.routers import notes

tags_metadata = [{"name": "Notes", "description": "APIs to CRUD notes"}]
app = FastAPI(
    title="React App Backend",
    description="This project provides APIs for the demo react app",
    version="0.1.0",
    openapi_tags=tags_metadata,
)

app.include_router(
    notes.router,
    prefix="/notes",
    tags=["Notes"],
    responses={404: {"description": "Not found"}},
)


@app.get("/", tags=["Redirects"], include_in_schema=False)
def redirect_root_to_docs():
    """Redirects / to /docs"""
    return RedirectResponse(url="/docs")

# addded this comment here
