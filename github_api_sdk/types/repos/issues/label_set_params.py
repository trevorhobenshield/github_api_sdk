

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Required, TypeAlias, TypedDict

__all__ = [
    "LabelSetParams",
    "Variant0",
    "Variant1",
    "Variant2",
    "Variant2Label",
    "Variant3",
    "Variant3Body",
    "Variant4",
]


class Variant0(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    labels: list[str]
    """The names of the labels to set for the issue.

    The labels you set replace any existing labels. You can pass an empty array to
    remove all labels. Alternatively, you can pass a single label as a `string` or
    an `array` of labels directly, but GitHub recommends passing an object with the
    `labels` key. You can also add labels to the existing labels for an issue. For
    more information, see
    "[Add labels to an issue](https://docs.github.com/rest/issues/labels#add-labels-to-an-issue)."
    """


class Variant1(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: list[str]


class Variant2(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    labels: Iterable[Variant2Label]


class Variant2Label(TypedDict, total=False):
    name: Required[str]


class Variant3(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: Iterable[Variant3Body]


class Variant3Body(TypedDict, total=False):
    name: Required[str]


class Variant4(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    body: str


LabelSetParams: TypeAlias = Union[Variant0, Variant1, Variant2, Variant3, Variant4]
