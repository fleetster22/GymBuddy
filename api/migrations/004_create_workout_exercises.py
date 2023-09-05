steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE workout_exercises (
            workout_id INTEGER REFERENCES workouts(id) ON DELETE CASCADE,
            exercise_id INTEGER REFERENCES exercises(id) ON DELETE RESTRICT,
            PRIMARY KEY (workout_id, exercise_id)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE workout_exercises;
        """,
    ],
]
