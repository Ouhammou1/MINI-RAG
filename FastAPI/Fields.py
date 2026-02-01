from fastapi import FastAPI , Path, Query , Body
from pydantic import BaseModel , Field
from typing  import     Optional
app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}


class Item(BaseModel):
    name  :str
    description :Optional[str]  = Field(None , title="this is the descrption " , max_length=300)
    price : float = Field(..., title = "the price nust be gt then zero ", gt=0)
    tax : float = Field(...)



@app.put("/items/{item_id}")
async def update(item_id : int , item: Item = Body(..., embed=True)):
    result = {"item_id" : item_id,
            "item" : item}

