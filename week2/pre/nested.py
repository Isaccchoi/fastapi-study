from fastapi import FastAPI, Body
from pydantic import BaseModel, HttpUrl

app = FastAPI()


class Image(BaseModel):
    url: HttpUrl # url 검증
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    # tags: list[int] = [] # list 형태
    tags: set[str] = set()  # set 형태
    # image: Image | None = None  # sub model 형태
    images: list[Image] | None = None  # list of submodel


@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {'item_id': item_id, 'item': item}
    return results

#
# # 좀더 복잡한 형태의 Nested Model도 가능
# class Image(BaseModel):
#     url: HttpUrl
#     name: str
#
#
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#     tags: set[str] = set()
#     images: list[Image] | None = None
#
#
# class Offer(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     items: list[Item]
#
#
# @app.post("/offers/")
# async def create_offer(offer: Offer):
#     return offer


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    return weights
