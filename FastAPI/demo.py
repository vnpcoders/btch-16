from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI



#define a pydantic model for request validataion
class Item(BaseModel):
    name:str
    price:float
    isOffer:bool=False

@app.get('/')
def read_out():
    return{"message":"welcome to FastAPI tutorial"}
