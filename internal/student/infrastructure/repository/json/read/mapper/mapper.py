from typing import List

from internal.student.domain.profile import Profile, Classes
from internal.student.infrastructure.repository.json.dto.classes import ClassesDTO
from internal.student.infrastructure.repository.json.dto.profile import ProfileDTO


class DTOStudentMapper:
    def dto_profile_to_domain(self, email: str, profile: ProfileDTO) -> Profile:

        return Profile(
                email,
                profile['name']
            )

    def dto_classes_to_domain(self, classes: List[ClassesDTO]) -> List[Classes]:
        domain_classes = []
        for dto_class in classes:
            domain_classes.append(Classes(
                dto_class['class_id'],
                dto_class['title'],
            ))
        return domain_classes
