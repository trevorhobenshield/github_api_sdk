

from typing import Optional

from ....._models import BaseModel

__all__ = ["AutofixCommitResponse"]


class AutofixCommitResponse(BaseModel):
    sha: Optional[str] = None
    """SHA of commit with autofix."""

    target_ref: Optional[str] = None
    """The Git reference of target branch for the commit.

    For more information, see
    "[Git References](https://git-scm.com/book/en/v2/Git-Internals-Git-References)"
    in the Git documentation.
    """
