

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["RunnerGenerateJitconfigParams"]


class RunnerGenerateJitconfigParams(TypedDict, total=False):
    owner: Required[str]

    labels: Required[list[str]]
    """The names of the custom labels to add to the runner.

    **Minimum items**: 1. **Maximum items**: 100.
    """

    name: Required[str]
    """The name of the new runner."""

    runner_group_id: Required[int]
    """The ID of the runner group to register the runner to."""

    work_folder: str
    """
    The working directory to be used for job execution, relative to the runner
    install directory.
    """
