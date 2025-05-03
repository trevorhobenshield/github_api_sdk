


from ...._models import BaseModel

__all__ = ["PorterAuthor"]


class PorterAuthor(BaseModel):
    id: int

    email: str

    import_url: str

    name: str

    remote_id: str

    remote_name: str

    url: str
