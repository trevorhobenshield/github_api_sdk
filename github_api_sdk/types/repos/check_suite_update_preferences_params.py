

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["CheckSuiteUpdatePreferencesParams", "AutoTriggerCheck"]


class CheckSuiteUpdatePreferencesParams(TypedDict, total=False):
    owner: Required[str]

    auto_trigger_checks: Iterable[AutoTriggerCheck]
    """
    Enables or disables automatic creation of CheckSuite events upon pushes to the
    repository. Enabled by default.
    """


class AutoTriggerCheck(TypedDict, total=False):
    app_id: Required[int]
    """The `id` of the GitHub App."""

    setting: Required[bool]
    """
    Set to `true` to enable automatic creation of CheckSuite events upon pushes to
    the repository, or `false` to disable them.
    """
