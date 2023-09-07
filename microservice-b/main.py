from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World from microservice B"}
@app.get("/home")
async def home():
    return {"Homepage of microsservice B"}
