

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "CheckRunUpdateParams",
    "Variant0",
    "Variant0Action",
    "Variant0Output",
    "Variant0OutputAnnotation",
    "Variant0OutputImage",
    "Variant1",
    "Variant1Action",
    "Variant1Output",
    "Variant1OutputAnnotation",
    "Variant1OutputImage",
]


class Variant0(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    conclusion: Required[
        Literal["action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"]
    ]
    """**Required if you provide `completed_at` or a `status` of `completed`**.

    The final conclusion of the check. **Note:** Providing `conclusion` will
    automatically set the `status` parameter to `completed`. You cannot change a
    check run conclusion to `stale`, only GitHub can set this.
    """

    actions: Iterable[Variant0Action]
    """Possible further actions the integrator can perform, which a user may trigger.

    Each action includes a `label`, `identifier` and `description`. A maximum of
    three actions are accepted. To learn more about check runs and requested
    actions, see
    "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."
    """

    completed_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """The time the check completed.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    details_url: str
    """The URL of the integrator's site that has the full details of the check."""

    external_id: str
    """A reference for the run on the integrator's system."""

    name: str
    """The name of the check. For example, "code-coverage"."""

    output: Variant0Output
    """
    Check runs can accept a variety of data in the `output` object, including a
    `title` and `summary` and can optionally provide descriptive details about the
    run.
    """

    started_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """
    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    status: Literal["completed"]


class Variant0Action(TypedDict, total=False):
    description: Required[str]
    """A short explanation of what this action would do.

    The maximum size is 40 characters.
    """

    identifier: Required[str]
    """A reference for the action on the integrator's system.

    The maximum size is 20 characters.
    """

    label: Required[str]
    """The text to be displayed on a button in the web UI.

    The maximum size is 20 characters.
    """


class Variant0OutputAnnotation(TypedDict, total=False):
    annotation_level: Required[Literal["notice", "warning", "failure"]]
    """The level of the annotation."""

    end_line: Required[int]
    """The end line of the annotation."""

    message: Required[str]
    """A short description of the feedback for these lines of code.

    The maximum size is 64 KB.
    """

    path: Required[str]
    """The path of the file to add an annotation to.

    For example, `assets/css/main.css`.
    """

    start_line: Required[int]
    """The start line of the annotation. Line numbers start at 1."""

    end_column: int
    """The end column of the annotation.

    Annotations only support `start_column` and `end_column` on the same line. Omit
    this parameter if `start_line` and `end_line` have different values.
    """

    raw_details: str
    """Details about this annotation. The maximum size is 64 KB."""

    start_column: int
    """The start column of the annotation.

    Annotations only support `start_column` and `end_column` on the same line. Omit
    this parameter if `start_line` and `end_line` have different values. Column
    numbers start at 1.
    """

    title: str
    """The title that represents the annotation. The maximum size is 255 characters."""


class Variant0OutputImage(TypedDict, total=False):
    alt: Required[str]
    """The alternative text for the image."""

    image_url: Required[str]
    """The full URL of the image."""

    caption: str
    """A short image description."""


class Variant0Output(TypedDict, total=False):
    summary: Required[str]
    """Can contain Markdown."""

    annotations: Iterable[Variant0OutputAnnotation]
    """Adds information from your analysis to specific lines of code.

    Annotations are visible in GitHub's pull request UI. Annotations are visible in
    GitHub's pull request UI. The Checks API limits the number of annotations to a
    maximum of 50 per API request. To create more than 50 annotations, you have to
    make multiple requests to the
    [Update a check run](https://docs.github.com/rest/checks/runs#update-a-check-run)
    endpoint. Each time you update the check run, annotations are appended to the
    list of annotations that already exist for the check run. GitHub Actions are
    limited to 10 warning annotations and 10 error annotations per step. For details
    about annotations in the UI, see
    "[About status checks](https://docs.github.com/articles/about-status-checks#checks)".
    """

    images: Iterable[Variant0OutputImage]
    """Adds images to the output displayed in the GitHub pull request UI."""

    text: str
    """Can contain Markdown."""

    title: str
    """**Required**."""


class Variant1(TypedDict, total=False):
    owner: Required[str]

    repo: Required[str]

    actions: Iterable[Variant1Action]
    """Possible further actions the integrator can perform, which a user may trigger.

    Each action includes a `label`, `identifier` and `description`. A maximum of
    three actions are accepted. To learn more about check runs and requested
    actions, see
    "[Check runs and requested actions](https://docs.github.com/rest/guides/using-the-rest-api-to-interact-with-checks#check-runs-and-requested-actions)."
    """

    completed_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """The time the check completed.

    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    conclusion: Literal[
        "action_required", "cancelled", "failure", "neutral", "success", "skipped", "stale", "timed_out"
    ]
    """**Required if you provide `completed_at` or a `status` of `completed`**.

    The final conclusion of the check. **Note:** Providing `conclusion` will
    automatically set the `status` parameter to `completed`. You cannot change a
    check run conclusion to `stale`, only GitHub can set this.
    """

    details_url: str
    """The URL of the integrator's site that has the full details of the check."""

    external_id: str
    """A reference for the run on the integrator's system."""

    name: str
    """The name of the check. For example, "code-coverage"."""

    output: Variant1Output
    """
    Check runs can accept a variety of data in the `output` object, including a
    `title` and `summary` and can optionally provide descriptive details about the
    run.
    """

    started_at: Annotated[str | datetime, PropertyInfo(format="iso8601")]
    """
    This is a timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
    format: `YYYY-MM-DDTHH:MM:SSZ`.
    """

    status: Literal["queued", "in_progress"]


class Variant1Action(TypedDict, total=False):
    description: Required[str]
    """A short explanation of what this action would do.

    The maximum size is 40 characters.
    """

    identifier: Required[str]
    """A reference for the action on the integrator's system.

    The maximum size is 20 characters.
    """

    label: Required[str]
    """The text to be displayed on a button in the web UI.

    The maximum size is 20 characters.
    """


class Variant1OutputAnnotation(TypedDict, total=False):
    annotation_level: Required[Literal["notice", "warning", "failure"]]
    """The level of the annotation."""

    end_line: Required[int]
    """The end line of the annotation."""

    message: Required[str]
    """A short description of the feedback for these lines of code.

    The maximum size is 64 KB.
    """

    path: Required[str]
    """The path of the file to add an annotation to.

    For example, `assets/css/main.css`.
    """

    start_line: Required[int]
    """The start line of the annotation. Line numbers start at 1."""

    end_column: int
    """The end column of the annotation.

    Annotations only support `start_column` and `end_column` on the same line. Omit
    this parameter if `start_line` and `end_line` have different values.
    """

    raw_details: str
    """Details about this annotation. The maximum size is 64 KB."""

    start_column: int
    """The start column of the annotation.

    Annotations only support `start_column` and `end_column` on the same line. Omit
    this parameter if `start_line` and `end_line` have different values. Column
    numbers start at 1.
    """

    title: str
    """The title that represents the annotation. The maximum size is 255 characters."""


class Variant1OutputImage(TypedDict, total=False):
    alt: Required[str]
    """The alternative text for the image."""

    image_url: Required[str]
    """The full URL of the image."""

    caption: str
    """A short image description."""


class Variant1Output(TypedDict, total=False):
    summary: Required[str]
    """Can contain Markdown."""

    annotations: Iterable[Variant1OutputAnnotation]
    """Adds information from your analysis to specific lines of code.

    Annotations are visible in GitHub's pull request UI. Annotations are visible in
    GitHub's pull request UI. The Checks API limits the number of annotations to a
    maximum of 50 per API request. To create more than 50 annotations, you have to
    make multiple requests to the
    [Update a check run](https://docs.github.com/rest/checks/runs#update-a-check-run)
    endpoint. Each time you update the check run, annotations are appended to the
    list of annotations that already exist for the check run. GitHub Actions are
    limited to 10 warning annotations and 10 error annotations per step. For details
    about annotations in the UI, see
    "[About status checks](https://docs.github.com/articles/about-status-checks#checks)".
    """

    images: Iterable[Variant1OutputImage]
    """Adds images to the output displayed in the GitHub pull request UI."""

    text: str
    """Can contain Markdown."""

    title: str
    """**Required**."""


CheckRunUpdateParams: TypeAlias = Union[Variant0, Variant1]
