


from .._models import BaseModel

__all__ = ["RateLimit"]


class RateLimit(BaseModel):
    limit: int

    remaining: int

    reset: int

    used: int
