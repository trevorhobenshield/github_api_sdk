

from __future__ import annotations

from typing import Dict
from typing_extensions import Required, TypedDict

__all__ = ["WorkflowDispatchParams"]


class WorkflowDispatchParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    ref: Required[str]
    """The git reference for the workflow. The reference can be a branch or tag name."""

    inputs: dict[str, object]
    """Input keys and values configured in the workflow file.

    The maximum number of properties is 10. Any default properties configured in the
    workflow file will be used when `inputs` are omitted.
    """
