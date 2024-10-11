from datetime import datetime
from typing import Annotated, TypeAlias

from sqlalchemy import BigInteger, DateTime, Integer
from sqlalchemy.orm import DeclarativeBase, registry

Int16: TypeAlias = Annotated[int, 16]
Int64: TypeAlias = Annotated[int, 64]


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            Int16: Integer,
            Int64: BigInteger,
            datetime: DateTime(timezone=True),
        }
    )
