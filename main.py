#  __________________
#  Import LIBARIES
from fastapi import FastAPI
from enum import Enum
#  Import FILES
#  __________________


class Fruit(Enum):
    apple = "apple"
    banana = "banana"
    orange = "orange"


app = FastAPI(
    title="FastAPI Tutorial",
    description="This is a pretty simple tutorial",
    summary="Not sure what this is!!!",
    version="1.0.0",
)


@app.get("/")
def index() -> dict[str, str]:
    return {"Hello": "World"}


@app.post("/")
def index_post() -> dict[str, str]:
    return {"message": "Post request"}


@app.put("/")
def index_put() -> dict[str, str]:
    return {"message": "Put request"}


@app.delete("/")
def index_delete() -> dict[str, str]:
    return {"message": "Delete request"}


# @app.get("/items/2")
# async def get_item_2() -> dict[str, int]:
#     return {"message": "Invalid"}


@app.get("/items/{item_id}")
async def get_item(item_id: int) -> dict[str, int]:
    return {"Hello": item_id}


@app.get("/items/2")
async def get_item_2() -> dict[str, int]:
    return {"message": "Invalid"}


@app.get("/fruits/{fruit}/{amount}")
async def get_fruit(fruit: Fruit, amount: int | None) -> dict[str, str]:
    if amount > 1:
        return {"fruit": f"{fruit.value}s =  {amount}"}
    if amount == 1:
        return {"fruit": f"{fruit.value} =  1"}
    return {"fruit": f"{fruit.value}"}


# def main():
#     print("Hello from fast-zeq!")
# if __name__ == "__main__":
#     main()
