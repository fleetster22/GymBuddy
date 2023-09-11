from pydantic import BaseModel
from typing import List, Union, Optional
from datetime import date
from queries.pool import pool
from queries.exercises import ExerciseIn, ExerciseOut


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
                    db.execute("SELECT * FROM workouts;")
                    workouts = []
                    for record in db.fetchall():
                        workout_id = record[0]

                        db.execute(
                            "SELECT exercises.* FROM exercises "
                            "JOIN workout_exercises ON exercises.id = workout_exercises.exercise_id "
                            "WHERE workout_exercises.workout_id = %s;",
                            [workout_id],
                        )
                        exercise_records = db.fetchall()
                        exercises = []
                        for exercise in exercise_records:
                            exercise_data = ExerciseOut(
                                id=exercise[0],
                                name=exercise[1],
                                type=exercise[2],
                                muscle=exercise[3],
                                equipment=exercise[4],
                                difficulty=exercise[5],
                                instructions=exercise[6],
                            )
                            exercises.append(exercise_data)

                        workout = WorkoutOut(
                            id=workout_id,
                            name=record[1],
                            difficulty=record[2],
                            description=record[3],
                            date=record[4],
                            exercises=exercises,
                        )
                        workouts.append(workout)
                    return workouts

        except Exception as e:
            return {"message": str(e)}

    def get_one(self, workout_id: int) -> Optional[WorkoutOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        SELECT * FROM workouts
                        WHERE id = %s
                        """,
                        [workout_id],
                    )
                    record = db.fetchone()
                    if record is None:
                        return None

                    db.execute(
                        "SELECT exercises.* FROM exercises "
                        "JOIN workout_exercises ON exercises.id = workout_exercises.exercise_id "
                        "WHERE workout_exercises.workout_id = %s;",
                        [workout_id],
                    )
                    exercise_records = db.fetchall()
                    exercises = []
                    for exercise in exercise_records:
                        exercise_data = {
                            "id": exercise[0],
                            "name": exercise[1],
                            "type": exercise[2],
                            "muscle": exercise[3],
                            "equipment": exercise[4],
                            "difficulty": exercise[5],
                            "instructions": exercise[6],
                        }
                        exercises.append(exercise_data)

                    return self.record_to_workout_out(record, exercises)
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

    def complete(self, workout_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE workouts
                        SET completed = TRUE
                        WHERE id = %s
                        """,
                        [workout_id],
                    )
                    return True
        except Exception as e:
            print(e)
            return {"message": "Could not complete that workout"}

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
                    return workout_id

        except Exception:
            return {"message": "Create did not work"}

    def workout_in_to_out(self, id: int, workout: WorkoutIn):
        old_data = workout.dict()
        return WorkoutOut(id=id, **old_data)

    def record_to_workout_out(self, record, exercises=None):
        return WorkoutOut(
            id=record[0],
            name=record[1],
            difficulty=record[2],
            description=record[3],
            date=record[4],
            exercises=exercises or [],
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
        except Exception as e:
            return {"message": str(e)}
