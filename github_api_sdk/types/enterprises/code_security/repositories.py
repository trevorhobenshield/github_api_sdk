

from typing import Optional
from typing_extensions import Literal

from ...._models import BaseModel
from ...repos.code_scanning.codeql.simple_repository import SimpleRepository

__all__ = ["Repositories"]


class Repositories(BaseModel):
    repository: Optional[SimpleRepository] = None
    """A GitHub repository."""

    status: Optional[
        Literal[
            "attached", "attaching", "detached", "removed", "enforced", "failed", "updating", "removed_by_enterprise"
        ]
    ] = None
    """The attachment status of the code security configuration on the repository."""
