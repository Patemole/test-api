from fastapi import FastAPI
import uvicorn 

app = FastAPI()

#get
@app.get("/")
async def hello_world():
    return {"hello" : "world"}


