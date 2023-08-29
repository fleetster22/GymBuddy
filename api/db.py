import os
from psycopg_pool import ConnectionPool

pool = ConnectionPool(conninfo=os.environ["DATABASE_URL"])


class WorkoutQueries:
    def workout_record_to_dict(self, row, name):
        workout = None
        if row is not None:
            workout = {}
            workout_fields = [
                "workout_id",
                "name",
                "description",
                "exercises",
                "date",
                "owner_id",
            ]
            for i, column in enumerate(name):
                if column.name in workout_fields:
                    workout[column.name] = row[i]
                workout["id"] = workout["workout_id"]

            owner = {}
            owner_fields = ["owner_id", "first", "last", "email"]
            for i, column in enumerate(name):
                if column.name in owner_fields:
                    owner[column.name] = row[i]
            owner["id"] = owner["owner_id"]

            workout["owner"] = owner
        return workout

    def get_workouts(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT w.id AS workout_id, w.name, w.description,
                        w.date, w.owner_id,
                    FROM workouts w
                    JOIN users u ON(u.id = w.owner_id)
                    ORDER BY w.date
                    """,
                )

                workouts = []
                rows = db.fetchall()
                for row in rows:
                    workout = self.workout_record_to_dict(self, row)
                    workouts.append(workout)
                return workouts

    def get_workout(self, workout_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT w.id AS workout_id, w.name, w.description,
                       w.exercises, w.date, w.owner_id,
                    FROM workouts w
                    JOIN users u ON(u.id = w.owner_id)
                    WHERE w.id = %s
                    """,
                    [workout_id],
                )

                row = db.fetchone()
                workout = self.workout_record_to_dict(row, db.description)
                return workout

    def create_workout(self, workout):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO workouts (name, description, exercises, date, owner_id)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id
                    """,
                    [
                        workout.name,
                        workout.description,
                        workout.exercises,
                        workout.date,
                        workout.owner_id,
                    ],
                )

                workout_id = db.fetchone()[0]
                return workout_id

    def update_workout(self, workout):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    UPDATE workouts
                    SET name = %s, description = %s, exercises = %s, date = %s
                    WHERE id = %s
                    """,
                    [
                        workout.name,
                        workout.description,
                        workout.exercises,
                        workout.date,
                        workout.workout_id,
                    ],
                )

    def delete_workout(self, workout_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM workouts
                    WHERE id = %s
                    """,
                    [workout_id],
                )


class UserQueries:
    def get_users(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, first, last, email
                    FROM users
                    ORDER BY last, first
                    """,
                )

                users = []
                for row in db.fetchall():
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                    users.append(record)

    def get_user(self, user_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT id, first, last, email
                    FROM users
                    WHERE id = %s
                    """,
                    [user_id],
                )

                record = None
                row = db.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                return record

    def create_user(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    user.first,
                    user.last,
                    user.email,
                ]
                db.execute(
                    """
                    INSERT INTO users (first, last, email)
                    VALUES (%s, %s, %s)
                    RETURNING id, first, last, email
                    """,
                    params,
                )

                record = None
                row = db.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                return record

    def update_user(self, user):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    user.first,
                    user.last,
                    user.email,
                    user.id,
                ]
                db.execute(
                    """
                    UPDATE users
                    SET first = %s, last = %s, email = %s
                    WHERE id = %s
                    """,
                    params,
                )

                record = None
                row = db.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                return record

    def delete_user(self, user_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM users
                    WHERE id = %s
                    """,
                    [user_id],
                )


class ExerciseQueries:
    def get_exercises(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT name, type, instructions, muscle, equipment,
                    difficulty, image
                    FROM exercises
                    ORDER BY diffculty, type
                    """,
                )

                exercises = []
                for row in db.fetchall():
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                    exercises.append(record)

                    return exercises

    def get_exercise(self, exercise_name):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT name, type, instructions, muscle, equipment,
                    difficulty, image
                    FROM exercises
                    WHERE id = %s
                    """,
                    [exercise_name],
                )

    def create_exercise_table(self, exercise):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    INSERT INTO exercises (name, type, muscle, equipment,
                    difficulty, instructions)
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """,
                    [
                        exercise.name,
                        exercise.type,
                        exercise.muscle,
                        exercise.equipment,
                        exercise.difficulty,
                        exercise.instructions,
                    ],
                )
