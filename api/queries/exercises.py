from pydantic import BaseModel


class Exercises(BaseModel):
    name: str
    type: str
    muscle: str
    difficulty: str
    equipment: str
    instructions: str
