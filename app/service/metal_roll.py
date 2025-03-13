from dataclasses import dataclass

from app.repository.metal_roll import MetalRollRepository
from app.schemas.metal_roll import MetalRollCreate


@dataclass
class MetalRollService:
    metal_roll_repository: MetalRollRepository

    async def get_all_metal_rolls(self):
        return await self.metal_roll_repository.get_all_metal_rolls()

    async def create_metal_roll(self, data: MetalRollCreate):
        return await self.metal_roll_repository.create_metal_roll(data)
