

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from ..applications.hook.insecure_ssl_param import InsecureSslParam

__all__ = ["HookCreateParams", "Config"]


class HookCreateParams(TypedDict, total=False):
    config: Required[Config]
    """Key/value pairs to provide settings for this webhook."""

    name: Required[str]
    """Must be passed as "web"."""

    active: bool
    """Determines if notifications are sent when the webhook is triggered.

    Set to `true` to send notifications.
    """

    events: list[str]
    """
    Determines what [events](https://docs.github.com/webhooks/event-payloads) the
    hook is triggered for. Set to `["*"]` to receive all possible events.
    """


class Config(TypedDict, total=False):
    url: Required[str]
    """The URL to which the payloads will be delivered."""

    content_type: str
    """The media type used to serialize the payloads.

    Supported values include `json` and `form`. The default is `form`.
    """

    insecure_ssl: InsecureSslParam
    """
    Determines whether the SSL certificate of the host for `url` will be verified
    when delivering payloads. Supported values include `0` (verification is
    performed) and `1` (verification is not performed). The default is `0`. **We
    strongly recommend not setting this to `1` as you are subject to
    man-in-the-middle and other attacks.**
    """

    password: str

    secret: str
    """
    If provided, the `secret` will be used as the `key` to generate the HMAC hex
    digest value for
    [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).
    """

    username: str
