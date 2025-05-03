

from typing import Optional

from ...._models import BaseModel
from .verification import Verification

__all__ = ["GitTag", "Object", "Tagger"]


class Object(BaseModel):
    sha: str

    type: str

    url: str


class Tagger(BaseModel):
    date: str

    email: str

    name: str


class GitTag(BaseModel):
    message: str
    """Message describing the purpose of the tag"""

    node_id: str

    object: Object

    sha: str

    tag: str
    """Name of the tag"""

    tagger: Tagger

    url: str
    """URL for the tag"""

    verification: Optional[Verification] = None
