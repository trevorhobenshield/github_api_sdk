


from ...._models import BaseModel

__all__ = ["BlobCreateResponse"]


class BlobCreateResponse(BaseModel):
    sha: str

    url: str
