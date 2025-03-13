from typing import Annotated

from fastapi import APIRouter, Depends

from app.dependecy import get_metal_roll_service
from app.schemas.metal_roll import MetalRollCreate, MetalRollInfo
from app.service.metal_roll import MetalRollService

router = APIRouter(
    prefix="/metal_roll",
    tags=["metal_roll"],
)


@router.get("/all")
async def get_all_metal_rolls(
    metal_roll_serv: Annotated[
        MetalRollService, Depends(get_metal_roll_service)
    ],
) -> list[MetalRollInfo]:
    return await metal_roll_serv.get_all_metal_rolls()


@router.post("/create")
async def create_metal_roll(
    data: MetalRollCreate,
    metal_roll_serv: Annotated[
        MetalRollService, Depends(get_metal_roll_service)
    ],
) -> MetalRollInfo:
    return await metal_roll_serv.create_metal_roll(data)
