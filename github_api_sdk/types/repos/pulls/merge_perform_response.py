


from ...._models import BaseModel

__all__ = ["MergePerformResponse"]


class MergePerformResponse(BaseModel):
    merged: bool

    message: str

    sha: str
