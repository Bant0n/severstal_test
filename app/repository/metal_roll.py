from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.metal_roll import MetalRoll
from app.schemas.metal_roll import MetalRollCreate


@dataclass
class MetalRollRepository:
    db_session: AsyncSession

    async def _get_single_metal_roll(self, metal_roll_id: int):
        async with self.db_session as session:
            result = await session.execute(
                select(MetalRoll).where(MetalRoll.id == metal_roll_id)
            )
            return result.scalars().first()

    async def _get_metal_rolls_by_period_date(
        self, start_date: datetime, end_date: datetime
    ):
        # Переделать
        start_date = start_date.replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        end_date = end_date.replace(
            hour=23, minute=59, second=59, microsecond=0
        )
        async with self.db_session as session:
            result = await session.execute(
                select(MetalRoll).filter(
                    MetalRoll.date_added >= start_date,
                    MetalRoll.date_added <= end_date,
                )
            )
            return result.scalars().all()

    async def create_metal_roll(self, data: MetalRollCreate):
        async with self.db_session as session:
            metal_roll = MetalRoll(**data.model_dump())
            session.add(metal_roll)
            await session.commit()
            return metal_roll

    async def get_all_metal_rolls(self):
        async with self.db_session as session:
            result = await session.execute(
                select(MetalRoll).where(MetalRoll.is_deleted.is_(False))
            )
            return result.scalars().all()

    async def get_all_deleted_metal_rolls(self):
        async with self.db_session as session:
            result = await session.execute(
                select(MetalRoll).where(MetalRoll.is_deleted.is_(True))
            )
            return result.scalars().all()

    async def delete_metal_roll(self, metal_roll_id: int):
        async with self.db_session as session:
            await session.execute(
                update(MetalRoll)
                .where(MetalRoll.id == metal_roll_id)
                .values(is_deleted=True, date_removed=datetime.now())
            )
            await session.commit()
            return await self._get_single_metal_roll(metal_roll_id)

    async def get_statistics(self, start_date: datetime, end_date: datetime):
        rolls = await self._get_metal_rolls_by_period_date(
            start_date, end_date
        )
        # Вынести в отдельный файл
        add_rolls_for_period = [roll for roll in rolls if not roll.is_deleted]
        deleted_rolls_for_period = [roll for roll in rolls if roll.is_deleted]
        max_length = max(roll.length for roll in add_rolls_for_period)
        min_length = min(roll.length for roll in add_rolls_for_period)
        sum_weight = sum(roll.weight for roll in add_rolls_for_period)

        return {
            "total_rolls": len(rolls),
            "active_rolls": len(add_rolls_for_period),
            "deleted_rolls": len(deleted_rolls_for_period),
            "max_length": max_length,
            "min_length": min_length,
            "sum_weight": sum_weight,
        }
