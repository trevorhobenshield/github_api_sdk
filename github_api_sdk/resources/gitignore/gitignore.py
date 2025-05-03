from __future__ import annotations

from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from .templates import (
    AsyncTemplatesResource,
    AsyncTemplatesResourceWithRawResponse,
    AsyncTemplatesResourceWithStreamingResponse,
    TemplatesResource,
    TemplatesResourceWithRawResponse,
    TemplatesResourceWithStreamingResponse,
)

__all__ = ["GitignoreResource", "AsyncGitignoreResource"]


class GitignoreResource(SyncAPIResource):
    @cached_property
    def templates(self) -> TemplatesResource:
        return TemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> GitignoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return GitignoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GitignoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return GitignoreResourceWithStreamingResponse(self)


class AsyncGitignoreResource(AsyncAPIResource):
    @cached_property
    def templates(self) -> AsyncTemplatesResource:
        return AsyncTemplatesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncGitignoreResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGitignoreResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGitignoreResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncGitignoreResourceWithStreamingResponse(self)


class GitignoreResourceWithRawResponse:
    def __init__(self, gitignore: GitignoreResource) -> None:
        self._gitignore = gitignore

    @cached_property
    def templates(self) -> TemplatesResourceWithRawResponse:
        return TemplatesResourceWithRawResponse(self._gitignore.templates)


class AsyncGitignoreResourceWithRawResponse:
    def __init__(self, gitignore: AsyncGitignoreResource) -> None:
        self._gitignore = gitignore

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithRawResponse:
        return AsyncTemplatesResourceWithRawResponse(self._gitignore.templates)


class GitignoreResourceWithStreamingResponse:
    def __init__(self, gitignore: GitignoreResource) -> None:
        self._gitignore = gitignore

    @cached_property
    def templates(self) -> TemplatesResourceWithStreamingResponse:
        return TemplatesResourceWithStreamingResponse(self._gitignore.templates)


class AsyncGitignoreResourceWithStreamingResponse:
    def __init__(self, gitignore: AsyncGitignoreResource) -> None:
        self._gitignore = gitignore

    @cached_property
    def templates(self) -> AsyncTemplatesResourceWithStreamingResponse:
        return AsyncTemplatesResourceWithStreamingResponse(self._gitignore.templates)
