from __future__ import annotations

import httpx
from typing_extensions import Literal

from ..._base_client import make_request_options
from ..._compat import cached_property
from ..._resource import AsyncAPIResource, SyncAPIResource
from ..._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ..._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.orgs.teams.team_repository import TeamRepository
from ...types.teams import repo_add_or_update_permissions_params, repo_list_params
from ...types.teams.repo_list_response import RepoListResponse

__all__ = ["ReposResource", "AsyncReposResource"]


class ReposResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReposResourceWithStreamingResponse(self)

    def list(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [List team repositories](https://docs.github.com/rest/teams/teams#list-team-repositories)
        > endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/teams/{team_id}/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    repo_list_params.RepoListParams,
                ),
            ),
            cast_to=RepoListResponse,
        )

    def add_or_update_permissions(
        self,
        repo: str,
        *,
        team_id: int,
        owner: str,
        permission: Literal["pull", "push", "admin"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > "[Add or update team repository permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions)"
        > endpoint.

        To add a repository to a team or update the team's permission on a repository,
        the authenticated user must have admin access to the repository, and must be
        able to see the team. The repository must be owned by the organization, or a
        direct fork of a repository owned by the organization. You will get a
        `422 Unprocessable Entity` status if you attempt to add a repository to a team
        that is not owned by the organization.

        Note that, if you choose not to pass any parameters, you'll need to set
        `Content-Length` to zero when calling out to this endpoint. For more
        information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          permission: The permission to grant the team on this repository. If no permission is
              specified, the team's `permission` attribute will be used to determine what
              permission to grant the team on this repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/teams/{team_id}/repos/{owner}/{repo}",
            body=maybe_transform({"permission": permission}, repo_add_or_update_permissions_params.RepoAddOrUpdatePermissionsParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def check_permissions(
        self,
        repo: str,
        *,
        team_id: int,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamRepository:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Check team permissions for a repository](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository)
        > endpoint.

        > [!NOTE] Repositories inherited through a parent team will also be checked.

        You can also get information about the specified repository, including what
        permissions the team grants on it, by passing the following custom
        [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types/)
        via the `Accept` header:

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/teams/{team_id}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamRepository,
        )

    def remove(
        self,
        repo: str,
        *,
        team_id: int,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Remove a repository from a team](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team)
        > endpoint.

        If the authenticated user is an organization owner or a team maintainer, they
        can remove any repositories from the team. To remove a repository from a team as
        an organization member, the authenticated user must have admin access to the
        repository and must be able to see the team. NOTE: This does not delete the
        repository, it just removes it from the team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/teams/{team_id}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncReposResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReposResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReposResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReposResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReposResourceWithStreamingResponse(self)

    async def list(
        self,
        team_id: int,
        *,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListResponse:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [List team repositories](https://docs.github.com/rest/teams/teams#list-team-repositories)
        > endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/teams/{team_id}/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    repo_list_params.RepoListParams,
                ),
            ),
            cast_to=RepoListResponse,
        )

    async def add_or_update_permissions(
        self,
        repo: str,
        *,
        team_id: int,
        owner: str,
        permission: Literal["pull", "push", "admin"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > "[Add or update team repository permissions](https://docs.github.com/rest/teams/teams#add-or-update-team-repository-permissions)"
        > endpoint.

        To add a repository to a team or update the team's permission on a repository,
        the authenticated user must have admin access to the repository, and must be
        able to see the team. The repository must be owned by the organization, or a
        direct fork of a repository owned by the organization. You will get a
        `422 Unprocessable Entity` status if you attempt to add a repository to a team
        that is not owned by the organization.

        Note that, if you choose not to pass any parameters, you'll need to set
        `Content-Length` to zero when calling out to this endpoint. For more
        information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        Args:
          permission: The permission to grant the team on this repository. If no permission is
              specified, the team's `permission` attribute will be used to determine what
              permission to grant the team on this repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/teams/{team_id}/repos/{owner}/{repo}",
            body=await async_maybe_transform({"permission": permission}, repo_add_or_update_permissions_params.RepoAddOrUpdatePermissionsParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def check_permissions(
        self,
        repo: str,
        *,
        team_id: int,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamRepository:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Check team permissions for a repository](https://docs.github.com/rest/teams/teams#check-team-permissions-for-a-repository)
        > endpoint.

        > [!NOTE] Repositories inherited through a parent team will also be checked.

        You can also get information about the specified repository, including what
        permissions the team grants on it, by passing the following custom
        [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types/)
        via the `Accept` header:

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/teams/{team_id}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamRepository,
        )

    async def remove(
        self,
        repo: str,
        *,
        team_id: int,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        > [!WARNING] > **Endpoint closing down notice:** This endpoint route is closing
        > down and will be removed from the Teams API. We recommend migrating your
        > existing code to use the new
        > [Remove a repository from a team](https://docs.github.com/rest/teams/teams#remove-a-repository-from-a-team)
        > endpoint.

        If the authenticated user is an organization owner or a team maintainer, they
        can remove any repositories from the team. To remove a repository from a team as
        an organization member, the authenticated user must have admin access to the
        repository and must be able to see the team. NOTE: This does not delete the
        repository, it just removes it from the team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/teams/{team_id}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.list = to_raw_response_wrapper(
            repos.list,
        )
        self.add_or_update_permissions = to_raw_response_wrapper(
            repos.add_or_update_permissions,
        )
        self.check_permissions = to_raw_response_wrapper(
            repos.check_permissions,
        )
        self.remove = to_raw_response_wrapper(
            repos.remove,
        )


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.list = async_to_raw_response_wrapper(
            repos.list,
        )
        self.add_or_update_permissions = async_to_raw_response_wrapper(
            repos.add_or_update_permissions,
        )
        self.check_permissions = async_to_raw_response_wrapper(
            repos.check_permissions,
        )
        self.remove = async_to_raw_response_wrapper(
            repos.remove,
        )


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.list = to_streamed_response_wrapper(
            repos.list,
        )
        self.add_or_update_permissions = to_streamed_response_wrapper(
            repos.add_or_update_permissions,
        )
        self.check_permissions = to_streamed_response_wrapper(
            repos.check_permissions,
        )
        self.remove = to_streamed_response_wrapper(
            repos.remove,
        )


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.list = async_to_streamed_response_wrapper(
            repos.list,
        )
        self.add_or_update_permissions = async_to_streamed_response_wrapper(
            repos.add_or_update_permissions,
        )
        self.check_permissions = async_to_streamed_response_wrapper(
            repos.check_permissions,
        )
        self.remove = async_to_streamed_response_wrapper(
            repos.remove,
        )
