from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from app.dependecy import get_metal_roll_service
from app.exception import MetalRollNotFoundException
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


@router.delete("/{metal_roll_id}/delete")
async def delete_metal_roll(
    metal_roll_id: int,
    metal_roll_serv: Annotated[
        MetalRollService, Depends(get_metal_roll_service)
    ],
) -> MetalRollInfo:
    try:
        return await metal_roll_serv.delete_metal_roll(
            metal_roll_id=metal_roll_id
        )
    except MetalRollNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.detail)
