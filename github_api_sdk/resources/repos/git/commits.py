from __future__ import annotations

from typing import List

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
from ...._types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos.git import commit_create_params
from ....types.repos.git.git_commit import GitCommit

__all__ = ["CommitsResource", "AsyncCommitsResource"]


class CommitsResource(SyncAPIResource):
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

    def create(
        self,
        repo: str,
        *,
        owner: str,
        message: str,
        tree: str,
        author: commit_create_params.Author | NotGiven = NOT_GIVEN,
        committer: commit_create_params.Committer | NotGiven = NOT_GIVEN,
        parents: list[str] | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitCommit:
        """
        Creates a new Git
        [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                          |
        | ------------- | --------- | ---------------------------------------------------------------------------------------------------- |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                      |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in the table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                    |
        | `payload`     | `string`  | The value that was signed.                                                                           |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                       |

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
          message: The commit message

          tree: The SHA of the tree object this commit points to

          author: Information about the author of the commit. By default, the `author` will be the
              authenticated user and the current date. See the `author` and `committer` object
              below for details.

          committer: Information about the person who is making the commit. By default, `committer`
              will use the information set in `author`. See the `author` and `committer`
              object below for details.

          parents: The full SHAs of the commits that were the parents of this commit. If omitted or
              empty, the commit will be written as a root commit. For a single parent, an
              array of one SHA should be provided; for a merge commit, an array of more than
              one should be provided.

          signature: The [PGP signature](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) of the
              commit. GitHub adds the signature to the `gpgsig` header of the created commit.
              For a commit signature to be verifiable by Git or GitHub, it must be an
              ASCII-armored detached PGP signature over the string commit as it would be
              written to the object database. To pass a `signature` parameter, you need to
              first manually create a valid PGP signature, which can be complicated. You may
              find it easier to
              [use the command line](https://git-scm.com/book/id/v2/Git-Tools-Signing-Your-Work)
              to create signed commits.

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
            f"/repos/{owner}/{repo}/git/commits",
            body=maybe_transform(
                {
                    "message": message,
                    "tree": tree,
                    "author": author,
                    "committer": committer,
                    "parents": parents,
                    "signature": signature,
                },
                commit_create_params.CommitCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitCommit,
        )

    def retrieve(
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
    ) -> GitCommit:
        """
        Gets a Git
        [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).

        To get the contents of a commit, see
        "[Get a commit](/rest/commits/commits#get-a-commit)."

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                          |
        | ------------- | --------- | ---------------------------------------------------------------------------------------------------- |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                      |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in the table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                    |
        | `payload`     | `string`  | The value that was signed.                                                                           |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                       |

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
            f"/repos/{owner}/{repo}/git/commits/{commit_sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitCommit,
        )


class AsyncCommitsResource(AsyncAPIResource):
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

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        message: str,
        tree: str,
        author: commit_create_params.Author | NotGiven = NOT_GIVEN,
        committer: commit_create_params.Committer | NotGiven = NOT_GIVEN,
        parents: list[str] | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitCommit:
        """
        Creates a new Git
        [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                          |
        | ------------- | --------- | ---------------------------------------------------------------------------------------------------- |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                      |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in the table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                    |
        | `payload`     | `string`  | The value that was signed.                                                                           |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                       |

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
          message: The commit message

          tree: The SHA of the tree object this commit points to

          author: Information about the author of the commit. By default, the `author` will be the
              authenticated user and the current date. See the `author` and `committer` object
              below for details.

          committer: Information about the person who is making the commit. By default, `committer`
              will use the information set in `author`. See the `author` and `committer`
              object below for details.

          parents: The full SHAs of the commits that were the parents of this commit. If omitted or
              empty, the commit will be written as a root commit. For a single parent, an
              array of one SHA should be provided; for a merge commit, an array of more than
              one should be provided.

          signature: The [PGP signature](https://en.wikipedia.org/wiki/Pretty_Good_Privacy) of the
              commit. GitHub adds the signature to the `gpgsig` header of the created commit.
              For a commit signature to be verifiable by Git or GitHub, it must be an
              ASCII-armored detached PGP signature over the string commit as it would be
              written to the object database. To pass a `signature` parameter, you need to
              first manually create a valid PGP signature, which can be complicated. You may
              find it easier to
              [use the command line](https://git-scm.com/book/id/v2/Git-Tools-Signing-Your-Work)
              to create signed commits.

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
            f"/repos/{owner}/{repo}/git/commits",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "tree": tree,
                    "author": author,
                    "committer": committer,
                    "parents": parents,
                    "signature": signature,
                },
                commit_create_params.CommitCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitCommit,
        )

    async def retrieve(
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
    ) -> GitCommit:
        """
        Gets a Git
        [commit object](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects).

        To get the contents of a commit, see
        "[Get a commit](/rest/commits/commits#get-a-commit)."

        **Signature verification object**

        The response will include a `verification` object that describes the result of
        verifying the commit's signature. The following fields are included in the
        `verification` object:

        | Name          | Type      | Description                                                                                          |
        | ------------- | --------- | ---------------------------------------------------------------------------------------------------- |
        | `verified`    | `boolean` | Indicates whether GitHub considers the signature in this commit to be verified.                      |
        | `reason`      | `string`  | The reason for verified value. Possible values and their meanings are enumerated in the table below. |
        | `signature`   | `string`  | The signature that was extracted from the commit.                                                    |
        | `payload`     | `string`  | The value that was signed.                                                                           |
        | `verified_at` | `string`  | The date the signature was verified by GitHub.                                                       |

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
            f"/repos/{owner}/{repo}/git/commits/{commit_sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitCommit,
        )


class CommitsResourceWithRawResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.create = to_raw_response_wrapper(
            commits.create,
        )
        self.retrieve = to_raw_response_wrapper(
            commits.retrieve,
        )


class AsyncCommitsResourceWithRawResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.create = async_to_raw_response_wrapper(
            commits.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            commits.retrieve,
        )


class CommitsResourceWithStreamingResponse:
    def __init__(self, commits: CommitsResource) -> None:
        self._commits = commits

        self.create = to_streamed_response_wrapper(
            commits.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            commits.retrieve,
        )


class AsyncCommitsResourceWithStreamingResponse:
    def __init__(self, commits: AsyncCommitsResource) -> None:
        self._commits = commits

        self.create = async_to_streamed_response_wrapper(
            commits.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            commits.retrieve,
        )
