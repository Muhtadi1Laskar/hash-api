from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "Hello from FastAPI!"}

@app.get("/hash/{hash_type}")
def read_item(hash_type: str, q: str = None):
    return {"hash_type": hash_type, "q": q}