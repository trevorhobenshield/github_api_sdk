

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OutsideCollaboratorConvertParams"]


class OutsideCollaboratorConvertParams(TypedDict, total=False):
    org: Required[str]

    async_: Annotated[bool, PropertyInfo(alias="async")]
    """When set to `true`, the request will be performed asynchronously.

    Returns a 202 status code when the job is successfully queued.
    """
