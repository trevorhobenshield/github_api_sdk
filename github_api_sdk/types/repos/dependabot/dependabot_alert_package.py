


from ...._models import BaseModel

__all__ = ["DependabotAlertPackage"]


class DependabotAlertPackage(BaseModel):
    ecosystem: str
    """The package's language or package management ecosystem."""

    name: str
    """The unique package name within its ecosystem."""
