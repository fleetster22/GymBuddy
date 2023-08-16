steps = [
    [
        # "Up" SQL statement
        """
        CREATE TABLE account (
            id SERIAL PRIMARY KEY NOT NULL,
            first_name VARCHAR(100) NOT NULL,
            last_name VARCHAR(100) NOT NULL,
            email VARCHAR(100) NOT NULL,
            password VARCHAR(100) NOT NULL,
            username VARCHAR(100) NOT NULL
        );
        """,
        # "Down" SQL statement
        """
        DROP TABLE dummy;
        """
    ]
]
