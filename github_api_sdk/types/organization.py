

from typing import Optional

from .._models import BaseModel

__all__ = ["Organization"]


class Organization(BaseModel):
    id: int

    avatar_url: str

    description: Optional[str] = None

    events_url: str

    hooks_url: str

    issues_url: str

    login: str

    members_url: str

    node_id: str

    public_members_url: str

    repos_url: str

    url: str
