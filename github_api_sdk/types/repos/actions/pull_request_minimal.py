


from ...._models import BaseModel

__all__ = ["PullRequestMinimal", "Base", "BaseRepo", "Head", "HeadRepo"]


class BaseRepo(BaseModel):
    id: int

    name: str

    url: str


class Base(BaseModel):
    ref: str

    repo: BaseRepo

    sha: str


class HeadRepo(BaseModel):
    id: int

    name: str

    url: str


class Head(BaseModel):
    ref: str

    repo: HeadRepo

    sha: str


class PullRequestMinimal(BaseModel):
    id: int

    base: Base

    head: Head

    number: int

    url: str
