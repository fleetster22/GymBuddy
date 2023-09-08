from main import app
from fastapi.testclient import TestClient
from pydantic import BaseModel
from queries.exercises import ExerciseRepository


client = TestClient(app)


class ExerciseOut(BaseModel):
    id: int
    name: str
    type: str
    muscle: str
    equipment: str
    difficulty: str
    instructions: str


class MockExerciseRepository(ExerciseRepository):
    def get_all(self):
        return [
            ExerciseOut(
                id=1,
                name="Push-Up",
                type="Strength",
                muscle="Chest",
                equipment="None",
                difficulty="Medium",
                instructions="Do a push-up.",
            )
        ]


app.dependency_overrides[ExerciseRepository] = MockExerciseRepository


def test_get_all_exercises():
    app.dependency_overrides[
        ExerciseRepository.get_all
    ] = MockExerciseRepository.get_all

    response = client.get("/api/exercises")
    data = response.json()
    print("Returned data:", data)

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Push-Up"
    assert data[0]["type"] == "Strength"
    assert data[0]["muscle"] == "Chest"
    assert data[0]["equipment"] == "None"
    assert data[0]["difficulty"] == "Medium"
    assert data[0]["instructions"] == "Do a push-up."
