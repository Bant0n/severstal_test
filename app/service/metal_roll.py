from dataclasses import dataclass

from app.exception import MetalRollNotFoundException
from app.repository.metal_roll import MetalRollRepository
from app.schemas.metal_roll import MetalRollCreate


@dataclass
class MetalRollService:
    metal_roll_repository: MetalRollRepository

    async def get_all_metal_rolls(self):
        return await self.metal_roll_repository.get_all_metal_rolls()

    async def create_metal_roll(self, data: MetalRollCreate):
        return await self.metal_roll_repository.create_metal_roll(data)

    async def delete_metal_roll(self, metal_roll_id: int):
        metal_roll = await self.metal_roll_repository._get_single_metal_roll(
            metal_roll_id=metal_roll_id
        )

        if not metal_roll:
            raise MetalRollNotFoundException

        await self.metal_roll_repository.delete_metal_roll(
            metal_roll_id=metal_roll_id
        )
        return metal_roll
