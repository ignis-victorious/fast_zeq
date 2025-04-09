#  __________________
#  Import LIBARIES
from fastapi import FastAPI
#  Import FILES
#  __________________


app = FastAPI(
    title="FastApi tutorial",
    description="All the basics of FastAPI",
    summary="Not sure what this is???",
    version="1.0.0s",
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


# def main():
#     print("Hello from fast-zeq!")
# if __name__ == "__main__":
#     main()
