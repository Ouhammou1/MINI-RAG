from fastapi import FastAPI
from fastapi import Query
app = FastAPI()

@app.get("/")
async def root():
    return {"message" : "hello"}


@app.get("/items")
async def read_items(name:str = "Unknown"):
    return {"name" :name}




@app.get("/validate")
async def validate_item(name :str = Query(... , min_length=3 , max_length=50, regex="^[a-zA-Z\s]"),
                        email: str = Query (..., max_length=100   )):
    return{ "name" : name,
            "Email": email}