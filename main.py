#  __________________
#  Import LIBARIES
from typing import Any
from fastapi import FastAPI, Path
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
# @app.get("/items/2")
# async def get_item_2() -> dict[str, int]:
#     return {"message": "Invalid"}


# Path(
#     ...,
#     alias="for",
#     title="A title i want to give",
#     description="Something that describe the above",
#     # Number Specific validation
#     gt=0,  # >0 - ge=1 #>=1, lt = 11 #<11, le = 10 #<=10, #multiple_of=3, #3,6,9,...
#     # String Specific validation
#     min_length=1,
#     max_length=10,
#     pattern="[a-zAz]+",  # regex="[a-zAz]+",
#     # Options
#     strict=True,
#     examples=["3", "6"],
#     deprecated=True,
#     # Others
# ),
@app.get("/items/{item_id}/{amount}")
async def get_item(
    item_id: str = ITEM_ID_VALIDATION, amount: int = ITEM_AMOUNT_VALIDATION
) -> dict[str, Any]:
    return {"Itam ID": item_id, "amount": amount}


# @app.get("/items/{item_id}")
# async def get_item(item_id: str = ITEM_ID_VALIDATION) -> dict[str, str]:
#     return {"Hello": item_id}


# @app.get("/items/{item_id}")
# async def get_item(item_id: int) -> dict[str, int]:
#     return {"Hello": item_id}


# @app.get("/items/2")
# async def get_item_2() -> dict[str, int]:
#     return {"message": "Invalid"}


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
