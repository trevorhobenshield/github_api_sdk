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
from ....types.repos.actions.actions_variable import ActionsVariable
from ....types.repos.environments import variable_create_params, variable_list_params, variable_update_params
from ....types.repos.environments.variable_list_response import VariableListResponse

__all__ = ["VariablesResource", "AsyncVariablesResource"]


class VariablesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VariablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return VariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VariablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return VariablesResourceWithStreamingResponse(self)

    def create(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        name: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create an environment variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          name: The name of the variable.

          value: The value of the variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._post(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables",
            body=maybe_transform(
                {
                    "name": name,
                    "value": value,
                },
                variable_create_params.VariableCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def retrieve(
        self,
        name: str,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsVariable:
        """
        Gets a specific variable in an environment.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsVariable,
        )

    def update(
        self,
        path_name: str,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        body_name: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates an environment variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          body_name: The name of the variable.

          value: The value of the variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables/{path_name}",
            body=maybe_transform(
                {
                    "body_name": body_name,
                    "value": value,
                },
                variable_update_params.VariableUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list(
        self,
        environment_name: str,
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
    ) -> VariableListResponse:
        """
        Lists all environment variables.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 30). For more information, see
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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables",
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
                    variable_list_params.VariableListParams,
                ),
            ),
            cast_to=VariableListResponse,
        )

    def delete(
        self,
        name: str,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an environment variable using the variable name.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class AsyncVariablesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVariablesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVariablesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVariablesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncVariablesResourceWithStreamingResponse(self)

    async def create(
        self,
        environment_name: str,
        *,
        owner: str,
        repo: str,
        name: str,
        value: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Create an environment variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

        Args:
          name: The name of the variable.

          value: The value of the variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "value": value,
                },
                variable_create_params.VariableCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def retrieve(
        self,
        name: str,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ActionsVariable:
        """
        Gets a specific variable in an environment.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ActionsVariable,
        )

    async def update(
        self,
        path_name: str,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        body_name: str | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates an environment variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          body_name: The name of the variable.

          value: The value of the variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables/{path_name}",
            body=await async_maybe_transform(
                {
                    "body_name": body_name,
                    "value": value,
                },
                variable_update_params.VariableUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list(
        self,
        environment_name: str,
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
    ) -> VariableListResponse:
        """
        Lists all environment variables.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `repo` scope to
        use this endpoint.

        Args:
          page: The page number of the results to fetch. For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 30). For more information, see
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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables",
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
                    variable_list_params.VariableListParams,
                ),
            ),
            cast_to=VariableListResponse,
        )

    async def delete(
        self,
        name: str,
        *,
        owner: str,
        repo: str,
        environment_name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an environment variable using the variable name.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the `repo` scope to use
        this endpoint.

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
        if not environment_name:
            raise ValueError(f"Expected a non-empty value for `environment_name` but received {environment_name!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/repos/{owner}/{repo}/environments/{environment_name}/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )


class VariablesResourceWithRawResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.create = to_raw_response_wrapper(
            variables.create,
        )
        self.retrieve = to_raw_response_wrapper(
            variables.retrieve,
        )
        self.update = to_raw_response_wrapper(
            variables.update,
        )
        self.list = to_raw_response_wrapper(
            variables.list,
        )
        self.delete = to_raw_response_wrapper(
            variables.delete,
        )


class AsyncVariablesResourceWithRawResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.create = async_to_raw_response_wrapper(
            variables.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            variables.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            variables.update,
        )
        self.list = async_to_raw_response_wrapper(
            variables.list,
        )
        self.delete = async_to_raw_response_wrapper(
            variables.delete,
        )


class VariablesResourceWithStreamingResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.create = to_streamed_response_wrapper(
            variables.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            variables.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            variables.update,
        )
        self.list = to_streamed_response_wrapper(
            variables.list,
        )
        self.delete = to_streamed_response_wrapper(
            variables.delete,
        )


class AsyncVariablesResourceWithStreamingResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.create = async_to_streamed_response_wrapper(
            variables.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            variables.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            variables.update,
        )
        self.list = async_to_streamed_response_wrapper(
            variables.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            variables.delete,
        )
