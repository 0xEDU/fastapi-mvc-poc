from dataclasses import dataclass
from typing import Union


@dataclass
class Item:
    id: int
    name: str
    description: Union[str, None]
