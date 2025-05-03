

from typing import Dict, Union, Optional
from datetime import datetime

from ..._models import BaseModel
from ..applications.user import User
from .nullable_integration import NullableIntegration

__all__ = ["Deployment"]


class Deployment(BaseModel):
    id: int
    """Unique identifier of the deployment"""

    created_at: datetime

    creator: Optional[User] = None
    """A GitHub user."""

    description: Optional[str] = None

    environment: str
    """Name for the target deployment environment."""

    node_id: str

    payload: Union[Dict[str, object], str]

    ref: str
    """The ref to deploy. This can be a branch, tag, or sha."""

    repository_url: str

    sha: str

    statuses_url: str

    task: str
    """Parameter to specify a task to execute"""

    updated_at: datetime

    url: str

    original_environment: Optional[str] = None

    performed_via_github_app: Optional[NullableIntegration] = None
    """GitHub apps are a new way to extend GitHub.

    They can be installed directly on organizations and user accounts and granted
    access to specific repositories. They come with granular permissions and
    built-in webhooks. GitHub apps are first class actors within GitHub.
    """

    production_environment: Optional[bool] = None
    """Specifies if the given environment is one that end-users directly interact with.

    Default: false.
    """

    transient_environment: Optional[bool] = None
    """
    Specifies if the given environment is will no longer exist at some point in the
    future. Default: false.
    """
