from main import app
from fastapi.testclient import TestClient
from pydantic import BaseModel
from queries.workouts import WorkoutRepository
from datetime import date
from queries.exercises import ExerciseIn


client = TestClient(app)


class WorkoutOut(BaseModel):
    id: int
    name: str
    difficulty: str
    description: str
    date: date
    exercises: list[ExerciseIn]


class MockWorkoutRepository(WorkoutRepository):
    def get_all(self):
        return [
            WorkoutOut(
                id=1,
                name="Beginner Strength",
                difficulty="Beginner",
                description="A beginner strength workout.",
                date=date.today(),
                exercises=[
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
            )
        ]


app.dependency_overrides[WorkoutRepository] = MockWorkoutRepository


def test_get_all_workouts():
    app.dependency_overrides[
        WorkoutRepository.get_all
    ] = MockWorkoutRepository.get_all

    response = client.get("/api/workouts")
    data = response.json()
    print("Returned data:", data)

    app.dependency_overrides = {}

    assert response.status_code == 200
    assert data[0]["id"] == 1
    assert data[0]["name"] == "Beginner Strength"
    assert data[0]["description"] == "A beginner strength workout."
    assert data[0]["date"] == date.today()
    assert data[0]["exercises"] == [
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
    ]
