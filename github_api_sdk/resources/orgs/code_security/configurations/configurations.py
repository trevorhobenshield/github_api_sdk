from __future__ import annotations

from typing import Iterable, Optional

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
from .....types.enterprises.code_security.configuration import Configuration
from .....types.enterprises.code_security.scanning_options_param import ScanningOptionsParam
from .....types.orgs.code_security import (
    configuration_attach_params,
    configuration_create_params,
    configuration_detach_params,
    configuration_list_params,
    configuration_list_repositories_params,
    configuration_update_params,
)
from .....types.orgs.code_security.configuration_list_repositories_response import ConfigurationListRepositoriesResponse
from .....types.orgs.code_security.configuration_list_response import ConfigurationListResponse
from .defaults import (
    AsyncDefaultsResource,
    AsyncDefaultsResourceWithRawResponse,
    AsyncDefaultsResourceWithStreamingResponse,
    DefaultsResource,
    DefaultsResourceWithRawResponse,
    DefaultsResourceWithStreamingResponse,
)

__all__ = ["ConfigurationsResource", "AsyncConfigurationsResource"]


class ConfigurationsResource(SyncAPIResource):
    @cached_property
    def defaults(self) -> DefaultsResource:
        return DefaultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return ConfigurationsResourceWithStreamingResponse(self)

    def create(
        self,
        org: str,
        *,
        description: str,
        name: str,
        advanced_security: Literal["enabled", "disabled"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup_options: ScanningOptionsParam | None | NotGiven = NOT_GIVEN,
        code_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_alerts: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_security_updates: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action_options: configuration_create_params.DependencyGraphAutosubmitActionOptions | NotGiven = NOT_GIVEN,
        enforcement: Literal["enforced", "unenforced"] | NotGiven = NOT_GIVEN,
        private_vulnerability_reporting: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass_options: configuration_create_params.SecretScanningDelegatedBypassOptions | NotGiven = NOT_GIVEN,
        secret_scanning_generic_secrets: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_non_provider_patterns: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_validity_checks: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Creates a code security configuration in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          description: A description of the code security configuration

          name: The name of the code security configuration. Must be unique within the
              organization.

          advanced_security: The enablement status of GitHub Advanced Security

          code_scanning_default_setup: The enablement status of code scanning default setup

          code_scanning_default_setup_options: Feature options for code scanning default setup

          code_scanning_delegated_alert_dismissal: The enablement status of code scanning delegated alert dismissal

          dependabot_alerts: The enablement status of Dependabot alerts

          dependabot_security_updates: The enablement status of Dependabot security updates

          dependency_graph: The enablement status of Dependency Graph

          dependency_graph_autosubmit_action: The enablement status of Automatic dependency submission

          dependency_graph_autosubmit_action_options: Feature options for Automatic dependency submission

          enforcement: The enforcement status for a security configuration

          private_vulnerability_reporting: The enablement status of private vulnerability reporting

          secret_scanning: The enablement status of secret scanning

          secret_scanning_delegated_alert_dismissal: The enablement status of secret scanning delegated alert dismissal

          secret_scanning_delegated_bypass: The enablement status of secret scanning delegated bypass

          secret_scanning_delegated_bypass_options: Feature options for secret scanning delegated bypass

          secret_scanning_generic_secrets: The enablement status of Copilot secret scanning

          secret_scanning_non_provider_patterns: The enablement status of secret scanning non provider patterns

          secret_scanning_push_protection: The enablement status of secret scanning push protection

          secret_scanning_validity_checks: The enablement status of secret scanning validity checks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/code-security/configurations",
            body=maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "advanced_security": advanced_security,
                    "code_scanning_default_setup": code_scanning_default_setup,
                    "code_scanning_default_setup_options": code_scanning_default_setup_options,
                    "code_scanning_delegated_alert_dismissal": code_scanning_delegated_alert_dismissal,
                    "dependabot_alerts": dependabot_alerts,
                    "dependabot_security_updates": dependabot_security_updates,
                    "dependency_graph": dependency_graph,
                    "dependency_graph_autosubmit_action": dependency_graph_autosubmit_action,
                    "dependency_graph_autosubmit_action_options": dependency_graph_autosubmit_action_options,
                    "enforcement": enforcement,
                    "private_vulnerability_reporting": private_vulnerability_reporting,
                    "secret_scanning": secret_scanning,
                    "secret_scanning_delegated_alert_dismissal": secret_scanning_delegated_alert_dismissal,
                    "secret_scanning_delegated_bypass": secret_scanning_delegated_bypass,
                    "secret_scanning_delegated_bypass_options": secret_scanning_delegated_bypass_options,
                    "secret_scanning_generic_secrets": secret_scanning_generic_secrets,
                    "secret_scanning_non_provider_patterns": secret_scanning_non_provider_patterns,
                    "secret_scanning_push_protection": secret_scanning_push_protection,
                    "secret_scanning_validity_checks": secret_scanning_validity_checks,
                },
                configuration_create_params.ConfigurationCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Configuration,
        )

    def retrieve(
        self,
        configuration_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Gets a code security configuration available in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/code-security/configurations/{configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Configuration,
        )

    def update(
        self,
        configuration_id: int,
        *,
        org: str,
        advanced_security: Literal["enabled", "disabled"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup_options: ScanningOptionsParam | None | NotGiven = NOT_GIVEN,
        code_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_alerts: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_security_updates: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action_options: configuration_update_params.DependencyGraphAutosubmitActionOptions | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enforcement: Literal["enforced", "unenforced"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        private_vulnerability_reporting: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass_options: configuration_update_params.SecretScanningDelegatedBypassOptions | NotGiven = NOT_GIVEN,
        secret_scanning_generic_secrets: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_non_provider_patterns: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_validity_checks: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Updates a code security configuration in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          advanced_security: The enablement status of GitHub Advanced Security

          code_scanning_default_setup: The enablement status of code scanning default setup

          code_scanning_default_setup_options: Feature options for code scanning default setup

          code_scanning_delegated_alert_dismissal: The enablement status of code scanning delegated alert dismissal

          dependabot_alerts: The enablement status of Dependabot alerts

          dependabot_security_updates: The enablement status of Dependabot security updates

          dependency_graph: The enablement status of Dependency Graph

          dependency_graph_autosubmit_action: The enablement status of Automatic dependency submission

          dependency_graph_autosubmit_action_options: Feature options for Automatic dependency submission

          description: A description of the code security configuration

          enforcement: The enforcement status for a security configuration

          name: The name of the code security configuration. Must be unique within the
              organization.

          private_vulnerability_reporting: The enablement status of private vulnerability reporting

          secret_scanning: The enablement status of secret scanning

          secret_scanning_delegated_alert_dismissal: The enablement status of secret scanning delegated alert dismissal

          secret_scanning_delegated_bypass: The enablement status of secret scanning delegated bypass

          secret_scanning_delegated_bypass_options: Feature options for secret scanning delegated bypass

          secret_scanning_generic_secrets: The enablement status of Copilot secret scanning

          secret_scanning_non_provider_patterns: The enablement status of secret scanning non-provider patterns

          secret_scanning_push_protection: The enablement status of secret scanning push protection

          secret_scanning_validity_checks: The enablement status of secret scanning validity checks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._patch(
            f"/orgs/{org}/code-security/configurations/{configuration_id}",
            body=maybe_transform(
                {
                    "advanced_security": advanced_security,
                    "code_scanning_default_setup": code_scanning_default_setup,
                    "code_scanning_default_setup_options": code_scanning_default_setup_options,
                    "code_scanning_delegated_alert_dismissal": code_scanning_delegated_alert_dismissal,
                    "dependabot_alerts": dependabot_alerts,
                    "dependabot_security_updates": dependabot_security_updates,
                    "dependency_graph": dependency_graph,
                    "dependency_graph_autosubmit_action": dependency_graph_autosubmit_action,
                    "dependency_graph_autosubmit_action_options": dependency_graph_autosubmit_action_options,
                    "description": description,
                    "enforcement": enforcement,
                    "name": name,
                    "private_vulnerability_reporting": private_vulnerability_reporting,
                    "secret_scanning": secret_scanning,
                    "secret_scanning_delegated_alert_dismissal": secret_scanning_delegated_alert_dismissal,
                    "secret_scanning_delegated_bypass": secret_scanning_delegated_bypass,
                    "secret_scanning_delegated_bypass_options": secret_scanning_delegated_bypass_options,
                    "secret_scanning_generic_secrets": secret_scanning_generic_secrets,
                    "secret_scanning_non_provider_patterns": secret_scanning_non_provider_patterns,
                    "secret_scanning_push_protection": secret_scanning_push_protection,
                    "secret_scanning_validity_checks": secret_scanning_validity_checks,
                },
                configuration_update_params.ConfigurationUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Configuration,
        )

    def list(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        target_type: Literal["global", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListResponse:
        """
        Lists all code security configurations available in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          target_type: The target type of the code security configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/code-security/configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "target_type": target_type,
                    },
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            cast_to=ConfigurationListResponse,
        )

    def delete(
        self,
        configuration_id: int,
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
        Deletes the desired code security configuration from an organization.
        Repositories attached to the configuration will retain their settings but will
        no longer be associated with the configuration.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/code-security/configurations/{configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def attach(
        self,
        configuration_id: int,
        *,
        org: str,
        scope: Literal["all", "all_without_configurations", "public", "private_or_internal", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Attach a code security configuration to a set of repositories.

        If the
        repositories specified are already attached to a configuration, they will be
        re-attached to the provided configuration.

        If insufficient GHAS licenses are available to attach the configuration to a
        repository, only free features will be enabled.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          scope: The type of repositories to attach the configuration to. `selected` means the
              configuration will be attached to only the repositories specified by
              `selected_repository_ids`

          selected_repository_ids: An array of repository IDs to attach the configuration to. You can only provide
              a list of repository ids when the `scope` is set to `selected`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._post(
            f"/orgs/{org}/code-security/configurations/{configuration_id}/attach",
            body=maybe_transform(
                {
                    "scope": scope,
                    "selected_repository_ids": selected_repository_ids,
                },
                configuration_attach_params.ConfigurationAttachParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    def detach(
        self,
        org: str,
        *,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Detach code security configuration(s) from a set of repositories.

        Repositories
        will retain their settings but will no longer be associated with the
        configuration.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          selected_repository_ids: An array of repository IDs to detach from configurations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/orgs/{org}/code-security/configurations/detach",
            body=maybe_transform(
                {"selected_repository_ids": selected_repository_ids},
                configuration_detach_params.ConfigurationDetachParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    def list_repositories(
        self,
        configuration_id: int,
        *,
        org: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListRepositoriesResponse:
        """
        Lists the repositories associated with a code security configuration in an
        organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: A comma-separated list of statuses. If specified, only repositories with these
              attachment statuses will be returned.

              Can be: `all`, `attached`, `attaching`, `detached`, `removed`, `enforced`,
              `failed`, `updating`, `removed_by_enterprise`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return self._get(
            f"/orgs/{org}/code-security/configurations/{configuration_id}/repositories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "status": status,
                    },
                    configuration_list_repositories_params.ConfigurationListRepositoriesParams,
                ),
            ),
            cast_to=ConfigurationListRepositoriesResponse,
        )


class AsyncConfigurationsResource(AsyncAPIResource):
    @cached_property
    def defaults(self) -> AsyncDefaultsResource:
        return AsyncDefaultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/github_api_sdk-python#with_streaming_response
        """
        return AsyncConfigurationsResourceWithStreamingResponse(self)

    async def create(
        self,
        org: str,
        *,
        description: str,
        name: str,
        advanced_security: Literal["enabled", "disabled"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup_options: ScanningOptionsParam | None | NotGiven = NOT_GIVEN,
        code_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_alerts: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_security_updates: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action_options: configuration_create_params.DependencyGraphAutosubmitActionOptions | NotGiven = NOT_GIVEN,
        enforcement: Literal["enforced", "unenforced"] | NotGiven = NOT_GIVEN,
        private_vulnerability_reporting: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass_options: configuration_create_params.SecretScanningDelegatedBypassOptions | NotGiven = NOT_GIVEN,
        secret_scanning_generic_secrets: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_non_provider_patterns: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_validity_checks: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Creates a code security configuration in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          description: A description of the code security configuration

          name: The name of the code security configuration. Must be unique within the
              organization.

          advanced_security: The enablement status of GitHub Advanced Security

          code_scanning_default_setup: The enablement status of code scanning default setup

          code_scanning_default_setup_options: Feature options for code scanning default setup

          code_scanning_delegated_alert_dismissal: The enablement status of code scanning delegated alert dismissal

          dependabot_alerts: The enablement status of Dependabot alerts

          dependabot_security_updates: The enablement status of Dependabot security updates

          dependency_graph: The enablement status of Dependency Graph

          dependency_graph_autosubmit_action: The enablement status of Automatic dependency submission

          dependency_graph_autosubmit_action_options: Feature options for Automatic dependency submission

          enforcement: The enforcement status for a security configuration

          private_vulnerability_reporting: The enablement status of private vulnerability reporting

          secret_scanning: The enablement status of secret scanning

          secret_scanning_delegated_alert_dismissal: The enablement status of secret scanning delegated alert dismissal

          secret_scanning_delegated_bypass: The enablement status of secret scanning delegated bypass

          secret_scanning_delegated_bypass_options: Feature options for secret scanning delegated bypass

          secret_scanning_generic_secrets: The enablement status of Copilot secret scanning

          secret_scanning_non_provider_patterns: The enablement status of secret scanning non provider patterns

          secret_scanning_push_protection: The enablement status of secret scanning push protection

          secret_scanning_validity_checks: The enablement status of secret scanning validity checks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/code-security/configurations",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "name": name,
                    "advanced_security": advanced_security,
                    "code_scanning_default_setup": code_scanning_default_setup,
                    "code_scanning_default_setup_options": code_scanning_default_setup_options,
                    "code_scanning_delegated_alert_dismissal": code_scanning_delegated_alert_dismissal,
                    "dependabot_alerts": dependabot_alerts,
                    "dependabot_security_updates": dependabot_security_updates,
                    "dependency_graph": dependency_graph,
                    "dependency_graph_autosubmit_action": dependency_graph_autosubmit_action,
                    "dependency_graph_autosubmit_action_options": dependency_graph_autosubmit_action_options,
                    "enforcement": enforcement,
                    "private_vulnerability_reporting": private_vulnerability_reporting,
                    "secret_scanning": secret_scanning,
                    "secret_scanning_delegated_alert_dismissal": secret_scanning_delegated_alert_dismissal,
                    "secret_scanning_delegated_bypass": secret_scanning_delegated_bypass,
                    "secret_scanning_delegated_bypass_options": secret_scanning_delegated_bypass_options,
                    "secret_scanning_generic_secrets": secret_scanning_generic_secrets,
                    "secret_scanning_non_provider_patterns": secret_scanning_non_provider_patterns,
                    "secret_scanning_push_protection": secret_scanning_push_protection,
                    "secret_scanning_validity_checks": secret_scanning_validity_checks,
                },
                configuration_create_params.ConfigurationCreateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Configuration,
        )

    async def retrieve(
        self,
        configuration_id: int,
        *,
        org: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Gets a code security configuration available in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/code-security/configurations/{configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Configuration,
        )

    async def update(
        self,
        configuration_id: int,
        *,
        org: str,
        advanced_security: Literal["enabled", "disabled"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        code_scanning_default_setup_options: ScanningOptionsParam | None | NotGiven = NOT_GIVEN,
        code_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_alerts: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependabot_security_updates: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        dependency_graph_autosubmit_action_options: configuration_update_params.DependencyGraphAutosubmitActionOptions | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        enforcement: Literal["enforced", "unenforced"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        private_vulnerability_reporting: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_alert_dismissal: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_delegated_bypass_options: configuration_update_params.SecretScanningDelegatedBypassOptions | NotGiven = NOT_GIVEN,
        secret_scanning_generic_secrets: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_non_provider_patterns: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_push_protection: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        secret_scanning_validity_checks: Literal["enabled", "disabled", "not_set"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Configuration:
        """
        Updates a code security configuration in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          advanced_security: The enablement status of GitHub Advanced Security

          code_scanning_default_setup: The enablement status of code scanning default setup

          code_scanning_default_setup_options: Feature options for code scanning default setup

          code_scanning_delegated_alert_dismissal: The enablement status of code scanning delegated alert dismissal

          dependabot_alerts: The enablement status of Dependabot alerts

          dependabot_security_updates: The enablement status of Dependabot security updates

          dependency_graph: The enablement status of Dependency Graph

          dependency_graph_autosubmit_action: The enablement status of Automatic dependency submission

          dependency_graph_autosubmit_action_options: Feature options for Automatic dependency submission

          description: A description of the code security configuration

          enforcement: The enforcement status for a security configuration

          name: The name of the code security configuration. Must be unique within the
              organization.

          private_vulnerability_reporting: The enablement status of private vulnerability reporting

          secret_scanning: The enablement status of secret scanning

          secret_scanning_delegated_alert_dismissal: The enablement status of secret scanning delegated alert dismissal

          secret_scanning_delegated_bypass: The enablement status of secret scanning delegated bypass

          secret_scanning_delegated_bypass_options: Feature options for secret scanning delegated bypass

          secret_scanning_generic_secrets: The enablement status of Copilot secret scanning

          secret_scanning_non_provider_patterns: The enablement status of secret scanning non-provider patterns

          secret_scanning_push_protection: The enablement status of secret scanning push protection

          secret_scanning_validity_checks: The enablement status of secret scanning validity checks

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._patch(
            f"/orgs/{org}/code-security/configurations/{configuration_id}",
            body=await async_maybe_transform(
                {
                    "advanced_security": advanced_security,
                    "code_scanning_default_setup": code_scanning_default_setup,
                    "code_scanning_default_setup_options": code_scanning_default_setup_options,
                    "code_scanning_delegated_alert_dismissal": code_scanning_delegated_alert_dismissal,
                    "dependabot_alerts": dependabot_alerts,
                    "dependabot_security_updates": dependabot_security_updates,
                    "dependency_graph": dependency_graph,
                    "dependency_graph_autosubmit_action": dependency_graph_autosubmit_action,
                    "dependency_graph_autosubmit_action_options": dependency_graph_autosubmit_action_options,
                    "description": description,
                    "enforcement": enforcement,
                    "name": name,
                    "private_vulnerability_reporting": private_vulnerability_reporting,
                    "secret_scanning": secret_scanning,
                    "secret_scanning_delegated_alert_dismissal": secret_scanning_delegated_alert_dismissal,
                    "secret_scanning_delegated_bypass": secret_scanning_delegated_bypass,
                    "secret_scanning_delegated_bypass_options": secret_scanning_delegated_bypass_options,
                    "secret_scanning_generic_secrets": secret_scanning_generic_secrets,
                    "secret_scanning_non_provider_patterns": secret_scanning_non_provider_patterns,
                    "secret_scanning_push_protection": secret_scanning_push_protection,
                    "secret_scanning_validity_checks": secret_scanning_validity_checks,
                },
                configuration_update_params.ConfigurationUpdateParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=Configuration,
        )

    async def list(
        self,
        org: str,
        *,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        target_type: Literal["global", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListResponse:
        """
        Lists all code security configurations available in an organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          target_type: The target type of the code security configuration

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/code-security/configurations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "target_type": target_type,
                    },
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            cast_to=ConfigurationListResponse,
        )

    async def delete(
        self,
        configuration_id: int,
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
        Deletes the desired code security configuration from an organization.
        Repositories attached to the configuration will retain their settings but will
        no longer be associated with the configuration.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/code-security/configurations/{configuration_id}",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def attach(
        self,
        configuration_id: int,
        *,
        org: str,
        scope: Literal["all", "all_without_configurations", "public", "private_or_internal", "selected"],
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """Attach a code security configuration to a set of repositories.

        If the
        repositories specified are already attached to a configuration, they will be
        re-attached to the provided configuration.

        If insufficient GHAS licenses are available to attach the configuration to a
        repository, only free features will be enabled.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          scope: The type of repositories to attach the configuration to. `selected` means the
              configuration will be attached to only the repositories specified by
              `selected_repository_ids`

          selected_repository_ids: An array of repository IDs to attach the configuration to. You can only provide
              a list of repository ids when the `scope` is set to `selected`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._post(
            f"/orgs/{org}/code-security/configurations/{configuration_id}/attach",
            body=await async_maybe_transform(
                {
                    "scope": scope,
                    "selected_repository_ids": selected_repository_ids,
                },
                configuration_attach_params.ConfigurationAttachParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=object,
        )

    async def detach(
        self,
        org: str,
        *,
        selected_repository_ids: Iterable[int] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """Detach code security configuration(s) from a set of repositories.

        Repositories
        will retain their settings but will no longer be associated with the
        configuration.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          selected_repository_ids: An array of repository IDs to detach from configurations.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/orgs/{org}/code-security/configurations/detach",
            body=await async_maybe_transform(
                {"selected_repository_ids": selected_repository_ids},
                configuration_detach_params.ConfigurationDetachParams,
            ),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout),
            cast_to=NoneType,
        )

    async def list_repositories(
        self,
        configuration_id: int,
        *,
        org: str,
        after: str | NotGiven = NOT_GIVEN,
        before: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ConfigurationListRepositoriesResponse:
        """
        Lists the repositories associated with a code security configuration in an
        organization.

        The authenticated user must be an administrator or security manager for the
        organization to use this endpoint.

        OAuth app tokens and personal access tokens (classic) need the `write:org` scope
        to use this endpoint.

        Args:
          after: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results after this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          before: A cursor, as given in the
              [Link header](https://docs.github.com/rest/guides/using-pagination-in-the-rest-api#using-link-headers).
              If specified, the query only searches for results before this cursor. For more
              information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          per_page: The number of results per page (max 100). For more information, see
              "[Using pagination in the REST API](https://docs.github.com/rest/using-the-rest-api/using-pagination-in-the-rest-api)."

          status: A comma-separated list of statuses. If specified, only repositories with these
              attachment statuses will be returned.

              Can be: `all`, `attached`, `attaching`, `detached`, `removed`, `enforced`,
              `failed`, `updating`, `removed_by_enterprise`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not org:
            raise ValueError(f"Expected a non-empty value for `org` but received {org!r}")
        return await self._get(
            f"/orgs/{org}/code-security/configurations/{configuration_id}/repositories",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "before": before,
                        "per_page": per_page,
                        "status": status,
                    },
                    configuration_list_repositories_params.ConfigurationListRepositoriesParams,
                ),
            ),
            cast_to=ConfigurationListRepositoriesResponse,
        )


class ConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = to_raw_response_wrapper(
            configurations.create,
        )
        self.retrieve = to_raw_response_wrapper(
            configurations.retrieve,
        )
        self.update = to_raw_response_wrapper(
            configurations.update,
        )
        self.list = to_raw_response_wrapper(
            configurations.list,
        )
        self.delete = to_raw_response_wrapper(
            configurations.delete,
        )
        self.attach = to_raw_response_wrapper(
            configurations.attach,
        )
        self.detach = to_raw_response_wrapper(
            configurations.detach,
        )
        self.list_repositories = to_raw_response_wrapper(
            configurations.list_repositories,
        )

    @cached_property
    def defaults(self) -> DefaultsResourceWithRawResponse:
        return DefaultsResourceWithRawResponse(self._configurations.defaults)


class AsyncConfigurationsResourceWithRawResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = async_to_raw_response_wrapper(
            configurations.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            configurations.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            configurations.update,
        )
        self.list = async_to_raw_response_wrapper(
            configurations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            configurations.delete,
        )
        self.attach = async_to_raw_response_wrapper(
            configurations.attach,
        )
        self.detach = async_to_raw_response_wrapper(
            configurations.detach,
        )
        self.list_repositories = async_to_raw_response_wrapper(
            configurations.list_repositories,
        )

    @cached_property
    def defaults(self) -> AsyncDefaultsResourceWithRawResponse:
        return AsyncDefaultsResourceWithRawResponse(self._configurations.defaults)


class ConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: ConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = to_streamed_response_wrapper(
            configurations.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            configurations.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = to_streamed_response_wrapper(
            configurations.list,
        )
        self.delete = to_streamed_response_wrapper(
            configurations.delete,
        )
        self.attach = to_streamed_response_wrapper(
            configurations.attach,
        )
        self.detach = to_streamed_response_wrapper(
            configurations.detach,
        )
        self.list_repositories = to_streamed_response_wrapper(
            configurations.list_repositories,
        )

    @cached_property
    def defaults(self) -> DefaultsResourceWithStreamingResponse:
        return DefaultsResourceWithStreamingResponse(self._configurations.defaults)


class AsyncConfigurationsResourceWithStreamingResponse:
    def __init__(self, configurations: AsyncConfigurationsResource) -> None:
        self._configurations = configurations

        self.create = async_to_streamed_response_wrapper(
            configurations.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            configurations.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            configurations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configurations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            configurations.delete,
        )
        self.attach = async_to_streamed_response_wrapper(
            configurations.attach,
        )
        self.detach = async_to_streamed_response_wrapper(
            configurations.detach,
        )
        self.list_repositories = async_to_streamed_response_wrapper(
            configurations.list_repositories,
        )

    @cached_property
    def defaults(self) -> AsyncDefaultsResourceWithStreamingResponse:
        return AsyncDefaultsResourceWithStreamingResponse(self._configurations.defaults)
