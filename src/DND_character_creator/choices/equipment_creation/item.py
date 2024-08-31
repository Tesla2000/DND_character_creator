from __future__ import annotations

from pydantic import BaseModel


class Item(BaseModel):
    name: str
    cost: int
    weight: int = 0
