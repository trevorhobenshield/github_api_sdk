


from ..._models import BaseModel

__all__ = ["Autolink"]


class Autolink(BaseModel):
    id: int

    is_alphanumeric: bool
    """Whether this autolink reference matches alphanumeric characters.

    If false, this autolink reference only matches numeric characters.
    """

    key_prefix: str
    """The prefix of a key that is linkified."""

    url_template: str
    """A template for the target URL that is generated if a key was found."""
