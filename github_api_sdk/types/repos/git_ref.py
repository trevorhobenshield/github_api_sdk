


from ..._models import BaseModel

__all__ = ["GitRef", "Object"]


class Object(BaseModel):
    sha: str
    """SHA for the reference"""

    type: str

    url: str


class GitRef(BaseModel):
    node_id: str

    object: Object

    ref: str

    url: str
