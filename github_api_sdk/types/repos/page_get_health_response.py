

from typing import Optional

from ..._models import BaseModel

__all__ = ["PageGetHealthResponse", "AltDomain", "Domain"]


class AltDomain(BaseModel):
    caa_error: Optional[str] = None

    dns_resolves: Optional[bool] = None

    enforces_https: Optional[bool] = None

    has_cname_record: Optional[bool] = None

    has_mx_records_present: Optional[bool] = None

    host: Optional[str] = None

    https_error: Optional[str] = None

    is_a_record: Optional[bool] = None

    is_apex_domain: Optional[bool] = None

    is_cloudflare_ip: Optional[bool] = None

    is_cname_to_fastly: Optional[bool] = None

    is_cname_to_github_user_domain: Optional[bool] = None

    is_cname_to_pages_dot_github_dot_com: Optional[bool] = None

    is_fastly_ip: Optional[bool] = None

    is_https_eligible: Optional[bool] = None

    is_non_github_pages_ip_present: Optional[bool] = None

    is_old_ip_address: Optional[bool] = None

    is_pages_domain: Optional[bool] = None

    is_pointed_to_github_pages_ip: Optional[bool] = None

    is_proxied: Optional[bool] = None

    is_served_by_pages: Optional[bool] = None

    is_valid: Optional[bool] = None

    is_valid_domain: Optional[bool] = None

    nameservers: Optional[str] = None

    reason: Optional[str] = None

    responds_to_https: Optional[bool] = None

    should_be_a_record: Optional[bool] = None

    uri: Optional[str] = None


class Domain(BaseModel):
    caa_error: Optional[str] = None

    dns_resolves: Optional[bool] = None

    enforces_https: Optional[bool] = None

    has_cname_record: Optional[bool] = None

    has_mx_records_present: Optional[bool] = None

    host: Optional[str] = None

    https_error: Optional[str] = None

    is_a_record: Optional[bool] = None

    is_apex_domain: Optional[bool] = None

    is_cloudflare_ip: Optional[bool] = None

    is_cname_to_fastly: Optional[bool] = None

    is_cname_to_github_user_domain: Optional[bool] = None

    is_cname_to_pages_dot_github_dot_com: Optional[bool] = None

    is_fastly_ip: Optional[bool] = None

    is_https_eligible: Optional[bool] = None

    is_non_github_pages_ip_present: Optional[bool] = None

    is_old_ip_address: Optional[bool] = None

    is_pages_domain: Optional[bool] = None

    is_pointed_to_github_pages_ip: Optional[bool] = None

    is_proxied: Optional[bool] = None

    is_served_by_pages: Optional[bool] = None

    is_valid: Optional[bool] = None

    is_valid_domain: Optional[bool] = None

    nameservers: Optional[str] = None

    reason: Optional[str] = None

    responds_to_https: Optional[bool] = None

    should_be_a_record: Optional[bool] = None

    uri: Optional[str] = None


class PageGetHealthResponse(BaseModel):
    alt_domain: Optional[AltDomain] = None

    domain: Optional[Domain] = None
