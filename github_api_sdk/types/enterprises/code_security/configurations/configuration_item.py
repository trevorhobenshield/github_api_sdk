

from typing import Optional
from typing_extensions import Literal

from ....._models import BaseModel
from ..configuration import Configuration

__all__ = ["ConfigurationItem"]


class ConfigurationItem(BaseModel):
    configuration: Optional[Configuration] = None
    """A code security configuration"""

    default_for_new_repos: Optional[Literal["public", "private_and_internal", "all"]] = None
    """
    The visibility of newly created repositories for which the code security
    configuration will be applied to by default
    """
