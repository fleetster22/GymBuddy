from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.workouts import (
    Error,
    WorkoutIn,
    WorkoutRepository,
    WorkoutOut,
)


router = APIRouter()


@router.post("/", response_model=Union[WorkoutOut, Error])
def create_workout(
    workout: WorkoutIn,
    response: Response,
    repo: WorkoutRepository = Depends(),
):
    response.status_code = 400
    return repo.create(workout)


@router.get("/", response_model=Union[List[WorkoutOut], Error])
def get_all(
    repo: WorkoutRepository = Depends(),
):
    return repo.get_all()


@router.put("/{workout_id}", response_model=Union[WorkoutOut, Error])
def update_workout(
    workout_id: int,
    workout: WorkoutIn,
    repo: WorkoutRepository = Depends(),
) -> Union[Error, WorkoutOut]:
    return repo.update(workout_id, workout)


@router.delete("/{workout_id}", response_model=bool)
def delete_workout(
    workout_id: int,
    repo: WorkoutRepository = Depends(),
) -> bool:
    return repo.delete(workout_id)


@router.get("/{workout_id}", response_model=Optional[WorkoutOut])
def get_one_workout(
    workout_id: int,
    response: Response,
    repo: WorkoutRepository = Depends(),
) -> WorkoutOut:
    workout = repo.get_one(workout_id)
    if workout is None:
        response.status_code = 404
    return workout
