from datetime import datetime

from pydantic import BaseModel


class MetalRollBase(BaseModel):
    length: float
    weight: float


class MetalRollCreate(MetalRollBase):
    pass


class MetalRoll(MetalRollBase):
    id: int
    date_added: datetime
    date_removed: datetime
