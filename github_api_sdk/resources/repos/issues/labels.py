from __future__ import annotations

import builtins
from typing import Iterable, List

import httpx
from typing_extensions import overload

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
    required_args,
)
from ....types.repos.issues import label_add_params, label_list_params, label_set_params
from ....types.repos.issues.label_add_response import LabelAddResponse
from ....types.repos.issues.label_list_response import LabelListResponse
from ....types.repos.issues.label_remove_response import LabelRemoveResponse
from ....types.repos.issues.label_set_response import LabelSetResponse

__all__ = ["LabelsResource", "AsyncLabelsResource"]


class LabelsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> LabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return LabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return LabelsResourceWithStreamingResponse(self)

    def list(
        self,
        issue_number: int,
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
    ) -> LabelListResponse:
        """
        Lists all labels for an issue.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )

    @overload
    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          labels: The names of the labels to add to the issue's existing labels. You can pass an
              empty array to remove all labels. Alternatively, you can pass a single label as
              a `string` or an `array` of labels directly, but GitHub recommends passing an
              object with the `labels` key. You can also replace all of the labels for an
              issue. For more information, see
              "[Set labels for an issue](https://docs.github.com/rest/issues/labels#set-labels-for-an-issue)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: Iterable[label_add_params.Variant2Label] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: Iterable[label_add_params.Variant3Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo"])
    def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | Iterable[label_add_params.Variant2Label] | NotGiven = NOT_GIVEN,
        body: builtins.list[str] | Iterable[label_add_params.Variant3Body] | str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._post(
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
            body=maybe_transform(
                {
                    "labels": labels,
                    "body": body,
                },
                label_add_params.LabelAddParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelAddResponse,
        )

    def remove(
        self,
        name: str,
        *,
        owner: str,
        repo: str,
        issue_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelRemoveResponse:
        """
        Removes the specified label from the issue, and returns the remaining labels on
        the issue. This endpoint returns a `404 Not Found` status if the label does not
        exist.

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
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._delete(
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelRemoveResponse,
        )

    def remove_all(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes all labels from an issue.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    @overload
    def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          labels: The names of the labels to set for the issue. The labels you set replace any
              existing labels. You can pass an empty array to remove all labels.
              Alternatively, you can pass a single label as a `string` or an `array` of labels
              directly, but GitHub recommends passing an object with the `labels` key. You can
              also add labels to the existing labels for an issue. For more information, see
              "[Add labels to an issue](https://docs.github.com/rest/issues/labels#add-labels-to-an-issue)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: Iterable[label_set_params.Variant2Label] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: Iterable[label_set_params.Variant3Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo"])
    def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | Iterable[label_set_params.Variant2Label] | NotGiven = NOT_GIVEN,
        body: builtins.list[str] | Iterable[label_set_params.Variant3Body] | str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return self._put(
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
            body=maybe_transform(
                {
                    "labels": labels,
                    "body": body,
                },
                label_set_params.LabelSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelSetResponse,
        )


class AsyncLabelsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncLabelsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLabelsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLabelsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncLabelsResourceWithStreamingResponse(self)

    async def list(
        self,
        issue_number: int,
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
    ) -> LabelListResponse:
        """
        Lists all labels for an issue.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
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
                    label_list_params.LabelListParams,
                ),
            ),
            cast_to=LabelListResponse,
        )

    @overload
    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          labels: The names of the labels to add to the issue's existing labels. You can pass an
              empty array to remove all labels. Alternatively, you can pass a single label as
              a `string` or an `array` of labels directly, but GitHub recommends passing an
              object with the `labels` key. You can also replace all of the labels for an
              issue. For more information, see
              "[Set labels for an issue](https://docs.github.com/rest/issues/labels#set-labels-for-an-issue)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: Iterable[label_add_params.Variant2Label] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: Iterable[label_add_params.Variant3Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        """Adds labels to an issue.

        If you provide an empty array of labels, all labels are
        removed from the issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo"])
    async def add(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | Iterable[label_add_params.Variant2Label] | NotGiven = NOT_GIVEN,
        body: builtins.list[str] | Iterable[label_add_params.Variant3Body] | str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelAddResponse:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
            body=await async_maybe_transform(
                {
                    "labels": labels,
                    "body": body,
                },
                label_add_params.LabelAddParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelAddResponse,
        )

    async def remove(
        self,
        name: str,
        *,
        owner: str,
        repo: str,
        issue_number: int,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelRemoveResponse:
        """
        Removes the specified label from the issue, and returns the remaining labels on
        the issue. This endpoint returns a `404 Not Found` status if the label does not
        exist.

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
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._delete(
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelRemoveResponse,
        )

    async def remove_all(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Removes all labels from an issue.

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
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    @overload
    async def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          labels: The names of the labels to set for the issue. The labels you set replace any
              existing labels. You can pass an empty array to remove all labels.
              Alternatively, you can pass a single label as a `string` or an `array` of labels
              directly, but GitHub recommends passing an object with the `labels` key. You can
              also add labels to the existing labels for an issue. For more information, see
              "[Add labels to an issue](https://docs.github.com/rest/issues/labels#add-labels-to-an-issue)."

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: builtins.list[str] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: Iterable[label_set_params.Variant2Label] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: Iterable[label_set_params.Variant3Body] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        """
        Removes any previous labels and sets the new labels for an issue.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["owner", "repo"])
    async def set(
        self,
        issue_number: int,
        *,
        owner: str,
        repo: str,
        labels: builtins.list[str] | Iterable[label_set_params.Variant2Label] | NotGiven = NOT_GIVEN,
        body: builtins.list[str] | Iterable[label_set_params.Variant3Body] | str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> LabelSetResponse:
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/issues/{issue_number}/labels",
            body=await async_maybe_transform(
                {
                    "labels": labels,
                    "body": body,
                },
                label_set_params.LabelSetParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=LabelSetResponse,
        )


class LabelsResourceWithRawResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.list = to_raw_response_wrapper(
            labels.list,
        )
        self.add = to_raw_response_wrapper(
            labels.add,
        )
        self.remove = to_raw_response_wrapper(
            labels.remove,
        )
        self.remove_all = to_raw_response_wrapper(
            labels.remove_all,
        )
        self.set = to_raw_response_wrapper(
            labels.set,
        )


class AsyncLabelsResourceWithRawResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.list = async_to_raw_response_wrapper(
            labels.list,
        )
        self.add = async_to_raw_response_wrapper(
            labels.add,
        )
        self.remove = async_to_raw_response_wrapper(
            labels.remove,
        )
        self.remove_all = async_to_raw_response_wrapper(
            labels.remove_all,
        )
        self.set = async_to_raw_response_wrapper(
            labels.set,
        )


class LabelsResourceWithStreamingResponse:
    def __init__(self, labels: LabelsResource) -> None:
        self._labels = labels

        self.list = to_streamed_response_wrapper(
            labels.list,
        )
        self.add = to_streamed_response_wrapper(
            labels.add,
        )
        self.remove = to_streamed_response_wrapper(
            labels.remove,
        )
        self.remove_all = to_streamed_response_wrapper(
            labels.remove_all,
        )
        self.set = to_streamed_response_wrapper(
            labels.set,
        )


class AsyncLabelsResourceWithStreamingResponse:
    def __init__(self, labels: AsyncLabelsResource) -> None:
        self._labels = labels

        self.list = async_to_streamed_response_wrapper(
            labels.list,
        )
        self.add = async_to_streamed_response_wrapper(
            labels.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            labels.remove,
        )
        self.remove_all = async_to_streamed_response_wrapper(
            labels.remove_all,
        )
        self.set = async_to_streamed_response_wrapper(
            labels.set,
        )
