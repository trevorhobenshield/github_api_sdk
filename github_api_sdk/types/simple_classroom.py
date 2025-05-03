


from .._models import BaseModel

__all__ = ["SimpleClassroom"]


class SimpleClassroom(BaseModel):
    id: int
    """Unique identifier of the classroom."""

    archived: bool
    """Returns whether classroom is archived or not."""

    name: str
    """The name of the classroom."""

    url: str
    """The url of the classroom on GitHub Classroom."""
