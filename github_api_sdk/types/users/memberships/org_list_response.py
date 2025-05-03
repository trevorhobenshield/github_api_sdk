

from typing import List
from typing_extensions import TypeAlias

from ...orgs.org_membership import OrgMembership

__all__ = ["OrgListResponse"]

OrgListResponse: TypeAlias = List[OrgMembership]
