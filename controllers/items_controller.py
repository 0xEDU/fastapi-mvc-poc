from fastapi import APIRouter
from models import Item
from repository import create_item

router = APIRouter(
    prefix="/items",
    tags=["item"]
)


@router.post("/")
async def create_item_endpoint(item: Item):
    create_item(item)
    return {'message': 'Item created successfully!'}
