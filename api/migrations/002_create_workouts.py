steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE workouts (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            description VARCHAR(1000) NOT NULL,
            date DATE
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE workouts;
        """,
    ],
]
