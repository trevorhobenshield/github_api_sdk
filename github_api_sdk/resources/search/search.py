from __future__ import annotations

from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from .code import (
    AsyncCodeResource,
    AsyncCodeResourceWithRawResponse,
    AsyncCodeResourceWithStreamingResponse,
    CodeResource,
    CodeResourceWithRawResponse,
    CodeResourceWithStreamingResponse,
)
from .commits import (
    AsyncCommitsResource,
    AsyncCommitsResourceWithRawResponse,
    AsyncCommitsResourceWithStreamingResponse,
    CommitsResource,
    CommitsResourceWithRawResponse,
    CommitsResourceWithStreamingResponse,
)
from .issues import (
    AsyncIssuesResource,
    AsyncIssuesResourceWithRawResponse,
    AsyncIssuesResourceWithStreamingResponse,
    IssuesResource,
    IssuesResourceWithRawResponse,
    IssuesResourceWithStreamingResponse,
)
from .labels import (
    AsyncLabelsResource,
    AsyncLabelsResourceWithRawResponse,
    AsyncLabelsResourceWithStreamingResponse,
    LabelsResource,
    LabelsResourceWithRawResponse,
    LabelsResourceWithStreamingResponse,
)
from .repositories import (
    AsyncRepositoriesResource,
    AsyncRepositoriesResourceWithRawResponse,
    AsyncRepositoriesResourceWithStreamingResponse,
    RepositoriesResource,
    RepositoriesResourceWithRawResponse,
    RepositoriesResourceWithStreamingResponse,
)
from .topics import (
    AsyncTopicsResource,
    AsyncTopicsResourceWithRawResponse,
    AsyncTopicsResourceWithStreamingResponse,
    TopicsResource,
    TopicsResourceWithRawResponse,
    TopicsResourceWithStreamingResponse,
)
from .users import (
    AsyncUsersResource,
    AsyncUsersResourceWithRawResponse,
    AsyncUsersResourceWithStreamingResponse,
    UsersResource,
    UsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
)

__all__ = ["SearchResource", "AsyncSearchResource"]


class SearchResource(SyncAPIResource):
    @cached_property
    def code(self) -> CodeResource:
        return CodeResource(self._client)

    @cached_property
    def commits(self) -> CommitsResource:
        return CommitsResource(self._client)

    @cached_property
    def issues(self) -> IssuesResource:
        return IssuesResource(self._client)

    @cached_property
    def labels(self) -> LabelsResource:
        return LabelsResource(self._client)

    @cached_property
    def repositories(self) -> RepositoriesResource:
        return RepositoriesResource(self._client)

    @cached_property
    def topics(self) -> TopicsResource:
        return TopicsResource(self._client)

    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> SearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return SearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return SearchResourceWithStreamingResponse(self)


class AsyncSearchResource(AsyncAPIResource):
    @cached_property
    def code(self) -> AsyncCodeResource:
        return AsyncCodeResource(self._client)

    @cached_property
    def commits(self) -> AsyncCommitsResource:
        return AsyncCommitsResource(self._client)

    @cached_property
    def issues(self) -> AsyncIssuesResource:
        return AsyncIssuesResource(self._client)

    @cached_property
    def labels(self) -> AsyncLabelsResource:
        return AsyncLabelsResource(self._client)

    @cached_property
    def repositories(self) -> AsyncRepositoriesResource:
        return AsyncRepositoriesResource(self._client)

    @cached_property
    def topics(self) -> AsyncTopicsResource:
        return AsyncTopicsResource(self._client)

    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncSearchResourceWithStreamingResponse(self)


class SearchResourceWithRawResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def code(self) -> CodeResourceWithRawResponse:
        return CodeResourceWithRawResponse(self._search.code)

    @cached_property
    def commits(self) -> CommitsResourceWithRawResponse:
        return CommitsResourceWithRawResponse(self._search.commits)

    @cached_property
    def issues(self) -> IssuesResourceWithRawResponse:
        return IssuesResourceWithRawResponse(self._search.issues)

    @cached_property
    def labels(self) -> LabelsResourceWithRawResponse:
        return LabelsResourceWithRawResponse(self._search.labels)

    @cached_property
    def repositories(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self._search.repositories)

    @cached_property
    def topics(self) -> TopicsResourceWithRawResponse:
        return TopicsResourceWithRawResponse(self._search.topics)

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._search.users)


class AsyncSearchResourceWithRawResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def code(self) -> AsyncCodeResourceWithRawResponse:
        return AsyncCodeResourceWithRawResponse(self._search.code)

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithRawResponse:
        return AsyncCommitsResourceWithRawResponse(self._search.commits)

    @cached_property
    def issues(self) -> AsyncIssuesResourceWithRawResponse:
        return AsyncIssuesResourceWithRawResponse(self._search.issues)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithRawResponse:
        return AsyncLabelsResourceWithRawResponse(self._search.labels)

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self._search.repositories)

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithRawResponse:
        return AsyncTopicsResourceWithRawResponse(self._search.topics)

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._search.users)


class SearchResourceWithStreamingResponse:
    def __init__(self, search: SearchResource) -> None:
        self._search = search

    @cached_property
    def code(self) -> CodeResourceWithStreamingResponse:
        return CodeResourceWithStreamingResponse(self._search.code)

    @cached_property
    def commits(self) -> CommitsResourceWithStreamingResponse:
        return CommitsResourceWithStreamingResponse(self._search.commits)

    @cached_property
    def issues(self) -> IssuesResourceWithStreamingResponse:
        return IssuesResourceWithStreamingResponse(self._search.issues)

    @cached_property
    def labels(self) -> LabelsResourceWithStreamingResponse:
        return LabelsResourceWithStreamingResponse(self._search.labels)

    @cached_property
    def repositories(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self._search.repositories)

    @cached_property
    def topics(self) -> TopicsResourceWithStreamingResponse:
        return TopicsResourceWithStreamingResponse(self._search.topics)

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._search.users)


class AsyncSearchResourceWithStreamingResponse:
    def __init__(self, search: AsyncSearchResource) -> None:
        self._search = search

    @cached_property
    def code(self) -> AsyncCodeResourceWithStreamingResponse:
        return AsyncCodeResourceWithStreamingResponse(self._search.code)

    @cached_property
    def commits(self) -> AsyncCommitsResourceWithStreamingResponse:
        return AsyncCommitsResourceWithStreamingResponse(self._search.commits)

    @cached_property
    def issues(self) -> AsyncIssuesResourceWithStreamingResponse:
        return AsyncIssuesResourceWithStreamingResponse(self._search.issues)

    @cached_property
    def labels(self) -> AsyncLabelsResourceWithStreamingResponse:
        return AsyncLabelsResourceWithStreamingResponse(self._search.labels)

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._search.repositories)

    @cached_property
    def topics(self) -> AsyncTopicsResourceWithStreamingResponse:
        return AsyncTopicsResourceWithStreamingResponse(self._search.topics)

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._search.users)
