from fastapi import APIRouter
import pprint

router = APIRouter(
    prefix = "/restaurant",
    tags = ["Restaurant"],
    responses = {404: {"message" : "Not found"}}
)

# Restaurant 
res_db = [
    {   #1
        "rest_id": "1",
        "rest_name" : "น้าไก่ไข่นุ่ม",
        "rest_location" : "ซอยเกกี 1",
        "rest_type" : "อาหารญี่ปุ่น",
        "rest_menu" : "ข้าวหมูทอดไข่นุ่ม , ข้าวห่อสาหร่าย",
        "rest_timeopen" : "17:00 – 22:00",
        "rest_tel"  : "087 673 3844"
    },
    {   #2
        "rest_id": "2",
        "rest_name" : "chefcommady",
        "rest_location" : "ซอยเกกี 2",
        "rest_type" : "อาหารจานเดียว",
        "rest_menu" : "เบอร์เกอร์, แกงกะหรี่, สปาเก็ตตี้",
        "rest_timeopen" : "8:30 – 24:00",
        "rest_tel"  : "090 699 4636"
    },
    {   #3
        "rest_id": "3",
        "rest_name" : "กะเพราบิลเลี่ยน",
        "rest_location" : "Billion Park",
        "rest_type" : "อาหารไทย",
        "rest_menu" : "กะเพรา",
        "rest_timeopen" : "16:30 – 4:00",
        "rest_tel"  : "082 998 9405"
    },
    {   #4
        "rest_id": "4",
        "rest_name" : "ข้าวมันไก่ป้าน้อย",
        "rest_location" : "Billion Park",
        "rest_type" : "อาหารตามสั่ง",
        "rest_menu" : "ข้าวหมกไก่",
        "rest_timeopen" : "10:00 – 2:00",
        "rest_tel"  : "088 623 9575, 063 676 7335"
    },
    {   #5
        "rest_id": "5",
        "rest_name" : "ไก่ทอดไฮโซ",
        "rest_location" : "499 ซอยฉลองกรุง 1",
        "rest_type" : "Street food, Fast food",
        "rest_menu" : "ไก่ทอด",
        "rest_timeopen" : "10:00 – 17:30",
        "rest_tel"  : "088 918 2062"
    },
    {   #6
        "rest_id": "6",
        "rest_name" : "นมมหาลัย",
        "rest_location" : "Billion Park",
        "rest_type" : "ขนมหวาน, เครื่องดื่ม",
        "rest_menu" : "โกโก้นมสดปั่น, ไอติมทอด",
        "rest_timeopen" : "17:00 – 23:30",
        "rest_tel"  : "098 829 8780"
    },
    {   #7
        "rest_id": "7",
        "rest_name" : "Dimple coffee",
        "rest_location" : "ซอยRNP",
        "rest_type" : "Coffee shop",
        "rest_menu" : "นมสดคาราเมล, ปังปิ้ง",
        "rest_timeopen" : "10:00 – 19:00",
        "rest_tel"  : "090 699 4636"
    },
    {   #8
        "rest_id": "8",
        "rest_name" : "ไข่หวานบ้านซูชิ",
        "rest_location" : "College Town",
        "rest_type" : "อาหารญี่ปุ่น",
        "rest_menu" : "ซูชิ, แซลม่อน",
        "rest_timeopen" : "12:00 – 22:00",
        "rest_tel"  : "083 788 4380"
    },
    {   #9
        "rest_id": "9",
        "rest_name" : "Long-Kin (กะเพราไข่ข้นชีสลาวา)",
        "rest_location" : "ซอยเกกี 4",
        "rest_type" : "อาหารไทย",
        "rest_menu" : "กะเพราไข่ข้นชีสลาวา",
        "rest_timeopen" : "12:00 - 21:00",
        "rest_tel"  : "085 727 7702 "
    },
    {   #10
        "rest_id": "10",
        "rest_name" : "หอมมนต์ (เตี๋ยวเรือต่อชาม)",
        "rest_location" : "ซอยเกกี 4",
        "rest_type" : "ก๋วยเตี๋ยว",
        "rest_menu" : "ก๋วยเตี๋ยวเรือ",
        "rest_timeopen" : "09:30 - 22:00",
        "rest_tel"  : "090 969 0502"
    }
]

#all restaurant
@router.get("/")
async def get_res():
    return res_db

#restaurant id sort by list
@router.get("/{res_id}/")
async def get_res_id(res_id : int):
    return res_db[res_id]

#Make a lot of effort
#search about restaurant
@router.get("/{about_res}/")
async def get_about_res(about_res : str):
    print("your about_res: "+about_res)
    res_list = res_db.split(":") 
    for i in res_list:
        if about_res in res_list:
            return res_db.index(i)

@router.get("/{rest_name}")
async def get_rest_name(rest_name : str):
    print("console rest_name is " + rest_name)
    count = -1
    for i in res_db:
        count = count + 1
        if i.get("rest_name") == rest_name:
            # pretty print dictionary [ref: https://datagy.io/python-pretty-print-dictionary/]
            pprint.pprint(res_db[count])
            return res_db[count]

    return {"error": rest_name};

@router.get("{rest_location}")
async def get_rest_location(rest_location : str):
    print("console rest_location is " + rest_location)
    count = -1
    data = []

    for i in res_db:
        count = count + 1
        if i.get("rest_location") == rest_location:
            data.append(res_db[count])

    pprint.pprint(data)
    return {"response": data}  
    

@router.get("/{token}")
async def get_token(token : str):
    token = "Mr. " + token;
    print("console token is " + token)
    return {"response": token};
