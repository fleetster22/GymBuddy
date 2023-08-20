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

class WorkoutOut(BaseModel):
    name: str
    description: str
    date: date


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
                        FROM workouts
                        WHERE id = %s
                        """,
                        [workout_id]
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_workoutout(record)
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
                        [workout_id]
                    )
                    return True
        except Exception as e:
            print(e)
            return False

    def update(self, workout_id: int, workout: WorkoutIn) -> Union[WorkoutOut, Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE workouts
                        SET name = %s
                          , date = %s
                          , description = %s
                        WHERE id = %s
                        """,
                        [
                            workout.name,
                            workout.description,
                            workout.date,
                            workout_id
                        ]
                    )
                    # old_data = workout.dict()
                    # return workoutOut(id=workout_id, **old_data)
                    return self.workout_in_to_out(workout_id, workout)
        except Exception as e:
            print(e)
            return {"message": "Could not update that workout"}

    def get_all(self) -> Union[Error, List[WorkoutOut]]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our SELECT statement
                    result = db.execute(
                        """
                        SELECT id, name, from_date, to_date, thoughts
                        FROM workouts
                        ORDER BY from_date;
                        """
                    )
                    # result = []
                    # for record in db:
                    #     workout = WorkoutOut(
                    #         id=record[0],
                    #         name=record[1],
                    #         description=record[2],
                    #         date=record[3],
                    #     )
                    #     result.append(workout)
                    # return result

                    return [
                        self.record_to_workout_out(record)
                        for record in result
                    ]
        except Exception as e:
            print(e)
            return {"message": "Could not get all workouts"}

    def create(self, workout: WorkoutIn) -> Union[WorkoutOut, Error]:
        try:
            # connect the database
            with pool.connection() as conn:
                # get a cursor (something to run SQL with)
                with conn.cursor() as db:
                    # Run our INSERT statement
                    result = db.execute(
                        """
                        INSERT INTO workouts
                            (name, description, date)
                        VALUES
                            (%s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            workout.name,
                            workout.description,
                            workout.date,
                        ]
                    )
                    id = result.fetchone()[0]
                    # Return new data
                    # old_data = workout.dict()
                    # return WorkoutOut(id=id, **old_data)
                    return self.workout_in_to_out(id, workout)
        except Exception:
            return {"message": "Create did not work"}

    def workout_in_to_out(self, id: int, workout: WorkoutIn):
        old_data = workout.dict()
        return WorkoutOut(id=id, **old_data)

    def record_to_workout_out(self, record):
        return WorkoutOut(
            id=record[0],
            name=record[1],
            description=record[2],
            date=record[3],
        )
