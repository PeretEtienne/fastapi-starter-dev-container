from typing import TypedDict

from fastapi import FastAPI

app = FastAPI()


class HomeResponse(TypedDict):
    Hello: str


@app.get("/")
def read_root() -> HomeResponse:
    test = "foo"
    uppercased = test.upper()

    return {"Hello": uppercased}
