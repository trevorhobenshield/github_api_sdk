from __future__ import annotations

from typing import Dict

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
from ...types.orgs import repo_create_params, repo_list_params
from ...types.orgs.full_repository import FullRepository
from ...types.orgs.repo_list_response import RepoListResponse

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
        org: str,
        *,
        name: str,
        allow_auto_merge: bool | NotGiven = NOT_GIVEN,
        allow_merge_commit: bool | NotGiven = NOT_GIVEN,
        allow_rebase_merge: bool | NotGiven = NOT_GIVEN,
        allow_squash_merge: bool | NotGiven = NOT_GIVEN,
        auto_init: bool | NotGiven = NOT_GIVEN,
        custom_properties: dict[str, object] | NotGiven = NOT_GIVEN,
        delete_branch_on_merge: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        gitignore_template: str | NotGiven = NOT_GIVEN,
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
        use_squash_pr_title_as_default: bool | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """Creates a new repository in the specified organization.

        The authenticated user
        must be a member of the organization.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to create a public repository, and `repo` scope to create a private
        repository.

        Args:
          name: The name of the repository.

          allow_auto_merge: Either `true` to allow auto-merge on pull requests, or `false` to disallow
              auto-merge.

          allow_merge_commit: Either `true` to allow merging pull requests with a merge commit, or `false` to
              prevent merging pull requests with merge commits.

          allow_rebase_merge: Either `true` to allow rebase-merging pull requests, or `false` to prevent
              rebase-merging.

          allow_squash_merge: Either `true` to allow squash-merging pull requests, or `false` to prevent
              squash-merging.

          auto_init: Pass `true` to create an initial commit with empty README.

          custom_properties: The custom properties for the new repository. The keys are the custom property
              names, and the values are the corresponding custom property values.

          delete_branch_on_merge: Either `true` to allow automatically deleting head branches when pull requests
              are merged, or `false` to prevent automatic deletion. **The authenticated user
              must be an organization owner to set this property to `true`.**

          description: A short description of the repository.

          gitignore_template: Desired language or platform
              [.gitignore template](https://github.com/github/gitignore) to apply. Use the
              name of the template without the extension. For example, "Haskell".

          has_downloads: Whether downloads are enabled.

          has_issues: Either `true` to enable issues for this repository or `false` to disable them.

          has_projects: Either `true` to enable projects for this repository or `false` to disable them.
              **Note:** If you're creating a repository in an organization that has disabled
              repository projects, the default is `false`, and if you pass `true`, the API
              returns an error.

          has_wiki: Either `true` to enable the wiki for this repository or `false` to disable it.

          homepage: A URL with more information about the repository.

          is_template: Either `true` to make this repo available as a template repository or `false` to
              prevent it.

          license_template: Choose an [open source license template](https://choosealicense.com/) that best
              suits your needs, and then use the
              [license keyword](https://docs.github.com/articles/licensing-a-repository/#searching-github-by-license-type)
              as the `license_template` string. For example, "mit" or "mpl-2.0".

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

          use_squash_pr_title_as_default: Either `true` to allow squash-merge commits to use pull request title, or
              `false` to use commit message. \\**\\**This property is closing down. Please use
              `squash_merge_commit_title` instead.

          visibility: The visibility of the repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/repos",
            body=maybe_transform(
                {
                    "name": name,
                    "allow_auto_merge": allow_auto_merge,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                    "allow_squash_merge": allow_squash_merge,
                    "auto_init": auto_init,
                    "custom_properties": custom_properties,
                    "delete_branch_on_merge": delete_branch_on_merge,
                    "description": description,
                    "gitignore_template": gitignore_template,
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
                    "use_squash_pr_title_as_default": use_squash_pr_title_as_default,
                    "visibility": visibility,
                },
                repo_create_params.RepoCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    def list(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "pushed", "full_name"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "public", "private", "forks", "sources", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListResponse:
        """
        Lists repositories for the specified organization.

        > [!NOTE] In order to see the `security_and_analysis` block for a repository you
        > must have admin permissions for the repository or be an owner or security
        > manager for the organization that owns the repository. For more information,
        > see
        > "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

        Args:
          direction: The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          type: Specifies the types of repositories you want returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "type": type,
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
        org: str,
        *,
        name: str,
        allow_auto_merge: bool | NotGiven = NOT_GIVEN,
        allow_merge_commit: bool | NotGiven = NOT_GIVEN,
        allow_rebase_merge: bool | NotGiven = NOT_GIVEN,
        allow_squash_merge: bool | NotGiven = NOT_GIVEN,
        auto_init: bool | NotGiven = NOT_GIVEN,
        custom_properties: dict[str, object] | NotGiven = NOT_GIVEN,
        delete_branch_on_merge: bool | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        gitignore_template: str | NotGiven = NOT_GIVEN,
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
        use_squash_pr_title_as_default: bool | NotGiven = NOT_GIVEN,
        visibility: Literal["public", "private"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FullRepository:
        """Creates a new repository in the specified organization.

        The authenticated user
        must be a member of the organization.

        OAuth app tokens and personal access tokens (classic) need the `public_repo` or
        `repo` scope to create a public repository, and `repo` scope to create a private
        repository.

        Args:
          name: The name of the repository.

          allow_auto_merge: Either `true` to allow auto-merge on pull requests, or `false` to disallow
              auto-merge.

          allow_merge_commit: Either `true` to allow merging pull requests with a merge commit, or `false` to
              prevent merging pull requests with merge commits.

          allow_rebase_merge: Either `true` to allow rebase-merging pull requests, or `false` to prevent
              rebase-merging.

          allow_squash_merge: Either `true` to allow squash-merging pull requests, or `false` to prevent
              squash-merging.

          auto_init: Pass `true` to create an initial commit with empty README.

          custom_properties: The custom properties for the new repository. The keys are the custom property
              names, and the values are the corresponding custom property values.

          delete_branch_on_merge: Either `true` to allow automatically deleting head branches when pull requests
              are merged, or `false` to prevent automatic deletion. **The authenticated user
              must be an organization owner to set this property to `true`.**

          description: A short description of the repository.

          gitignore_template: Desired language or platform
              [.gitignore template](https://github.com/github/gitignore) to apply. Use the
              name of the template without the extension. For example, "Haskell".

          has_downloads: Whether downloads are enabled.

          has_issues: Either `true` to enable issues for this repository or `false` to disable them.

          has_projects: Either `true` to enable projects for this repository or `false` to disable them.
              **Note:** If you're creating a repository in an organization that has disabled
              repository projects, the default is `false`, and if you pass `true`, the API
              returns an error.

          has_wiki: Either `true` to enable the wiki for this repository or `false` to disable it.

          homepage: A URL with more information about the repository.

          is_template: Either `true` to make this repo available as a template repository or `false` to
              prevent it.

          license_template: Choose an [open source license template](https://choosealicense.com/) that best
              suits your needs, and then use the
              [license keyword](https://docs.github.com/articles/licensing-a-repository/#searching-github-by-license-type)
              as the `license_template` string. For example, "mit" or "mpl-2.0".

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

          use_squash_pr_title_as_default: Either `true` to allow squash-merge commits to use pull request title, or
              `false` to use commit message. \\**\\**This property is closing down. Please use
              `squash_merge_commit_title` instead.

          visibility: The visibility of the repository.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/repos",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "allow_auto_merge": allow_auto_merge,
                    "allow_merge_commit": allow_merge_commit,
                    "allow_rebase_merge": allow_rebase_merge,
                    "allow_squash_merge": allow_squash_merge,
                    "auto_init": auto_init,
                    "custom_properties": custom_properties,
                    "delete_branch_on_merge": delete_branch_on_merge,
                    "description": description,
                    "gitignore_template": gitignore_template,
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
                    "use_squash_pr_title_as_default": use_squash_pr_title_as_default,
                    "visibility": visibility,
                },
                repo_create_params.RepoCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=FullRepository,
        )

    async def list(
        self,
        org: str,
        *,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "pushed", "full_name"] | NotGiven = NOT_GIVEN,
        type: Literal["all", "public", "private", "forks", "sources", "member"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RepoListResponse:
        """
        Lists repositories for the specified organization.

        > [!NOTE] In order to see the `security_and_analysis` block for a repository you
        > must have admin permissions for the repository or be an owner or security
        > manager for the organization that owns the repository. For more information,
        > see
        > "[Managing security managers in your organization](https://docs.github.com/organizations/managing-peoples-access-to-your-organization-with-roles/managing-security-managers-in-your-organization)."

        Args:
          direction: The order to sort by. Default: `asc` when using `full_name`, otherwise `desc`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: The property to sort the results by.

          type: Specifies the types of repositories you want returned.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/repos",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direction": direction,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "type": type,
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
