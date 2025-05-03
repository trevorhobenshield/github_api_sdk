

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel
from .enterprises.code_security.configuration import Configuration

__all__ = ["RepoGetCodeSecurityConfigurationResponse"]


class RepoGetCodeSecurityConfigurationResponse(BaseModel):
    configuration: Optional[Configuration] = None
    """A code security configuration"""

    status: Optional[
        Literal[
            "attached", "attaching", "detached", "removed", "enforced", "failed", "updating", "removed_by_enterprise"
        ]
    ] = None
    """The attachment status of the code security configuration on the repository."""
