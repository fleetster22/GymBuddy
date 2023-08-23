from authenticator import authenticator
from fastapi import APIRouter, HTTPException, Depends
import httpx
from queries.exercises import Exercises
from dotenv import load_dotenv


load_dotenv()

router = APIRouter()

# API_BASE_URL = os.getenv("API_BASE_URL")
API_BASE_URL = "https://api.api-ninjas.com/v1/exercises"
API_KEY = "g5KMn4OGpap61pP8YMZiww==WQh3U1iN7LE3M6ua"


TIMEOUT = 10


# get all exercises from 3rd party API
@router.get("/", response_model=list[Exercises], tags=["exercises"])
async def list_exercises(
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_BASE_URL,
            headers={"X-Api-Key": API_KEY},
            timeout=TIMEOUT,
        )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()


# get exercise by name
@router.get(
    "/name/{name}",
    response_model=list[Exercises],
    tags=["exercises"],
)
async def get_exercise_by_name(
    name: str,
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}?name={name}",
            headers={"X-Api-Key": API_KEY},
            timeout=TIMEOUT,
        )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()


# get exercises by difficulty
@router.get(
    "/difficulty/{difficulty}",
    response_model=list[Exercises],
    tags=["exercises"],
)
async def get_exercises_by_difficulty(
    difficulty: str,
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}?difficulty={difficulty}",
            headers={"X-Api-Key": API_KEY},
            timeout=TIMEOUT,
        )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()


# get exercises by muscle group
@router.get(
    "/muscle/{muscle}", response_model=list[Exercises], tags=["exercises"]
)
async def get_exercises_by_muscle_group(
    muscle: str,
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}?muscle={muscle}",
            headers={"X-Api-Key": API_KEY},
            timeout=TIMEOUT,
        )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()


# get exercises by type
@router.get("/type/{type}", response_model=list[Exercises], tags=["exercises"])
async def get_exercise_by_type(
    type: str,
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{API_BASE_URL}?type={type}",
            headers={"X-Api-Key": API_KEY},
            timeout=TIMEOUT,
        )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()
