

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ProjectAddOrUpdatePermissionsParams"]


class ProjectAddOrUpdatePermissionsParams(TypedDict, total=False):
    team_id: Required[int]

    permission: Literal["read", "write", "admin"]
    """The permission to grant to the team for this project.

    Default: the team's `permission` attribute will be used to determine what
    permission to grant the team on this project. Note that, if you choose not to
    pass any parameters, you'll need to set `Content-Length` to zero when calling
    this endpoint. For more information, see
    "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."
    """
