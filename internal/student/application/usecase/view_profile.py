from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str
    age: int

class StudentService:
    def get_student_profile(self, student_id: int) -> Student:
        # Aquí implementa la obtención de datos del estudiante desde la base de datos real o estructura de datos
        pass

class StudentUsecase:
    def __init__(self, service: StudentService):
        self.service = service

    def get_student_profile(self, student_id: int) -> Student:
        return self.service.get_student_profile(student_id)
