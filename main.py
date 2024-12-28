from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    tax: Optional[float] = None


app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello, World!"}


@app.get("/countries/{country_name}")
def get_country(country_name: str):
    return {"country_name": country_name}


# クエリパラメーター
@app.get("/countries/")  # 引数を書かない
def get_country(country_name: str = "japan"):  # デフォルト値を設定
    return {"country_name": country_name}


# オプショナルパラメーター
@app.get("/countries/")
def get_country(country_name: Optional[str] = None):  # 必須ではない設定にする方法
    return {"country_name": country_name}


@app.post("/items/")
def create_item(item: Item):
    return {"message": f"{item.name}は、税込み{item.price * item.tax}円です。"}
