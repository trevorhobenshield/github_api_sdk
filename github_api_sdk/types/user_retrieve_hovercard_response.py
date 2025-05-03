

from typing import List

from .._models import BaseModel

__all__ = ["UserRetrieveHovercardResponse", "Context"]


class Context(BaseModel):
    message: str

    octicon: str


class UserRetrieveHovercardResponse(BaseModel):
    contexts: List[Context]
