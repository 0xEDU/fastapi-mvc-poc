from fastapi import FastAPI
from dotenv import load_dotenv
from controllers import item_controller

load_dotenv()

app = FastAPI()
app.include_router(item_controller)


@app.get("/")
async def root():
    return {"message": "Hello World"}
