

from typing import List
from typing_extensions import TypeAlias

from .email import Email

__all__ = ["EmailSetVisibilityResponse"]

EmailSetVisibilityResponse: TypeAlias = List[Email]
