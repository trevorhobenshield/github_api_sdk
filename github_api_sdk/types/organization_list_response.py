

from typing import List
from typing_extensions import TypeAlias

from .organization import Organization

__all__ = ["OrganizationListResponse"]

OrganizationListResponse: TypeAlias = List[Organization]
