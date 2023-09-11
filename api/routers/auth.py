from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from fastapi import (
    Depends,
    Request,
    APIRouter,
)

from queries.accounts import (
    AccountOut,
)

from .accounts import AccountToken

router = APIRouter()


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
