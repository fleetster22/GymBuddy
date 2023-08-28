from fastapi import APIRouter, HTTPException, Depends
from typing import List, Union
import httpx
from queries.exercises import (
    ExerciseIn,
    Error,
    ExerciseRepository,
)
import requests

from authenticator import authenticator

router = APIRouter()

API_BASE_URL = "https://api.api-ninjas.com/v1/exercises"
API_KEY = "g5KMn4OGpap61pP8YMZiww==WQh3U1iN7LE3M6ua"
TIMEOUT = 10


@router.post(
    "/fetch_and_create_exercises",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def fetch_and_create_exercises():
    response = requests.get(
        API_BASE_URL,
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
    )
    if response.status_code != 200:
        return Error(response.text)

    return response.json()


@router.get(
    "/",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def list_exercises():
    response = requests.get(
        API_BASE_URL, headers={"X-Api-Key": API_KEY}, timeout=TIMEOUT
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.get(
    "/name/{name}",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercise_by_name(name=str):
    response = requests.get(
        API_BASE_URL, headers={"X-Api-Key": API_KEY}, timeout=TIMEOUT
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.get(
    "/difficulty/{difficulty}",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercises_by_difficulty(difficulty: str):
    response = (
        requests.get(
            API_BASE_URL, headers={"X-Api-Key": API_KEY}, timeout=TIMEOUT
        ),
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.get(
    "/muscle/{muscle}",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercises_by_muscle_group(
    muscle: str,
):
    response = requests.get(
        API_BASE_URL, headers={"X-Api-Key": API_KEY}, timeout=TIMEOUT
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.get(
    "/type/{type}",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercise_by_type(type: str):
    response = requests.get(
        API_BASE_URL, headers={"X-Api-Key": API_KEY}, timeout=TIMEOUT
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.post("/")
async def create_exercise(
    exercise: ExerciseIn, repo: ExerciseRepository = Depends()
):
    return repo.create(exercise)
