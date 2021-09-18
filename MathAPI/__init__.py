from MathAPI.routers import armstrong, database, numbersystem, pallindrome, strong
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

def custom_openai():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(title="MathAPI", version=1.0, routes=app.routes, description="API Application to perform mathimatical operations")
    app.openapi_schema = openapi_schema
    return openapi_schema

app.openapi = custom_openai

app.include_router(numbersystem.router)
app.include_router(database.router)
app.include_router(armstrong.router)
app.include_router(pallindrome.router)
app.include_router(strong.router)



