#  __________________
#  Import LIBARIES
from typing import Any
from fastapi import FastAPI, Path, Query
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


ITEM_ID_VALIDATION = Path(..., title="The string ID of the Item", max_length=5)
ITEM_AMOUNT_VALIDATION = Path(..., title="The number of item to get", ge=1, le=99)


@app.get("/items/{item_id}/{amount}")
async def get_items(
    item_id: str = ITEM_ID_VALIDATION, amount: int = ITEM_AMOUNT_VALIDATION
) -> dict[str, Any]:
    return {"Itam ID": item_id, "amount": amount}


@app.get("/fruits/{fruit}/{amount}")
async def get_fruit(fruit: Fruit, amount: int | None) -> dict[str, str]:
    if amount > 1:
        return {"fruit": f"{fruit.value}s =  {amount}"}
    if amount == 1:
        return {"fruit": f"{fruit.value} =  1"}
    return {"fruit": f"{fruit.value}"}


@app.get("/item/{item_id}")
async def get_item(
    item_id: str,
    amount: float,
    available: bool = True,
    count: int = 0,
    name: str | None = None,
    # item_id: str, count: int = 0, name: str = "Default name"
) -> dict[str, Any]:
    return {"Itam ID": item_id, "available": available, "count": count, "nmen": name}


@app.get("/item-list")
async def get_item_list(item_ids: list[int] = Query(None)) -> dict[str, list[int]]:
    return {"item_ids": item_ids}


# def main():
#     print("Hello from fast-zeq!")
# if __name__ == "__main__":
#     main()
