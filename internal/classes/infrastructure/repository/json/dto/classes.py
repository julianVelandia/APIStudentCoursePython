from dataclasses import dataclass
from typing import List

@dataclass
class ClassesDTO:
    class_id: str
    title: str
    creation_date: str
    content: List[str]
    read_time: float

@dataclass
class ClassesStudentDTO:
    class_id: str
    title: str
