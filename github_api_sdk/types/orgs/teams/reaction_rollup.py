


from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["ReactionRollup"]


class ReactionRollup(BaseModel):
    minus_1: int = FieldInfo(alias="-1")

    plus_1: int = FieldInfo(alias="+1")

    confused: int

    eyes: int

    heart: int

    hooray: int

    laugh: int

    rocket: int

    total_count: int

    url: str
