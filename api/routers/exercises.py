from typing import Union, Optional
from fastapi import APIRouter, Depends, HTTPException
from queries.exercises import (
    ExerciseIn,
    ExercisesOut,
    Error,
    ExerciseRepository,
)

import os
import requests

router = APIRouter()

API_BASE_URL = os.environ.get("API_BASE_URL")
API_KEY = os.environ.get("API_KEY")
TIMEOUT = 10


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
    "/filter",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercises_by_filter(
    difficulty: Optional[str] = None, exercise_type: Optional[str] = None
):
    params = {}

    if difficulty:
        params["difficulty"] = difficulty
    if exercise_type:
        params["type"] = exercise_type

    response = requests.get(
        API_BASE_URL,
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
        params=params,
    )

    if response.status_code != 200:
        return Error(response.text)

    return response.json()


@router.get(
    "/name/{name}",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercise_by_name(name: str):
    response = requests.get(
        f"{API_BASE_URL}?name={name}",
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
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
    response = requests.get(
        f"{API_BASE_URL}?difficulty={difficulty}",
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
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
        f"{API_BASE_URL}?muscle={muscle}",
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.get(
    "/type/{type}",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def get_exercise_by_type(exercise_type: str):
    response = requests.get(
        f"{API_BASE_URL}?type={exercise_type}",
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
    )
    if response.status_code != 200:
        return Error(response.text)
    return response.json()


@router.get(
    "/db_exercises",
    response_model=ExercisesOut,
)
async def get_exercises_from_db(
    repo: ExerciseRepository = Depends(),
):
    return ExercisesOut(**repo.get_all())


@router.delete("/{exercise_id}", response_model=bool)
def delete_exercise(
    exercise_id: int,
    repo: ExerciseRepository = Depends(),
) -> bool:
    try:
        return repo.delete(exercise_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.post(
    "/fetch_and_create_exercises",
    response_model=Union[list, Error],
    tags=["exercises"],
)
async def fetch_and_create_exercise(
    difficulty: str = "beginner",
    exercise_type: str = "cardio",
    repo: ExerciseRepository = Depends(),
):
    params = {"difficulty": difficulty}
    params["type"] = exercise_type

    response = requests.get(
        API_BASE_URL,
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
        params=params,
    )

    if response.status_code != 200:
        return Error(response.text)

    exercises = response.json()

    for exercise in exercises:
        db_exercise = ExerciseIn(
            name=exercise["name"],
            type=exercise.get("type", ""),
            muscle=exercise.get("muscle", ""),
            equipment=exercise.get("equipment", ""),
            difficulty=exercise.get("difficulty", ""),
            instructions=exercise.get("instructions", ""),
        )

        repo.create(db_exercise)

    return exercises
