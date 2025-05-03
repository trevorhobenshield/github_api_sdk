from __future__ import annotations

import httpx
from typing_extensions import Literal

from ...._base_client import make_request_options
from ...._compat import cached_property
from ...._resource import AsyncAPIResource, SyncAPIResource
from ...._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.orgs.members.codespace import Codespace
from ....types.repos import (
    pull_create_codespace_params,
    pull_create_params,
    pull_list_commits_params,
    pull_list_files_params,
    pull_list_params,
    pull_update_branch_params,
    pull_update_params,
)
from ....types.repos.pull_list_commits_response import PullListCommitsResponse
from ....types.repos.pull_list_files_response import PullListFilesResponse
from ....types.repos.pull_list_response import PullListResponse
from ....types.repos.pull_request import PullRequest
from ....types.repos.pull_update_branch_response import PullUpdateBranchResponse
from .comments.comments import (
    AsyncCommentsResource,
    AsyncCommentsResourceWithRawResponse,
    AsyncCommentsResourceWithStreamingResponse,
    CommentsResource,
    CommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
)
from .merge import (
    AsyncMergeResource,
    AsyncMergeResourceWithRawResponse,
    AsyncMergeResourceWithStreamingResponse,
    MergeResource,
    MergeResourceWithRawResponse,
    MergeResourceWithStreamingResponse,
)
from .requested_reviewers import (
    AsyncRequestedReviewersResource,
    AsyncRequestedReviewersResourceWithRawResponse,
    AsyncRequestedReviewersResourceWithStreamingResponse,
    RequestedReviewersResource,
    RequestedReviewersResourceWithRawResponse,
    RequestedReviewersResourceWithStreamingResponse,
)
from .reviews import (
    AsyncReviewsResource,
    AsyncReviewsResourceWithRawResponse,
    AsyncReviewsResourceWithStreamingResponse,
    ReviewsResource,
    ReviewsResourceWithRawResponse,
    ReviewsResourceWithStreamingResponse,
)

__all__ = ["PullsResource", "AsyncPullsResource"]


class PullsResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def merge(self) -> MergeResource:
        return MergeResource(self._client)

    @cached_property
    def requested_reviewers(self) -> RequestedReviewersResource:
        return RequestedReviewersResource(self._client)

    @cached_property
    def reviews(self) -> ReviewsResource:
        return ReviewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> PullsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return PullsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PullsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return PullsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        base: str,
        head: str,
        body: str | NotGiven = NOT_GIVEN,
        draft: bool | NotGiven = NOT_GIVEN,
        head_repo: str | NotGiven = NOT_GIVEN,
        issue: int | NotGiven = NOT_GIVEN,
        maintainer_can_modify: bool | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequest:
        """
        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To open or update a pull request in a public repository, you must have write
        access to the head or the source branch. For organization-owned repositories,
        you must be a member of the organization that owns the repository to open or
        update a pull request.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          base: The name of the branch you want the changes pulled into. This should be an
              existing branch on the current repository. You cannot submit a pull request to
              one repository that requests a merge to a base of another repository.

          head: The name of the branch where your changes are implemented. For cross-repository
              pull requests in the same network, namespace `head` with a user like this:
              `username:branch`.

          body: The contents of the pull request.

          draft: Indicates whether the pull request is a draft. See
              "[Draft Pull Requests](https://docs.github.com/articles/about-pull-requests#draft-pull-requests)"
              in the GitHub Help documentation to learn more.

          head_repo: The name of the repository where the changes in the pull request were made. This
              field is required for cross-repository pull requests if both repositories are
              owned by the same organization.

          issue: An issue in the repository to convert to a pull request. The issue title, body,
              and comments will become the title, body, and comments on the new pull request.
              Required unless `title` is specified.

          maintainer_can_modify: Indicates whether
              [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/)
              the pull request.

          title: The title of the new pull request. Required unless `issue` is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/pulls",
            body=maybe_transform(
                {
                    "base": base,
                    "head": head,
                    "body": body,
                    "draft": draft,
                    "head_repo": head_repo,
                    "issue": issue,
                    "maintainer_can_modify": maintainer_can_modify,
                    "title": title,
                },
                pull_create_params.PullCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequest,
        )

    def retrieve(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequest:
        """
        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Lists details of a pull request by providing its number.

        When you get,
        [create](https://docs.github.com/rest/pulls/pulls/#create-a-pull-request), or
        [edit](https://docs.github.com/rest/pulls/pulls#update-a-pull-request) a pull
        request, GitHub creates a merge commit to test whether the pull request can be
        automatically merged into the base branch. This test commit is not added to the
        base branch or the head branch. You can review the status of the test commit
        using the `mergeable` key. For more information, see
        "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

        The value of the `mergeable` attribute can be `true`, `false`, or `null`. If the
        value is `null`, then GitHub has started a background job to compute the
        mergeability. After giving the job time to complete, resubmit the request. When
        the job finishes, you will see a non-`null` value for the `mergeable` attribute
        in the response. If `mergeable` is `true`, then `merge_commit_sha` will be the
        SHA of the _test_ merge commit.

        The value of the `merge_commit_sha` attribute changes depending on the state of
        the pull request. Before merging a pull request, the `merge_commit_sha`
        attribute holds the SHA of the _test_ merge commit. After merging a pull
        request, the `merge_commit_sha` attribute changes depending on how you merged
        the pull request:

        - If merged as a
          [merge commit](https://docs.github.com/articles/about-merge-methods-on-github/),
          `merge_commit_sha` represents the SHA of the merge commit.
        - If merged via a
          [squash](https://docs.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits),
          `merge_commit_sha` represents the SHA of the squashed commit on the base
          branch.
        - If
          [rebased](https://docs.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits),
          `merge_commit_sha` represents the commit that the base branch was updated to.

        Pass the appropriate
        [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)
        to fetch diff and patch formats.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.
        - **`application/vnd.github.diff`**: For more information, see
          "[git-diff](https://git-scm.com/docs/git-diff)" in the Git documentation. If a
          diff is corrupt, contact us through the
          [GitHub Support portal](https://support.github.com/). Include the repository
          name and pull request ID in your message.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequest,
        )

    def update(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        base: str | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        maintainer_can_modify: bool | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequest:
        """
        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To open or update a pull request in a public repository, you must have write
        access to the head or the source branch. For organization-owned repositories,
        you must be a member of the organization that owns the repository to open or
        update a pull request.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          base: The name of the branch you want your changes pulled into. This should be an
              existing branch on the current repository. You cannot update the base branch on
              a pull request to point to another repository.

          body: The contents of the pull request.

          maintainer_can_modify: Indicates whether
              [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/)
              the pull request.

          state: State of this Pull Request. Either `open` or `closed`.

          title: The title of the pull request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._patch(
            f"/repos/{owner}/{repo}/pulls/{pull_number}",
            body=maybe_transform(
                {
                    "base": base,
                    "body": body,
                    "maintainer_can_modify": maintainer_can_modify,
                    "state": state,
                    "title": title,
                },
                pull_update_params.PullUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequest,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        base: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        head: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "popularity", "long-running"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullListResponse:
        """
        Lists pull requests in a specified repository.

        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          base: Filter pulls by base branch name. Example: `gh-pages`.

          direction: The direction of the sort. Default: `desc` when sort is `created` or sort is not
              specified, otherwise `asc`.

          head: Filter pulls by head user or head organization and branch name in the format of
              `user:ref-name` or `organization:ref-name`. For example:
              `github:new-script-format` or `octocat:test-branch`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: What to sort results by. `popularity` will sort by the number of comments.
              `long-running` will sort by date created and will limit the results to pull
              requests that have been open for more than a month and have had activity within
              the past month.

          state: Either `open`, `closed`, or `all` to filter by state.

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
            f"/repos/{owner}/{repo}/pulls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "base": base,
                        "direction": direction,
                        "head": head,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    pull_list_params.PullListParams,
                ),
            ),
            cast_to=PullListResponse,
        )

    def create_codespace(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        devcontainer_path: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"] | NotGiven = NOT_GIVEN,
        idle_timeout_minutes: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        multi_repo_permissions_opt_out: bool | NotGiven = NOT_GIVEN,
        retention_period_minutes: int | NotGiven = NOT_GIVEN,
        working_directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Creates a codespace owned by the authenticated user for the specified pull
        request.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: IP for location auto-detection when proxying a request

          devcontainer_path: Path to devcontainer.json config to use for this codespace

          display_name: Display name for this codespace

          geo: The geographic area for this codespace. If not specified, the value is assigned
              by IP. This property replaces `location`, which is closing down.

          idle_timeout_minutes: Time in minutes before codespace stops from inactivity

          location: The requested location for a new codespace. Best efforts are made to respect
              this upon creation. Assigned by IP if not provided.

          machine: Machine type to use for this codespace

          multi_repo_permissions_opt_out: Whether to authorize requested permissions from devcontainer.json

          retention_period_minutes: Duration in minutes after codespace has gone idle in which it will be deleted.
              Must be integer minutes between 0 and 43200 (30 days).

          working_directory: Working directory for this codespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/codespaces",
            body=maybe_transform(
                {
                    "client_ip": client_ip,
                    "devcontainer_path": devcontainer_path,
                    "display_name": display_name,
                    "geo": geo,
                    "idle_timeout_minutes": idle_timeout_minutes,
                    "location": location,
                    "machine": machine,
                    "multi_repo_permissions_opt_out": multi_repo_permissions_opt_out,
                    "retention_period_minutes": retention_period_minutes,
                    "working_directory": working_directory,
                },
                pull_create_codespace_params.PullCreateCodespaceParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    def list_commits(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullListCommitsResponse:
        """Lists a maximum of 250 commits for a pull request.

        To receive a complete commit
        list for pull requests with more than 250 commits, use the
        [List commits](https://docs.github.com/rest/commits/commits#list-commits)
        endpoint.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
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
                    pull_list_commits_params.PullListCommitsParams,
                ),
            ),
            cast_to=PullListCommitsResponse,
        )

    def list_files(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullListFilesResponse:
        """
        Lists the files in a specified pull request.

        > [!NOTE] Responses include a maximum of 3000 files. The paginated response
        > returns 30 files per page by default.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
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
                    pull_list_files_params.PullListFilesParams,
                ),
            ),
            cast_to=PullListFilesResponse,
        )

    def update_branch(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        expected_head_sha: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullUpdateBranchResponse:
        """
        Updates the pull request branch with the latest upstream changes by merging HEAD
        from the base branch into the pull request branch. Note: If making a request on
        behalf of a GitHub App you must also have permissions to write the contents of
        the head repository.

        Args:
          expected_head_sha: The expected SHA of the pull request's HEAD ref. This is the most recent commit
              on the pull request's branch. If the expected SHA does not match the pull
              request's HEAD, you will receive a `422 Unprocessable Entity` status. You can
              use the
              "[List commits](https://docs.github.com/rest/commits/commits#list-commits)"
              endpoint to find the most recent commit SHA. Default: SHA of the pull request's
              current HEAD ref.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch",
            body=maybe_transform({"expected_head_sha": expected_head_sha}, pull_update_branch_params.PullUpdateBranchParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullUpdateBranchResponse,
        )


class AsyncPullsResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def merge(self) -> AsyncMergeResource:
        return AsyncMergeResource(self._client)

    @cached_property
    def requested_reviewers(self) -> AsyncRequestedReviewersResource:
        return AsyncRequestedReviewersResource(self._client)

    @cached_property
    def reviews(self) -> AsyncReviewsResource:
        return AsyncReviewsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncPullsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPullsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPullsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncPullsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        base: str,
        head: str,
        body: str | NotGiven = NOT_GIVEN,
        draft: bool | NotGiven = NOT_GIVEN,
        head_repo: str | NotGiven = NOT_GIVEN,
        issue: int | NotGiven = NOT_GIVEN,
        maintainer_can_modify: bool | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequest:
        """
        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To open or update a pull request in a public repository, you must have write
        access to the head or the source branch. For organization-owned repositories,
        you must be a member of the organization that owns the repository to open or
        update a pull request.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          base: The name of the branch you want the changes pulled into. This should be an
              existing branch on the current repository. You cannot submit a pull request to
              one repository that requests a merge to a base of another repository.

          head: The name of the branch where your changes are implemented. For cross-repository
              pull requests in the same network, namespace `head` with a user like this:
              `username:branch`.

          body: The contents of the pull request.

          draft: Indicates whether the pull request is a draft. See
              "[Draft Pull Requests](https://docs.github.com/articles/about-pull-requests#draft-pull-requests)"
              in the GitHub Help documentation to learn more.

          head_repo: The name of the repository where the changes in the pull request were made. This
              field is required for cross-repository pull requests if both repositories are
              owned by the same organization.

          issue: An issue in the repository to convert to a pull request. The issue title, body,
              and comments will become the title, body, and comments on the new pull request.
              Required unless `title` is specified.

          maintainer_can_modify: Indicates whether
              [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/)
              the pull request.

          title: The title of the new pull request. Required unless `issue` is specified.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/pulls",
            body=await async_maybe_transform(
                {
                    "base": base,
                    "head": head,
                    "body": body,
                    "draft": draft,
                    "head_repo": head_repo,
                    "issue": issue,
                    "maintainer_can_modify": maintainer_can_modify,
                    "title": title,
                },
                pull_create_params.PullCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequest,
        )

    async def retrieve(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequest:
        """
        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Lists details of a pull request by providing its number.

        When you get,
        [create](https://docs.github.com/rest/pulls/pulls/#create-a-pull-request), or
        [edit](https://docs.github.com/rest/pulls/pulls#update-a-pull-request) a pull
        request, GitHub creates a merge commit to test whether the pull request can be
        automatically merged into the base branch. This test commit is not added to the
        base branch or the head branch. You can review the status of the test commit
        using the `mergeable` key. For more information, see
        "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".

        The value of the `mergeable` attribute can be `true`, `false`, or `null`. If the
        value is `null`, then GitHub has started a background job to compute the
        mergeability. After giving the job time to complete, resubmit the request. When
        the job finishes, you will see a non-`null` value for the `mergeable` attribute
        in the response. If `mergeable` is `true`, then `merge_commit_sha` will be the
        SHA of the _test_ merge commit.

        The value of the `merge_commit_sha` attribute changes depending on the state of
        the pull request. Before merging a pull request, the `merge_commit_sha`
        attribute holds the SHA of the _test_ merge commit. After merging a pull
        request, the `merge_commit_sha` attribute changes depending on how you merged
        the pull request:

        - If merged as a
          [merge commit](https://docs.github.com/articles/about-merge-methods-on-github/),
          `merge_commit_sha` represents the SHA of the merge commit.
        - If merged via a
          [squash](https://docs.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits),
          `merge_commit_sha` represents the SHA of the squashed commit on the base
          branch.
        - If
          [rebased](https://docs.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits),
          `merge_commit_sha` represents the commit that the base branch was updated to.

        Pass the appropriate
        [media type](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)
        to fetch diff and patch formats.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.
        - **`application/vnd.github.diff`**: For more information, see
          "[git-diff](https://git-scm.com/docs/git-diff)" in the Git documentation. If a
          diff is corrupt, contact us through the
          [GitHub Support portal](https://support.github.com/). Include the repository
          name and pull request ID in your message.

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
            f"/repos/{owner}/{repo}/pulls/{pull_number}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequest,
        )

    async def update(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        base: str | NotGiven = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        maintainer_can_modify: bool | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed"] | NotGiven = NOT_GIVEN,
        title: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullRequest:
        """
        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        To open or update a pull request in a public repository, you must have write
        access to the head or the source branch. For organization-owned repositories,
        you must be a member of the organization that owns the repository to open or
        update a pull request.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          base: The name of the branch you want your changes pulled into. This should be an
              existing branch on the current repository. You cannot update the base branch on
              a pull request to point to another repository.

          body: The contents of the pull request.

          maintainer_can_modify: Indicates whether
              [maintainers can modify](https://docs.github.com/articles/allowing-changes-to-a-pull-request-branch-created-from-a-fork/)
              the pull request.

          state: State of this Pull Request. Either `open` or `closed`.

          title: The title of the pull request.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._patch(
            f"/repos/{owner}/{repo}/pulls/{pull_number}",
            body=await async_maybe_transform(
                {
                    "base": base,
                    "body": body,
                    "maintainer_can_modify": maintainer_can_modify,
                    "state": state,
                    "title": title,
                },
                pull_update_params.PullUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullRequest,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        base: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        head: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sort: Literal["created", "updated", "popularity", "long-running"] | NotGiven = NOT_GIVEN,
        state: Literal["open", "closed", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullListResponse:
        """
        Lists pull requests in a specified repository.

        Draft pull requests are available in public repositories with GitHub Free and
        GitHub Free for organizations, GitHub Pro, and legacy per-repository billing
        plans, and in public and private repositories with GitHub Team and GitHub
        Enterprise Cloud. For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

        Args:
          base: Filter pulls by base branch name. Example: `gh-pages`.

          direction: The direction of the sort. Default: `desc` when sort is `created` or sort is not
              specified, otherwise `asc`.

          head: Filter pulls by head user or head organization and branch name in the format of
              `user:ref-name` or `organization:ref-name`. For example:
              `github:new-script-format` or `octocat:test-branch`.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sort: What to sort results by. `popularity` will sort by the number of comments.
              `long-running` will sort by date created and will limit the results to pull
              requests that have been open for more than a month and have had activity within
              the past month.

          state: Either `open`, `closed`, or `all` to filter by state.

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
            f"/repos/{owner}/{repo}/pulls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "base": base,
                        "direction": direction,
                        "head": head,
                        "page": page,
                        "per_page": per_page,
                        "sort": sort,
                        "state": state,
                    },
                    pull_list_params.PullListParams,
                ),
            ),
            cast_to=PullListResponse,
        )

    async def create_codespace(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        client_ip: str | NotGiven = NOT_GIVEN,
        devcontainer_path: str | NotGiven = NOT_GIVEN,
        display_name: str | NotGiven = NOT_GIVEN,
        geo: Literal["EuropeWest", "SoutheastAsia", "UsEast", "UsWest"] | NotGiven = NOT_GIVEN,
        idle_timeout_minutes: int | NotGiven = NOT_GIVEN,
        location: str | NotGiven = NOT_GIVEN,
        machine: str | NotGiven = NOT_GIVEN,
        multi_repo_permissions_opt_out: bool | NotGiven = NOT_GIVEN,
        retention_period_minutes: int | NotGiven = NOT_GIVEN,
        working_directory: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Codespace:
        """
        Creates a codespace owned by the authenticated user for the specified pull
        request.

        OAuth app tokens and personal access tokens (classic) need the `codespace` scope
        to use this endpoint.

        Args:
          client_ip: IP for location auto-detection when proxying a request

          devcontainer_path: Path to devcontainer.json config to use for this codespace

          display_name: Display name for this codespace

          geo: The geographic area for this codespace. If not specified, the value is assigned
              by IP. This property replaces `location`, which is closing down.

          idle_timeout_minutes: Time in minutes before codespace stops from inactivity

          location: The requested location for a new codespace. Best efforts are made to respect
              this upon creation. Assigned by IP if not provided.

          machine: Machine type to use for this codespace

          multi_repo_permissions_opt_out: Whether to authorize requested permissions from devcontainer.json

          retention_period_minutes: Duration in minutes after codespace has gone idle in which it will be deleted.
              Must be integer minutes between 0 and 43200 (30 days).

          working_directory: Working directory for this codespace

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/codespaces",
            body=await async_maybe_transform(
                {
                    "client_ip": client_ip,
                    "devcontainer_path": devcontainer_path,
                    "display_name": display_name,
                    "geo": geo,
                    "idle_timeout_minutes": idle_timeout_minutes,
                    "location": location,
                    "machine": machine,
                    "multi_repo_permissions_opt_out": multi_repo_permissions_opt_out,
                    "retention_period_minutes": retention_period_minutes,
                    "working_directory": working_directory,
                },
                pull_create_codespace_params.PullCreateCodespaceParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Codespace,
        )

    async def list_commits(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullListCommitsResponse:
        """Lists a maximum of 250 commits for a pull request.

        To receive a complete commit
        list for pull requests with more than 250 commits, use the
        [List commits](https://docs.github.com/rest/commits/commits#list-commits)
        endpoint.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/commits",
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
                    pull_list_commits_params.PullListCommitsParams,
                ),
            ),
            cast_to=PullListCommitsResponse,
        )

    async def list_files(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullListFilesResponse:
        """
        Lists the files in a specified pull request.

        > [!NOTE] Responses include a maximum of 3000 files. The paginated response
        > returns 30 files per page by default.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."

        - **`application/vnd.github.raw+json`**: Returns the raw markdown body. Response
          will include `body`. This is the default if you do not pass any specific media
          type.
        - **`application/vnd.github.text+json`**: Returns a text only representation of
          the markdown body. Response will include `body_text`.
        - **`application/vnd.github.html+json`**: Returns HTML rendered from the body's
          markdown. Response will include `body_html`.
        - **`application/vnd.github.full+json`**: Returns raw, text, and HTML
          representations. Response will include `body`, `body_text`, and `body_html`.

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
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/files",
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
                    pull_list_files_params.PullListFilesParams,
                ),
            ),
            cast_to=PullListFilesResponse,
        )

    async def update_branch(
        self,
        pull_number: int,
        *,
        owner: str,
        repo: str,
        expected_head_sha: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PullUpdateBranchResponse:
        """
        Updates the pull request branch with the latest upstream changes by merging HEAD
        from the base branch into the pull request branch. Note: If making a request on
        behalf of a GitHub App you must also have permissions to write the contents of
        the head repository.

        Args:
          expected_head_sha: The expected SHA of the pull request's HEAD ref. This is the most recent commit
              on the pull request's branch. If the expected SHA does not match the pull
              request's HEAD, you will receive a `422 Unprocessable Entity` status. You can
              use the
              "[List commits](https://docs.github.com/rest/commits/commits#list-commits)"
              endpoint to find the most recent commit SHA. Default: SHA of the pull request's
              current HEAD ref.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/pulls/{pull_number}/update-branch",
            body=await async_maybe_transform({"expected_head_sha": expected_head_sha}, pull_update_branch_params.PullUpdateBranchParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=PullUpdateBranchResponse,
        )


class PullsResourceWithRawResponse:
    def __init__(self, pulls: PullsResource) -> None:
        self._pulls = pulls

        self.create = to_raw_response_wrapper(
            pulls.create,
        )
        self.retrieve = to_raw_response_wrapper(
            pulls.retrieve,
        )
        self.update = to_raw_response_wrapper(
            pulls.update,
        )
        self.list = to_raw_response_wrapper(
            pulls.list,
        )
        self.create_codespace = to_raw_response_wrapper(
            pulls.create_codespace,
        )
        self.list_commits = to_raw_response_wrapper(
            pulls.list_commits,
        )
        self.list_files = to_raw_response_wrapper(
            pulls.list_files,
        )
        self.update_branch = to_raw_response_wrapper(
            pulls.update_branch,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._pulls.comments)

    @cached_property
    def merge(self) -> MergeResourceWithRawResponse:
        return MergeResourceWithRawResponse(self._pulls.merge)

    @cached_property
    def requested_reviewers(self) -> RequestedReviewersResourceWithRawResponse:
        return RequestedReviewersResourceWithRawResponse(self._pulls.requested_reviewers)

    @cached_property
    def reviews(self) -> ReviewsResourceWithRawResponse:
        return ReviewsResourceWithRawResponse(self._pulls.reviews)


class AsyncPullsResourceWithRawResponse:
    def __init__(self, pulls: AsyncPullsResource) -> None:
        self._pulls = pulls

        self.create = async_to_raw_response_wrapper(
            pulls.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            pulls.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            pulls.update,
        )
        self.list = async_to_raw_response_wrapper(
            pulls.list,
        )
        self.create_codespace = async_to_raw_response_wrapper(
            pulls.create_codespace,
        )
        self.list_commits = async_to_raw_response_wrapper(
            pulls.list_commits,
        )
        self.list_files = async_to_raw_response_wrapper(
            pulls.list_files,
        )
        self.update_branch = async_to_raw_response_wrapper(
            pulls.update_branch,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._pulls.comments)

    @cached_property
    def merge(self) -> AsyncMergeResourceWithRawResponse:
        return AsyncMergeResourceWithRawResponse(self._pulls.merge)

    @cached_property
    def requested_reviewers(self) -> AsyncRequestedReviewersResourceWithRawResponse:
        return AsyncRequestedReviewersResourceWithRawResponse(self._pulls.requested_reviewers)

    @cached_property
    def reviews(self) -> AsyncReviewsResourceWithRawResponse:
        return AsyncReviewsResourceWithRawResponse(self._pulls.reviews)


class PullsResourceWithStreamingResponse:
    def __init__(self, pulls: PullsResource) -> None:
        self._pulls = pulls

        self.create = to_streamed_response_wrapper(
            pulls.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            pulls.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            pulls.update,
        )
        self.list = to_streamed_response_wrapper(
            pulls.list,
        )
        self.create_codespace = to_streamed_response_wrapper(
            pulls.create_codespace,
        )
        self.list_commits = to_streamed_response_wrapper(
            pulls.list_commits,
        )
        self.list_files = to_streamed_response_wrapper(
            pulls.list_files,
        )
        self.update_branch = to_streamed_response_wrapper(
            pulls.update_branch,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._pulls.comments)

    @cached_property
    def merge(self) -> MergeResourceWithStreamingResponse:
        return MergeResourceWithStreamingResponse(self._pulls.merge)

    @cached_property
    def requested_reviewers(self) -> RequestedReviewersResourceWithStreamingResponse:
        return RequestedReviewersResourceWithStreamingResponse(self._pulls.requested_reviewers)

    @cached_property
    def reviews(self) -> ReviewsResourceWithStreamingResponse:
        return ReviewsResourceWithStreamingResponse(self._pulls.reviews)


class AsyncPullsResourceWithStreamingResponse:
    def __init__(self, pulls: AsyncPullsResource) -> None:
        self._pulls = pulls

        self.create = async_to_streamed_response_wrapper(
            pulls.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            pulls.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            pulls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            pulls.list,
        )
        self.create_codespace = async_to_streamed_response_wrapper(
            pulls.create_codespace,
        )
        self.list_commits = async_to_streamed_response_wrapper(
            pulls.list_commits,
        )
        self.list_files = async_to_streamed_response_wrapper(
            pulls.list_files,
        )
        self.update_branch = async_to_streamed_response_wrapper(
            pulls.update_branch,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._pulls.comments)

    @cached_property
    def merge(self) -> AsyncMergeResourceWithStreamingResponse:
        return AsyncMergeResourceWithStreamingResponse(self._pulls.merge)

    @cached_property
    def requested_reviewers(self) -> AsyncRequestedReviewersResourceWithStreamingResponse:
        return AsyncRequestedReviewersResourceWithStreamingResponse(self._pulls.requested_reviewers)

    @cached_property
    def reviews(self) -> AsyncReviewsResourceWithStreamingResponse:
        return AsyncReviewsResourceWithStreamingResponse(self._pulls.reviews)
