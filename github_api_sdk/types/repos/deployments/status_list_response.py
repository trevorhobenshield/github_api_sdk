

from typing import List
from typing_extensions import TypeAlias

from .deployment_status import DeploymentStatus

__all__ = ["StatusListResponse"]

StatusListResponse: TypeAlias = List[DeploymentStatus]
