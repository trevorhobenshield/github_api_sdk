

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel
from ....enterprises.code_security.configuration import Configuration

__all__ = ["DefaultSetResponse"]


class DefaultSetResponse(BaseModel):
    configuration: Optional[Configuration] = None
    """A code security configuration"""

    default_for_new_repos: Optional[Literal["all", "none", "private_and_internal", "public"]] = None
    """
    Specifies which types of repository this security configuration is applied to by
    default.
    """
