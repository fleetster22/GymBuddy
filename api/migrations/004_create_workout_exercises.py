steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE workout_exercises (
            workout_id INTEGER REFERENCES workouts(id),
            exercise_name VARCHAR REFERENCES exercises(name),
            PRIMARY KEY (workout_id, exercise_name)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE workout_exercises;
        """,
    ],
]
