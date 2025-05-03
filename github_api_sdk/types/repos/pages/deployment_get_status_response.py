

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DeploymentGetStatusResponse"]


class DeploymentGetStatusResponse(BaseModel):
    status: Optional[
        Literal[
            "deployment_in_progress",
            "syncing_files",
            "finished_file_sync",
            "updating_pages",
            "purging_cdn",
            "deployment_cancelled",
            "deployment_failed",
            "deployment_content_failed",
            "deployment_attempt_error",
            "deployment_lost",
            "succeed",
        ]
    ] = None
    """The current status of the deployment."""
