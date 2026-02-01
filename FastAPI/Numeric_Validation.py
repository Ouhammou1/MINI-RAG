from fastapi import FastAPI , Path, Query

app = FastAPI()


@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get('/items/{item_id}')
async def  get_item(item_id:int =Path(... , ge=1 , le=210),
                    title="item_id" ,
                    description="the item id must be greater than or equal 1" ):
    return {"item id":item_id}


@app.get("items/")
async def get_items(
        min_price : float = Query(... , ge=1 , description="price must be greater than 0 " ),
        max_price : float = Query(... , le=1000 , description="price must be less than or equal 1000" )
        ):
        return {"min_price" : min_price,
                "max_price" : max_price}