from random import sample
from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime, date
from queries.pool import pool
from queries.exercises import ExerciseIn


class Error(BaseModel):
    message: str


class WorkoutIn(BaseModel):
    name: str
    difficulty: str
    description: str
    date: date
    exercises: list[ExerciseIn]


class WorkoutOut(WorkoutIn):
    id: int


class WorkoutToDB(BaseModel):
    name: str
    difficulty: str
    description: str
    date: date


class WorkoutRepository:
    def get_all(self) -> Union[Error, List[WorkoutOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT * FROM workouts;
                        """
                    )
                    records = db.fetchall()
                    return [
                        self.record_to_workout_out(record)
                        for record in records
                    ]

        except Exception as e:
            print(e)
            return {"message": "Could not get all workouts"}

    def get_one(self, workout_id: int) -> WorkoutOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT * FROM workouts
                        WHERE id = %s
                        """,
                        [workout_id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_workout_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get that workout"}

    def delete(self, workout_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM workouts
                        WHERE id = %s
                        """,
                        [workout_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(
        self, workout_id: int, workout: WorkoutIn
    ) -> Union[WorkoutOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE workouts
                        SET name = %s,
                          difficulty = %s,
                          description = %s,
                          date = %s

                        WHERE id = %s
                        """,
                        [
                            workout.name,
                            workout.difficulty,
                            workout.description,
                            workout.date,
                            workout_id,
                        ],
                    )
                    return self.workout_in_to_out(workout_id, workout)
        except Exception as e:
            print(e)
            return {"message": "Could not update that workout"}

    def create(self, workout: WorkoutIn) -> Union[WorkoutOut, Error]:
        # print("Hello World")
        # print(workout)
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO workouts
                            (name, difficulty, description, date)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            workout.name,
                            workout.difficulty,
                            workout.description,
                            workout.date,
                        ],
                    )
                    workout_id = result.fetchone()[0]
                    # print("Workout ID:", workout_id)
                    return workout_id

        except Exception:
            return {"message": "Create did not work"}

    def workout_in_to_out(self, id: int, workout: WorkoutIn):
        old_data = workout.dict()
        return WorkoutOut(id=id, **old_data)

    def record_to_workout_out(self, record) -> WorkoutOut:
        return WorkoutOut(
            id=record[0],
            name=record[1],
            description=record[2],
            date=datetime.strptime(record[3], "%Y-%m-%d").date(),
            difficulty=str(record[4]),
        )

    def link_exercise_to_workout(self, workout_id: int, exercise_id: int):
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO workout_exercises
                            (workout_id, exercise_id)
                        VALUES
                            (%s, %s);
                        """,
                        [
                            workout_id,
                            exercise_id,
                        ],
                    )
                    return True
        except Exception:
            return {"message": "Create did not work"}
