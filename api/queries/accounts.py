from pydantic import BaseModel


class DuplicateAccountError(ValueError):
    pass


class Account(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str


class AccountOut(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str


class AccountOutWithPassword(AccountOut):
    hashed_password: str


class AccountQueries:
    def get(self, email: str) -> AccountOutWithPassword:
        return
    def create(self, info: AccountIn, hashed_password: str) -> AccountOutWithPassword:
        return
