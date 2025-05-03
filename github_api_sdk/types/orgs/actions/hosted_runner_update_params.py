

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["HostedRunnerUpdateParams"]


class HostedRunnerUpdateParams(TypedDict, total=False):
    org: Required[str]

    enable_static_ip: bool
    """Whether this runner should be updated with a static public IP.

    Note limit on account. To list limits on account, use
    `GET actions/hosted-runners/limits`
    """

    maximum_runners: int
    """The maximum amount of runners to scale up to.

    Runners will not auto-scale above this number. Use this setting to limit your
    cost.
    """

    name: str
    """Name of the runner.

    Must be between 1 and 64 characters and may only contain upper and lowercase
    letters a-z, numbers 0-9, '.', '-', and '\\__'.
    """

    runner_group_id: int
    """The existing runner group to add this runner to."""
