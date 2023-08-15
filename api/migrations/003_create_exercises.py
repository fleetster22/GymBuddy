steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE exercises (
            id SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            type VARCHAR(30) NOT NULL,
            muscle VARCHAR(30) NOT NULL,
            difficulty VARCHAR(22)
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE exercises;
        """,
    ]
]
