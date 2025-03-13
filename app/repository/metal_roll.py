from dataclasses import dataclass

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.metal_roll import MetalRoll
from app.schemas.metal_roll import MetalRollCreate


@dataclass
class MetalRollRepository:
    db_session: AsyncSession

    async def create_metal_roll(self, data: MetalRollCreate):
        async with self.db_session as session:
            metal_roll = MetalRoll(**data.model_dump())
            session.add(metal_roll)
            await session.commit()
            return metal_roll

    async def _get_single_metal_roll(self, metal_roll_id: int):
        async with self.db_session as session:
            result = await session.execute(
                select(MetalRoll).where(MetalRoll.id == metal_roll_id)
            )
            return result.scalars().first()

    async def get_all_metal_rolls(self):
        async with self.db_session as session:
            result = await session.execute(select(MetalRoll))
            return result.scalars().all()

    async def delete_metal_roll(self, metal_roll_id: int):
        async with self.db_session as session:
            await session.execute(
                delete(MetalRoll).where(MetalRoll.id == metal_roll_id)
            )
            await session.commit()
