from typing import List, Union
from fastapi import APIRouter, Depends, Response
from queries.accounts import AccountIn, AccountOut, AccountRepository, Error

router = APIRouter()


@router.post("/", response_model=Union[AccountOut, Error])
def create_account(
    account: AccountIn, response: Response, repo: AccountRepository = Depends()
):
    response.status_code = 400
    return repo.create_account(account)


@router.get("/", response_model=List[AccountOut])
def get_all_accounts(repo: AccountRepository = Depends()):
    return repo.get_all_accounts()


@router.get("/{account_id}", response_model=Union[AccountOut, Error])
def get_account_by_id(
    account_id: str,
    repo: AccountRepository = Depends(),
) -> bool:
    return repo.get_account_by_id(account_id)


@router.put("/{account_id}", response_model=Union[AccountOut, Error])
def update_account(
    account_id: str,
    account: AccountIn,
    repo: AccountRepository = Depends(),
) -> Union[AccountOut, Error]:
    return repo.update_account(account_id, account)


@router.delete("/{account_id}", response_model=bool)
def delete_account(
    account_id: str,
    repo: AccountRepository = Depends(),
) -> bool:
    return repo.delete_account(account_id)
