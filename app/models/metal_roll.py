from datetime import datetime

from sqlalchemy import Float, Integer, func
from sqlalchemy.orm import Mapped, mapped_column

from app.core.db import Base


class MetalRoll(Base):
    __tablename__ = "metal_roll"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    length: Mapped[float] = mapped_column(Float, nullable=False)
    weight: Mapped[float] = mapped_column(Float, nullable=False)
    date_added: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    date_removed: Mapped[datetime] = mapped_column(
        nullable=True,
    )
    is_deleted: Mapped[bool] = mapped_column(default=False)
