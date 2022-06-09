from fastapi import FastAPI, Path, Query

app = FastAPI()


# float 검증
@app.get("/items/{item_id}")
async def read_items(
        *,
        item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
        q: str,
        size: float = Query(gt=0, lt=10.5)
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 숫자 검증
@app.get("/items/{item_id}")
async def read_items(
        *, item_id: int = Path(title="The ID of the item to get", ge=1, le=100), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


# 매개변수 전달
@app.get("/items/{item_id}")
async def read_items(*, item_id: int = Path(title="The ID of the item to get"), q: str):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results


@app.get('/items/{item_id}')
async def read_items(
        item_id: int = Path(title='The ID if item to get', default=...),
        q: str | None = Query(default=None, alias='item-query')
):
    results = {'item_id': item_id}
    if q:
        results.update({'q': q})
    return results
