from fastapi import APIRouter, Depends, Response, HTTPException
from typing import List, Optional, Union
from queries.workouts import (
    Error,
    WorkoutIn,
    WorkoutRepository,
    WorkoutOut,
)

from routers.exercises import list_exercises
from random import sample


router = APIRouter()


@router.post("/create", response_model=Union[WorkoutOut, Error])
async def create_workout(
    workout: WorkoutIn,
    response: Response,
    repo: WorkoutRepository = Depends(),
):
    try:
        workout.date = workout.date.isoformat()
        exercise_list = await list_exercises()

        if len(exercise_list) < 1:
            response.status_code = 400
            return {"message": "No exercises found"}

        new_workout = repo.create(workout)
        if new_workout is None:
            response.status_code = 400
            return {"message": "Could not create that workout"}
        new_workout.exercises = sample(exercise_list, 3)
        response.status_code = 201
        return new_workout
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.get(
    "/accounts/{account_id}/", response_model=Union[List[WorkoutOut], Error]
)
def get_all(
    repo: WorkoutRepository = Depends(),
):
    try:
        return repo.get_all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.put("/{workout_id}", response_model=Union[WorkoutOut, Error])
def update_workout(
    workout_id: int,
    workout: WorkoutIn,
    repo: WorkoutRepository = Depends(),
) -> Union[Error, WorkoutOut]:
    try:
        return repo.update(workout_id, workout)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.delete("/{workout_id}", response_model=bool)
def delete_workout(
    workout_id: int,
    repo: WorkoutRepository = Depends(),
) -> bool:
    try:
        return repo.delete(workout_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.get("/{workout_id}", response_model=Optional[WorkoutOut])
def get_one_workout(
    workout_id: int,
    repo: WorkoutRepository = Depends(),
) -> WorkoutOut:
    workout = repo.get_one(workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout
