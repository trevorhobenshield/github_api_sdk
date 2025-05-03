

from __future__ import annotations

from typing import List, Union
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = ["EmailCreateParams", "Variant0", "Variant1", "Variant2"]


class Variant0(TypedDict, total=False):
    emails: Required[list[str]]
    """Adds one or more email addresses to your GitHub account.

    Must contain at least one email address. **Note:** Alternatively, you can pass a
    single email address or an `array` of emails addresses directly, but we
    recommend that you pass an object using the `emails` key.
    """


class Variant1(TypedDict, total=False):
    body: list[str]


class Variant2(TypedDict, total=False):
    body: str


EmailCreateParams: TypeAlias = Union[Variant0, Variant1, Variant2]
