from fastapi import FastAPI , Path, Query , Body
from pydantic import BaseModel , HttpUrl
from typing import Optional


app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello world"}


class Image(BaseModel):
    url : HttpUrl
    description : str





class Item(BaseModel):
    name : str 
    price  : Optional[float] = None
    Quantity : int
    image : Image

class Product(BaseModel):
    item : Item
    image : Image

@app.put("/items/{item_id}")
async def update_item(item_id , item : Item):
    result = {"item_id" : item_id ,
                "item" : item }
    return result



@app.post("/product/{item_id}")
async def add_product(item : Item ,image: Image):
    result = {"item" : item ,
                "Image" : image }
    return {"result" : result}
