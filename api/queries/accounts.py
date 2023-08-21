from pydantic import BaseModel
from typing import List, Optional, Union
from queries.pool import pool


class Error(BaseModel):
    message: str


class AccountIn(BaseModel):
    email: str
    password: str
    first_name: str
    last_name: str


class AccountOut(BaseModel):
    id: str
    email: str
    first_name: str
    last_name: str


class AccountOutWithPassword(AccountOut):
    password: str


class AccountRepository:
    def create_account(self, account: AccountIn) -> AccountOut:
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    "INSERT INTO accounts (first_name, last_name, email) VALUES (%s, %s, %s) RETURNING id",
                    (
                        account.first_name,
                        account.last_name,
                        account.email,
                    ),
                )
                id = result.fetchone()[0]
                return self.account_in_to_out(id, account)

    def get_all_accounts(self) -> Union[Error, List[AccountOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute("SELECT * FROM accounts")
                    result = db.fetchall()
                    return [AccountOut(id=id, **data) for id, *data in result]
        except Exception as e:
            return Error(message=str(e))

    def get_account_by_id(self, account_id: str) -> Optional[AccountOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        "SELECT * FROM accounts WHERE id=%s", (account_id,)
                    )
                    record = result.fetchone()
                    return self.record_to_account_out(record)
        except Exception as e:
            return Error(message=str(e))

    def update_account(
        self, account_id: str, account: AccountIn
    ) -> Union[AccountOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        "UPDATE accounts SET first_name=%s, last_name=%s, email=%s WHERE id=%s RETURNING *",
                        (
                            account.first_name,
                            account.last_name,
                            account.email,
                            account_id,
                        ),
                    )
                    return self.account_in_to_out(account_id, account)
        except Exception as e:
            return Error(message=str(e))

    def delete_account(self, account_id: str) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        "DELETE FROM accounts WHERE id=%s", [account_id]
                    )
                    return True
        except Exception as e:
            return Error(message=str(e))

    def account_in_to_out(self, id: str, account: AccountIn) -> AccountOut:
        old_data = account.dict()
        return AccountOut(id=id, **old_data)

    def record_to_account_out(self, record):
        return AccountOut(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            email=record[3],
        )
