from fastapi import APIRouter, HTTPException, Depends
from typing import List, Union
import httpx
from queries.exercises import (
    ExerciseIn,
    ExerciseOut,
    Error,
)
import os
from authenticator import authenticator

router = APIRouter()

API_BASE_URL = os.environ.get("API_BASE_URL")
API_KEY = os.environ.get("API_KEY")
TIMEOUT = 10


def handle_response(response):
    """Handle http response for errors"""
    if response.status_code not in (200, 201):
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()


@router.get(
    "/",
    response_model=Union[List[ExerciseOut], Error],
    tags=["exercises"],
)
async def list_exercises(
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            API_BASE_URL,
            headers={"X-Api-Key": API_KEY},
            timeout=TIMEOUT,
        )
    return handle_response(response)


@router.get(
    "/name/{name}",
    response_model=Union[List[ExerciseOut], Error],
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
    return handle_response(response)


@router.get(
    "/difficulty/{difficulty}",
    response_model=Union[List[ExerciseOut], Error],
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
    return handle_response(response)


@router.get(
    "/muscle/{muscle}",
    response_model=Union[List[ExerciseOut], Error],
    tags=["exercises"],
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
    return handle_response(response)


@router.get(
    "/type/{type}",
    response_model=Union[List[ExerciseOut], Error],
    tags=["exercises"],
)
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
    return handle_response(response)


@router.post(
    "/create_exercise_table",
    response_model=Union[List[ExerciseOut], Error],
    tags=["exercises"],
)
async def add_exercise(
    exercise: ExerciseIn,
    _account_data: dict = Depends(authenticator.get_current_account_data),
):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{API_BASE_URL}",
            headers={"X-Api-Key": API_KEY},
            data=exercise.json(),
            timeout=TIMEOUT,
        )
    return handle_response(response)
