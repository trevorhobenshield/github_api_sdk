from . import types
from ._base_client import DefaultAsyncHttpxClient, DefaultHttpxClient
from ._client import (
    AsyncClient,
    AsyncGitHubAPI,
    AsyncStream,
    Client,
    GitHubAPI,
    RequestOptions,
    Stream,
    Timeout,
    Transport,
)
from ._constants import DEFAULT_CONNECTION_LIMITS, DEFAULT_MAX_RETRIES, DEFAULT_TIMEOUT
from ._exceptions import (
    APIConnectionError,
    APIError,
    APIResponseValidationError,
    APIStatusError,
    APITimeoutError,
    AuthenticationError,
    BadRequestError,
    ConflictError,
    GitHubAPIError,
    InternalServerError,
    NotFoundError,
    PermissionDeniedError,
    RateLimitError,
    UnprocessableEntityError,
)
from ._models import BaseModel
from ._response import APIResponse as APIResponse
from ._response import AsyncAPIResponse as AsyncAPIResponse
from ._types import NOT_GIVEN, NoneType, NotGiven, Omit, ProxiesTypes, Transport
from ._utils import file_from_path
from ._utils._logs import setup_logging as _setup_logging
from ._version import __title__, __version__

__all__ = [
    "types",
    "__version__",
    "__title__",
    "NoneType",
    "Transport",
    "ProxiesTypes",
    "NotGiven",
    "NOT_GIVEN",
    "Omit",
    "GitHubAPIError",
    "APIError",
    "APIStatusError",
    "APITimeoutError",
    "APIConnectionError",
    "APIResponseValidationError",
    "BadRequestError",
    "AuthenticationError",
    "PermissionDeniedError",
    "NotFoundError",
    "ConflictError",
    "UnprocessableEntityError",
    "RateLimitError",
    "InternalServerError",
    "Timeout",
    "RequestOptions",
    "Client",
    "AsyncClient",
    "Stream",
    "AsyncStream",
    "GitHubAPI",
    "AsyncGitHubAPI",
    "file_from_path",
    "BaseModel",
    "DEFAULT_TIMEOUT",
    "DEFAULT_MAX_RETRIES",
    "DEFAULT_CONNECTION_LIMITS",
    "DefaultHttpxClient",
    "DefaultAsyncHttpxClient",
]

_setup_logging()

# Update the __module__ attribute for exported symbols so that
# error messages point to this module instead of the module
# it was originally defined in, e.g.
# github_api_sdk._exceptions.NotFoundError -> github_api_sdk.NotFoundError
__locals = locals()
for __name in __all__:
    if not __name.startswith("__"):
        try:
            __locals[__name].__module__ = "github_api_sdk"
        except (TypeError, AttributeError):
            # Some of our exported symbols are builtins which we can't set attributes for.
            pass
