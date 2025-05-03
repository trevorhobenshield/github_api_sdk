

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DefaultSetupRetrieveResponse"]


class DefaultSetupRetrieveResponse(BaseModel):
    languages: Optional[
        List[
            Literal[
                "actions",
                "c-cpp",
                "csharp",
                "go",
                "java-kotlin",
                "javascript-typescript",
                "javascript",
                "python",
                "ruby",
                "typescript",
                "swift",
            ]
        ]
    ] = None
    """Languages to be analyzed."""

    query_suite: Optional[Literal["default", "extended"]] = None
    """CodeQL query suite to be used."""

    runner_label: Optional[str] = None
    """Runner label to be used if the runner type is labeled."""

    runner_type: Optional[Literal["standard", "labeled"]] = None
    """Runner type to be used."""

    schedule: Optional[Literal["weekly"]] = None
    """The frequency of the periodic analysis."""

    state: Optional[Literal["configured", "not-configured"]] = None
    """Code scanning default setup has been configured or not."""

    updated_at: Optional[datetime] = None
    """Timestamp of latest configuration update."""
