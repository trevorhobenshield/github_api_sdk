


from ..._models import BaseModel

__all__ = ["DependencyGraphCreateSnapshotResponse"]


class DependencyGraphCreateSnapshotResponse(BaseModel):
    id: int
    """ID of the created snapshot."""

    created_at: str
    """The time at which the snapshot was created."""

    message: str
    """
    A message providing further details about the result, such as why the
    dependencies were not updated.
    """

    result: str
    """Either "SUCCESS", "ACCEPTED", or "INVALID".

    "SUCCESS" indicates that the snapshot was successfully created and the
    repository's dependencies were updated. "ACCEPTED" indicates that the snapshot
    was successfully created, but the repository's dependencies were not updated.
    "INVALID" indicates that the snapshot was malformed.
    """
