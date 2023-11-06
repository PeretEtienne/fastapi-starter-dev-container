from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    test = "foo"
    uppercased = test.upper()

    return {"Hello": uppercased}