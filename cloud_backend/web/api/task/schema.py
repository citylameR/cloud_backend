from pydantic import BaseModel


class Msg(BaseModel):
    """Simple message."""

    msg: str
