from fastapi import FastAPI, Body
from pydantic import BaseModel, Field

app = FastAPI()


# # Config에 schema extra 넣는 형태
# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "name": "Foo",
#                 "description": "A very nice",
#                 "price": 35.2,
#                 "tax": 3.2
#             }
#         }

# # Field를 이용해 example을 넣는 형태 => 이게 제일 편해보이나 Field에 내용이 많이 들어갈 경우 복잡해질 수 있음
# class Item(BaseModel):
#     name: str = Field(example="Foo")
#     description: str | None = Field(default=None, example='a very nice')
#     price: float = Field(example=35.2)
#     tax: float | None = Field(defalt=None, example=1.1)


# class Item(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None
#
#
# # 컨트롤러에 들어가는 형태, 한 컨트롤러에만 보여서 같은 거를 여러번 적용하거나 할 필요가 있음, 상황에 따라 괜찮을지도?
# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item = Body(
#         example={
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 35.4,
#             "tax": 3.2,
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# 여러 종류의 example을 한번에 보여줄 수 있음 
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results