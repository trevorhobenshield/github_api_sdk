

from typing import List
from typing_extensions import TypeAlias

from ...deployment import Deployment

__all__ = ["PendingDeploymentReviewResponse"]

PendingDeploymentReviewResponse: TypeAlias = List[Deployment]
