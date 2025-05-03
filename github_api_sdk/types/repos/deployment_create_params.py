

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Required, TypedDict

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    owner: Required[str]

    ref: Required[str]
    """The ref to deploy. This can be a branch, tag, or SHA."""

    auto_merge: bool
    """
    Attempts to automatically merge the default branch into the requested ref, if
    it's behind the default branch.
    """

    description: str | None
    """Short description of the deployment."""

    environment: str
    """
    Name for the target deployment environment (e.g., `production`, `staging`,
    `qa`).
    """

    payload: dict[str, object] | str
    """JSON payload with extra information about the deployment."""

    production_environment: bool
    """Specifies if the given environment is one that end-users directly interact with.

    Default: `true` when `environment` is `production` and `false` otherwise.
    """

    required_contexts: list[str]
    """
    The [status](https://docs.github.com/rest/commits/statuses) contexts to verify
    against commit status checks. If you omit this parameter, GitHub verifies all
    unique contexts before creating a deployment. To bypass checking entirely, pass
    an empty array. Defaults to all unique contexts.
    """

    task: str
    """Specifies a task to execute (e.g., `deploy` or `deploy:migrations`)."""

    transient_environment: bool
    """
    Specifies if the given environment is specific to the deployment and will no
    longer exist at some point in the future. Default: `false`
    """
