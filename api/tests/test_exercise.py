from main import app
from fastapi.testclient import TestClient
from db import ExerciseQueries

client = TestClient(app)


class MockExerciseQueries:
    def get_exercises(self):
        return [{}]


def test_get_all_exercises():
    app.dependency_overrides[ExerciseQueries] = MockExerciseQueries

    response = client.get("/api/exercises")

    assert response.status_code == 200
    assert response.json() == {"exercises": [{}]}

    app.dependency_overrides = {}
