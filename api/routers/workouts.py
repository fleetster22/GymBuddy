from datetime import date
from fastapi import APIRouter, Depends, HTTPException
from typing import Union, Optional, List
from queries.workouts import (
    Error,
    WorkoutIn,
    WorkoutRepository,
    WorkoutOut,
    WorkoutToDB,
)
from authenticator import authenticator
from queries.exercises import ExerciseRepository

router = APIRouter()


@router.post("/create", response_model=Union[WorkoutOut, Error])
async def create_workout(
    workout: WorkoutIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    workout_repo: WorkoutRepository = Depends(),
    exercise_repo: ExerciseRepository = Depends(),
):
    try:
        exercise_id_list = []
        exercises = workout.exercises
        for exercise in exercises:
            entry = exercise_repo.get_one_exercise(exercise.name)
            if entry:
                exercise_id_list.append(entry[0])
            else:
                entry = exercise_repo.create(exercise)
                exercise_id_list.append(entry.id)

        new_workout = WorkoutToDB(
            name=workout.name,
            difficulty=workout.difficulty,
            description=workout.description,
            date=workout.date,
        )
        workout_id = workout_repo.create(new_workout)
        workout_repo.add_to_history(
            workout_id, account_data["id"], workout.date
        )

        for exercise_id in exercise_id_list:
            workout_repo.link_exercise_to_workout(workout_id, exercise_id)

        for exercise in workout_repo.get_all():
            workout_out = WorkoutOut(
                id=workout_id,
                name=workout.name,
                difficulty=workout.difficulty,
                description=workout.description,
                date=workout.date,
                exercises=exercises,
            )
        return workout_out

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.get(
    "/",
    response_model=Union[list, Error],
    tags=["workouts"],
)
async def get_all(
    account_data: Optional[dict] = Depends(
        authenticator.try_get_current_account_data
    ),
    workout_repo: WorkoutRepository = Depends(),
):
    try:
        if not account_data:
            raise HTTPException(status_code=401, detail="Not authorized")
        return workout_repo.get_history(account_data["id"])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.put("/{workout_id}", response_model=Union[WorkoutOut, Error])
def update_workout(
    workout_id: int,
    workout: WorkoutIn,
    account_data: dict = Depends(authenticator.get_current_account_data),
    workout_repo: WorkoutRepository = Depends(),
) -> Union[Error, WorkoutOut]:
    try:
        return workout_repo.update(workout_id, workout)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.delete("/{workout_id}", response_model=bool)
def delete_workout(
    workout_id: int,
    account_data: dict = Depends(authenticator.get_current_account_data),
    workout_repo: WorkoutRepository = Depends(),
) -> bool:
    try:
        return workout_repo.delete(workout_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")


@router.get("/{workout_id}", response_model=WorkoutOut)
def get_one_workout(
    workout_id: int,
    account_data: Optional[dict] = Depends(
        authenticator.try_get_current_account_data
    ),
    workout_repo: WorkoutRepository = Depends(),
) -> WorkoutOut:
    workout = workout_repo.get_one(workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


@router.get("/get_join_table", response_model=WorkoutToDB)
def get_join_table(
    workout_id: int,
    account_data: dict = Depends(authenticator.get_current_account_data),
    workout_repo: WorkoutRepository = Depends(),
) -> WorkoutToDB:
    workout = workout_repo.link_exercise_to_workout(workout_id)
    if workout is None:
        raise HTTPException(status_code=404, detail="Workout not found")
    return workout


@router.post("/{workout_id}/complete", response_model=bool)
def complete_workout(
    workout_id: int,
    account_data: dict = Depends(authenticator.get_current_account_data),
    workout_repo: WorkoutRepository = Depends(),
) -> bool:
    try:
        workout_repo.add_to_history(
            workout_id, account_data["id"], date.today()
        )
        return workout_repo.complete(workout_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")
