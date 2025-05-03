


from ..._models import BaseModel

__all__ = ["ReleaseGenerateNotesResponse"]


class ReleaseGenerateNotesResponse(BaseModel):
    body: str
    """
    The generated body describing the contents of the release supporting markdown
    formatting
    """

    name: str
    """The generated name of the release"""
