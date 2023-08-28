from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.workouts import (
    Error,
    WorkoutIn,
    WorkoutRepository,
    WorkoutOut,
)

# from .exercises import list_exercises
# from random import sample


router = APIRouter()


@router.post("/create", response_model=Union[WorkoutOut, Error])
async def create_workout(
    workout: WorkoutIn,
    response: Response,
    repo: WorkoutRepository = Depends(),
):
    # # Fetch all exercises from the database
    # exercise_list = repo.list_exercises()

    # # Filter exercises by the desired difficulty
    # difficulty_filtered_exercises = [
    #     ex for ex in exercise_list if ex["difficulty"] == workout.difficulty
    # ]

    # #  Group the exercises by type
    # type_grouped_exercises = {}
    # for exercise in difficulty_filtered_exercises:
    #     if exercise["type"] not in type_grouped_exercises:
    #         type_grouped_exercises[exercise["type"]] = []
    #     type_grouped_exercises[exercise["type"]].append(exercise)

    # # Randomly select one exercise from each type
    # selected_exercises = []
    # for exercise_type, exercises in type_grouped_exercises.items():
    #     selected_exercises.append(sample(exercises, 1)[0])

    # new_workout = repo.create(workout)
    # for exercise in selected_exercises:
    #     repo.link_exercise_to_workout(new_workout.id, exercise["name"])

    # response.status_code = 201
    # return new_workout


@router.get("/", response_model=Union[List[WorkoutOut], Error])
def get_all(
    repo: WorkoutRepository = Depends(),
):
    return repo.get_all()


@router.get("/difficulty/{difficulty}", response_model=List[WorkoutOut])
def get_workouts_by_difficulty(
    difficulty: str,
    repo: WorkoutRepository = Depends(),
):
    return repo.get_all_by_difficulty(difficulty)


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
