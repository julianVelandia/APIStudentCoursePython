from pydantic import BaseModel
from typing import List


class StudentClass(BaseModel):
    class_id: str
    title: str


class StudentResponse(BaseModel):
    email: str
    name: str
    classes_done: List[StudentClass]

