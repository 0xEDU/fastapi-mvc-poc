from models import Item
from database import connection


def create_item(item: Item):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO items (id, name, description, price) VALUES (%s, %s, %s)"
                       , (item.id, item.name, item.description))
    connection.commit()