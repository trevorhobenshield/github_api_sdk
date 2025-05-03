

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["CodeownerListErrorsResponse", "Error"]


class Error(BaseModel):
    column: int
    """The column number where this errors occurs."""

    kind: str
    """The type of error."""

    line: int
    """The line number where this errors occurs."""

    message: str
    """
    A human-readable description of the error, combining information from multiple
    fields, laid out for display in a monospaced typeface (for example, a
    command-line setting).
    """

    path: str
    """The path of the file where the error occured."""

    source: Optional[str] = None
    """The contents of the line where the error occurs."""

    suggestion: Optional[str] = None
    """Suggested action to fix the error.

    This will usually be `null`, but is provided for some common errors.
    """


class CodeownerListErrorsResponse(BaseModel):
    errors: List[Error]
