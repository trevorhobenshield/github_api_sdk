

import datetime
from typing import TYPE_CHECKING, List, Optional

from ..._models import BaseModel

__all__ = [
    "CopilotUsageMetricsDay",
    "CopilotDotcomChat",
    "CopilotDotcomChatModel",
    "CopilotDotcomPullRequests",
    "CopilotDotcomPullRequestsRepository",
    "CopilotDotcomPullRequestsRepositoryModel",
    "CopilotIdeChat",
    "CopilotIdeChatEditor",
    "CopilotIdeChatEditorModel",
    "CopilotIdeCodeCompletions",
    "CopilotIdeCodeCompletionsEditor",
    "CopilotIdeCodeCompletionsEditorModel",
    "CopilotIdeCodeCompletionsEditorModelLanguage",
    "CopilotIdeCodeCompletionsLanguage",
]


class CopilotDotcomChatModel(BaseModel):
    custom_model_training_date: Optional[str] = None
    """The training date for the custom model (if applicable)."""

    is_custom_model: Optional[bool] = None
    """Indicates whether a model is custom or default."""

    name: Optional[str] = None
    """Name of the model used for Copilot Chat.

    If the default model is used will appear as 'default'.
    """

    total_chats: Optional[int] = None
    """Total number of chats initiated by users on github.com."""

    total_engaged_users: Optional[int] = None
    """
    Total number of users who prompted Copilot Chat on github.com at least once for
    each model.
    """


class CopilotDotcomChat(BaseModel):
    models: Optional[List[CopilotDotcomChatModel]] = None
    """List of model metrics for a custom models and the default model."""

    total_engaged_users: Optional[int] = None
    """Total number of users who prompted Copilot Chat on github.com at least once."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CopilotDotcomPullRequestsRepositoryModel(BaseModel):
    custom_model_training_date: Optional[str] = None
    """The training date for the custom model."""

    is_custom_model: Optional[bool] = None
    """Indicates whether a model is custom or default."""

    name: Optional[str] = None
    """Name of the model used for Copilot pull request summaries.

    If the default model is used will appear as 'default'.
    """

    total_engaged_users: Optional[int] = None
    """
    The number of users who generated pull request summaries using Copilot for Pull
    Requests in the given repository and model.
    """

    total_pr_summaries_created: Optional[int] = None
    """
    The number of pull request summaries generated using Copilot for Pull Requests
    in the given repository.
    """


class CopilotDotcomPullRequestsRepository(BaseModel):
    models: Optional[List[CopilotDotcomPullRequestsRepositoryModel]] = None
    """List of model metrics for custom models and the default model."""

    name: Optional[str] = None
    """Repository name"""

    total_engaged_users: Optional[int] = None
    """
    The number of users who generated pull request summaries using Copilot for Pull
    Requests in the given repository.
    """


class CopilotDotcomPullRequests(BaseModel):
    repositories: Optional[List[CopilotDotcomPullRequestsRepository]] = None
    """
    Repositories in which users used Copilot for Pull Requests to generate pull
    request summaries
    """

    total_engaged_users: Optional[int] = None
    """
    The number of users who used Copilot for Pull Requests on github.com to generate
    a pull request summary at least once.
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CopilotIdeChatEditorModel(BaseModel):
    custom_model_training_date: Optional[str] = None
    """The training date for the custom model."""

    is_custom_model: Optional[bool] = None
    """Indicates whether a model is custom or default."""

    name: Optional[str] = None
    """Name of the model used for Copilot Chat.

    If the default model is used will appear as 'default'.
    """

    total_chat_copy_events: Optional[int] = None
    """
    The number of times users copied a code suggestion from Copilot Chat using the
    keyboard, or the 'Copy' UI element, for the given editor.
    """

    total_chat_insertion_events: Optional[int] = None
    """
    The number of times users accepted a code suggestion from Copilot Chat using the
    'Insert Code' UI element, for the given editor.
    """

    total_chats: Optional[int] = None
    """The total number of chats initiated by users in the given editor and model."""

    total_engaged_users: Optional[int] = None
    """The number of users who prompted Copilot Chat in the given editor and model."""


class CopilotIdeChatEditor(BaseModel):
    models: Optional[List[CopilotIdeChatEditorModel]] = None
    """List of model metrics for custom models and the default model."""

    name: Optional[str] = None
    """Name of the given editor."""

    total_engaged_users: Optional[int] = None
    """The number of users who prompted Copilot Chat in the specified editor."""


class CopilotIdeChat(BaseModel):
    editors: Optional[List[CopilotIdeChatEditor]] = None

    total_engaged_users: Optional[int] = None
    """Total number of users who prompted Copilot Chat in the IDE."""

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CopilotIdeCodeCompletionsEditorModelLanguage(BaseModel):
    name: Optional[str] = None
    """
    Name of the language used for Copilot code completion suggestions, for the given
    editor.
    """

    total_code_acceptances: Optional[int] = None
    """
    The number of Copilot code suggestions accepted for the given editor, for the
    given language. Includes both full and partial acceptances.
    """

    total_code_lines_accepted: Optional[int] = None
    """
    The number of lines of code accepted from Copilot code suggestions for the given
    editor, for the given language.
    """

    total_code_lines_suggested: Optional[int] = None
    """
    The number of lines of code suggested by Copilot code completions for the given
    editor, for the given language.
    """

    total_code_suggestions: Optional[int] = None
    """
    The number of Copilot code suggestions generated for the given editor, for the
    given language.
    """

    total_engaged_users: Optional[int] = None
    """
    Number of users who accepted at least one Copilot code completion suggestion for
    the given editor, for the given language. Includes both full and partial
    acceptances.
    """


class CopilotIdeCodeCompletionsEditorModel(BaseModel):
    custom_model_training_date: Optional[str] = None
    """The training date for the custom model."""

    is_custom_model: Optional[bool] = None
    """Indicates whether a model is custom or default."""

    languages: Optional[List[CopilotIdeCodeCompletionsEditorModelLanguage]] = None
    """Code completion metrics for active languages, for the given editor."""

    name: Optional[str] = None
    """Name of the model used for Copilot code completion suggestions.

    If the default model is used will appear as 'default'.
    """

    total_engaged_users: Optional[int] = None
    """
    Number of users who accepted at least one Copilot code completion suggestion for
    the given editor, for the given language and model. Includes both full and
    partial acceptances.
    """


class CopilotIdeCodeCompletionsEditor(BaseModel):
    models: Optional[List[CopilotIdeCodeCompletionsEditorModel]] = None
    """List of model metrics for custom models and the default model."""

    name: Optional[str] = None
    """Name of the given editor."""

    total_engaged_users: Optional[int] = None
    """
    Number of users who accepted at least one Copilot code completion suggestion for
    the given editor. Includes both full and partial acceptances.
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CopilotIdeCodeCompletionsLanguage(BaseModel):
    name: Optional[str] = None
    """Name of the language used for Copilot code completion suggestions."""

    total_engaged_users: Optional[int] = None
    """
    Number of users who accepted at least one Copilot code completion suggestion for
    the given language. Includes both full and partial acceptances.
    """


class CopilotIdeCodeCompletions(BaseModel):
    editors: Optional[List[CopilotIdeCodeCompletionsEditor]] = None

    languages: Optional[List[CopilotIdeCodeCompletionsLanguage]] = None
    """Code completion metrics for active languages."""

    total_engaged_users: Optional[int] = None
    """
    Number of users who accepted at least one Copilot code suggestion, across all
    active editors. Includes both full and partial acceptances.
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...


class CopilotUsageMetricsDay(BaseModel):
    date: datetime.date
    """The date for which the usage metrics are aggregated, in `YYYY-MM-DD` format."""

    copilot_dotcom_chat: Optional[CopilotDotcomChat] = None
    """Usage metrics for Copilot Chat in GitHub.com"""

    copilot_dotcom_pull_requests: Optional[CopilotDotcomPullRequests] = None
    """Usage metrics for Copilot for pull requests."""

    copilot_ide_chat: Optional[CopilotIdeChat] = None
    """Usage metrics for Copilot Chat in the IDE."""

    copilot_ide_code_completions: Optional[CopilotIdeCodeCompletions] = None
    """Usage metrics for Copilot editor code completions in the IDE."""

    total_active_users: Optional[int] = None
    """
    The total number of Copilot users with activity belonging to any Copilot
    feature, globally, for the given day. Includes passive activity such as
    receiving a code suggestion, as well as engagement activity such as accepting a
    code suggestion or prompting chat. Does not include authentication events. Is
    not limited to the individual features detailed on the endpoint.
    """

    total_engaged_users: Optional[int] = None
    """
    The total number of Copilot users who engaged with any Copilot feature, for the
    given day. Examples include but are not limited to accepting a code suggestion,
    prompting Copilot chat, or triggering a PR Summary. Does not include
    authentication events. Is not limited to the individual features detailed on the
    endpoint.
    """

    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
