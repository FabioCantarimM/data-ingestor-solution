from pydantic import BaseModel
from typing import Optional

class StoreSchema(BaseModel):
    id: int
    name: str
    location: str
    currency: str
    cotation_relation_dolar: Optional[float] = None