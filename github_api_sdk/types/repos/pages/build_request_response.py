


from ...._models import BaseModel

__all__ = ["BuildRequestResponse"]


class BuildRequestResponse(BaseModel):
    status: str

    url: str
