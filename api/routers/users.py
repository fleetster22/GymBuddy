from fastapi import APIRouter, Depends
from models.users import BaseUser, UserWithId
from queries.users import UsersQueries

router = APIRouter()


@router.get("/", response_model=list | None)
def get_users(queries: UsersQueries = Depends()):
    return queries.get_users()


@router.get("/{id}", response_model=UserWithId | None)
def get_user_by_id(id: str, queries: UsersQueries = Depends()):
    return queries.get_user_by_id(id)


@router.post("/create", response_model=BaseUser | None)
def create_user(user: BaseUser, queries: UsersQueries = Depends()):
    return queries.create_user(user)


@router.put("/update/{id}", response_model=UserWithId | None)
def update_user(id: str, user: UserWithId, queries: UsersQueries = Depends()):
    return queries.update_user(user, id)


@router.delete("/delete/{id}", response_model=bool | None)
def delete_user(id: str, queries: UsersQueries = Depends()):
    return queries.delete_user(id)
