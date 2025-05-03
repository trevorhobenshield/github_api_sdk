

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["RepositoryRuleMaxFileSize", "Parameters"]


class Parameters(BaseModel):
    max_file_size: int
    """The maximum file size allowed in megabytes.

    This limit does not apply to Git Large File Storage (Git LFS).
    """


class RepositoryRuleMaxFileSize(BaseModel):
    type: Literal["max_file_size"]

    parameters: Optional[Parameters] = None
