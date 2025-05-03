from __future__ import annotations

from datetime import datetime
from typing import Union

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
from ....types.repos import (
    commit_get_check_runs_params,
    commit_get_check_suites_params,
    commit_get_pulls_params,
    commit_get_status_params,
    commit_get_statuses_params,
    commit_list_params,
    commit_retrieve_params,
)
from ....types.repos.commit import Commit
from ....types.repos.commit_branches_where_head_response import CommitBranchesWhereHeadResponse
from ....types.repos.commit_get_check_runs_response import CommitGetCheckRunsResponse
from ....types.repos.commit_get_check_suites_response import CommitGetCheckSuitesResponse
from ....types.repos.commit_get_pulls_response import CommitGetPullsResponse
from ....types.repos.commit_get_status_response import CommitGetStatusResponse
from ....types.repos.commit_get_statuses_response import CommitGetStatusesResponse
from ....types.repos.commit_list_response import CommitListResponse
from .comments import (
    AsyncCommentsResource,
    AsyncCommentsResourceWithRawResponse,
    AsyncCommentsResourceWithStreamingResponse,
    CommentsResource,
    CommentsResourceWithRawResponse,
    CommentsResourceWithStreamingResponse,
)

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
    @cached_property
    def comments(self) -> CommentsResource:
        return CommentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> CommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CommitsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        ref: str,
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
    ) -> Commit:
        """Returns the contents of a single commit reference.

        You must have `read` access
        for the repository to use this endpoint.

        > [!NOTE] If there are more than 300 files in the commit diff and the default
        > JSON media type is requested, the response will include pagination link
        > headers for the remaining files, up to a limit of 3000 files. Each page
        > contains the static commit information, and the only changes are to the file
        > listing.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."
        Pagination query parameters are not supported for these media types.

        - **`application/vnd.github.diff`**: Returns the diff of the commit. Larger
          diffs may time out and return a 5xx status code.
        - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs
          with binary data will have no `patch` property. Larger diffs may time out and
          return a 5xx status code.
        - **`application/vnd.github.sha`**: Returns the commit's SHA-1 hash. You can use
          this endpoint to check if a remote reference's SHA-1 hash is the same as your
          local reference's SHA-1 hash by providing the local SHA-1 reference as the
          ETag.

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                      |
        | ------------- | --------- | ------------------------------------------------------------------------------------------------ |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                  |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                |
        | `payload`     | `string`  | The value that was signed.                                                                       |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                   |

        These are the possible values for `reason` in the `verification` object:

        | Value                    | Description                                                                                                                     |
        | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
        | `expired_key`            | The key that made the signature is expired.                                                                                     |
        | `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                         |
        | `gpgverify_error`        | There was an error communicating with the signature verification service.                                                       |
        | `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                    |
        | `unsigned`               | The object does not include a signature.                                                                                        |
        | `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                    |
        | `no_user`                | No user was associated with the `committer` email address in the commit.                                                        |
        | `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. |
        | `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.           |
        | `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                |
        | `malformed_signature`    | There was an error parsing the signature.                                                                                       |
        | `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                    |
        | `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                |

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{ref}",
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
                    commit_retrieve_params.CommitRetrieveParams,
                ),
            ),
            cast_to=Commit,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        author: str | NotGiven = NOT_GIVEN,
        committer: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        until: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitListResponse:
        """
        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                      |
        | ------------- | --------- | ------------------------------------------------------------------------------------------------ |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                  |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                |
        | `payload`     | `string`  | The value that was signed.                                                                       |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                   |

        These are the possible values for `reason` in the `verification` object:

        | Value                    | Description                                                                                                                     |
        | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
        | `expired_key`            | The key that made the signature is expired.                                                                                     |
        | `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                         |
        | `gpgverify_error`        | There was an error communicating with the signature verification service.                                                       |
        | `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                    |
        | `unsigned`               | The object does not include a signature.                                                                                        |
        | `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                    |
        | `no_user`                | No user was associated with the `committer` email address in the commit.                                                        |
        | `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. |
        | `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.           |
        | `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                |
        | `malformed_signature`    | There was an error parsing the signature.                                                                                       |
        | `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                    |
        | `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                |

        Args:
          author: GitHub username or email address to use to filter by commit author.

          committer: GitHub username or email address to use to filter by commit committer.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          path: Only commits containing this file path will be returned.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sha: SHA or branch to start listing commits from. Default: the repository’s default
              branch (usually `main`).

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be between
              1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned.

          until: Only commits before this date will be returned. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be between
              1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned.

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
            f"/repos/{owner}/{repo}/commits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "author": author,
                        "committer": committer,
                        "page": page,
                        "path": path,
                        "per_page": per_page,
                        "sha": sha,
                        "since": since,
                        "until": until,
                    },
                    commit_list_params.CommitListParams,
                ),
            ),
            cast_to=CommitListResponse,
        )

    def branches_where_head(
        self,
        commit_sha: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitBranchesWhereHeadResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Returns all branches where the given commit SHA is the HEAD, or latest commit
        for the branch.

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
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CommitBranchesWhereHeadResponse,
        )

    def get_check_runs(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        app_id: int | NotGiven = NOT_GIVEN,
        check_name: str | NotGiven = NOT_GIVEN,
        filter: Literal["latest", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitGetCheckRunsResponse:
        """Lists check runs for a commit ref.

        The `ref` can be a SHA, branch name, or a tag
        name.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        If there are more than 1000 check suites on a single git reference, this
        endpoint will limit check runs to the 1000 most recent check suites. To iterate
        over all possible check runs, use the
        [List check suites for a Git reference](https://docs.github.com/rest/reference/checks#list-check-suites-for-a-git-reference)
        endpoint and provide the `check_suite_id` parameter to the
        [List check runs in a check suite](https://docs.github.com/rest/reference/checks#list-check-runs-in-a-check-suite)
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

        Args:
          check_name: Returns check runs with the specified `name`.

          filter: Filters check runs by their `completed_at` timestamp. `latest` returns the most
              recent check runs.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: Returns check runs with the specified `status`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/check-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "check_name": check_name,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    commit_get_check_runs_params.CommitGetCheckRunsParams,
                ),
            ),
            cast_to=CommitGetCheckRunsResponse,
        )

    def get_check_suites(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        app_id: int | NotGiven = NOT_GIVEN,
        check_name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitGetCheckSuitesResponse:
        """Lists check suites for a commit `ref`.

        The `ref` can be a SHA, branch name, or a
        tag name.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array
        > and a `null` value for `head_branch`.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

        Args:
          app_id: Filters check suites by GitHub App `id`.

          check_name: Returns check runs with the specified `name`.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/check-suites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "app_id": app_id,
                        "check_name": check_name,
                        "page": page,
                        "per_page": per_page,
                    },
                    commit_get_check_suites_params.CommitGetCheckSuitesParams,
                ),
            ),
            cast_to=CommitGetCheckSuitesResponse,
        )

    def get_pulls(
        self,
        commit_sha: str,
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
    ) -> CommitGetPullsResponse:
        """Lists the merged pull request that introduced the commit to the repository.

        If
        the commit is not present in the default branch, it will return merged and open
        pull requests associated with the commit.

        To list the open or merged pull requests associated with a branch, you can set
        the `commit_sha` parameter to the branch name.

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
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
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
                    commit_get_pulls_params.CommitGetPullsParams,
                ),
            ),
            cast_to=CommitGetPullsResponse,
        )

    def get_status(
        self,
        ref: str,
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
    ) -> CommitGetStatusResponse:
        """
        Users with pull access in a repository can access a combined view of commit
        statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.

        Additionally, a combined `state` is returned. The `state` is one of:

        - **failure** if any of the contexts report as `error` or `failure`
        - **pending** if there are no statuses or a context is `pending`
        - **success** if the latest status for all contexts is `success`

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/status",
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
                    commit_get_status_params.CommitGetStatusParams,
                ),
            ),
            cast_to=CommitGetStatusResponse,
        )

    def get_statuses(
        self,
        ref: str,
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
    ) -> CommitGetStatusesResponse:
        """
        Users with pull access in a repository can view commit statuses for a given ref.
        The ref can be a SHA, a branch name, or a tag name. Statuses are returned in
        reverse chronological order. The first status in the list will be the latest
        one.

        This resource is also available via a legacy route:
        `GET /repos/:owner/:repo/statuses/:ref`.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/statuses",
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
                    commit_get_statuses_params.CommitGetStatusesParams,
                ),
            ),
            cast_to=CommitGetStatusesResponse,
        )


class AsyncCommitsResource(AsyncAPIResource):
    @cached_property
    def comments(self) -> AsyncCommentsResource:
        return AsyncCommentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCommitsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCommitsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCommitsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCommitsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        ref: str,
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
    ) -> Commit:
        """Returns the contents of a single commit reference.

        You must have `read` access
        for the repository to use this endpoint.

        > [!NOTE] If there are more than 300 files in the commit diff and the default
        > JSON media type is requested, the response will include pagination link
        > headers for the remaining files, up to a limit of 3000 files. Each page
        > contains the static commit information, and the only changes are to the file
        > listing.

        This endpoint supports the following custom media types. For more information,
        see
        "[Media types](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#media-types)."
        Pagination query parameters are not supported for these media types.

        - **`application/vnd.github.diff`**: Returns the diff of the commit. Larger
          diffs may time out and return a 5xx status code.
        - **`application/vnd.github.patch`**: Returns the patch of the commit. Diffs
          with binary data will have no `patch` property. Larger diffs may time out and
          return a 5xx status code.
        - **`application/vnd.github.sha`**: Returns the commit's SHA-1 hash. You can use
          this endpoint to check if a remote reference's SHA-1 hash is the same as your
          local reference's SHA-1 hash by providing the local SHA-1 reference as the
          ETag.

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                      |
        | ------------- | --------- | ------------------------------------------------------------------------------------------------ |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                  |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                |
        | `payload`     | `string`  | The value that was signed.                                                                       |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                   |

        These are the possible values for `reason` in the `verification` object:

        | Value                    | Description                                                                                                                     |
        | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
        | `expired_key`            | The key that made the signature is expired.                                                                                     |
        | `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                         |
        | `gpgverify_error`        | There was an error communicating with the signature verification service.                                                       |
        | `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                    |
        | `unsigned`               | The object does not include a signature.                                                                                        |
        | `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                    |
        | `no_user`                | No user was associated with the `committer` email address in the commit.                                                        |
        | `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. |
        | `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.           |
        | `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                |
        | `malformed_signature`    | There was an error parsing the signature.                                                                                       |
        | `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                    |
        | `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                |

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{ref}",
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
                    commit_retrieve_params.CommitRetrieveParams,
                ),
            ),
            cast_to=Commit,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        author: str | NotGiven = NOT_GIVEN,
        committer: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        sha: str | NotGiven = NOT_GIVEN,
        since: str | datetime | NotGiven = NOT_GIVEN,
        until: str | datetime | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitListResponse:
        """
        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                      |
        | ------------- | --------- | ------------------------------------------------------------------------------------------------ |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                  |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                |
        | `payload`     | `string`  | The value that was signed.                                                                       |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                   |

        These are the possible values for `reason` in the `verification` object:

        | Value                    | Description                                                                                                                     |
        | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
        | `expired_key`            | The key that made the signature is expired.                                                                                     |
        | `not_signing_key`        | The "signing" flag is not among the usage flags in the GPG key that made the signature.                                         |
        | `gpgverify_error`        | There was an error communicating with the signature verification service.                                                       |
        | `gpgverify_unavailable`  | The signature verification service is currently unavailable.                                                                    |
        | `unsigned`               | The object does not include a signature.                                                                                        |
        | `unknown_signature_type` | A non-PGP signature was found in the commit.                                                                                    |
        | `no_user`                | No user was associated with the `committer` email address in the commit.                                                        |
        | `unverified_email`       | The `committer` email address in the commit was associated with a user, but the email address is not verified on their account. |
        | `bad_email`              | The `committer` email address in the commit is not included in the identities of the PGP key that made the signature.           |
        | `unknown_key`            | The key that made the signature has not been registered with any user's account.                                                |
        | `malformed_signature`    | There was an error parsing the signature.                                                                                       |
        | `invalid`                | The signature could not be cryptographically verified using the key whose key-id was found in the signature.                    |
        | `valid`                  | None of the above errors applied, so the signature is considered to be verified.                                                |

        Args:
          author: GitHub username or email address to use to filter by commit author.

          committer: GitHub username or email address to use to filter by commit committer.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          path: Only commits containing this file path will be returned.

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          sha: SHA or branch to start listing commits from. Default: the repository’s default
              branch (usually `main`).

          since: Only show results that were last updated after the given time. This is a
              timestamp in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be between
              1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned.

          until: Only commits before this date will be returned. This is a timestamp in
              [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format:
              `YYYY-MM-DDTHH:MM:SSZ`. Due to limitations of Git, timestamps must be between
              1970-01-01 and 2099-12-31 (inclusive) or unexpected results may be returned.

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
            f"/repos/{owner}/{repo}/commits",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "author": author,
                        "committer": committer,
                        "page": page,
                        "path": path,
                        "per_page": per_page,
                        "sha": sha,
                        "since": since,
                        "until": until,
                    },
                    commit_list_params.CommitListParams,
                ),
            ),
            cast_to=CommitListResponse,
        )

    async def branches_where_head(
        self,
        commit_sha: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitBranchesWhereHeadResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Returns all branches where the given commit SHA is the HEAD, or latest commit
        for the branch.

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
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/branches-where-head",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=CommitBranchesWhereHeadResponse,
        )

    async def get_check_runs(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        app_id: int | NotGiven = NOT_GIVEN,
        check_name: str | NotGiven = NOT_GIVEN,
        filter: Literal["latest", "all"] | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: Literal["queued", "in_progress", "completed"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitGetCheckRunsResponse:
        """Lists check runs for a commit ref.

        The `ref` can be a SHA, branch name, or a tag
        name.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array.

        If there are more than 1000 check suites on a single git reference, this
        endpoint will limit check runs to the 1000 most recent check suites. To iterate
        over all possible check runs, use the
        [List check suites for a Git reference](https://docs.github.com/rest/reference/checks#list-check-suites-for-a-git-reference)
        endpoint and provide the `check_suite_id` parameter to the
        [List check runs in a check suite](https://docs.github.com/rest/reference/checks#list-check-runs-in-a-check-suite)
        endpoint.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

        Args:
          check_name: Returns check runs with the specified `name`.

          filter: Filters check runs by their `completed_at` timestamp. `latest` returns the most
              recent check runs.

          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: Returns check runs with the specified `status`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/check-runs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "check_name": check_name,
                        "filter": filter,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    commit_get_check_runs_params.CommitGetCheckRunsParams,
                ),
            ),
            cast_to=CommitGetCheckRunsResponse,
        )

    async def get_check_suites(
        self,
        ref: str,
        *,
        owner: str,
        repo: str,
        app_id: int | NotGiven = NOT_GIVEN,
        check_name: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CommitGetCheckSuitesResponse:
        """Lists check suites for a commit `ref`.

        The `ref` can be a SHA, branch name, or a
        tag name.

        > [!NOTE] The endpoints to manage checks only look for pushes in the repository
        > where the check suite or check run were created. Pushes to a branch in a
        > forked repository are not detected and return an empty `pull_requests` array
        > and a `null` value for `head_branch`.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint on a private repository.

        Args:
          app_id: Filters check suites by GitHub App `id`.

          check_name: Returns check runs with the specified `name`.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/check-suites",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "app_id": app_id,
                        "check_name": check_name,
                        "page": page,
                        "per_page": per_page,
                    },
                    commit_get_check_suites_params.CommitGetCheckSuitesParams,
                ),
            ),
            cast_to=CommitGetCheckSuitesResponse,
        )

    async def get_pulls(
        self,
        commit_sha: str,
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
    ) -> CommitGetPullsResponse:
        """Lists the merged pull request that introduced the commit to the repository.

        If
        the commit is not present in the default branch, it will return merged and open
        pull requests associated with the commit.

        To list the open or merged pull requests associated with a branch, you can set
        the `commit_sha` parameter to the branch name.

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
        if not commit_sha:
            raise ValueError(f"Expected a non-empty value for `commit_sha` but received {commit_sha!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{commit_sha}/pulls",
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
                    commit_get_pulls_params.CommitGetPullsParams,
                ),
            ),
            cast_to=CommitGetPullsResponse,
        )

    async def get_status(
        self,
        ref: str,
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
    ) -> CommitGetStatusResponse:
        """
        Users with pull access in a repository can access a combined view of commit
        statuses for a given ref. The ref can be a SHA, a branch name, or a tag name.

        Additionally, a combined `state` is returned. The `state` is one of:

        - **failure** if any of the contexts report as `error` or `failure`
        - **pending** if there are no statuses or a context is `pending`
        - **success** if the latest status for all contexts is `success`

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/status",
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
                    commit_get_status_params.CommitGetStatusParams,
                ),
            ),
            cast_to=CommitGetStatusResponse,
        )

    async def get_statuses(
        self,
        ref: str,
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
    ) -> CommitGetStatusesResponse:
        """
        Users with pull access in a repository can view commit statuses for a given ref.
        The ref can be a SHA, a branch name, or a tag name. Statuses are returned in
        reverse chronological order. The first status in the list will be the latest
        one.

        This resource is also available via a legacy route:
        `GET /repos/:owner/:repo/statuses/:ref`.

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
        if not ref:
            raise ValueError(f"Expected a non-empty value for `ref` but received {ref!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/commits/{ref}/statuses",
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
                    commit_get_statuses_params.CommitGetStatusesParams,
                ),
            ),
            cast_to=CommitGetStatusesResponse,
        )


class CommitsResourceWithRawResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.retrieve = to_raw_response_wrapper(
            commits.retrieve,
        )
        self.list = to_raw_response_wrapper(
            commits.list,
        )
        self.branches_where_head = to_raw_response_wrapper(
            commits.branches_where_head,
        )
        self.get_check_runs = to_raw_response_wrapper(
            commits.get_check_runs,
        )
        self.get_check_suites = to_raw_response_wrapper(
            commits.get_check_suites,
        )
        self.get_pulls = to_raw_response_wrapper(
            commits.get_pulls,
        )
        self.get_status = to_raw_response_wrapper(
            commits.get_status,
        )
        self.get_statuses = to_raw_response_wrapper(
            commits.get_statuses,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithRawResponse:
        return CommentsResourceWithRawResponse(self._commits.comments)


class AsyncCommitsResourceWithRawResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.retrieve = async_to_raw_response_wrapper(
            commits.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            commits.list,
        )
        self.branches_where_head = async_to_raw_response_wrapper(
            commits.branches_where_head,
        )
        self.get_check_runs = async_to_raw_response_wrapper(
            commits.get_check_runs,
        )
        self.get_check_suites = async_to_raw_response_wrapper(
            commits.get_check_suites,
        )
        self.get_pulls = async_to_raw_response_wrapper(
            commits.get_pulls,
        )
        self.get_status = async_to_raw_response_wrapper(
            commits.get_status,
        )
        self.get_statuses = async_to_raw_response_wrapper(
            commits.get_statuses,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithRawResponse:
        return AsyncCommentsResourceWithRawResponse(self._commits.comments)


class CommitsResourceWithStreamingResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.retrieve = to_streamed_response_wrapper(
            commits.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            commits.list,
        )
        self.branches_where_head = to_streamed_response_wrapper(
            commits.branches_where_head,
        )
        self.get_check_runs = to_streamed_response_wrapper(
            commits.get_check_runs,
        )
        self.get_check_suites = to_streamed_response_wrapper(
            commits.get_check_suites,
        )
        self.get_pulls = to_streamed_response_wrapper(
            commits.get_pulls,
        )
        self.get_status = to_streamed_response_wrapper(
            commits.get_status,
        )
        self.get_statuses = to_streamed_response_wrapper(
            commits.get_statuses,
        )

    @cached_property
    def comments(self) -> CommentsResourceWithStreamingResponse:
        return CommentsResourceWithStreamingResponse(self._commits.comments)


class AsyncCommitsResourceWithStreamingResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.retrieve = async_to_streamed_response_wrapper(
            commits.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            commits.list,
        )
        self.branches_where_head = async_to_streamed_response_wrapper(
            commits.branches_where_head,
        )
        self.get_check_runs = async_to_streamed_response_wrapper(
            commits.get_check_runs,
        )
        self.get_check_suites = async_to_streamed_response_wrapper(
            commits.get_check_suites,
        )
        self.get_pulls = async_to_streamed_response_wrapper(
            commits.get_pulls,
        )
        self.get_status = async_to_streamed_response_wrapper(
            commits.get_status,
        )
        self.get_statuses = async_to_streamed_response_wrapper(
            commits.get_statuses,
        )

    @cached_property
    def comments(self) -> AsyncCommentsResourceWithStreamingResponse:
        return AsyncCommentsResourceWithStreamingResponse(self._commits.comments)
