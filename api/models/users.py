from pydantic import BaseModel


class BaseUser(BaseModel):
    first: str
    last: str
    email: str
    password: str


class UserWithId(BaseUser):
    id: str
