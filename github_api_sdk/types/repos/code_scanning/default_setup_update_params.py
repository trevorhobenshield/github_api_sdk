

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal, Required, TypedDict

__all__ = ["DefaultSetupUpdateParams"]


class DefaultSetupUpdateParams(TypedDict, total=False):
    owner: Required[str]

    languages: list[
        Literal["actions", "c-cpp", "csharp", "go", "java-kotlin", "javascript-typescript", "python", "ruby", "swift"]
    ]
    """CodeQL languages to be analyzed."""

    query_suite: Literal["default", "extended"]
    """CodeQL query suite to be used."""

    runner_label: str | None
    """Runner label to be used if the runner type is labeled."""

    runner_type: Literal["standard", "labeled"]
    """Runner type to be used."""

    state: Literal["configured", "not-configured"]
    """The desired state of code scanning default setup."""
