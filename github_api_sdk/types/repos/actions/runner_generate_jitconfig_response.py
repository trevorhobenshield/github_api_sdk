


from ...._models import BaseModel
from ...orgs.actions.self_hosted_runner import SelfHostedRunner

__all__ = ["RunnerGenerateJitconfigResponse"]


class RunnerGenerateJitconfigResponse(BaseModel):
    encoded_jit_config: str
    """The base64 encoded runner configuration."""

    runner: SelfHostedRunner
    """A self hosted runner"""
