

from typing import Optional
from datetime import datetime

from ..._models import BaseModel
from ..orgs.nullable_license_simple import NullableLicenseSimple
from .nullable_community_health_file import NullableCommunityHealthFile

__all__ = ["CommunityRetrieveProfileResponse", "Files", "FilesCodeOfConduct"]


class FilesCodeOfConduct(BaseModel):
    html_url: Optional[str] = None

    key: str

    name: str

    url: str


class Files(BaseModel):
    code_of_conduct: Optional[FilesCodeOfConduct] = None
    """Code of Conduct Simple"""

    code_of_conduct_file: Optional[NullableCommunityHealthFile] = None

    contributing: Optional[NullableCommunityHealthFile] = None

    issue_template: Optional[NullableCommunityHealthFile] = None

    license: Optional[NullableLicenseSimple] = None
    """License Simple"""

    pull_request_template: Optional[NullableCommunityHealthFile] = None

    readme: Optional[NullableCommunityHealthFile] = None


class CommunityRetrieveProfileResponse(BaseModel):
    description: Optional[str] = None

    documentation: Optional[str] = None

    files: Files

    health_percentage: int

    updated_at: Optional[datetime] = None

    content_reports_enabled: Optional[bool] = None
