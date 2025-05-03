


from ...._models import BaseModel

__all__ = ["DependabotPublicKey"]


class DependabotPublicKey(BaseModel):
    key: str
    """The Base64 encoded public key."""

    key_id: str
    """The identifier for the key."""
