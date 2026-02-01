from fastapi import FastAPI , Path, Query , Body
from pydantic import BaseModel
from typing import Optional


app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello world"}

class Item(BaseModel):
    name :str
    description : str
    price : float

class User(BaseModel):
    username: str
    full_name : str

class Age(BaseModel):
        age :int 

@app.put('/item/{item_id}')
async def  update_item(
        *,
        item_id : int = Path(..., title="the item id " , ge =0 ,le=100),
        q : Optional[str] = None,
        item : Optional[Item] = None,
        user : Optional[User] = None  ,
        age : Optional[Age] = Body(None)
            ):
        result = {"item_id" : item_id}
        if q:
            result.update({"q" : q})
        if item:
            result.update({"item" : item})
        if user:
            result.update({"user" : user})
        if age:
            result.update({"age" : age})
        
        return result
