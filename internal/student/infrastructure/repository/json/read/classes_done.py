import json
from typing import List

from internal.student.domain.profile import Classes
from internal.student.infrastructure.repository.json.dto.classes import ClassesDTO


class DTOStudentMapper:
    def dto_classes_to_domain(self, classes: List[ClassesDTO]) -> List[Classes]:
        pass


class ClassesDoneRepositoryRead(DTOStudentMapper):
    def __init__(self, mapper: DTOStudentMapper, filename_classes_done: str):
        self.filename_classes_done = filename_classes_done
        self.mapper = mapper

    def get_classes_done_by_email(self, email: str) -> List[Classes]:
        try:
            with open(self.filename_classes_done, 'r', encoding='utf-8') as file:
                classes_done_by_user = json.load(file)
        except FileNotFoundError:
            return []

        classes_dto = classes_done_by_user.get(email, [])
        classes_done = self.mapper.dto_classes_to_domain(classes_dto)

        return classes_done
