steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE exercises (
            name VARCHAR(100) PRIMARY KEY NOT NULL,
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
