from main import app
from fastapi.testclient import TestClient
from pydantic import BaseModel
from queries.workouts import WorkoutRepository
from datetime import date
from queries.exercises import ExerciseOut


client = TestClient(app)


class WorkoutOut(BaseModel):
    id: int
    name: str
    difficulty: str
    description: str
    date: date
    exercises: list[ExerciseOut]


class MockWorkoutRepository(WorkoutRepository):
    def get_all(self):
        return []

    def create_workout(self, workout):
        result = [
            {
                "id": 1010,
                "name": "Incline Hammer Curls",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "dumbbell",
                "difficulty": "beginner",
                "instructions": "Seat yourself on an incline bench with a dumbbell in each hand. You should pressed firmly against he back with your feet together. ",
            },
            {
                "id": 1011,
                "name": "Wide-grip barbell curl",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "barbell",
                "difficulty": "beginner",
                "instructions": "Stand up with your torso upright while holding a barbell at the wide outer handle. The palm of your hands should be facing forward. ",
            },
            {
                "id": 1012,
                "name": "EZ-bar spider curl",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "barbell",
                "difficulty": "beginner",
                "instructions": "Start out by setting the bar on the part of the preacher bench that you would normally sit on. ",
            },
        ]

        result.append(workout)
        return result


def test_get_all_workouts():
    app.dependency_overrides[
        WorkoutRepository.get_all
    ] = MockWorkoutRepository.get_all

    response = client.get("/api/workouts")

    assert response.status_code == 200
    assert response.json() == {"workouts": []}

    app.dependency_overrides = {}


def test_create_workout():
    app.dependency_overrides[
        WorkoutRepository.create
    ] = MockWorkoutRepository.create_workout

    json = {
        "id": 1097,
        "name": "test",
        "difficulty": "beginner",
        "description": "test",
        "date": "2023-01-01",
        "exercises": [
            {
                "id": 1010,
                "name": "Incline Hammer Curls",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "dumbbell",
                "difficulty": "beginner",
                "instructions": "Seat yourself on an incline bench with a dumbbell in each hand. You should pressed firmly against he back with your feet together. ",
            },
            {
                "id": 1011,
                "name": "Wide-grip barbell curl",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "barbell",
                "difficulty": "beginner",
                "instructions": "Stand up with your torso upright while holding a barbell at the wide outer handle. The palm of your hands should be facing forward. ",
            },
            {
                "id": 1012,
                "name": "EZ-bar spider curl",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "barbell",
                "difficulty": "beginner",
                "instructions": "Start out by setting the bar on the part of the preacher bench that you would normally sit on. ",
            },
        ],
    }

    expected = {
        "id": 1097,
        "name": "test",
        "difficulty": "beginner",
        "description": "test",
        "date": "2023-01-01",
        "exercises": [
            {
                "name": "Incline Hammer Curls",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "dumbbell",
                "difficulty": "beginner",
                "instructions": "Seat yourself on an incline bench with a dumbbell in each hand. You should pressed firmly against he back with your feet together. ",
            },
            {
                "name": "Wide-grip barbell curl",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "barbell",
                "difficulty": "beginner",
                "instructions": "Stand up with your torso upright while holding a barbell at the wide outer handle. The palm of your hands should be facing forward. ",
            },
            {
                "name": "EZ-bar spider curl",
                "type": "strength",
                "muscle": "biceps",
                "equipment": "barbell",
                "difficulty": "beginner",
                "instructions": "Start out by setting the bar on the part of the preacher bench that you would normally sit on. ",
            },
        ],
    }

    response = client.post("/api/workouts/create", json=json)

    assert response.status_code == 200
    assert response.json() == expected

    app.dependency_overrides = {}
