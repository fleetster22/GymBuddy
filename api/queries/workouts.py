from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool


class Error(BaseModel):
    message: str


class WorkoutIn(BaseModel):
    name: str
    description: str
    date: date
    difficulty: str
    exercises: List[str] = []


class WorkoutOut(BaseModel):
    id: int
    name: str
    description: str
    date: date
    exercises: List[str] = []


class WorkoutRepository:
    def get_one(self, workout_id: int) -> Optional[WorkoutOut]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT id
                             , name
                             , description
                             , date
                             , difficulty
                        FROM workouts
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
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
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
                        SET name = %s
                          , date = %s
                          , description = %s
                          , difficulty = %s
                        WHERE id = %s
                        """,
                        [
                            workout.name,
                            workout.description,
                            workout.date,
                            workout.difficulty,
                            workout_id,
                        ],
                    )
                    return self.workout_in_to_out(workout_id, workout)
        except Exception as e:
            print(e)
            return {"message": "Could not update that workout"}

    def get_all(self) -> Union[Error, List[WorkoutOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT *FROM workouts;
                        """
                    )
                    return [
                        self.record_to_workout_out(record) for record in result
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not get all workouts"}

    def get_all_by_difficulty(self, difficulty: str) -> List[WorkoutOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, name, description, date, difficulty
                        FROM workouts
                        WHERE difficulty = %s
                        """,
                        [difficulty],
                    )
                    records = result.fetchall()
                    return [
                        self.record_to_workout_out(record)
                        for record in records
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not get the workouts by difficulty"}

    def create(self, workout: WorkoutIn) -> Union[WorkoutOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO workouts
                            (name, description, date, difficulty)
                        VALUES
                            (%s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            workout.name,
                            workout.description,
                            workout.date,
                            workout.difficulty,
                        ],
                    )
                    id = result.fetchone()[0]

                    return self.workout_in_to_out(id, workout)
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
            date=record[3],
            difficulty=record[4],
        )

    def link_exercise_to_workout(self, workout_id: int, exercise_name: str):
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    db.execute(
                        """
                        INSERT INTO workout_exercises
                            (workout_id, exercise_name)
                        VALUES
                            (%s, %s);
                        """,
                        [
                            workout_id,
                            exercise_name,
                        ],
                    )
                    # Return new data
                    return True
        except Exception:
            return {"message": "Create did not work"}
