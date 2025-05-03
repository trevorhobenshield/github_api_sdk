

from typing import Optional

from .._models import BaseModel

__all__ = ["Classroom", "Organization"]


class Organization(BaseModel):
    id: int

    avatar_url: str

    html_url: str

    login: str

    name: Optional[str] = None

    node_id: str


class Classroom(BaseModel):
    id: int
    """Unique identifier of the classroom."""

    archived: bool
    """Whether classroom is archived."""

    name: str
    """The name of the classroom."""

    organization: Organization
    """A GitHub organization."""

    url: str
    """The URL of the classroom on GitHub Classroom."""
