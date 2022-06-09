from fastapi import FastAPI, Cookie, Header

app = FastAPI()

# 헤더
# @app.get("/items/")
# async def read_items(user_agent: str | None = Header(default=None, )):
#     return {"User-Agent": user_agent}


# 중복 헤더
@app.get("/items/")
async def read_items(x_token: list[str] | None = Header(default=None)):
    return {"X-Token values": x_token}
