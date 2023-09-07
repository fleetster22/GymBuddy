steps = [
    """
    CREATE TABLE workout_history (
        id SERIAL PRIMARY KEY NOT NULL,
        workout_id INTEGER NOT NULL,
        account_id INTEGER NOT NULL,
        date DATE NOT NULL,
        FOREIGN KEY (workout_id) REFERENCES workouts (id),
        FOREIGN KEY (account_id) REFERENCES account (id)
    );
    """,
    """
    DROP TABLE workout_history;
    """,
]
