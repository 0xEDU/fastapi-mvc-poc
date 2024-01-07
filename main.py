from fastapi import FastAPI
from controllers import item_controller


app = FastAPI()
app.include_router(item_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
