from fastapi import FastAPI
from controllers import items_controller


app = FastAPI()
app.include_router(items_controller.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
