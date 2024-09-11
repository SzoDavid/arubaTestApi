from pydantic import BaseModel


class NameReq(BaseModel):
    name: str
