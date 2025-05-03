

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["TeamMembership"]


class TeamMembership(BaseModel):
    role: Literal["member", "maintainer"]
    """The role of the user in the team."""

    state: Literal["active", "pending"]
    """The state of the user's membership in the team."""

    url: str
