from __future__ import annotations

from typing import Iterable

import httpx
from typing_extensions import Literal

from ....._base_client import make_request_options
from ....._compat import cached_property
from ....._resource import AsyncAPIResource, SyncAPIResource
from ....._response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ....._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ....._utils import (
    async_maybe_transform,
    maybe_transform,
)
from .....types.orgs.actions import variable_create_params, variable_list_params, variable_update_params
from .....types.orgs.actions.organization_variable import OrganizationVariable
from .....types.orgs.actions.variable_list_response import VariableListResponse
from .repositories import (
    AsyncRepositoriesResource,
    AsyncRepositoriesResourceWithRawResponse,
    AsyncRepositoriesResourceWithStreamingResponse,
    RepositoriesResource,
    RepositoriesResourceWithRawResponse,
    RepositoriesResourceWithStreamingResponse,
)

__all__ = ["VariablesResource", "AsyncVariablesResource"]


class VariablesResource(SyncAPIResource):
    @cached_property
    def repositories(self) -> RepositoriesResource:
        return RepositoriesResource(self._client)

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
        org: str,
        *,
        name: str,
        value: str,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Creates an organization variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          name: The name of the variable.

          value: The value of the variable.

          visibility: The type of repositories in the organization that can access the variable.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the variable.

          selected_repository_ids: An array of repository ids that can access the organization variable. You can
              only provide a list of repository ids when the `visibility` is set to
              `selected`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/actions/variables",
            body=maybe_transform(
                {
                    "name": name,
                    "value": value,
                    "visibility": visibility,
                    "selected_repository_ids": selected_repository_ids,
                },
                variable_create_params.VariableCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def update(
        self,
        path_name: str,
        *,
        org: str,
        body_name: str | NotGiven = NOT_GIVEN,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        visibility: Literal["all", "private", "selected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates an organization variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          body_name: The name of the variable.

          selected_repository_ids: An array of repository ids that can access the organization variable. You can
              only provide a list of repository ids when the `visibility` is set to
              `selected`.

          value: The value of the variable.

          visibility: The type of repositories in the organization that can access the variable.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._patch(
            f"/orgs/{org}/actions/variables/{path_name}",
            body=maybe_transform(
                {
                    "body_name": body_name,
                    "selected_repository_ids": selected_repository_ids,
                    "value": value,
                    "visibility": visibility,
                },
                variable_update_params.VariableUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list(
        self,
        org: str,
        *,
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
        Lists all organization variables.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/actions/variables",
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
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an organization variable using the variable name.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/actions/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def get(
        self,
        name: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationVariable:
        """
        Gets a specific variable in an organization.

        The authenticated user must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return self._get(
            f"/orgs/{org}/actions/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationVariable,
        )


class AsyncVariablesResource(AsyncAPIResource):
    @cached_property
    def repositories(self) -> AsyncRepositoriesResource:
        return AsyncRepositoriesResource(self._client)

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
        org: str,
        *,
        name: str,
        value: str,
        visibility: Literal["all", "private", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Creates an organization variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          name: The name of the variable.

          value: The value of the variable.

          visibility: The type of repositories in the organization that can access the variable.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the variable.

          selected_repository_ids: An array of repository ids that can access the organization variable. You can
              only provide a list of repository ids when the `visibility` is set to
              `selected`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/actions/variables",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "value": value,
                    "visibility": visibility,
                    "selected_repository_ids": selected_repository_ids,
                },
                variable_create_params.VariableCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def update(
        self,
        path_name: str,
        *,
        org: str,
        body_name: str | NotGiven = NOT_GIVEN,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        value: str | NotGiven = NOT_GIVEN,
        visibility: Literal["all", "private", "selected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Updates an organization variable that you can reference in a GitHub Actions
        workflow.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

        Args:
          body_name: The name of the variable.

          selected_repository_ids: An array of repository ids that can access the organization variable. You can
              only provide a list of repository ids when the `visibility` is set to
              `selected`.

          value: The value of the variable.

          visibility: The type of repositories in the organization that can access the variable.
              `selected` means only the repositories specified by `selected_repository_ids`
              can access the variable.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not path_name:
            raise ValueError(f"Expected a non-empty value for `path_name` but received {path_name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._patch(
            f"/orgs/{org}/actions/variables/{path_name}",
            body=await async_maybe_transform(
                {
                    "body_name": body_name,
                    "selected_repository_ids": selected_repository_ids,
                    "value": value,
                    "visibility": visibility,
                },
                variable_update_params.VariableUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list(
        self,
        org: str,
        *,
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
        Lists all organization variables.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth app tokens and personal access tokens (classic) need the `admin:org` scope
        to use this endpoint. If the repository is private, the `repo` scope is also
        required.

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
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/actions/variables",
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
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Deletes an organization variable using the variable name.

        Authenticated users must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/actions/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def get(
        self,
        name: str,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OrganizationVariable:
        """
        Gets a specific variable in an organization.

        The authenticated user must have collaborator access to a repository to create,
        update, or read variables.

        OAuth tokens and personal access tokens (classic) need the`admin:org` scope to
        use this endpoint. If the repository is private, OAuth tokens and personal
        access tokens (classic) need the `repo` scope to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        if not name:
            raise ValueError(f"Expected a non-empty value for `name` but received {name!r}")
        return await self._get(
            f"/orgs/{org}/actions/variables/{name}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=OrganizationVariable,
        )


class VariablesResourceWithRawResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.create = to_raw_response_wrapper(
            variables.create,
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
        self.get = to_raw_response_wrapper(
            variables.get,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithRawResponse:
        return RepositoriesResourceWithRawResponse(self._variables.repositories)


class AsyncVariablesResourceWithRawResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.create = async_to_raw_response_wrapper(
            variables.create,
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
        self.get = async_to_raw_response_wrapper(
            variables.get,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithRawResponse:
        return AsyncRepositoriesResourceWithRawResponse(self._variables.repositories)


class VariablesResourceWithStreamingResponse:
    def __init__(self, variables: VariablesResource) -> None:
        self._variables = variables

        self.create = to_streamed_response_wrapper(
            variables.create,
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
        self.get = to_streamed_response_wrapper(
            variables.get,
        )

    @cached_property
    def repositories(self) -> RepositoriesResourceWithStreamingResponse:
        return RepositoriesResourceWithStreamingResponse(self._variables.repositories)


class AsyncVariablesResourceWithStreamingResponse:
    def __init__(self, variables: AsyncVariablesResource) -> None:
        self._variables = variables

        self.create = async_to_streamed_response_wrapper(
            variables.create,
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
        self.get = async_to_streamed_response_wrapper(
            variables.get,
        )

    @cached_property
    def repositories(self) -> AsyncRepositoriesResourceWithStreamingResponse:
        return AsyncRepositoriesResourceWithStreamingResponse(self._variables.repositories)
