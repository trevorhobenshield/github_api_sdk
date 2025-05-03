


from .._models import BaseModel

__all__ = ["SimpleClassroomRepository"]


class SimpleClassroomRepository(BaseModel):
    id: int
    """A unique identifier of the repository."""

    default_branch: str
    """The default branch for the repository."""

    full_name: str
    """The full, globally unique name of the repository."""

    html_url: str
    """The URL to view the repository on GitHub.com."""

    node_id: str
    """The GraphQL identifier of the repository."""

    private: bool
    """Whether the repository is private."""
