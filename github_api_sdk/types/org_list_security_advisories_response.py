

from typing import List
from typing_extensions import TypeAlias

from .repos.repository_advisory import RepositoryAdvisory

__all__ = ["OrgListSecurityAdvisoriesResponse"]

OrgListSecurityAdvisoriesResponse: TypeAlias = List[RepositoryAdvisory]
