from pydantic import BaseModel
from typing import List


class ClassesResponse(BaseModel):
    class_id: str
    title: str
    creation_date: str
    content: List[str]
    read_time: float
