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
        "name" : "น้าไก่ไข่นุ่ม",
        "location" : "ซอยเกกี 1",
        "ประเภทอาหาร" : "อาหารญี่ปุ่น",
        "เมนูแนะนำ" : "ข้าวหมูทอดไข่นุ่ม , ข้าวห่อสาหร่าย",
        "เวลาเปิด-ปิด" : "17:00 – 22:00",
        "เบอร์โทรติดต่อ"  : "087 673 3844"
    },
    {   #2
        "name" : "chefcommady",
        "location" : "ซอยเกกี 2",
        "ประเภทอาหาร" : "อาหารจานเดียว",
        "เมนูแนะนำ" : "เบอร์เกอร์, แกงกะหรี่, สปาเก็ตตี้",
        "เวลาเปิด-ปิด" : "8:30 – 24:00",
        "เบอร์โทรติดต่อ"  : "090 699 4636"
    },
    {   #3
        "name" : "กะเพราบิลเลี่ยน",
        "location" : "Billion Park",
        "ประเภทอาหาร" : "อาหารไทย",
        "เมนูแนะนำ" : "กะเพรา",
        "เวลาเปิด-ปิด" : "16:30 – 4:00",
        "เบอร์โทรติดต่อ"  : "082 998 9405"
    },
    {   #4
        "name" : "ข้าวมันไก่ป้าน้อย",
        "location" : "Billion Park",
        "ประเภทอาหาร" : "อาหารตามสั่ง",
        "เมนูแนะนำ" : "ข้าวหมกไก่",
        "เวลาเปิด-ปิด" : "10:00 – 2:00",
        "เบอร์โทรติดต่อ"  : "088 623 9575, 063 676 7335"
    },
    {   #5
        "name" : "ไก่ทอดไฮโซ",
        "location" : "499 ซอยฉลองกรุง 1",
        "ประเภทอาหาร" : "Street food, Fast food",
        "เมนูแนะนำ" : "ไก่ทอด",
        "เวลาเปิด-ปิด" : "10:00 – 17:30",
        "เบอร์โทรติดต่อ"  : "088 918 2062"
    },
    {   #6
        "name" : "นมมหาลัย",
        "location" : "Billion Park",
        "ประเภทอาหาร" : "ขนมหวาน, เครื่องดื่ม",
        "เมนูแนะนำ" : "โกโก้นมสดปั่น, ไอติมทอด",
        "เวลาเปิด-ปิด" : "17:00 – 23:30",
        "เบอร์โทรติดต่อ"  : "098 829 8780"
    },
    {   #7
        "name" : "Dimple coffee",
        "location" : "ซอยRNP",
        "ประเภทอาหาร" : "Coffee shop",
        "เมนูแนะนำ" : "นมสดคาราเมล, ปังปิ้ง",
        "เวลาเปิด-ปิด" : "10:00 – 19:00",
        "เบอร์โทรติดต่อ"  : "090 699 4636"
    },
    {   #8
        "name" : "ไข่หวานบ้านซูชิ",
        "location" : "College Town",
        "ประเภทอาหาร" : "อาหารญี่ปุ่น",
        "เมนูแนะนำ" : "ซูชิ, แซลม่อน",
        "เวลาเปิด-ปิด" : "12:00 – 22:00",
        "เบอร์โทรติดต่อ"  : "083 788 4380"
    },
    {   #9
        "name" : "Long-Kin (กะเพราไข่ข้นชีสลาวา)",
        "location" : "ซอยเกกี 4",
        "ประเภทอาหาร" : "อาหารไทย",
        "เมนูแนะนำ" : "กะเพราไข่ข้นชีสลาวา",
        "เวลาเปิด-ปิด" : "12:00 - 21:00",
        "เบอร์โทรติดต่อ"  : "085 727 7702 "
    },
    {   #10
        "name" : "หอมมนต์ (เตี๋ยวเรือต่อชาม)",
        "location" : "ซอยเกกี 4",
        "ประเภทอาหาร" : "ก๋วยเตี๋ยว",
        "เมนูแนะนำ" : "ก๋วยเตี๋ยวเรือ",
        "เวลาเปิด-ปิด" : "09:30 - 22:00",
        "เบอร์โทรติดต่อ"  : "090 969 0502"
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
        if i.get("name") == rest_name:
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
        if i.get("location") == rest_location:
            # pretty print dictionary [ref: https://datagy.io/python-pretty-print-dictionary/]
            data.append(res_db[count])

    pprint.pprint(data)
    return {"response": data}  
    

@router.get("/{green_res}")
async def get_green_res(green_res : str):
    green_res = "Mr. " + green_res;
    print("console green_res is " + green_res)
    return {"response": green_res};
