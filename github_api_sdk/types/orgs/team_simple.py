

from typing import Optional

from ..._models import BaseModel

__all__ = ["TeamSimple"]


class TeamSimple(BaseModel):
    id: int
    """Unique identifier of the team"""

    description: Optional[str] = None
    """Description of the team"""

    html_url: str

    members_url: str

    name: str
    """Name of the team"""

    node_id: str

    permission: str
    """Permission that the team will have for its repositories"""

    repositories_url: str

    slug: str

    url: str
    """URL for the team"""

    ldap_dn: Optional[str] = None
    """Distinguished Name (DN) that team maps to within LDAP environment"""

    notification_setting: Optional[str] = None
    """The notification setting the team has set"""

    privacy: Optional[str] = None
    """The level of privacy this team should have"""
