from pydantic import BaseModel
from queries.pool import pool
from typing import Dict


class DuplicateAccountError(ValueError):
    pass


class Account(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class AccountIn(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str


class AccountOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    password: str


class AccountOutWithPassword(AccountIn):
    id: int


class AccountQueries:
    def create(
            self, info: AccountIn, hashed_password: str
            ) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO account
                        (first_name, last_name, email, password)
                        VALUES
                        (%s,%s,%s,%s)
                        RETURNING id;
                        """,
                        [
                            info.first_name,
                            info.last_name,
                            info.email,
                            hashed_password,
                        ]
                    )
                    id = result.fetchone()[0]
                    old_data = info.dict()
                    return AccountOut(id=id, **old_data)
        except Exception:
            return {"message": "error!"}
# pass in hashed_password not just password

    def get(self, email: str) -> AccountOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT id, first_name, last_name, email, password
                        FROM account
                        WHERE email = %s;
                        """,
                        [email],
                    )
                    record = db.fetchone()

                    if record:
                        columns = [desc[0] for desc in db.description]
                        data = dict(zip(columns, record))
                        return AccountOutWithPassword(**data)
                    else:
                        return {
                            "message":
                            f"This email{email} is not registered to an account."
                        }
        except Exception:
            return AccountOutWithPassword(message="Could not access account.")

    def update(self, email: str, info: AccountIn) -> AccountOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        UPDATE account
                        SET
                        first_name = %s, last_name = %s, email = %s, password = %s
                        WHERE email= %s
                        RETURNING id;
                        """,
                        [
                            info.first_name,
                            info.last_name,
                            info.email,
                            info.password,
                            email,
                        ]
                    )
                    conn.commit()
                    id = result.fetchone()[0]
                    old_data = info.dict()
                    return AccountOut(id=id, **old_data)
        except Exception:
            return {"message": "Account cannot be updated."}

    def delete(self, id: int) -> Dict[str, str]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM account
                        WHERE id= %s
                        RETURNING id;
                        """,
                        [id],

                    )
                    conn.commit()
                    return {
                        "message": f"The account with this id {id} has been deleted."
                    }
        except Exception:
            return {"message": "Account cannot be deleted."}
