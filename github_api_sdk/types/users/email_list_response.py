

from typing import List
from typing_extensions import TypeAlias

from .email import Email

__all__ = ["EmailListResponse"]

EmailListResponse: TypeAlias = List[Email]
