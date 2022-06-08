from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/q/")
async def dynamic_query_params(request: Request):
    return request.query_params
