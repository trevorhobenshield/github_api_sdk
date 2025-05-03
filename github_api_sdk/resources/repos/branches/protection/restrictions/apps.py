from __future__ import annotations

from typing import List

import httpx

from ......_base_client import make_request_options
from ......_compat import cached_property
from ......_resource import AsyncAPIResource, SyncAPIResource
from ......_response import (
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
)
from ......_types import NOT_GIVEN, Body, Headers, NotGiven, Query
from ......_utils import (
    async_maybe_transform,
    maybe_transform,
)
from ......types.repos.branches.protection.restrictions import app_add_params, app_remove_params, app_set_params
from ......types.repos.branches.protection.restrictions.app_add_response import AppAddResponse
from ......types.repos.branches.protection.restrictions.app_remove_response import AppRemoveResponse
from ......types.repos.branches.protection.restrictions.app_retrieve_response import AppRetrieveResponse
from ......types.repos.branches.protection.restrictions.app_set_response import AppSetResponse

__all__ = ["AppsResource", "AsyncAppsResource"]


class AppsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AppsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppRetrieveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Lists the GitHub Apps that have push access to this branch. Only GitHub Apps
        that are installed on the repository and that have been granted write access to
        the repository contents can be added as authorized actors on a protected branch.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._get(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppRetrieveResponse,
        )

    def add(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        apps: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppAddResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Grants the specified apps push access for this branch. Only GitHub Apps that are
        installed on the repository and that have been granted write access to the
        repository contents can be added as authorized actors on a protected branch.

        Args:
          apps: The GitHub Apps that have push access to this branch. Use the slugified version
              of the app name. **Note**: The list of users, apps, and teams in total is
              limited to 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._post(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            body=maybe_transform({"apps": apps}, app_add_params.AppAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppAddResponse,
        )

    def remove(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        apps: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppRemoveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Removes the ability of an app to push to this branch. Only GitHub Apps that are
        installed on the repository and that have been granted write access to the
        repository contents can be added as authorized actors on a protected branch.

        Args:
          apps: The GitHub Apps that have push access to this branch. Use the slugified version
              of the app name. **Note**: The list of users, apps, and teams in total is
              limited to 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            body=maybe_transform({"apps": apps}, app_remove_params.AppRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppRemoveResponse,
        )

    def set(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        apps: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppSetResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Replaces the list of apps that have push access to this branch. This removes all
        apps that previously had push access and grants push access to the new list of
        apps. Only GitHub Apps that are installed on the repository and that have been
        granted write access to the repository contents can be added as authorized
        actors on a protected branch.

        Args:
          apps: The GitHub Apps that have push access to this branch. Use the slugified version
              of the app name. **Note**: The list of users, apps, and teams in total is
              limited to 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return self._put(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            body=maybe_transform({"apps": apps}, app_set_params.AppSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppSetResponse,
        )


class AsyncAppsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAppsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncAppsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppRetrieveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Lists the GitHub Apps that have push access to this branch. Only GitHub Apps
        that are installed on the repository and that have been granted write access to
        the repository contents can be added as authorized actors on a protected branch.

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
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppRetrieveResponse,
        )

    async def add(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        apps: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppAddResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Grants the specified apps push access for this branch. Only GitHub Apps that are
        installed on the repository and that have been granted write access to the
        repository contents can be added as authorized actors on a protected branch.

        Args:
          apps: The GitHub Apps that have push access to this branch. Use the slugified version
              of the app name. **Note**: The list of users, apps, and teams in total is
              limited to 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._post(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            body=await async_maybe_transform({"apps": apps}, app_add_params.AppAddParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppAddResponse,
        )

    async def remove(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        apps: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppRemoveResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Removes the ability of an app to push to this branch. Only GitHub Apps that are
        installed on the repository and that have been granted write access to the
        repository contents can be added as authorized actors on a protected branch.

        Args:
          apps: The GitHub Apps that have push access to this branch. Use the slugified version
              of the app name. **Note**: The list of users, apps, and teams in total is
              limited to 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._delete(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            body=await async_maybe_transform({"apps": apps}, app_remove_params.AppRemoveParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppRemoveResponse,
        )

    async def set(
        self,
        branch: str,
        *,
        owner: str,
        repo: str,
        apps: list[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AppSetResponse:
        """
        Protected branches are available in public repositories with GitHub Free and
        GitHub Free for organizations, and in public and private repositories with
        GitHub Pro, GitHub Team, GitHub Enterprise Cloud, and GitHub Enterprise Server.
        For more information, see
        [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products)
        in the GitHub Help documentation.

        Replaces the list of apps that have push access to this branch. This removes all
        apps that previously had push access and grants push access to the new list of
        apps. Only GitHub Apps that are installed on the repository and that have been
        granted write access to the repository contents can be added as authorized
        actors on a protected branch.

        Args:
          apps: The GitHub Apps that have push access to this branch. Use the slugified version
              of the app name. **Note**: The list of users, apps, and teams in total is
              limited to 100 items.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not owner:
            raise ValueError(f"Expected a non-empty value for `owner` but received {owner!r}")
        if not repo:
            raise ValueError(f"Expected a non-empty value for `repo` but received {repo!r}")
        if not branch:
            raise ValueError(f"Expected a non-empty value for `branch` but received {branch!r}")
        return await self._put(
            f"/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/apps",
            body=await async_maybe_transform({"apps": apps}, app_set_params.AppSetParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=AppSetResponse,
        )


class AppsResourceWithRawResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.retrieve = to_raw_response_wrapper(
            apps.retrieve,
        )
        self.add = to_raw_response_wrapper(
            apps.add,
        )
        self.remove = to_raw_response_wrapper(
            apps.remove,
        )
        self.set = to_raw_response_wrapper(
            apps.set,
        )


class AsyncAppsResourceWithRawResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.retrieve = async_to_raw_response_wrapper(
            apps.retrieve,
        )
        self.add = async_to_raw_response_wrapper(
            apps.add,
        )
        self.remove = async_to_raw_response_wrapper(
            apps.remove,
        )
        self.set = async_to_raw_response_wrapper(
            apps.set,
        )


class AppsResourceWithStreamingResponse:
    def __init__(self, apps: AppsResource) -> None:
        self._apps = apps

        self.retrieve = to_streamed_response_wrapper(
            apps.retrieve,
        )
        self.add = to_streamed_response_wrapper(
            apps.add,
        )
        self.remove = to_streamed_response_wrapper(
            apps.remove,
        )
        self.set = to_streamed_response_wrapper(
            apps.set,
        )


class AsyncAppsResourceWithStreamingResponse:
    def __init__(self, apps: AsyncAppsResource) -> None:
        self._apps = apps

        self.retrieve = async_to_streamed_response_wrapper(
            apps.retrieve,
        )
        self.add = async_to_streamed_response_wrapper(
            apps.add,
        )
        self.remove = async_to_streamed_response_wrapper(
            apps.remove,
        )
        self.set = async_to_streamed_response_wrapper(
            apps.set,
        )
