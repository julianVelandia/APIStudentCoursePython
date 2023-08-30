from dataclasses import dataclass
from typing import List

@dataclass
class Class:
    class_id: str
    title: str
    creation_date: str
    content: List[str]
    read_time: float

@dataclass
class ClassStudent:
    class_id: str
    title: str
