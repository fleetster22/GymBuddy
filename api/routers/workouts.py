from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.workouts import (
    Error,
    WorkoutIn,
    WorkoutRepository,
    WorkoutOut,
)

from .exercises import list_exercises


router = APIRouter()


@router.post("/", response_model=Union[WorkoutOut, Error])
async def create_workout(
    workout: WorkoutIn,
    response: Response,
    repo: WorkoutRepository = Depends(),
):
    # fetched_exercises = await list_exercises()

    # matching_exercises = [
    #     ex for ex in fetched_exercises if ex["name"] in workout.exercises
    # ]

    ExerciseList = workout["exercises"]
    ExerciseNames = []
    for exercise in ExerciseList:
        ExerciseNames.append(exercise["name"])

    workout["exercises"] = ExerciseNames

    new_workout = repo.create(workout)
    for exercise in ExerciseList:
        repo.link_exercise_to_workout(new_workout.id, exercise["id"])
    response.status_code = 201
    return new_workout




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
