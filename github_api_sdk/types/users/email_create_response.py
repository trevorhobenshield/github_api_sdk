

from typing import List
from typing_extensions import TypeAlias

from .email import Email

__all__ = ["EmailCreateResponse"]

EmailCreateResponse: TypeAlias = List[Email]
