

from typing import List, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["AlertRuleSummary"]


class AlertRuleSummary(BaseModel):
    id: Optional[str] = None
    """A unique identifier for the rule used to detect the alert."""

    description: Optional[str] = None
    """A short description of the rule used to detect the alert."""

    full_description: Optional[str] = None
    """A description of the rule used to detect the alert."""

    help: Optional[str] = None
    """Detailed documentation for the rule as GitHub Flavored Markdown."""

    help_uri: Optional[str] = None
    """A link to the documentation for the rule used to detect the alert."""

    name: Optional[str] = None
    """The name of the rule used to detect the alert."""

    security_severity_level: Optional[Literal["low", "medium", "high", "critical"]] = None
    """The security severity of the alert."""

    severity: Optional[Literal["none", "note", "warning", "error"]] = None
    """The severity of the alert."""

    tags: Optional[List[str]] = None
    """A set of tags applicable for the rule."""
