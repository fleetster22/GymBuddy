steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE workouts (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            difficulty VARCHAR(20),
            description VARCHAR(1000) NOT NULL,
            date DATE
            completed BOOLEAN NOT NULL DEFAULT FALSE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE workouts;
        """,
    ],
]
