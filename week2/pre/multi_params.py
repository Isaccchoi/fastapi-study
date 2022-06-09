from fastapi import FastAPI, Path, Body
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


# 단일 항목에서도 embed를 사용시 key와 같이 들어와야합니다.
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


# body parameter 와 query 섞기 가능
@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item: Item,
        user: User,
        importance: int = Body(gt=0),
        q: str | None = None
):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results


# body parameter 단일 변수 가져오는 방법
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, user: User, importance: int = Body()):
    results = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return results


""" body값 추가로 가져오는 방법
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}
"""


# multiple body paremeter
@app.put('/items/{item_id}')
async def update_item(item_id: int, item: Item, user: User):
    results = {'item_id': item_id, 'item': item, 'user': user}
    return results


""" Parameter name을 Key로 쓸 수 있음
{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}
"""


# mixed Path, Query body parameter
@app.put('/items/{item_id}/')
async def update_item(
        *,
        item_id: int = Path(title='The ID of the item to get', ge=0, le=1000),
        q: str | None = None,
        item: Item | None = None
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    if item:
        results.update({'item': item})
    return results
