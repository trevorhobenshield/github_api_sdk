


from ..._models import BaseModel

__all__ = ["TemplateRetrieveResponse"]


class TemplateRetrieveResponse(BaseModel):
    name: str

    source: str
