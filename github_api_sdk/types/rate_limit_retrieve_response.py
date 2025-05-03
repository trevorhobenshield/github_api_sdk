

from typing import Optional

from .._models import BaseModel
from .rate_limit import RateLimit

__all__ = ["RateLimitRetrieveResponse", "Resources"]


class Resources(BaseModel):
    core: RateLimit

    search: RateLimit

    actions_runner_registration: Optional[RateLimit] = None

    code_scanning_autofix: Optional[RateLimit] = None

    code_scanning_upload: Optional[RateLimit] = None

    code_search: Optional[RateLimit] = None

    dependency_snapshots: Optional[RateLimit] = None

    graphql: Optional[RateLimit] = None

    integration_manifest: Optional[RateLimit] = None

    scim: Optional[RateLimit] = None

    source_import: Optional[RateLimit] = None


class RateLimitRetrieveResponse(BaseModel):
    rate: RateLimit

    resources: Resources
