from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix = "/user",
    tags = ["User"],
    responses = {404: {"message": "Not found"}}
)

user_db = [
    {
        "name": "Tle"
    },
    {
        "name": "Tle"
    },
    {
        "name": "Ing"
    },
    {
        "name": "Pear"
    },
    {
        "name": "Cheer"
    }
]

class User(BaseModel):
    name : str

@router.get("/")
async def get_users():
    return user_db


@router.get("/{user_id}")
async def get_user(user_id : int):
    return user_db[user_id - 1]

@router.post("/")
async def create_user(user : User):
    result = user.dict()
    user_db.append(result)
    return user_db[-1]

@router.put("/{user_id}")
async def edit_user(user_id : int, user : User):
    result = user.dict()
    user_db[user_id - 1].update(result)
    return result

@router.delete("/{user_id}")
async def edit_user(user_id : int):
    user = user_db.pop(user_id - 1)
    return user