from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ..._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ..._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ...types.orgs.full_repository import FullRepository
from ...types.users import repo_create_params, repo_list_params
from ...types.users.repo_list_response import RepoListResponse

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

    def create(
        self,
        *,
        name: str,
        allow_auto_merge: bool | NotGiven = NOT_GIVEN,
        allow_merge_commit: bool | NotGiven = NOT_GIVEN,
        allow_rebase_merge: bool | NotGiven = NOT_GIVEN,
        allow_squash_merge: bool | NotGiven = NOT_GIVEN,
        auto_init: bool | NotGiven = NOT_GIVEN,
        delete_branch_on_merge: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        gitignore_template: str | NotGiven = NOT_GIVEN,
        has_discussions: bool | NotGiven = NOT_GIVEN,
        has_downloads: bool | NotGiven = NOT_GIVEN,
        has_issues: bool | NotGiven = NOT_GIVEN,
        has_projects: bool | NotGiven = NOT_GIVEN,
        has_wiki: bool | NotGiven = NOT_GIVEN,
        homepage: str | NotGiven = NOT_GIVEN,
        is_template: bool | NotGiven = NOT_GIVEN,
        license_template: str | NotGiven = NOT_GIVEN,
        merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | NotGiven = NOT_GIVEN,
        merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | NotGiven = NOT_GIVEN,
        squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | NotGiven = NOT_GIVEN,
        team_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """
        Creates a new repository for the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to create a public repository, and `repo` scope to create a private
        repository.

        Args:
          name: The name of the repository.

          allow_auto_merge: Whether to allow Auto-merge to be used on pull requests.

          allow_merge_commit: Whether to allow merge commits for pull requests.

          allow_rebase_merge: Whether to allow rebase merges for pull requests.

          allow_squash_merge: Whether to allow squash merges for pull requests.

          auto_init: Whether the repository is initialized with a minimal README.

          delete_branch_on_merge: Whether to delete head branches when pull requests are merged

          description: A short description of the repository.

          gitignore_template: The desired language or platform to apply to the .gitignore.

          has_discussions: Whether discussions are enabled.

          has_downloads: Whether downloads are enabled.

          has_issues: Whether issues are enabled.

          has_projects: Whether projects are enabled.

          has_wiki: Whether the wiki is enabled.

          homepage: A URL with more information about the repository.

          is_template: Whether this repository acts as a template that can be used to generate new
              repositories.

          license_template: The license keyword of the open source license for this repository.

          merge_commit_message: The default value for a merge commit message.

              - `PR_TITLE` - default to the pull request's title.
              - `PR_BODY` - default to the pull request's body.
              - `BLANK` - default to a blank commit message.

          merge_commit_title: Required when using `merge_commit_message`.

              The default value for a merge commit title.

              - `PR_TITLE` - default to the pull request's title.
              - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
                Merge pull request #123 from branch-name).

          private: Whether the repository is private.

          squash_merge_commit_message:
              The default value for a squash merge commit message:

              - `PR_BODY` - default to the pull request's body.
              - `COMMIT_MESSAGES` - default to the branch's commit messages.
              - `BLANK` - default to a blank commit message.

          squash_merge_commit_title: Required when using `squash_merge_commit_message`.

              The default value for a squash merge commit title:

              - `PR_TITLE` - default to the pull request's title.
              - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
                the pull request's title (when more than one commit).

          team_id: The id of the team that will be granted access to this repository. This is only
              valid when creating a repository in an organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/user/repos",
            body=maybe_transform(
                {
                    "name": name,
                    "allow_auto_merge": allow_auto_merge,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                    "allow_squash_merge": allow_squash_merge,
                    "auto_init": auto_init,
                    "delete_branch_on_merge": delete_branch_on_merge,
                    "description": description,
                    "gitignore_template": gitignore_template,
                    "has_discussions": has_discussions,
                    "has_downloads": has_downloads,
                    "has_issues": has_issues,
                    "has_projects": has_projects,
                    "has_wiki": has_wiki,
                    "homepage": homepage,
                    "is_template": is_template,
                    "license_template": license_template,
                    "merge_commit_message": merge_commit_message,
                    "merge_commit_title": merge_commit_title,
                    "private": private,
                    "squash_merge_commit_message": squash_merge_commit_message,
                    "squash_merge_commit_title": squash_merge_commit_title,
                    "team_id": team_id,
                },
                repo_create_params.RepoCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    def list(
        self,
        *,
        affiliation: str | NotGiven = NOT_GIVEN,
        before: str | datetime | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "pushed", "full_name"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "owner", "public", "private", "member"] | NotGiven = NOT_GIVEN,
        visibility: Literal["all", "public", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListResponse:
        """
        Lists repositories that the authenticated user has explicit permission (`:read`,
        `:write`, or `:admin`) to access.

        The authenticated user has explicit permission to access repositories they own,
        repositories where they are a collaborator, and repositories that they can
        access through an organization membership.

        Args:
          affiliation:
              Comma-separated list of values. Can include:

              - `owner`: Repositories that are owned by the authenticated user.
              - `collaborator`: Repositories that the user has been added to as a
                collaborator.
              - `organization_member`: Repositories that the user has access to through being
                a member of an organization. This includes every repository on every team that
                the user is on.

          before: Only show repositories updated before the given time. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          direction: The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show repositories updated after the given time. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: The property to sort the results by.

          type: Limit results to repositories of the specified type. Will cause a `422` error if
              used in the same request as **visibility** or **affiliation**.

          visibility: Limit results to repositories with the specified visibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "affiliation": affiliation,
                        "before": before,
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                        "type": type,
                        "visibility": visibility,
                    },
                    repo_list_params.RepoListParams,
                ),
            ),
            cast_to=RepoListResponse,
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

    async def create(
        self,
        *,
        name: str,
        allow_auto_merge: bool | NotGiven = NOT_GIVEN,
        allow_merge_commit: bool | NotGiven = NOT_GIVEN,
        allow_rebase_merge: bool | NotGiven = NOT_GIVEN,
        allow_squash_merge: bool | NotGiven = NOT_GIVEN,
        auto_init: bool | NotGiven = NOT_GIVEN,
        delete_branch_on_merge: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        gitignore_template: str | NotGiven = NOT_GIVEN,
        has_discussions: bool | NotGiven = NOT_GIVEN,
        has_downloads: bool | NotGiven = NOT_GIVEN,
        has_issues: bool | NotGiven = NOT_GIVEN,
        has_projects: bool | NotGiven = NOT_GIVEN,
        has_wiki: bool | NotGiven = NOT_GIVEN,
        homepage: str | NotGiven = NOT_GIVEN,
        is_template: bool | NotGiven = NOT_GIVEN,
        license_template: str | NotGiven = NOT_GIVEN,
        merge_commit_message: Literal["PR_BODY", "PR_TITLE", "BLANK"] | NotGiven = NOT_GIVEN,
        merge_commit_title: Literal["PR_TITLE", "MERGE_MESSAGE"] | NotGiven = NOT_GIVEN,
        private: bool | NotGiven = NOT_GIVEN,
        squash_merge_commit_message: Literal["PR_BODY", "COMMIT_MESSAGES", "BLANK"] | NotGiven = NOT_GIVEN,
        squash_merge_commit_title: Literal["PR_TITLE", "COMMIT_OR_PR_TITLE"] | NotGiven = NOT_GIVEN,
        team_id: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """
        Creates a new repository for the authenticated user.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to create a public repository, and `repo` scope to create a private
        repository.

        Args:
          name: The name of the repository.

          allow_auto_merge: Whether to allow Auto-merge to be used on pull requests.

          allow_merge_commit: Whether to allow merge commits for pull requests.

          allow_rebase_merge: Whether to allow rebase merges for pull requests.

          allow_squash_merge: Whether to allow squash merges for pull requests.

          auto_init: Whether the repository is initialized with a minimal README.

          delete_branch_on_merge: Whether to delete head branches when pull requests are merged

          description: A short description of the repository.

          gitignore_template: The desired language or platform to apply to the .gitignore.

          has_discussions: Whether discussions are enabled.

          has_downloads: Whether downloads are enabled.

          has_issues: Whether issues are enabled.

          has_projects: Whether projects are enabled.

          has_wiki: Whether the wiki is enabled.

          homepage: A URL with more information about the repository.

          is_template: Whether this repository acts as a template that can be used to generate new
              repositories.

          license_template: The license keyword of the open source license for this repository.

          merge_commit_message: The default value for a merge commit message.

              - `PR_TITLE` - default to the pull request's title.
              - `PR_BODY` - default to the pull request's body.
              - `BLANK` - default to a blank commit message.

          merge_commit_title: Required when using `merge_commit_message`.

              The default value for a merge commit title.

              - `PR_TITLE` - default to the pull request's title.
              - `MERGE_MESSAGE` - default to the classic title for a merge message (e.g.,
                Merge pull request #123 from branch-name).

          private: Whether the repository is private.

          squash_merge_commit_message:
              The default value for a squash merge commit message:

              - `PR_BODY` - default to the pull request's body.
              - `COMMIT_MESSAGES` - default to the branch's commit messages.
              - `BLANK` - default to a blank commit message.

          squash_merge_commit_title: Required when using `squash_merge_commit_message`.

              The default value for a squash merge commit title:

              - `PR_TITLE` - default to the pull request's title.
              - `COMMIT_OR_PR_TITLE` - default to the commit's title (if only one commit) or
                the pull request's title (when more than one commit).

          team_id: The id of the team that will be granted access to this repository. This is only
              valid when creating a repository in an organization.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/user/repos",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allow_auto_merge": allow_auto_merge,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                    "allow_squash_merge": allow_squash_merge,
                    "auto_init": auto_init,
                    "delete_branch_on_merge": delete_branch_on_merge,
                    "description": description,
                    "gitignore_template": gitignore_template,
                    "has_discussions": has_discussions,
                    "has_downloads": has_downloads,
                    "has_issues": has_issues,
                    "has_projects": has_projects,
                    "has_wiki": has_wiki,
                    "homepage": homepage,
                    "is_template": is_template,
                    "license_template": license_template,
                    "merge_commit_message": merge_commit_message,
                    "merge_commit_title": merge_commit_title,
                    "private": private,
                    "squash_merge_commit_message": squash_merge_commit_message,
                    "squash_merge_commit_title": squash_merge_commit_title,
                    "team_id": team_id,
                },
                repo_create_params.RepoCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    async def list(
        self,
        *,
        affiliation: str | NotGiven = NOT_GIVEN,
        before: str | datetime | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "pushed", "full_name"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "owner", "public", "private", "member"] | NotGiven = NOT_GIVEN,
        visibility: Literal["all", "public", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListResponse:
        """
        Lists repositories that the authenticated user has explicit permission (`:read`,
        `:write`, or `:admin`) to access.

        The authenticated user has explicit permission to access repositories they own,
        repositories where they are a collaborator, and repositories that they can
        access through an organization membership.

        Args:
          affiliation:
              Comma-separated list of values. Can include:

              - `owner`: Repositories that are owned by the authenticated user.
              - `collaborator`: Repositories that the user has been added to as a
                collaborator.
              - `organization_member`: Repositories that the user has access to through being
                a member of an organization. This includes every repository on every team that
                the user is on.

          before: Only show repositories updated before the given time. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          direction: The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          since: Only show repositories updated after the given time. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`.

          sort: The property to sort the results by.

          type: Limit results to repositories of the specified type. Will cause a `422` error if
              used in the same request as **visibility** or **affiliation**.

          visibility: Limit results to repositories with the specified visibility.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "affiliation": affiliation,
                        "before": before,
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "since": since,
                        "sort": sort,
                        "type": type,
                        "visibility": visibility,
                    },
                    repo_list_params.RepoListParams,
                ),
            ),
            cast_to=RepoListResponse,
        )


class ReposResourceWithRawResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.create = to_raw_response_wrapper(
            repos.create,
        )
        self.list = to_raw_response_wrapper(
            repos.list,
        )


class AsyncReposResourceWithRawResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.create = async_to_raw_response_wrapper(
            repos.create,
        )
        self.list = async_to_raw_response_wrapper(
            repos.list,
        )


class ReposResourceWithStreamingResponse:
    def __init__(self, repos: ReposResource) -> None:
        self._repos = repos

        self.create = to_streamed_response_wrapper(
            repos.create,
        )
        self.list = to_streamed_response_wrapper(
            repos.list,
        )


class AsyncReposResourceWithStreamingResponse:
    def __init__(self, repos: AsyncReposResource) -> None:
        self._repos = repos

        self.create = async_to_streamed_response_wrapper(
            repos.create,
        )
        self.list = async_to_streamed_response_wrapper(
            repos.list,
        )
