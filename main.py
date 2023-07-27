from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None
  
class User(BaseModel):
  name: str
  age: int
  country: str

class ModelName(str, Enum):
  rahman = "rahman"
  alex = "alex"
  jurig = "jurig"

@app.get("/models/{model_name}")
async def models(model_name: ModelName):
  if model_name is ModelName.rahman:
    return {"model_name": model_name, "message": "Programming Enthusiast"}
  if model_name is ModelName.alex:
    return {"model_name": model_name, "message": "Pembohong handal"}
  if model_name is ModelName.jurig:
    return {"model_name": model_name, "message": "Ghosting orang"}

@app.get("/users/me")
async def user_me():
  return {"user_id": 666, "name": "Rahman", "country": "Indonesia"}

@app.get("/users")
async def users():
  return ["Rahman", "Jenskin", "Udin"]

@app.get("/users/{user_id}")
async def user_me(user_id: int):
  return {"user_id": user_id}

@app.put("/users/{user_id}")
async def user_me(user_id: int, user: User):
  return {"user_id": user_id, "name": user.name, "country": user.country}

@app.get("/")
async def read_root():
  return {"Hello" : "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q : Union[str, None] = None):
  return {"item_id" :  item_id, "q" : q}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
  return {"item_id" : item_id ,"item_name" : item.name, "item_price": item.price, "is_offer": item.is_offer}