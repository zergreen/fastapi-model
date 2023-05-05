from fastapi import FastAPI
from pydantic import BaseModel
from routers import restaurant
from fastapi.middleware.cors import CORSMiddleware
import json

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

@app.get("/hello")
async def hello():
    return {"helloooo"}

@app.get("/xss-params")
async def xss(cookie:str):
    f = open("xss-cookie.txt", "a")
    f.write(f"cookies : {cookie} \n")
    f.close()
    return {f"cookies : {cookie}"}

@app.get("/see-cookies")
async def seecookie():
    f = open("xss-cookie.txt", "r")
    return {f.read()}
