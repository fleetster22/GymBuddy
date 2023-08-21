from pydantic import BaseModel


class Exercises(BaseModel):
    name: str
    type: str
    muscle: str
    equipment: str
    difficulty: str
    instructions: str
