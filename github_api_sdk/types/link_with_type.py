


from .._models import BaseModel

__all__ = ["LinkWithType"]


class LinkWithType(BaseModel):
    href: str

    type: str
