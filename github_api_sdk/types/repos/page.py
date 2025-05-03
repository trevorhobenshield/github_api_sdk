

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Page", "HTTPSCertificate", "Source"]


class HTTPSCertificate(BaseModel):
    description: str

    domains: List[str]
    """Array of the domain set and its alternate name (if it is configured)"""

    state: Literal[
        "new",
        "authorization_created",
        "authorization_pending",
        "authorized",
        "authorization_revoked",
        "issued",
        "uploaded",
        "approved",
        "errored",
        "bad_authz",
        "destroy_pending",
        "dns_changed",
    ]

    expires_at: Optional[date] = None


class Source(BaseModel):
    branch: str

    path: str


class Page(BaseModel):
    cname: Optional[str] = None
    """The Pages site's custom domain"""

    custom_404: bool
    """Whether the Page has a custom 404 page."""

    public: bool
    """Whether the GitHub Pages site is publicly visible.

    If set to `true`, the site is accessible to anyone on the internet. If set to
    `false`, the site will only be accessible to users who have at least `read`
    access to the repository that published the site.
    """

    status: Optional[Literal["built", "building", "errored"]] = None
    """The status of the most recent build of the Page."""

    url: str
    """The API address for accessing this Page resource."""

    build_type: Optional[Literal["legacy", "workflow"]] = None
    """The process in which the Page will be built."""

    html_url: Optional[str] = None
    """The web address the Page can be accessed from."""

    https_certificate: Optional[HTTPSCertificate] = None

    https_enforced: Optional[bool] = None
    """Whether https is enabled on the domain"""

    pending_domain_unverified_at: Optional[datetime] = None
    """The timestamp when a pending domain becomes unverified."""

    protected_domain_state: Optional[Literal["pending", "verified", "unverified"]] = None
    """The state if the domain is verified"""

    source: Optional[Source] = None
