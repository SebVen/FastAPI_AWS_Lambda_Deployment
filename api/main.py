from mangum import Mangum
from fastapi import FastAPI
from .routers import convert_length_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app=app)