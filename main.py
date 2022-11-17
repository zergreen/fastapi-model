from fastapi import FastAPI
from pydantic import BaseModel
from routers import restaurant
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(restaurant.router)

@app.get("/")
async def root():
    return {"ทดสอบการทำข้อมูล"}

origins = [
    "http://localhost:3050"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)