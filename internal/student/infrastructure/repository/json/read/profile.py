import json

from internal.student.domain.profile import Profile
from internal.student.infrastructure.repository.json.dto.profile import ProfileDTO


class DTOStudentMapper:
    def dto_profile_to_domain(self, email: str, profile: ProfileDTO) -> Profile:
        pass


class ProfileRepositoryRead(DTOStudentMapper):
    def __init__(self, mapper: DTOStudentMapper, filename_profile: str):
        self.mapper = mapper
        self.filename_profile = filename_profile

    def get_profile_by_email(self, email: str) -> Profile:
        try:
            with open(self.filename_profile, 'r', encoding='utf-8') as file:
                profiles = json.load(file)

        except FileNotFoundError:
            raise Exception(f"Profile not found for email: {email}")

        found_profile_dto = profiles.get(email)

        if not found_profile_dto:
            raise Exception(f"Profile not found for email: {email}")

        found_profile = self.mapper.dto_profile_to_domain(email, found_profile_dto)

        return found_profile
