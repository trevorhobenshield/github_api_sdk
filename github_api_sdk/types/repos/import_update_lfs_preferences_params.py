

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["ImportUpdateLFSPreferencesParams"]


class ImportUpdateLFSPreferencesParams(TypedDict, total=False):
    owner: Required[str]

    use_lfs: Required[Literal["opt_in", "opt_out"]]
    """Whether to store large files during the import.

    `opt_in` means large files will be stored using Git LFS. `opt_out` means large
    files will be removed during the import.
    """
