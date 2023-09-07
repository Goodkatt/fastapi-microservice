from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from microservice A"}

@app.get("/home")
async def home():
    return {"Homepage of microsservice A"}