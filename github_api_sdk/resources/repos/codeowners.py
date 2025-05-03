from __future__ import annotations

import httpx

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
from ...types.repos import codeowner_list_errors_params
from ...types.repos.codeowner_list_errors_response import CodeownerListErrorsResponse

__all__ = ["CodeownersResource", "AsyncCodeownersResource"]


class CodeownersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CodeownersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return CodeownersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CodeownersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return CodeownersResourceWithStreamingResponse(self)

    def list_errors(
        self,
        repo: str,
        *,
        owner: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeownerListErrorsResponse:
        """
        List any syntax errors that are detected in the CODEOWNERS file.

        For more information about the correct CODEOWNERS syntax, see
        "[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)."

        Args:
          ref: A branch, tag or commit name used to determine which version of the CODEOWNERS
              file to use. Default: the repository's default branch (e.g. `main`)

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
            f"/repos/{owner}/{repo}/codeowners/errors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"ref": ref}, codeowner_list_errors_params.CodeownerListErrorsParams),
            ),
            cast_to=CodeownerListErrorsResponse,
        )


class AsyncCodeownersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCodeownersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCodeownersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCodeownersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncCodeownersResourceWithStreamingResponse(self)

    async def list_errors(
        self,
        repo: str,
        *,
        owner: str,
        ref: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CodeownerListErrorsResponse:
        """
        List any syntax errors that are detected in the CODEOWNERS file.

        For more information about the correct CODEOWNERS syntax, see
        "[About code owners](https://docs.github.com/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners)."

        Args:
          ref: A branch, tag or commit name used to determine which version of the CODEOWNERS
              file to use. Default: the repository's default branch (e.g. `main`)

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
            f"/repos/{owner}/{repo}/codeowners/errors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"ref": ref}, codeowner_list_errors_params.CodeownerListErrorsParams),
            ),
            cast_to=CodeownerListErrorsResponse,
        )


class CodeownersResourceWithRawResponse:
    def __init__(self, codeowners: CodeownersResource) -> None:
        self._codeowners = codeowners

        self.list_errors = to_raw_response_wrapper(
            codeowners.list_errors,
        )


class AsyncCodeownersResourceWithRawResponse:
    def __init__(self, codeowners: AsyncCodeownersResource) -> None:
        self._codeowners = codeowners

        self.list_errors = async_to_raw_response_wrapper(
            codeowners.list_errors,
        )


class CodeownersResourceWithStreamingResponse:
    def __init__(self, codeowners: CodeownersResource) -> None:
        self._codeowners = codeowners

        self.list_errors = to_streamed_response_wrapper(
            codeowners.list_errors,
        )


class AsyncCodeownersResourceWithStreamingResponse:
    def __init__(self, codeowners: AsyncCodeownersResource) -> None:
        self._codeowners = codeowners

        self.list_errors = async_to_streamed_response_wrapper(
            codeowners.list_errors,
        )
