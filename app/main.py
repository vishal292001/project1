
from fastapi import FastAPI
import uvicorn
from pymongo import MongoClient
from pydantic import BaseModel
import test

app = FastAPI()

client = MongoClient("mongodb://database:27017")
print("Connection Successfullll")

class SearchUser(BaseModel):
    item_id: int



@app.get("/")
def read_root():
    return {"Hello": "This is my first database api"}

@app.post("/read")

async def read(item: SearchUser):
    item = item.dict()
    print(">>>>>>>>>>>>>>>>>>>>>>",item)
    db = client["example"]
    col = db["Videos"]
    x = col.find({'_id':item['item_id']})
    for data in x:
        return data
 


if __name__== '__main__':
    uvicorn.run(app, port = 8081, host= "0.0.0.0")