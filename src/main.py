from fastapi import FastAPI

from src.views import router as items_router
from src.bootstrap import init


init()
app = FastAPI()
app.include_router(items_router)


@app.get("/")
async def hello_world():
    return {"Hello": "world!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
