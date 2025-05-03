

from typing import Optional

from ...._models import BaseModel
from .insecure_ssl import InsecureSsl

__all__ = ["Webhook"]


class Webhook(BaseModel):
    content_type: Optional[str] = None
    """The media type used to serialize the payloads.

    Supported values include `json` and `form`. The default is `form`.
    """

    insecure_ssl: Optional[InsecureSsl] = None
    """
    Determines whether the SSL certificate of the host for `url` will be verified
    when delivering payloads. Supported values include `0` (verification is
    performed) and `1` (verification is not performed). The default is `0`. **We
    strongly recommend not setting this to `1` as you are subject to
    man-in-the-middle and other attacks.**
    """

    secret: Optional[str] = None
    """
    If provided, the `secret` will be used as the `key` to generate the HMAC hex
    digest value for
    [delivery signature headers](https://docs.github.com/webhooks/event-payloads/#delivery-headers).
    """

    url: Optional[str] = None
    """The URL to which the payloads will be delivered."""
