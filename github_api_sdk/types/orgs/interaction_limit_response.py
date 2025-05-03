

from datetime import datetime

from ..._models import BaseModel
from .interaction_group import InteractionGroup

__all__ = ["InteractionLimitResponse"]


class InteractionLimitResponse(BaseModel):
    expires_at: datetime

    limit: InteractionGroup
    """
    The type of GitHub user that can comment, open issues, or create pull requests
    while the interaction limit is in effect.
    """

    origin: str
