steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE exercises (
            id int SERIAL PRIMARY KEY NOT NULL,
            name VARCHAR(100) NOT NULL,
            type VARCHAR(30) NOT NULL,
            muscle VARCHAR(30) NOT NULL,
            equipment VARCHAR(100) NOT NULL,
            difficulty VARCHAR(22),
            instructions VARCHAR(1000) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE exercises;
        """,
    ]
]
