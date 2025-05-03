

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["StatusCreateParams"]


class StatusCreateParams(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    state: Required[Literal["error", "failure", "inactive", "in_progress", "queued", "pending", "success"]]
    """The state of the status.

    When you set a transient deployment to `inactive`, the deployment will be shown
    as `destroyed` in GitHub.
    """

    auto_inactive: bool
    """
    Adds a new `inactive` status to all prior non-transient, non-production
    environment deployments with the same repository and `environment` name as the
    created status's deployment. An `inactive` status is only added to deployments
    that had a `success` state. Default: `true`
    """

    description: str
    """A short description of the status.

    The maximum description length is 140 characters.
    """

    environment: str
    """
    Name for the target deployment environment, which can be changed when setting a
    deploy status. For example, `production`, `staging`, or `qa`. If not defined,
    the environment of the previous status on the deployment will be used, if it
    exists. Otherwise, the environment of the deployment will be used.
    """

    environment_url: str
    """Sets the URL for accessing your environment. Default: `""`"""

    log_url: str
    """The full URL of the deployment's output.

    This parameter replaces `target_url`. We will continue to accept `target_url` to
    support legacy uses, but we recommend replacing `target_url` with `log_url`.
    Setting `log_url` will automatically set `target_url` to the same value.
    Default: `""`
    """

    target_url: str
    """The target URL to associate with this status.

    This URL should contain output to keep the user updated while the task is
    running or serve as historical information for what happened in the deployment.

    > [!NOTE] It's recommended to use the `log_url` parameter, which replaces
    > `target_url`.
    """
