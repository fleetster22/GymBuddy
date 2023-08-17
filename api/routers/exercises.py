from fastapi import APIRouter, HTTPException
from queries.exercises import Exercises
import requests
from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

API_BASE_URL = os.getenv("API_BASE_URL")
API_KEY = os.getenv("X-API-KEY")

TIMEOUT = 10


# get all exercises => returns a list of 10 exercises
@router.get("/", response_model=list[Exercises], tags=["exercises"])
def list_exercises():
    response = requests.get(
        API_BASE_URL, headers={"X-Api-Key": API_KEY}, timeout=TIMEOUT
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()


# get exercise by name
@router.get(
    "/name/{exercise_name}", response_model=Exercises, tags=["exercises"]
)
def get_exercise_by_name(exercise_name: str):
    response = requests.get(
        f"{API_BASE_URL}/name/{exercise_name}",
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
    "/difficulty/{difficulty_level}",
    response_model=list[Exercises],
    tags=["exercises"],
)
def get_exercise_by_difficulty(difficulty_level: str):
    response = requests.get(
        f"{API_BASE_URL}/difficulty/{difficulty_level}",
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
def get_exercise_by_muscle_group(muscle_group: str):
    response = requests.get(
        f"{API_BASE_URL}/muscle/{muscle_group}",
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
def get_exercise_by_type(exercise_type: str):
    response = requests.get(
        f"{API_BASE_URL}/type/{exercise_type}",
        headers={"X-Api-Key": API_KEY},
        timeout=TIMEOUT,
    )
    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code, detail=response.text
        )
    return response.json()
