from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def get():
    return {"message" , "hello there "}

items = [
    {"id":1 , "name":"book" , "price":"15" , "stock": True},
    {"id":2 , "name":"game" , "price":"50" , "stock": True},
    {"id":3 , "name":"cd" , "price":"30" , "stock": True},
    {"id":4 , "name":"magazine" , "price":"10" , "stock": False},
    {"id":5 , "name":"book" , "price":"10" , "stock": True},
    {"id":6 , "name":"game" , "price":"10" , "stock": True}
]



@app.get("/items")
async def list_iterms(start : int =0 , end :int  =10, id : int =None):
    if id:
        item = next((item  for item in items if item["id"]==id),None)
        if item:
            return item
        else:
            return {"message" , "item not found"}
    return items[start:start + end]