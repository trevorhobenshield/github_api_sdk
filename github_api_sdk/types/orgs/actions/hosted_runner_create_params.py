

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["HostedRunnerCreateParams", "Image"]


class HostedRunnerCreateParams(TypedDict, total=False):
    image: Required[Image]
    """The image of runner.

    To list all available images, use
    `GET /actions/hosted-runners/images/github-owned` or
    `GET /actions/hosted-runners/images/partner`.
    """

    name: Required[str]
    """Name of the runner.

    Must be between 1 and 64 characters and may only contain upper and lowercase
    letters a-z, numbers 0-9, '.', '-', and '\\__'.
    """

    runner_group_id: Required[int]
    """The existing runner group to add this runner to."""

    size: Required[str]
    """The machine size of the runner.

    To list available sizes, use `GET actions/hosted-runners/machine-sizes`
    """

    enable_static_ip: bool
    """Whether this runner should be created with a static public IP.

    Note limit on account. To list limits on account, use
    `GET actions/hosted-runners/limits`
    """

    maximum_runners: int
    """The maximum amount of runners to scale up to.

    Runners will not auto-scale above this number. Use this setting to limit your
    cost.
    """


class Image(TypedDict, total=False):
    id: str
    """The unique identifier of the runner image."""

    source: Literal["github", "partner", "custom"]
    """The source of the runner image."""
