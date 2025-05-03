


from ..._models import BaseModel

__all__ = ["SocialAccount"]


class SocialAccount(BaseModel):
    provider: str

    url: str
