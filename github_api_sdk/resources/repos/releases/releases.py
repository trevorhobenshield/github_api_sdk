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
from ...._types import NOT_GIVEN, Body, Headers, NoneType, NotGiven, Query
from ...._utils import (
    async_maybe_transform,
    maybe_transform,
)
from ....types.repos import (
    release_create_params,
    release_generate_notes_params,
    release_list_params,
    release_update_params,
)
from ....types.repos.release import Release
from ....types.repos.release_generate_notes_response import ReleaseGenerateNotesResponse
from ....types.repos.release_list_response import ReleaseListResponse
from .assets import (
    AssetsResource,
    AssetsResourceWithRawResponse,
    AssetsResourceWithStreamingResponse,
    AsyncAssetsResource,
    AsyncAssetsResourceWithRawResponse,
    AsyncAssetsResourceWithStreamingResponse,
)
from .reactions import (
    AsyncReactionsResource,
    AsyncReactionsResourceWithRawResponse,
    AsyncReactionsResourceWithStreamingResponse,
    ReactionsResource,
    ReactionsResourceWithRawResponse,
    ReactionsResourceWithStreamingResponse,
)

__all__ = ["ReleasesResource", "AsyncReleasesResource"]


class ReleasesResource(SyncAPIResource):
    @cached_property
    def assets(self) -> AssetsResource:
        return AssetsResource(self._client)

    @cached_property
    def reactions(self) -> ReactionsResource:
        return ReactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ReleasesResourceWithStreamingResponse(self)

    def create(
        self,
        repo: str,
        *,
        owner: str,
        tag_name: str,
        body: str | NotGiven = NOT_GIVEN,
        discussion_category_name: str | NotGiven = NOT_GIVEN,
        draft: bool | NotGiven = NOT_GIVEN,
        generate_release_notes: bool | NotGiven = NOT_GIVEN,
        make_latest: Literal["true", "false", "legacy"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prerelease: bool | NotGiven = NOT_GIVEN,
        target_commitish: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Users with push access to the repository can create a release.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          tag_name: The name of the tag.

          body: Text describing the contents of the tag.

          discussion_category_name: If specified, a discussion of the specified category is created and linked to
              the release. The value must be a category that already exists in the repository.
              For more information, see
              "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."

          draft: `true` to create a draft (unpublished) release, `false` to create a published
              one.

          generate_release_notes: Whether to automatically generate the name and body for this release. If `name`
              is specified, the specified name will be used; otherwise, a name will be
              automatically generated. If `body` is specified, the body will be pre-pended to
              the automatically generated notes.

          make_latest: Specifies whether this release should be set as the latest release for the
              repository. Drafts and prereleases cannot be set as latest. Defaults to `true`
              for newly published releases. `legacy` specifies that the latest release should
              be determined based on the release creation date and higher semantic version.

          name: The name of the release.

          prerelease: `true` to identify the release as a prerelease. `false` to identify the release
              as a full release.

          target_commitish: Specifies the commitish value that determines where the Git tag is created from.
              Can be any branch or commit SHA. Unused if the Git tag already exists. Default:
              the repository's default branch.

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
            f"/repos/{owner}/{repo}/releases",
            body=maybe_transform(
                {
                    "tag_name": tag_name,
                    "body": body,
                    "discussion_category_name": discussion_category_name,
                    "draft": draft,
                    "generate_release_notes": generate_release_notes,
                    "make_latest": make_latest,
                    "name": name,
                    "prerelease": prerelease,
                    "target_commitish": target_commitish,
                },
                release_create_params.ReleaseCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    def retrieve(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Gets a public release with the specified release ID.

        > [!NOTE] This returns an `upload_url` key corresponding to the endpoint for
        > uploading release assets. This key is a hypermedia resource. For more
        > information, see
        > "[Getting started with the REST API](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)."

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
            f"/repos/{owner}/{repo}/releases/{release_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    def update(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        discussion_category_name: str | NotGiven = NOT_GIVEN,
        draft: bool | NotGiven = NOT_GIVEN,
        make_latest: Literal["true", "false", "legacy"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prerelease: bool | NotGiven = NOT_GIVEN,
        tag_name: str | NotGiven = NOT_GIVEN,
        target_commitish: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Users with push access to the repository can edit a release.

        Args:
          body: Text describing the contents of the tag.

          discussion_category_name: If specified, a discussion of the specified category is created and linked to
              the release. The value must be a category that already exists in the repository.
              If there is already a discussion linked to the release, this parameter is
              ignored. For more information, see
              "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."

          draft: `true` makes the release a draft, and `false` publishes the release.

          make_latest: Specifies whether this release should be set as the latest release for the
              repository. Drafts and prereleases cannot be set as latest. Defaults to `true`
              for newly published releases. `legacy` specifies that the latest release should
              be determined based on the release creation date and higher semantic version.

          name: The name of the release.

          prerelease: `true` to identify the release as a prerelease, `false` to identify the release
              as a full release.

          tag_name: The name of the tag.

          target_commitish: Specifies the commitish value that determines where the Git tag is created from.
              Can be any branch or commit SHA. Unused if the Git tag already exists. Default:
              the repository's default branch.

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
            f"/repos/{owner}/{repo}/releases/{release_id}",
            body=maybe_transform(
                {
                    "body": body,
                    "discussion_category_name": discussion_category_name,
                    "draft": draft,
                    "make_latest": make_latest,
                    "name": name,
                    "prerelease": prerelease,
                    "tag_name": tag_name,
                    "target_commitish": target_commitish,
                },
                release_update_params.ReleaseUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseListResponse:
        """
        This returns a list of releases, which does not include regular Git tags that
        have not been associated with a release. To get a list of Git tags, use the
        [Repository Tags API](https://docs.github.com/rest/repos/repos#list-repository-tags).

        Information about published releases are available to everyone. Only users with
        push access will receive listings for draft releases.

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
            f"/repos/{owner}/{repo}/releases",
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
                    release_list_params.ReleaseListParams,
                ),
            ),
            cast_to=ReleaseListResponse,
        )

    def delete(
        self,
        release_id: int,
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
        Users with push access to the repository can delete a release.

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
            f"/repos/{owner}/{repo}/releases/{release_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def generate_notes(
        self,
        repo: str,
        *,
        owner: str,
        tag_name: str,
        configuration_file_path: str | NotGiven = NOT_GIVEN,
        previous_tag_name: str | NotGiven = NOT_GIVEN,
        target_commitish: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseGenerateNotesResponse:
        """
        Generate a name and body describing a
        [release](https://docs.github.com/rest/releases/releases#get-a-release). The
        body content will be markdown formatted and contain information like the changes
        since last release and users who contributed. The generated release notes are
        not saved anywhere. They are intended to be generated and used when creating a
        new release.

        Args:
          tag_name: The tag name for the release. This can be an existing tag or a new one.

          configuration_file_path: Specifies a path to a file in the repository containing configuration settings
              used for generating the release notes. If unspecified, the configuration file
              located in the repository at '.github/release.yml' or '.github/release.yaml'
              will be used. If that is not present, the default configuration will be used.

          previous_tag_name: The name of the previous tag to use as the starting point for the release notes.
              Use to manually specify the range for the set of changes considered as part this
              release.

          target_commitish: Specifies the commitish value that will be the target for the release's tag.
              Required if the supplied tag_name does not reference an existing tag. Ignored if
              the tag_name already exists.

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
            f"/repos/{owner}/{repo}/releases/generate-notes",
            body=maybe_transform(
                {
                    "tag_name": tag_name,
                    "configuration_file_path": configuration_file_path,
                    "previous_tag_name": previous_tag_name,
                    "target_commitish": target_commitish,
                },
                release_generate_notes_params.ReleaseGenerateNotesParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReleaseGenerateNotesResponse,
        )

    def retrieve_by_tag(
        self,
        tag: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Get a published release with the specified tag.

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
        if not tag:
            raise ValueError(f"Expected a non-empty value for `tag` but received {tag!r}")
        return self._get(
            f"/repos/{owner}/{repo}/releases/tags/{tag}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    def retrieve_latest(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        View the latest published full release for the repository.

        The latest release is the most recent non-prerelease, non-draft release, sorted
        by the `created_at` attribute. The `created_at` attribute is the date of the
        commit used for the release, and not the date when the release was drafted or
        published.

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
            f"/repos/{owner}/{repo}/releases/latest",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )


class AsyncReleasesResource(AsyncAPIResource):
    @cached_property
    def assets(self) -> AsyncAssetsResource:
        return AsyncAssetsResource(self._client)

    @cached_property
    def reactions(self) -> AsyncReactionsResource:
        return AsyncReactionsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncReleasesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncReleasesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReleasesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncReleasesResourceWithStreamingResponse(self)

    async def create(
        self,
        repo: str,
        *,
        owner: str,
        tag_name: str,
        body: str | NotGiven = NOT_GIVEN,
        discussion_category_name: str | NotGiven = NOT_GIVEN,
        draft: bool | NotGiven = NOT_GIVEN,
        generate_release_notes: bool | NotGiven = NOT_GIVEN,
        make_latest: Literal["true", "false", "legacy"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prerelease: bool | NotGiven = NOT_GIVEN,
        target_commitish: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Users with push access to the repository can create a release.

        This endpoint triggers
        [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).
        Creating content too quickly using this endpoint may result in secondary rate
        limiting. For more information, see
        "[Rate limits for the API](https://docs.github.com/rest/using-the-rest-api/rate-limits-for-the-rest-api#about-secondary-rate-limits)"
        and
        "[Best practices for using the REST API](https://docs.github.com/rest/guides/best-practices-for-using-the-rest-api)."

        Args:
          tag_name: The name of the tag.

          body: Text describing the contents of the tag.

          discussion_category_name: If specified, a discussion of the specified category is created and linked to
              the release. The value must be a category that already exists in the repository.
              For more information, see
              "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."

          draft: `true` to create a draft (unpublished) release, `false` to create a published
              one.

          generate_release_notes: Whether to automatically generate the name and body for this release. If `name`
              is specified, the specified name will be used; otherwise, a name will be
              automatically generated. If `body` is specified, the body will be pre-pended to
              the automatically generated notes.

          make_latest: Specifies whether this release should be set as the latest release for the
              repository. Drafts and prereleases cannot be set as latest. Defaults to `true`
              for newly published releases. `legacy` specifies that the latest release should
              be determined based on the release creation date and higher semantic version.

          name: The name of the release.

          prerelease: `true` to identify the release as a prerelease. `false` to identify the release
              as a full release.

          target_commitish: Specifies the commitish value that determines where the Git tag is created from.
              Can be any branch or commit SHA. Unused if the Git tag already exists. Default:
              the repository's default branch.

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
            f"/repos/{owner}/{repo}/releases",
            body=await async_maybe_transform(
                {
                    "tag_name": tag_name,
                    "body": body,
                    "discussion_category_name": discussion_category_name,
                    "draft": draft,
                    "generate_release_notes": generate_release_notes,
                    "make_latest": make_latest,
                    "name": name,
                    "prerelease": prerelease,
                    "target_commitish": target_commitish,
                },
                release_create_params.ReleaseCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    async def retrieve(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Gets a public release with the specified release ID.

        > [!NOTE] This returns an `upload_url` key corresponding to the endpoint for
        > uploading release assets. This key is a hypermedia resource. For more
        > information, see
        > "[Getting started with the REST API](https://docs.github.com/rest/using-the-rest-api/getting-started-with-the-rest-api#hypermedia)."

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
            f"/repos/{owner}/{repo}/releases/{release_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    async def update(
        self,
        release_id: int,
        *,
        owner: str,
        repo: str,
        body: str | NotGiven = NOT_GIVEN,
        discussion_category_name: str | NotGiven = NOT_GIVEN,
        draft: bool | NotGiven = NOT_GIVEN,
        make_latest: Literal["true", "false", "legacy"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        prerelease: bool | NotGiven = NOT_GIVEN,
        tag_name: str | NotGiven = NOT_GIVEN,
        target_commitish: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Users with push access to the repository can edit a release.

        Args:
          body: Text describing the contents of the tag.

          discussion_category_name: If specified, a discussion of the specified category is created and linked to
              the release. The value must be a category that already exists in the repository.
              If there is already a discussion linked to the release, this parameter is
              ignored. For more information, see
              "[Managing categories for discussions in your repository](https://docs.github.com/discussions/managing-discussions-for-your-community/managing-categories-for-discussions-in-your-repository)."

          draft: `true` makes the release a draft, and `false` publishes the release.

          make_latest: Specifies whether this release should be set as the latest release for the
              repository. Drafts and prereleases cannot be set as latest. Defaults to `true`
              for newly published releases. `legacy` specifies that the latest release should
              be determined based on the release creation date and higher semantic version.

          name: The name of the release.

          prerelease: `true` to identify the release as a prerelease, `false` to identify the release
              as a full release.

          tag_name: The name of the tag.

          target_commitish: Specifies the commitish value that determines where the Git tag is created from.
              Can be any branch or commit SHA. Unused if the Git tag already exists. Default:
              the repository's default branch.

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
            f"/repos/{owner}/{repo}/releases/{release_id}",
            body=await async_maybe_transform(
                {
                    "body": body,
                    "discussion_category_name": discussion_category_name,
                    "draft": draft,
                    "make_latest": make_latest,
                    "name": name,
                    "prerelease": prerelease,
                    "tag_name": tag_name,
                    "target_commitish": target_commitish,
                },
                release_update_params.ReleaseUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    async def list(
        self,
        repo: str,
        *,
        owner: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseListResponse:
        """
        This returns a list of releases, which does not include regular Git tags that
        have not been associated with a release. To get a list of Git tags, use the
        [Repository Tags API](https://docs.github.com/rest/repos/repos#list-repository-tags).

        Information about published releases are available to everyone. Only users with
        push access will receive listings for draft releases.

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
            f"/repos/{owner}/{repo}/releases",
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
                    release_list_params.ReleaseListParams,
                ),
            ),
            cast_to=ReleaseListResponse,
        )

    async def delete(
        self,
        release_id: int,
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
        Users with push access to the repository can delete a release.

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
            f"/repos/{owner}/{repo}/releases/{release_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def generate_notes(
        self,
        repo: str,
        *,
        owner: str,
        tag_name: str,
        configuration_file_path: str | NotGiven = NOT_GIVEN,
        previous_tag_name: str | NotGiven = NOT_GIVEN,
        target_commitish: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ReleaseGenerateNotesResponse:
        """
        Generate a name and body describing a
        [release](https://docs.github.com/rest/releases/releases#get-a-release). The
        body content will be markdown formatted and contain information like the changes
        since last release and users who contributed. The generated release notes are
        not saved anywhere. They are intended to be generated and used when creating a
        new release.

        Args:
          tag_name: The tag name for the release. This can be an existing tag or a new one.

          configuration_file_path: Specifies a path to a file in the repository containing configuration settings
              used for generating the release notes. If unspecified, the configuration file
              located in the repository at '.github/release.yml' or '.github/release.yaml'
              will be used. If that is not present, the default configuration will be used.

          previous_tag_name: The name of the previous tag to use as the starting point for the release notes.
              Use to manually specify the range for the set of changes considered as part this
              release.

          target_commitish: Specifies the commitish value that will be the target for the release's tag.
              Required if the supplied tag_name does not reference an existing tag. Ignored if
              the tag_name already exists.

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
            f"/repos/{owner}/{repo}/releases/generate-notes",
            body=await async_maybe_transform(
                {
                    "tag_name": tag_name,
                    "configuration_file_path": configuration_file_path,
                    "previous_tag_name": previous_tag_name,
                    "target_commitish": target_commitish,
                },
                release_generate_notes_params.ReleaseGenerateNotesParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=ReleaseGenerateNotesResponse,
        )

    async def retrieve_by_tag(
        self,
        tag: str,
        *,
        owner: str,
        repo: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        Get a published release with the specified tag.

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
        if not tag:
            raise ValueError(f"Expected a non-empty value for `tag` but received {tag!r}")
        return await self._get(
            f"/repos/{owner}/{repo}/releases/tags/{tag}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )

    async def retrieve_latest(
        self,
        repo: str,
        *,
        owner: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Release:
        """
        View the latest published full release for the repository.

        The latest release is the most recent non-prerelease, non-draft release, sorted
        by the `created_at` attribute. The `created_at` attribute is the date of the
        commit used for the release, and not the date when the release was drafted or
        published.

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
            f"/repos/{owner}/{repo}/releases/latest",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Release,
        )


class ReleasesResourceWithRawResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.create = to_raw_response_wrapper(
            releases.create,
        )
        self.retrieve = to_raw_response_wrapper(
            releases.retrieve,
        )
        self.update = to_raw_response_wrapper(
            releases.update,
        )
        self.list = to_raw_response_wrapper(
            releases.list,
        )
        self.delete = to_raw_response_wrapper(
            releases.delete,
        )
        self.generate_notes = to_raw_response_wrapper(
            releases.generate_notes,
        )
        self.retrieve_by_tag = to_raw_response_wrapper(
            releases.retrieve_by_tag,
        )
        self.retrieve_latest = to_raw_response_wrapper(
            releases.retrieve_latest,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithRawResponse:
        return AssetsResourceWithRawResponse(self._releases.assets)

    @cached_property
    def reactions(self) -> ReactionsResourceWithRawResponse:
        return ReactionsResourceWithRawResponse(self._releases.reactions)


class AsyncReleasesResourceWithRawResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.create = async_to_raw_response_wrapper(
            releases.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            releases.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            releases.update,
        )
        self.list = async_to_raw_response_wrapper(
            releases.list,
        )
        self.delete = async_to_raw_response_wrapper(
            releases.delete,
        )
        self.generate_notes = async_to_raw_response_wrapper(
            releases.generate_notes,
        )
        self.retrieve_by_tag = async_to_raw_response_wrapper(
            releases.retrieve_by_tag,
        )
        self.retrieve_latest = async_to_raw_response_wrapper(
            releases.retrieve_latest,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithRawResponse:
        return AsyncAssetsResourceWithRawResponse(self._releases.assets)

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithRawResponse:
        return AsyncReactionsResourceWithRawResponse(self._releases.reactions)


class ReleasesResourceWithStreamingResponse:
    def __init__(self, releases: ReleasesResource) -> None:
        self._releases = releases

        self.create = to_streamed_response_wrapper(
            releases.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            releases.update,
        )
        self.list = to_streamed_response_wrapper(
            releases.list,
        )
        self.delete = to_streamed_response_wrapper(
            releases.delete,
        )
        self.generate_notes = to_streamed_response_wrapper(
            releases.generate_notes,
        )
        self.retrieve_by_tag = to_streamed_response_wrapper(
            releases.retrieve_by_tag,
        )
        self.retrieve_latest = to_streamed_response_wrapper(
            releases.retrieve_latest,
        )

    @cached_property
    def assets(self) -> AssetsResourceWithStreamingResponse:
        return AssetsResourceWithStreamingResponse(self._releases.assets)

    @cached_property
    def reactions(self) -> ReactionsResourceWithStreamingResponse:
        return ReactionsResourceWithStreamingResponse(self._releases.reactions)


class AsyncReleasesResourceWithStreamingResponse:
    def __init__(self, releases: AsyncReleasesResource) -> None:
        self._releases = releases

        self.create = async_to_streamed_response_wrapper(
            releases.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            releases.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            releases.update,
        )
        self.list = async_to_streamed_response_wrapper(
            releases.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            releases.delete,
        )
        self.generate_notes = async_to_streamed_response_wrapper(
            releases.generate_notes,
        )
        self.retrieve_by_tag = async_to_streamed_response_wrapper(
            releases.retrieve_by_tag,
        )
        self.retrieve_latest = async_to_streamed_response_wrapper(
            releases.retrieve_latest,
        )

    @cached_property
    def assets(self) -> AsyncAssetsResourceWithStreamingResponse:
        return AsyncAssetsResourceWithStreamingResponse(self._releases.assets)

    @cached_property
    def reactions(self) -> AsyncReactionsResourceWithStreamingResponse:
        return AsyncReactionsResourceWithStreamingResponse(self._releases.reactions)
