from fastapi import (
    Depends,
    HTTPException,
    status,
    Response,
    APIRouter,
    Request,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator

from pydantic import BaseModel

from queries.accounts import (
    AccountIn,
    AccountOut,
    AccountQueries,
    DuplicateAccountError,
)


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: AccountOut


class HttpError(BaseModel):
    detail: str


router = APIRouter()


@router.get("/protected", response_model=bool)
async def get_protected(
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return True


@router.get("/token", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: AccountOut = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


@router.post("/create", response_model=AccountToken | HttpError)
async def create_account(
    info: AccountIn,
    request: Request,
    response: Response,
    accounts: AccountQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = accounts.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create an account with those credentials",
        )
    form = AccountForm(username=info.email, password=info.password)
    token = await authenticator.login(response, request, form, accounts)
    return AccountToken(account=account, **token.dict())


@router.put("/update", response_model=AccountOut | HttpError)
async def update_account(
    account_form: AccountIn,
    current_account: AccountToken = Depends(
        authenticator.get_current_account_data
    ),
    repo: AccountQueries = Depends(),
<<<<<<< HEAD
<<<<<<< HEAD
    ) -> AccountOut:
=======
) -> AccountOut:
>>>>>>> 1b3ef1dd5112ebe16c95fb87aa0329a9b3e46de9
=======
) -> AccountOut:
>>>>>>> ca27da871de74be01d6e4ecbaf70f8d4e53f32f9
    if not current_account:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Log in to update your account.",
        )
    try:
        update_account = repo.update(current_account["email"], account_form)
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot update account with those credentials",
        )
    return update_account


<<<<<<< HEAD
<<<<<<< HEAD

@router.delete("/delete")
async def delete_account(
    current_account: AccountToken = Depends(authenticator.get_current_account_data),
=======
=======
>>>>>>> ca27da871de74be01d6e4ecbaf70f8d4e53f32f9
@router.delete("/delete")
async def delete_account(
    current_account: AccountToken = Depends(
        authenticator.get_current_account_data
    ),
<<<<<<< HEAD
>>>>>>> 1b3ef1dd5112ebe16c95fb87aa0329a9b3e46de9
=======
>>>>>>> ca27da871de74be01d6e4ecbaf70f8d4e53f32f9
    repo: AccountQueries = Depends(),
) -> AccountOut:
    if not current_account:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Log in to delete your account.",
        )
    try:
        deleted_account = repo.delete(current_account["id"])
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete account with those credentials",
        )
    return deleted_account


@router.get("/detail")
async def get_account_detail(
    account_id: str, repo: AccountQueries = Depends(),
) -> AccountIn:
    account = repo.get_by_id(account_id)
    if isinstance(account, dict):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=account["message"]
        )
    return account
