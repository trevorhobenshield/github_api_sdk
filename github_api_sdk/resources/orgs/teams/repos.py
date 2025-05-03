from __future__ import annotations

import httpx

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs.teams import repo_list_params, repo_update_params
from ....types.orgs.teams.repo_list_response import RepoListResponse
from ....types.orgs.teams.team_repository import TeamRepository

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

    def retrieve(
        self,
        repo: str,
        *,
        org: str,
        team_slug: str,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamRepository:
        """
        Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull`
        permission for a repository. Repositories inherited through a parent team will
        also be checked.

        You can also get information about the specified repository, including what
        permissions the team grants on it, by passing the following custom
        [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types/)
        via the `application/vnd.github.v3.repository+json` accept header.

        If a team doesn't have permission for the repository, you will receive a
        `404 Not Found` response status.

        If the repository is private, you must have at least `read` permission for that
        repository, and your token must have the `repo` or `admin:org` scope. Otherwise,
        you will receive a `404 Not Found` response status.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamRepository,
        )

    def update(
        self,
        repo: str,
        *,
        org: str,
        team_slug: str,
        owner: str,
        permission: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        To add a repository to a team or update the team's permission on a repository,
        the authenticated user must have admin access to the repository, and must be
        able to see the team. The repository must be owned by the organization, or a
        direct fork of a repository owned by the organization. You will get a
        `422 Unprocessable Entity` status if you attempt to add a repository to a team
        that is not owned by the organization. Note that, if you choose not to pass any
        parameters, you'll need to set `Content-Length` to zero when calling out to this
        endpoint. For more information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

        For more information about the permission levels, see
        "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)".

        Args:
          permission: The permission to grant the team on this repository. We accept the following
              permissions to be set: `pull`, `triage`, `push`, `maintain`, `admin` and you can
              also specify a custom repository role name, if the owning organization has
              defined any. If no permission is specified, the team's `permission` attribute
              will be used to determine what permission to grant the team on this repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._put(
            f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
            body=maybe_transform({"permission": permission}, repo_update_params.RepoUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list(
        self,
        team_slug: str,
        *,
        org: str,
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
        Lists a team's repositories visible to the authenticated user.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/repos`.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return self._get(
            f"/orgs/{org}/teams/{team_slug}/repos",
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

    def delete(
        self,
        repo: str,
        *,
        org: str,
        team_slug: str,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        If the authenticated user is an organization owner or a team maintainer, they
        can remove any repositories from the team. To remove a repository from a team as
        an organization member, the authenticated user must have admin access to the
        repository and must be able to see the team. This does not delete the
        repository, it just removes it from the team.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
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

    async def retrieve(
        self,
        repo: str,
        *,
        org: str,
        team_slug: str,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TeamRepository:
        """
        Checks whether a team has `admin`, `push`, `maintain`, `triage`, or `pull`
        permission for a repository. Repositories inherited through a parent team will
        also be checked.

        You can also get information about the specified repository, including what
        permissions the team grants on it, by passing the following custom
        [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types/)
        via the `application/vnd.github.v3.repository+json` accept header.

        If a team doesn't have permission for the repository, you will receive a
        `404 Not Found` response status.

        If the repository is private, you must have at least `read` permission for that
        repository, and your token must have the `repo` or `admin:org` scope. Otherwise,
        you will receive a `404 Not Found` response status.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=TeamRepository,
        )

    async def update(
        self,
        repo: str,
        *,
        org: str,
        team_slug: str,
        owner: str,
        permission: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        To add a repository to a team or update the team's permission on a repository,
        the authenticated user must have admin access to the repository, and must be
        able to see the team. The repository must be owned by the organization, or a
        direct fork of a repository owned by the organization. You will get a
        `422 Unprocessable Entity` status if you attempt to add a repository to a team
        that is not owned by the organization. Note that, if you choose not to pass any
        parameters, you'll need to set `Content-Length` to zero when calling out to this
        endpoint. For more information, see
        "[HTTP method](https://docs.github.com/rest/guides/getting-started-with-the-rest-api#http-method)."

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `PUT /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

        For more information about the permission levels, see
        "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)".

        Args:
          permission: The permission to grant the team on this repository. We accept the following
              permissions to be set: `pull`, `triage`, `push`, `maintain`, `admin` and you can
              also specify a custom repository role name, if the owning organization has
              defined any. If no permission is specified, the team's `permission` attribute
              will be used to determine what permission to grant the team on this repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._put(
            f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
            body=await async_maybe_transform({"permission": permission}, repo_update_params.RepoUpdateParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list(
        self,
        team_slug: str,
        *,
        org: str,
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
        Lists a team's repositories visible to the authenticated user.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `GET /organizations/{org_id}/team/{team_id}/repos`.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        return await self._get(
            f"/orgs/{org}/teams/{team_slug}/repos",
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

    async def delete(
        self,
        repo: str,
        *,
        org: str,
        team_slug: str,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        If the authenticated user is an organization owner or a team maintainer, they
        can remove any repositories from the team. To remove a repository from a team as
        an organization member, the authenticated user must have admin access to the
        repository and must be able to see the team. This does not delete the
        repository, it just removes it from the team.

        > [!NOTE] You can also specify a team by `org_id` and `team_id` using the route
        > `DELETE /organizations/{org_id}/team/{team_id}/repos/{owner}/{repo}`.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not team_slug:
            raise ValueError(f"Expected a non-empty value for `team_slug` but received {team_slug!r}")
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_raw_response_wrapper(
            repos.retrieve,
        )
        self.update = to_raw_response_wrapper(
            repos.update,
        )
        self.list = to_raw_response_wrapper(
            repos.list,
        )
        self.delete = to_raw_response_wrapper(
            repos.delete,
        )


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_raw_response_wrapper(
            repos.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            repos.update,
        )
        self.list = async_to_raw_response_wrapper(
            repos.list,
        )
        self.delete = async_to_raw_response_wrapper(
            repos.delete,
        )


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.retrieve = to_streamed_response_wrapper(
            repos.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            repos.update,
        )
        self.list = to_streamed_response_wrapper(
            repos.list,
        )
        self.delete = to_streamed_response_wrapper(
            repos.delete,
        )


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.retrieve = async_to_streamed_response_wrapper(
            repos.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            repos.update,
        )
        self.list = async_to_streamed_response_wrapper(
            repos.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            repos.delete,
        )
