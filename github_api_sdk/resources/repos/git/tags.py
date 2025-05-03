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
from ....types.repos.git import tag_create_params
from ....types.repos.git.git_tag import GitTag

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        message: str,
        object: str,
        tag: str,
        type: Literal["commit", "tree", "blob"],
        tagger: tag_create_params.Tagger | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTag:
        """
        Note that creating a tag object does not create the reference that makes a tag
        in Git. If you want to create an annotated tag in Git, you have to do this call
        to create the tag object, and then
        [create](https://docs.github.com/rest/git/refs#create-a-reference) the
        `refs/tags/[tag]` reference. If you want to create a lightweight tag, you only
        have to [create](https://docs.github.com/rest/git/refs#create-a-reference) the
        tag reference - this call would be unnecessary.

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
          message: The tag message.

          object: The SHA of the git object this is tagging.

          tag: The tag's name. This is typically a version (e.g., "v0.0.1").

          type: The type of the object we're tagging. Normally this is a `commit` but it can
              also be a `tree` or a `blob`.

          tagger: An object with information about the individual creating the tag.

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
            f"/repos/{owner}/{repo}/git/tags",
            body=maybe_transform(
                {
                    "message": message,
                    "object": object,
                    "tag": tag,
                    "type": type,
                    "tagger": tagger,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitTag,
        )

    def retrieve(
        self,
        tag_sha: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTag:
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not tag_sha:
            raise ValueError(f"Expected a non-empty value for `tag_sha` but received {tag_sha!r}")
        return self._get(
            f"/repos/{owner}/{repo}/git/tags/{tag_sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitTag,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        message: str,
        object: str,
        tag: str,
        type: Literal["commit", "tree", "blob"],
        tagger: tag_create_params.Tagger | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTag:
        """
        Note that creating a tag object does not create the reference that makes a tag
        in Git. If you want to create an annotated tag in Git, you have to do this call
        to create the tag object, and then
        [create](https://docs.github.com/rest/git/refs#create-a-reference) the
        `refs/tags/[tag]` reference. If you want to create a lightweight tag, you only
        have to [create](https://docs.github.com/rest/git/refs#create-a-reference) the
        tag reference - this call would be unnecessary.

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
          message: The tag message.

          object: The SHA of the git object this is tagging.

          tag: The tag's name. This is typically a version (e.g., "v0.0.1").

          type: The type of the object we're tagging. Normally this is a `commit` but it can
              also be a `tree` or a `blob`.

          tagger: An object with information about the individual creating the tag.

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
            f"/repos/{owner}/{repo}/git/tags",
            body=await async_maybe_transform(
                {
                    "message": message,
                    "object": object,
                    "tag": tag,
                    "type": type,
                    "tagger": tagger,
                },
                tag_create_params.TagCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitTag,
        )

    async def retrieve(
        self,
        tag_sha: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GitTag:
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
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not tag_sha:
            raise ValueError(f"Expected a non-empty value for `tag_sha` but received {tag_sha!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/git/tags/{tag_sha}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=GitTag,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.create = to_raw_response_wrapper(
            tags.create,
        )
        self.retrieve = to_raw_response_wrapper(
            tags.retrieve,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.create = async_to_raw_response_wrapper(
            tags.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            tags.retrieve,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.create = to_streamed_response_wrapper(
            tags.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            tags.retrieve,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.create = async_to_streamed_response_wrapper(
            tags.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            tags.retrieve,
        )
