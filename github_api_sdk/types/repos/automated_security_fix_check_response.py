


from ..._models import BaseModel

__all__ = ["AutomatedSecurityFixCheckResponse"]


class AutomatedSecurityFixCheckResponse(BaseModel):
    enabled: bool
    """Whether Dependabot security updates are enabled for the repository."""

    paused: bool
    """Whether Dependabot security updates are paused for the repository."""
