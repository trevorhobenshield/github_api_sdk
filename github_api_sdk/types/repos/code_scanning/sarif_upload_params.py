

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SarifUploadParams"]


class SarifUploadParams(TypedDict, total=False):
    owner: Required[str]

    commit_sha: Required[str]
    """The SHA of the commit to which the analysis you are uploading relates."""

    ref: Required[str]
    """
    The full Git reference, formatted as `refs/heads/<branch name>`,
    `refs/tags/<tag>`, `refs/pull/<number>/merge`, or `refs/pull/<number>/head`.
    """

    sarif: Required[str]
    """A Base64 string representing the SARIF file to upload.

    You must first compress your SARIF file using
    [`gzip`](http://www.gnu.org/software/gzip/manual/gzip.html) and then translate
    the contents of the file into a Base64 encoding string. For more information,
    see
    "[SARIF support for code scanning](https://docs.github.com/code-security/secure-coding/sarif-support-for-code-scanning)."
    """

    checkout_uri: str
    """
    The base directory used in the analysis, as it appears in the SARIF file. This
    property is used to convert file paths from absolute to relative, so that alerts
    can be mapped to their correct location in the repository.
    """

    started_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """The time that the analysis run began.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    tool_name: str
    """The name of the tool used to generate the code scanning analysis.

    If this parameter is not used, the tool name defaults to "API". If the uploaded
    SARIF contains a tool GUID, this will be available for filtering using the
    `tool_guid` parameter of operations such as
    `GET /repos/{owner}/{repo}/code-scanning/alerts`.
    """

    validate: bool
    """
    Whether the SARIF file will be validated according to the code scanning
    specifications. This parameter is intended to help integrators ensure that the
    uploaded SARIF files are correctly rendered by code scanning.
    """
