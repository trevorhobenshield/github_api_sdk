

from typing import List, Optional

from ..._models import BaseModel
from ..minimal_repository import MinimalRepository

__all__ = ["CheckSuiteUpdatePreferencesResponse", "Preferences", "PreferencesAutoTriggerCheck"]


class PreferencesAutoTriggerCheck(BaseModel):
    app_id: int

    setting: bool


class Preferences(BaseModel):
    auto_trigger_checks: Optional[List[PreferencesAutoTriggerCheck]] = None


class CheckSuiteUpdatePreferencesResponse(BaseModel):
    preferences: Preferences

    repository: MinimalRepository
    """Minimal Repository"""
