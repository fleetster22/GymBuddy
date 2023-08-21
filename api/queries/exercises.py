from pydantic import BaseModel


# class Error(BaseModel):
#     message: str


# class ExerciseIn(BaseModel):
#     name: str
#     type: str
#     muscle: str
#     difficulty: str
#     equipment: str
#     instructions: str


class Exercises(BaseModel):
    name: str
    type: str
    muscle: str
    equipment: str
    difficulty: str
    instructions: str


# class ExerciseRepository:
#     pass

# def create_exercise(self, exercise: ExerciseIn) -> ExerciseOut:
#     with pool.connection() as conn:
#         with conn.cursor() as db:
#             result = db.execute(
#                 "INSERT INTO exercises (name, type, muscle, difficulty, equipment, instructions) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id",
#                 (
#                     exercise.name,
#                     exercise.type,
#                     exercise.muscle,
#                     exercise.difficulty,
#                     exercise.equipment,
#                     exercise.instructions,
#                 ),
#             )
#             id = result.fetchone()[0]
#             old_data = exercise.dict()
#             return ExerciseOut(id=id, **old_data)

# def update_exercise(self, id: str, exercise: Exercises):
#     return updated_exercise

# def delete_exercise(self, id: str):
#     return deleted_exercise
