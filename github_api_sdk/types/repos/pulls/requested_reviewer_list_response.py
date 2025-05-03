

from typing import List

from ...._models import BaseModel
from ...orgs.team import Team
from ...orgs.simple_user import SimpleUser

__all__ = ["RequestedReviewerListResponse"]


class RequestedReviewerListResponse(BaseModel):
    teams: List[Team]

    users: List[SimpleUser]
