from fastapi import Depends
from app.core.db import get_async_session
from sqlalchemy.ext.asyncio import AsyncSession

from app.repository.metal_roll import MetalRollRepository
from app.service.metal_roll import MetalRollService


def get_metal_roll_repository(
    db_session: AsyncSession = Depends(get_async_session),
) -> MetalRollRepository:
    return MetalRollRepository(db_session)


def get_metal_roll_service(
    metal_roll_repository: MetalRollRepository = Depends(
        get_metal_roll_repository
    ),
) -> MetalRollService:
    return MetalRollService(metal_roll_repository)
