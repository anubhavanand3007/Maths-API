from MathAPI.routers import armstrong, pallindrome, strong
from fastapi import FastAPI
from .routers import armstrong

app = FastAPI()

app.include_router(armstrong.router)
app.include_router(pallindrome.router)
app.include_router(strong.router)



